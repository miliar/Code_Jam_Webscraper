#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int n;
    char g[4][4];
    int x[10];
    int o[10];
    int p[10];
    ifstream in("googlecodejam.in");
    ofstream out("googlecodejam.out");
    in>>n;
    for(int i=0;i<n;i++)
    {
        for(int i=0;i<10;i++)
        {
        x[i]=0;
        o[i]=0;
        p[i]=0;
        }
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                in>>g[j][k];
                if(g[j][k]=='.') {p[j]++;p[k+4]++;}
                if(g[j][k]=='X') {x[j]++;x[k+4]++;}
                if(g[j][k]=='O') {o[j]++;o[k+4]++;}
                if(g[j][k]=='T') {x[j]++;o[j]++;x[k+4]++;o[k+4]++;}
                if(j==k)
                {
                    if(g[j][k]=='.') p[8]++;
                    if(g[j][k]=='X') x[8]++;
                    if(g[j][k]=='O') o[8]++;
                    if(g[j][k]=='T') {x[8]++;o[8]++;}
                }
                if(j+k==3)
                {
                    if(g[j][k]=='.') p[9]++;
                    if(g[j][k]=='X') x[9]++;
                    if(g[j][k]=='O') o[9]++;
                    if(g[j][k]=='T') {x[9]++;o[9]++;}
                }
            }
        }
        for(int j=0;j<10;j++)
        {
            if(x[j]==4){out<<"Case #"<<i+1<<": X won"<<endl;goto end;}
            if(o[j]==4){out<<"Case #"<<i+1<<": O won"<<endl;goto end;}
        }
        for(int j=0;j<10;j++) if(p[j]>0){out<<"Case #"<<i+1<<": Game has not completed"<<endl;goto end;}
        out<<"Case #"<<i+1<<": Draw"<<endl;
        end:;
    }
    return 0;
}
