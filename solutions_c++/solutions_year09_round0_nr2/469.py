#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
using namespace std;
int alt[105][105];
int change[105][105];
int end[105][105];
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
map<int,char> basin;

int min(int x,int y)
{
    int min=alt[x][y];
    int mindir=-1;
    for (int i=0;i<4;i++)
        if (alt[x+dir[i][0]][y+dir[i][1]]<min) 
        {
            min=alt[x+dir[i][0]][y+dir[i][1]];
            mindir=i;
        }
    return mindir;
}

int main(int argc, char *argv[])
{
    int t,h,w;
    ifstream fin("B-large.in.txt");
    ofstream fout("outputb_large.txt");
    fin>>t;
    for (int i=1;i<=t;i++)
    {
        basin.clear();
        fin>>h>>w;
        char c='a';
        for (int j=1;j<=h;j++)
            for (int k=1;k<=w;k++)
                fin>>alt[j][k];
        for (int j=0;j<=h+1;j++) {alt[j][0]=15000; alt[j][w+1]=15000;}
        for (int k=0;k<=w+1;k++) {alt[0][k]=15000; alt[h+1][k]=15000;}
        for (int j=1;j<=h;j++)
            for (int k=1;k<=w;k++)
                change[j][k]=min(j,k);
                
        for (int j=1;j<=h;j++)
            for (int k=1;k<=w;k++)
            {
                int jj=j,kk=k;
                while (change[jj][kk]!=-1)
                {
                    jj=jj+dir[change[jj][kk]][0];
                    kk=kk+dir[change[jj][kk]][1];
                }
                end[j][k]=jj*12000+kk;
            }
        
        map<int,char>::iterator it;
        fout<<"Case #"<<i<<":"<<endl;
        for (int j=1;j<=h;j++){
            for (int k=1;k<=w;k++)
            {
                int l=end[j][k];
                it=basin.find(l);
                if (it==basin.end())
                {
                    fout<<c<<" ";
                    basin[l]=c;
                    c++;
                }
                else
                {
                    fout<<basin[l]<<" ";
                }
            }
            fout<<endl;
        }
    }
    system("pause");
    return 0;
}
