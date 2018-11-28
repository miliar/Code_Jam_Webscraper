#include<fstream>
#include<algorithm>
using namespace std;
ifstream fin("ASmall.in");
ofstream fout("ASmall.out");
int st[35],p[35];
int main()
{
    int T,N,K;
    fin>>T;
    for(int cs=0;cs<T;cs++)
    {
         fout<<"Case #"<<cs+1<<": ";
         fin>>N>>K;
         memset(st,0,sizeof(st));
         memset(p,0,sizeof(p));
         p[0]=1;
         while(K--)
         {
            for(int i=0;i<N;i++)
            {
                if(p[i])
                {
                   if(st[i])
                   st[i]=0;
                   else
                   st[i]=1;
                }
                else break;
            }
            for(int i=0;i<N;i++)
            {
                if(st[i]&&p[i])
                p[i+1]=1;
                else
                p[i+1]=0;
            }
            
         }
         if(st[N-1]&&p[N-1])
         fout<<"ON"<<endl;
         else
         fout<<"OFF"<<endl;
    }
}
