#include <fstream>
#include <cmath>
using namespace std;
ofstream fout ("c9.out");
ifstream fin ("c9.in");

int n,k,tt,now,s,t,del,ans;
int ma[2000][2000];
int bl[2000];
int pr[5000000],la[5000000],ro[5000000],up[5000000];
void ins(int a, int b)
    {
        int bi=1;
        now++;
        pr[now]=la[a];
        la[a]=now;
        ro[now]=b;
        up[now]=bi;
        now++;
        pr[now]=la[b];
        la[b]=now;
        ro[now]=a;
        up[now]=0;
    }
bool dfs(int nu, int mi)
    {
        if (nu==t)
            {
                del=mi;
                return 1;
            }
        bl[nu]=ans;
        int tmp=la[nu];
        while (tmp)
            {
                if ((bl[ro[tmp]]<ans)&&(up[tmp])&&(dfs(ro[tmp],min(mi,up[tmp]))))
                    {
                        up[tmp]-=del;
                        up[tmp^1]+=del;
                        return 1;
                    }
                tmp=pr[tmp];
            }
        return 0;
    }
int main()
    {
        fin >> tt;
        for (int al=0; al<tt; al++)
            {
                fin >> n >> k;
                for (int i=0; i<n; i++)
                    for (int j=0; j<k; j++)
                        fin >> ma[i][j];
                for (int i=0; i<n+n+30; i++)
                    la[i]=0;
                now=1;
                for (int i=0; i<n; i++)
                    {
                        for (int j=0; j<n; j++)
                            {
                                bool flag=0;
                                for (int x=0; x<k; x++)
                                    if (ma[i][x]-ma[j][x]<=0)
                                        {
                                            flag=1;
                                            break;
                                        }
                                if (flag)
                                    continue;
                                ins(i,j+n);
                            }
                        ins(n+n+1,i);
                        //ins(i,i+n);
                        ins(i+n,n+n+2);
                    }
                t=n+n+2;
                s=n+n+1;
                for (int i=0; i<n+n+30; i++)
                    bl[i]=-1;
                ans=0;
                while (dfs(s,100000)) ans+=del;
                fout << "Case #" << al+1 << ": " << n-ans << endl;
            }
    }
