#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int T;
int S,Q;

struct MM
{
    public:
           char a[101];
}mm[100];

int cnt[100];
int num;

bool cmp(MM a,MM b)
{
     return strcmp(a.a,b.a)<0;
}

int search(char a[101])
{
    int low=0;
    int high=S-1;
    int mid;
    int tt;
    while(low<=high)
    {
        mid=(low+high)>>1;
        tt=strcmp(a,mm[mid].a);
        if(tt==0)
            return mid;
        else if(tt>0)
            low=mid+1;
        else
            high=mid-1;
    }
    return -1;
}

void init()
{
    int i;
    scanf("%d\n",&S);
    for(i=0;i<S;i++)
        gets(mm[i].a);
    sort(mm,mm+S,cmp);
}

void solve()
{
     int i,tt;
     int ans=0;
     char name[101];
     memset(cnt,0,sizeof(cnt));
     num=0;
     scanf("%d\n",&Q);
     while(Q--)
     {
        gets(name);
        tt=search(name);
        if(tt==-1)
           continue;
        if(cnt[tt]==0)
        {
           cnt[tt]++;
           num++;
           if(num==S)
           {
               memset(cnt,0,sizeof(cnt));
               cnt[tt]++;
               num=1;
               ans++;
           }
        }
     }
     printf("%d\n",ans);
}

int main()
{
    int i;
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        init(),solve();
    }
    return 0;
}
               
      
