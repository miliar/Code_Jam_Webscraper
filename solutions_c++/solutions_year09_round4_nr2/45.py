#include <fstream>
#include <cmath>
using namespace std;
ofstream fout ("b.out");
ifstream fin ("b.in");

char ch;
bool flag;
int r,c,tt,f;
bool ma[100][100];
bool bl[100][100][100];
void dfs(int x, int y, int nu)
    {
        if (flag)
            return;
        int tx=x;
        while ((x+1<r)&&(!ma[x+1][y])) x++;
        if (x-tx>f)
            return;
        if (x+1==r)
            {
                flag=1;
                return;
            }
        if (bl[x][y][nu])
            return;
        bl[x][y][nu]=1;
    //    fout << x << ' ' << y << ' ' << nu << endl;
  //      if ((x==3)&&(y==4)&&(nu==1)) 
    //        fout << endl;
        if ((y-1>=0)&&(!ma[x][y-1]))
            dfs(x,y-1,nu);
        if ((y+1<c)&&(!ma[x][y+1]))
            dfs(x,y+1,nu);
        if ((!ma[x][y-1])&&(ma[x+1][y-1]))
            {
                if (nu>0)
                    {
                        ma[x+1][y-1]=0;
                        dfs(x,y,nu-1);
                        ma[x+1][y-1]=1;
                    }
            }
        if ((!ma[x][y+1])&&(ma[x+1][y+1]))
            {
                if (nu>0)
                    {
                        ma[x+1][y+1]=0;
                        dfs(x,y,nu-1);
                        ma[x+1][y+1]=1;
                    }
            }
        bl[x][y][nu]=0;
    }
int main()
    {
        fin >> tt;
        for (int al=0; al<tt; al++)
            {
                fin >> r >> c >> f;
                for (int i=0; i<r; i++)
                    for (int j=0; j<c; j++)
                        {
                            fin >> ch;
                            if (ch=='#')
                                ma[i][j]=1;
                            else
                                ma[i][j]=0;
                        }
                int an=-1;
                for (int i=0; i<(r*c)/2+5; i++)
                    {
                        flag=0;
                        memset(bl,0,sizeof(bl));
                        dfs(0,0,i);
                        if (flag)
                            {
                                an=i;
                                break;
                            }
                    }
                if (an==-1)
                    fout << "Case #" << al+1 << ": No"<< endl;
                else
                    fout << "Case #" << al+1 << ": Yes " << an << endl;
            }
    }
