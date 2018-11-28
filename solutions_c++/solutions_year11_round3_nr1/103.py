#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <sstream>

using namespace std;
int row, col;
char p[55][55];
void print(){
            for(int r = 0; r < row; r++)
            {
                for(int c= 0; c< col;c++)
                {
                    cout<<p[r][c];
                }
                cout<<endl;
            }}
int main(int argc, char **argv)
{
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int t = 1; t <= T; t++)
    {
        fin>>row>>col;
        for(int r = 0; r < row; r++)
        {
            for(int c = 0; c < col; c++)
            {
                char tmp;
                fin>>tmp;
                p[r][c] = tmp;
            }
        }

        fout<<"Case #"<<t<<":"<<endl;
        bool im = false;
        for(int r = 0; r < row; r++)
        {print();
            for(int c = 0; c < col; c++)
            {
                if(p[r][c] == '#')
                {
                    if(r+1 >= row || c+1>=col||
                            p[r][c+1]!='#' ||
                            p[r+1][c]!='#' ||
                            p[r+1][c+1]!='#')
                    {
                        im = true;
                        break;
                    }
                    else
                    {
                        p[r][c]='/';
                        p[r][c+1]='\\';
                        p[r+1][c]='\\';
                        p[r+1][c+1]='/';

                    }
                }
            }
        }
        if(im)
            fout<<"Impossible"<<endl;
        else
            for(int r = 0; r < row; r++)
            {
                for(int c= 0; c< col;c++)
                {
                    fout<<p[r][c];
                }
                fout<<endl;
            }
    }
    return 0;
}
