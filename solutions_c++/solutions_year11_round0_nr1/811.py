#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

char ch;
int t,n,ti,ans,m,d,s,o;
int pa[2][105],sum[2],c[105],p[105],now[2],a[2];

inline int f(char ch)
{
    if(ch=='O') return 0; else return 1;
}

int main()
{
    int i;
    fin>>t;
    for(ti=1;ti<=t;ti++)
    {
        fin>>n;
        ans=0; 
        now[0]=1; now[1]=1;
        a[0]=0; a[1]=0;
        
        for(i=1;i<=n;i++)
        {
            fin>>ch>>p[i];
            c[i]=f(ch);
            pa[c[i]][++a[c[i]]]=p[i];
        }
        a[0]=0; a[1]=0;
        for(i=1;i<=n;i++)
        {
            a[c[i]]++;
            s=abs(now[c[i]]-p[i]);
            ans+=s+1;
            now[c[i]]=p[i];
            d=now[1-c[i]]-pa[1-c[i]][a[1-c[i]]+1];
            if(s+1>=abs(d)) now[1-c[i]]=pa[1-c[i]][a[1-c[i]]+1];
            else
            {
                if(d==0) o=0;
                else
                    if(d<0) o=1; else o=-1;
                now[1-c[i]]+=o*(s+1);
            }
            //fout<<s<<' ';
        }
        
            
        fout<<"Case #"<<ti<<": "<<ans<<endl; 
    }
    return 0;
}
