#include<cstdio>
#include<cstring>
#define maxn 110
using namespace std;

char color[maxn][5];
int pos[maxn],nextpos1[maxn],nextpos2[maxn];
int n,indx;
int sign(int src,int dest)
{
    if(src<dest) return 1;
    else if(src>dest) return -1;
    else return 0;
}
int main()
{
//    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%s%d",color[i],pos+i);
        int last1=n,last2=n;
        for(int i=n-1;i>=0;i--) {
              if(color[i][0]=='O') last1=pos[i];
            else last2=pos[i];
            nextpos1[i]=last1;
            nextpos2[i]=last2;          
        }
        
        indx=0;
        int p1=1,p2=1;
        int cnt=0;
        while(indx<n)
        {
             cnt++;
                 //printf("%d:%d %d\n",cnt,p1,p2);
            if(color[indx][0]=='O' && p1==pos[indx]) {
                p2+=sign(p2,nextpos2[indx]);
                indx++;
                continue;
            }
            if(color[indx][0]=='B' && p2==pos[indx]) {
                p1+=sign(p1,nextpos1[indx]);
                indx++;
                continue;
            }
            p1+=sign(p1,nextpos1[indx]);
            p2+=sign(p2,nextpos2[indx]);
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
