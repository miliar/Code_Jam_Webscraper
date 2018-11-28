/*
ID: wscmyjy2
PROG: contact
LANG: C++
*/
#include <fstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

bool bl[1100];
bool map[1100][1100];
int base[110];
int tt;
int main()
    {
        ofstream fout ("A-large.out");
        freopen("A-large.in","r",stdin);
        for (int i=2; i<=10; i++)
            {
                for (int j=1; j<=1000; j++)                
                    {
                        for (int k=1; k<=1000; k++)
                            bl[k]=0;
                        int tm=j;
                        while (bl[tm]==0)
                            {
                                bl[tm]=1;
                                int su=0;
                                while (tm>0)
                                    {
                                        su+=(tm%i)*(tm%i);
                                        tm=tm/i;
                                    }
                                tm=su;
                            }
                        if (tm==1)
                            map[i][j]=1;
                        else
                            map[i][j]=0;
                    }
            }
        scanf("%d",&tt);
        for (int o=0; o<tt; o++)
            {
                char buf;
                base[0]=0;
                while(1)
                    {
                        scanf("%d",&base[++base[0]]);
                        scanf("%c",&buf);
                        if(buf=='\n') break;
                    }
                for (int ti=2; ; ti++)
                    {
                        bool flag=0;
                        for (int i=1; i<=base[0]; i++)
                            {
                                int tii=ti;
                                int su=0;
                                while (tii>0)
                                    {
                                        su+=(tii%base[i])*(tii%base[i]);
                                        tii=tii/base[i];
                                    }
                                tii=su;
                                if (map[base[i]][tii]==0)
                                    {
                                        flag=1;
                                        break;
                                    }
                            }
                        if (flag==0)
                            {
                                fout << "Case #" << o+1 << ": "  << ti << endl;
                                break;
                            }
                    }
            }
    }
