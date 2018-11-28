#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
main(){
  int t;scanf("%d",&t);for(int tt=1;tt<=t;tt++){
    char buf[1000];
    scanf("%s",buf);
    int n=strlen(buf),cnt[100]={};
    int space,next,first;
    for(int i=n-1;i>=0;i--){
        for(int j=buf[i]-'0'+1;j<10;j++)if(cnt[j]){
          cnt[j]--;
          cnt[buf[i]-'0']++;
          buf[i]='0'+j;
//          printf("%d\n",buf[i]-'0');
          next=i+1;
          space=n-i-1;
          for(int k=1;k<10;k++)space-=cnt[k];
          while(space--)buf[next++]='0';
          for(int k=1;k<10;k++)while(cnt[k]--)buf[next++]='0'+k;
          buf[next]=0;
          goto ok;        
        }
        if(buf[i]!='0')cnt[buf[i]-'0']++;
    }
    first=1;while(!cnt[first])first++;
    buf[0]='0'+first;cnt[first]--;
    space=n;next=1;
    for(int k=1;k<10;k++)space-=cnt[k];
    while(space--)buf[next++]='0';
    for(int k=1;k<10;k++)while(cnt[k]--)buf[next++]='0'+k;
    buf[next]=0;
ok:;
    printf("Case #%d: %s\n",tt,buf);
  }
}

