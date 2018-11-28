#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>

#define LOG(x) // x

using namespace std;

struct Coord {
    Coord(int x,int y) :x(x),y(y) {}
    int x,y;
};

vector<Coord> next(const Coord& c,int w, int h)
{
    vector<Coord> rc;
    rc.push_back(Coord(c.x,c.y-1)); // N
    rc.push_back(Coord(c.x-1,c.y)); // W
    rc.push_back(Coord(c.x+1,c.y)); // E
    rc.push_back(Coord(c.x,c.y+1)); // S

    vector<Coord> result;
    for (int i = 0; i < rc.size(); ++i) {
        if ((rc[i].x >= 0) && (rc[i].y >= 0) && (rc[i].x < w) && (rc[i].y < h))
            result.push_back(rc[i]);
    }
    return result;
}

void print_table(const vector<vector<int> >& color, map<int,int>& color_char)
{
    cerr << endl;
    for (int i =0; i < color.size(); ++i) {
        for (int j = 0; j < color[0].size(); ++j) {
            int col = color[i][j];
            char ch = '*';
            if (col != 0) {
                ch = color_char[col];
            }
            cerr << col << string(&ch,1) << " ";
        }
        cerr << endl;
    }
    cerr << endl;
}

string solve(const vector<vector<int> >& m)
{
    int w = m[0].size();
    int h = m.size();
    map<int,int> color_char;
    vector<vector<int> > color;
    for (int i = 0; i < h; ++i) {
        vector<int> color_row;
        for (int j = 0; j < w;++j) {
            color_row.push_back(0);
        }
        color.push_back(color_row);
    }
    
    int act_color_char = 'a';
    int act_color = 1;
    
    for (int yi = 0; yi< h; ++yi) {
        for (int xi = 0; xi < w; ++xi) {
            Coord c(xi,yi);
            if (color[c.y][c.x] == 0) {
                color_char[act_color] = act_color_char;
                color[c.y][c.x] = act_color;
                vector<Coord> n = next(c,w,h);
                while(n.size() != 0) {
                    int min = INT_MAX;
                    Coord minp = c;
                    for (int i = 0; i < n.size(); ++i) {
                        Coord& p = n[i];
                        if (m[p.y][p.x] < min) {
                            min = m[p.y][p.x];
                            minp = p;
                        }
                    }
                    n = vector<Coord>();
                    if (min < m[c.y][c.x]) {
                        if (color[minp.y][minp.x] != 0) {
                            color_char[act_color] = color_char[color[minp.y][minp.x]];
                        } else {
                            color[minp.y][minp.x] = act_color;
                            c = minp;
                            n = next(minp,w,h);
                        }
                    }
                }
                if (color_char[act_color] == act_color_char)
                    act_color_char++;
                act_color++;
            }
            LOG(print_table(color,color_char);)
        }
    }
    
    string result;
    LOG(cerr << "w" << w << " h" << h << endl;)
    for (int yi = 0; yi< h; ++yi) {
        string row;
        for (int xi = 0; xi < w; ++xi) {
            char c = (char)color_char[color[yi][xi]];
            row += string(&c,1);
            //row += "1";
            row += " ";
        }
        result += "\n";
        result += row;
    }
    
    return result;
}

void test(istream& input, ostream& output)
{
    int numcases;
    input >> numcases;
    
    
     for (int i = 0; i < numcases; ++i) {
        vector<vector<int> > map;
        int h,w;
        input >> h >> w;
        for (int hi = 0; hi < h; ++hi) {
            vector<int> row;
            for (int wi = 0; wi < w; ++wi) {
                int v = 0;
                input >> v;
                row.push_back(v);
            }
            map.push_back(row);
        }
        
        output << "Case #" << i+1 << ":" << solve(map) << endl;
     } 

    std::string line;
}

void run_test_data(void)
{
    string testdatadir = "../../test_data/";
    string basename = "small_input";
    basename = "B-large.in";
    string input_path = testdatadir+basename+".txt";
    ifstream input;
    input.exceptions(input.failbit | input.badbit);
    input.open(input_path.c_str());
    string output_path = testdatadir+basename+".output.txt";
    ofstream output;
    output.exceptions(output.failbit | output.badbit);
    output.open(output_path.c_str(),std::ios::out|std::ios::trunc);
    
    test(input,output);
}

int main (int argc, char * const argv[]) {
    // insert code here...
    try {
        run_test_data();
        return 0;
    } catch (exception& err) {
        cerr << "Exception cathed:" << endl;
        cerr << err.what() << endl;
    } catch(...) {
        cerr << "Unkown exception catched" << endl;
        cerr << endl;
    }
    cerr << "Some error occured!\n";
    return 1;
}
