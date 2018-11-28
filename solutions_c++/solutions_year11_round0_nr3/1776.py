#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int f[1005];
int bit[21];

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    
    int t;
    int cas=1;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        memset(bit,0,sizeof(bit));
        int i,j;
        for(i=0;i<n;i++)
          cin>>f[i];
        sort(f,f+n);
        int res=0;
        for(i=0;i<n;i++)
          for(j=0;j<=20;j++)
            if(f[i]&(1<<j))
              bit[j]++;
        for(j=0;j<=20;j++)
          if(bit[j]&1){res=-1;break;}
        printf("Case #%d: ",cas++);
        if(res==-1) printf("NO\n");
        else{
           for(i=1;i<n;i++)
             res+=f[i];
           printf("%d\n",res);
        }
    }
}
