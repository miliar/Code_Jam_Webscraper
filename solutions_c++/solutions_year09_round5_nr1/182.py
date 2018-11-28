#include <fstream>
#include <cmath>
#include <map>
#include <string>
using namespace std;
ofstream fout ("a2.out");
ifstream fin ("a2.in");

map <string,int> ma;
const int fx[4]={0,0,-1,1};
const int fy[4]={-1,1,0,0};
int tt,n,m,al,tii,co,mi,oo,tf=0;
char ch[20][20],aa;
int lx[100],ly[100];
string has;
bool ok;
int bl[20][20];
void ff(int x, int y)
    {
        bl[x][y]=tii;
        int tx,ty;
        for (int k=0; k<4; k++)
            {
                tx=fx[k]+x;
                ty=fy[k]+y;
                if ((0<=tx)&&(tx<n)&&(0<=ty)&&(ty<m))
                    {
                        if ((bl[tx][ty]<tii)&&((ch[tx][ty]=='o')||(ch[tx][ty]=='w')))
                            {
                                co++;
                                ff(tx,ty);
                            }
                    }
            }
    }
bool bre()
    {
        co=1;
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                if (ch[i][j]=='o')
                    {
                        tii++;
                        ff(i,j);
                        if (co==al)
                            return 1;
                        else
                            return 0;
                    }
        return 1;
    }
bool check(int tim)
    {
        co=0;
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                if (ch[i][j]=='x')
                    {
                        lx[co]=i;
                        ly[co]=j;
                        co++;
                    }
        int an=0;
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                if (ch[i][j]=='o')
                    {
                        mi=192837465;
                        for (int k=0; k<al; k++)
                            mi=min(mi,abs(i-lx[k])+abs(j-ly[k]));
                        an=an+mi;
                    }
        if (tim>=an)
            return 1;
        else
            return 0;
    }
void dfs(int ti, int ki)
    {
        if (ok==1)
            return;
        has="";
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                has=has+ch[i][j];
        int as=ti;
        while (as>0)
            {
                aa='0'+(as%10);
                has=has+aa;
                as=as/10;
            }
        if (ma[has])
            return;
        ma[has]=1;
        if (ti==0)
            {
                bool flag=0;
                for (int i=0; i<n; i++)
                    for (int j=0; j<m; j++)
                        if (ch[i][j]=='o')
                            {
                                flag=1;
                                break;
                            }
                if (flag==0)
                    ok=1;
                return;
            }
        int tx,ty,tx2,ty2;
        char t1,t2;
        int ss=0;
        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                if ((ch[i][j]=='o')||(ch[i][j]=='w'))
                    {
                        for (int k=0; k<4; k++)
                            {
                                tx=fx[k]+i;
                                ty=fy[k]+j;
                                tx2=-fx[k]+i;
                                ty2=-fy[k]+j;
                                if ((0<=tx)&&(tx<n)&&(0<=ty)&&(ty<m)&&(0<=tx2)&&(tx2<n)&&(0<=ty2)&&(ty2<m))
                                    {
                                        if (((ch[tx][ty]=='.')||(ch[tx][ty]=='x'))&&((ch[tx2][ty2]=='x')||(ch[tx2][ty2]=='.')))
                                            {
                                                t1=ch[i][j];
                                                t2=ch[tx][ty];
                                                if (ch[i][j]=='w')
                                                    ch[i][j]='x';
                                                else
                                                    ch[i][j]='.';
                                                if (ch[tx][ty]=='x')
                                                    ch[tx][ty]='w';
                                                else
                                                    ch[tx][ty]='o';
                                                ss=0;
                                                for (int k1=0; k1<4; k1++)
                                                    {
                                                        tx=fx[k]+i;
                                                        ty=fy[k]+j;
                                                        if ((0<=tx)&&(tx<n)&&(0<=ty)&&(ty<m))
                                                            {
                                                                if (ch[tx][ty]=='#')
                                                                    ss++;
                                                            }
                                                    }
                                                if (!((ch[tx][ty]=='o')&&(ss>=2)))
                                                    if (check(ti))
                                                        {
                                                            if (!bre())
                                                                {
                                                                    if (ki==1)
                                                                        dfs(ti-1,0);
                                                                }
                                                            else
                                                                dfs(ti-1,1);
                                                        }
                                                
                                                ch[i][j]=t1;
                                                ch[tx][ty]=t2;
                                            }
                                    }
                            }
                    }
    }
int main()
    {
        fin >> tt;
        tii=0;
        for (oo=0; oo<tt; oo++)
            {
                fin >> n >> m;
                al=0;
                for (int i=0; i<n; i++)
                    for (int j=0; j<m; j++)
                        {
                            fin >> ch[i][j];
                            if ((ch[i][j]=='o')||(ch[i][j]=='w'))
                                al++;
                        }
                for (int i=0; i<=(n+m)*al; i++)
                    {
                        ok=0;
                        tf++;
                        dfs(i,1);
                        if (ok)
                            {
                                fout << "Case #" << oo+1 << ": " << i << endl;
                                break;
                            }
                    }
                if (!ok)
                    fout << "Case #" << oo+1 << ": " << "-1" << endl;
            }
    }
