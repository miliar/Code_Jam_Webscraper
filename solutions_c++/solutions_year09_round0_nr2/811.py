#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

class Node {
public:
    Node() : w(0), x(-1), y(-1), flow(NULL), incoming(0), label(0) {}
    int w, x, y;
    struct Node* flow;
    struct Node* in[4];
    int incoming;
    char label;
};

class link {
    int x, y;
    int w;
};

struct dir {
    int dx, dy;
};

dir dir4[] = {{0,-1}, {-1,0}, {1,0}, {0,1}};

int row[100], col[100];
int all;

Node** global_map;

void label(Node& node, char c) {
    if(node.label!=0)
        return;
    row[node.x]--;
    row[node.y]--;
    node.label = c;
    --all;
    if(node.flow)
        label(*node.flow, c);
    for(int i = 0; i < node.incoming; i++)
        label(*node.in[i], c);
}

int main(int ac, char **av)
{
    int n, w, h, i, min;
    struct Node* min_node;

    cin >> n;
    for(i=1; i<=n; ++i) {
        cin >> h >> w;
        Node ** map = new Node*[h];
        global_map = map;
        all = h * w;
        for(int j = 0; j < h; j++) {
            col[j] = w;
            map[j] = new Node[w];
            for(int k = 0; k < w; k++) {
                row[k] = h;
                map[j][k].y = j;
                map[j][k].x = k;
                cin >> map[j][k].w;
            }
        }
        for(int j = 0; j < h; j++) {
            for(int k = 0; k < w; k++) {
                min = INT_MAX;
                for(int d = 0; d < 4; d++) {
                    int x = k+dir4[d].dx;
                    int y = j+dir4[d].dy;
                    if(x<0 || y<0 || x>=w || y>=h)
                        continue;
                    if(map[y][x].w < min) {
                        min_node = &map[y][x];
                        min = map[y][x].w;
                    }
                }
                if(min==INT_MAX)
                    continue;
                if(min < map[j][k].w) {
                    map[j][k].flow = min_node;
                    min_node->in[ min_node->incoming++ ] = &map[j][k];
                }
            }
        }
        char ch = 'a';
        while(all > 0) {
            bool found = false;
            int x,y;
            for(int j = 0; j < h; j++) {
                for(int k = 0; k < w; k++) {
                    if(map[j][k].label ==0) {
                        found = true;
                        y=j;
                        x=k;
                        break;
                    }
                }
                if(found)
                    break;
            }
            label(map[y][x], ch);
            ch++;
        }

        cout << "Case #" << i << ':' << endl;
        for(int j = 0; j < h; j++) {
            for(int k = 0; k < w; k++) {
                if(k == w-1)
                    cout << map[j][k].label << endl;
                else
                    cout << map[j][k].label << ' ';
            }
        }
        for(int j = 0; j < h; j++)
            delete[] map[j];
        delete[] map;
    }

    return 0;
}
