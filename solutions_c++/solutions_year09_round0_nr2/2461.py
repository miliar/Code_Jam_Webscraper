#include <iostream>
#include <vector>
#include <list>
#include <limits>
#include <deque>

using namespace std;

struct Cell
{
    int x, y;
    int height;

    Cell() {}
    Cell(int xx, int yy, int h) : x(xx), y(yy), height(h) {}
    Cell(const Cell& src) : x(src.x), y(src.y), height(src.height) {}
};

typedef list<Cell> cell_list;

void add_to_cell_list(const Cell& c, cell_list& cl)
{
    if(cl.empty()) { cl.push_back(c); }
    else
    {
        cell_list::iterator itr;
        for(itr = cl.begin();itr != cl.end();++itr)
        {
            if(c.height <= itr->height)
            {
                cl.insert(itr, c);
                break;
            }
        }
        if(itr == cl.end()) { cl.push_back(c); }
    }
}

char label[26];
char* map_label[100][100];
Cell map[100][100];
int map_width;
int map_height;

void get_cell_flow(const Cell& src, int& x, int& y)
{
    int cost = src.height;
    x = src.x;
    y = src.y;

    if(src.y > 0)
    {
        if(map[src.x][src.y - 1].height < cost)
        {
            x = src.x;
            y = src.y - 1;
            cost = map[x][y].height;
        }
    }

    if(src.x > 0)
    {
        if(map[src.x - 1][src.y].height < cost)
        {
            x = src.x - 1;
            y = src.y;
            cost = map[x][y].height;
        }
    }

    if(src.x < (map_width - 1))
    {
        if(map[src.x + 1][src.y].height < cost)
        {
            x = src.x + 1;
            y = src.y;
            cost = map[x][y].height;
        }
    }

    if(src.y < (map_height - 1))
    {
        if(map[src.x][src.y + 1].height < cost)
        {
            x = src.x;
            y = src.y + 1;
        }
    }
}

void add_cell_to_sink(const Cell& c, const Cell& sink, deque<Cell>& stack)
{
    int x, y;

    if(c.height != sink.height)
    {
        get_cell_flow(c, x, y);
        if((x == sink.x) && (y == sink.y))
        {
             map_label[c.x][c.y] = map_label[sink.x][sink.y];
             stack.push_back(c);
        }      
    }
}

void process_sink(Cell sink)
{
    deque<Cell> stack;
    stack.push_back(sink);

    do
    {
        sink = stack.front();
        stack.pop_front();

        if((sink.y > 0) && (map_label[sink.x][sink.y - 1] == 0))
        {
            add_cell_to_sink(map[sink.x][sink.y - 1], sink, stack);
        }

        if((sink.x > 0) && (map_label[sink.x - 1][sink.y] == 0))
        {
            add_cell_to_sink(map[sink.x - 1][sink.y], sink, stack);
        }

        if((sink.x < (map_width - 1)) && (map_label[sink.x + 1][sink.y] == 0))
        {
            add_cell_to_sink(map[sink.x + 1][sink.y], sink, stack);
        }

        if((sink.y < (map_height - 1)) && (map_label[sink.x][sink.y + 1] == 0))
        {
            add_cell_to_sink(map[sink.x][sink.y + 1], sink, stack);
        }
    }while(!stack.empty());
}

void read(cell_list& cl)
{
    int a;

    cl.clear();

    cin >> map_height >> map_width;
    for(int i = 0;i < map_height;i++)
    {
        for(int j = 0;j < map_width;j++)
        {
            cin >> a;
            map[j][i] = Cell(j, i, a);
            add_to_cell_list(map[j][i], cl);
        }
    }
}

int main()
{
    int T, labelIndex;
    cell_list cl;

    cin >> T;
    for(int i = 0;i < T;++i)
    {
        read(cl);
        memset(label, 0, 26);
        memset(map_label, 0, 100 * 100);

        labelIndex = 0;
        for(cell_list::iterator itr = cl.begin();itr != cl.end();++itr)
        {
            if(map_label[itr->x][itr->y] == 0)
            {
                map_label[itr->x][itr->y] = &(label[labelIndex]);
                process_sink(map[itr->x][itr->y]);
                ++labelIndex;
            }
        }

        labelIndex = 0;
        cout << "Case #" << (i + 1) << ":" << endl;
        for(int j = 0;j < map_height;++j)
        {
            for(int k = 0;k < map_width;++k)
            {
                if((*(map_label[k][j])) == 0)
                {
                    *(map_label[k][j]) = labelIndex + 'a';
                    ++labelIndex;
                }
                cout << (*(map_label[k][j])) << " ";
            }
            cout << endl;
        }
    }

    return 0;
}