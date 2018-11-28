#include <set>
#include <cstdio>
using namespace std;
int T,N,sum,min;
char b,c,a;
int Sc,Oc,Ic;
char S[128][128],prev;
set<char> O[128];
int used[128];
char res[1000];
int main(){
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        for(int i=0;i<128;i++){
        for(int j=0;j<128;j++)
            S[i][j]=-1;
            O[i].clear();
            used[i]=0;
        }
        prev=0;
        N=0;
        int fd=0;
        scanf("%d",&Sc);
        getchar();
        for(int i=0;i<Sc;i++){
            scanf("%c%c%c",&a,&b,&c);
            S[a][b]=c;
            S[b][a]=c;
        }
        scanf("%d",&Oc);
        getchar();
        for(int i=0;i<Oc;i++){
            scanf("%c%c",&a,&b);
            O[a].insert(b);
            O[b].insert(a);
        }
        scanf("%d",&Ic);
        getchar();
        for(int i=0;i<Ic;i++){
            scanf("%c",&a);
            if (prev!=-1 && S[a][prev]!=-1)
            {
                  res[N-1]=S[a][prev];
                  used[prev]--;
                  prev=-1;
            }else{
                fd=0;
                for(int k=0;k<128;k++)
                  if (used[k]>0 && (O[a].count(k)>0))
                    fd=1;
                if (fd)
                //O used intersects O[a]
                {
                    for(int k=0;k<128;k++) used[k]=0;//.clear();
                    prev=-1;
                    N=0;
                }
                //inak
                else
                {
                    used[a]++;
                    prev=a;
                    res[N++]=a;
                }
            }
        }
        printf("Case #%d: [",t+1);
        for(int i=0;i<N;i++)
          {
              if (i!=0) printf(", ");
              printf("%c",res[i]);
          }
        printf("]\n");
        }

}
