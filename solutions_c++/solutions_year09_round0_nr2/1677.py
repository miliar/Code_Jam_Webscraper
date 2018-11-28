#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int h,w,map[128][128],group[128][128];
char l,lab[128][128];

inline int getAtt(int x,int y)
{
    if(x<0 || x>=h || y<0 || y>=w) return 9999999;
    return map[x][y];
}

void root(int x,int y)
{
    int i=x,j=y;
    while(group[i][j]!=((i<<16)|j))
    {
        i=group[i][j]>>16;
        j=group[i][j]&0xFFFF;
    }
    int v=(i<<16)|j;
    while(x!=i || y!=j)
    {
        int s=x,t=y;
        x=group[x][y]>>16;
        y=group[x][y]&0xFFFF;
        group[s][t]=v;
    }
}

inline char giveLab(int x,int y)
{
    if(lab[x][y]) return lab[x][y];
    lab[x][y]=l++;
    return lab[x][y];
}

void work()
{
    for(int i=0;i<h;++i)
        for(int j=0;j<w;++j)
        {
            int minNeb=map[i][j],temp;
            group[i][j]=(i<<16)|j;
            if((temp=getAtt(i-1,j))<minNeb)
            {
                minNeb=temp;
                group[i][j]=((i-1)<<16)|j;
            }
            if((temp=getAtt(i,j-1))<minNeb)
            {
                minNeb=temp;
                group[i][j]=(i<<16)|(j-1);
            }
            if((temp=getAtt(i,j+1))<minNeb)
            {
                minNeb=temp;
                group[i][j]=(i<<16)|(j+1);
            }
            if((temp=getAtt(i+1,j))<minNeb)
            {
                minNeb=temp;
                group[i][j]=((i+1)<<16)|j;
            }
        }
    for(int i=0;i<h;++i)
        for(int j=0;j<w;++j) root(i,j);
    l='a';
    for(int i=0;i<h;++i)
        for(int j=0;j<w;++j) lab[i][j]='\0';
    for(int i=0;i<h;++i)
        for(int j=0;j<w;++j)
            lab[i][j]=giveLab(group[i][j]>>16,group[i][j]&0xFFFF);
}

int main()
{
    ifstream fin("B-small-attempt1.in");
    ofstream fout("out.txt");
    int n;
    fin>>n;
    for(int i=0;i<n;++i)
    {
        fin>>h>>w;
        for(int j=0;j<h;++j)
            for(int k=0;k<w;++k) fin>>map[j][k];
        work();
        fout<<"Case #"<<i+1<<":"<<endl;
        for(int j=0;j<h;++j)
        {
            fout<<lab[j][0];
            for(int k=1;k<w;++k) fout<<" "<<lab[j][k];
            fout<<endl;
        }
    }
    return 0;
}
