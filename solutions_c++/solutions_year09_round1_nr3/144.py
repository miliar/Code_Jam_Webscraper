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
ofstream fout ("C-large.out");
ifstream fin ("C-large.in");

double an;
double f[50][2]={0};
int c,n;
int pr[100000];
int la[100000];
int ro[100000];
double zh[100000];
int main()
    {
        int tt;
        fin >> tt;
        for (int o=0; o<tt; o++)
            {
                for (int i=0; i<=c; i++)
                    la[i]=0;
                fin >> c >> n;
                if (n>=c)
                    {
                        fout<<setprecision(7)<<setiosflags(ios::fixed  | ios::showpoint);
                        an=1;
                        fout << "Case #" << o+1 << ": " << an << endl;
                        continue;
                    }
                int now=0;
                for (int i=0; i<=c; i++)
                    for (int j=0; j<=n; j++)
                        if (i+j<=c)
                            {
                                if ((i==c)&&(j==0)) continue;
                                int las=c-i;
                                double zhi=1;
                                double han,ha1;
                                for (int k=0; k<j; k++)
                                    {
                                        ha1=(c-k);
                                        zhi*=1/ha1;
                                    }
                                for (int k=0; k<n-j; k++)
                                    {
                                        ha1=(c-k-j);
                                        zhi*=1/ha1;
                                    }
                                int all=las;
                                for (int k=1; k<=j; k++)
                                    {
                                        zhi*=all;
                                        all--;
                                    }
                                all=i;
                                for (int k=1; k<=n-j; k++)
                                    {
                                        zhi*=all;
                                        all--;
                                    }
                                all=n;
                                for (int k=1; k<=n-j; k++)
                                    {
                                        han=k;
                                        zhi*=all/han;
                                        all--;
                                    }
                                now++;
                                pr[now]=la[i+j];
                                la[i+j]=now;
                                ro[now]=i;
                                zh[now]=zhi;
                               // fout << i+j << ' ' << i << ' ' << zhi << endl;
                            }
                int fan=0;
                for (int j=0; j<=c; j++)
                    f[0][j]=0;
                f[0][0]=1;
                an=0;
                for (int i=1; i<100000; i++)
                    {
                        fan=1-fan;
                        for (int j=0; j<=c; j++)
                            {
                                f[j][fan]=0;
                                int tmp=la[j];
                                while (tmp>0)
                                    {
                                        f[j][fan]+=f[ro[tmp]][1-fan]*zh[tmp];
                                        tmp=pr[tmp];
                                    }
                            }
                        an+=f[c][fan]*i;
                    }
                fout<<setprecision(7)<<setiosflags(ios::fixed  | ios::showpoint);
                fout << "Case #" << o+1 << ": " << an << endl;
            }
    }
