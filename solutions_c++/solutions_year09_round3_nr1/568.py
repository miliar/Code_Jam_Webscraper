#include <cstdio>
#include <string.h>
#include <stdlib.h>
using namespace std;

long long int powl(long long int x, int y){
  int i;
  long long int r=1;
  for(i=0;i<y;i++)
    r=r*x;
 
  return r;
}

int main(){
  int t, a[100], b[100];
  char s[70];
  scanf("%d",&t);
  for(int i=1;i<=t;i++){
    scanf("%s",s);
    int cou=0;
    memset(a,-1,sizeof(a));
    memset(b,-1,sizeof(b));
    for(int j=0;j<strlen(s);j++){
      if(s[j]>='a'&&s[j]<='z'){
	if(a[s[j]-'a'+20]==-1){
	  a[s[j]-'a'+20]=cou;
	  b[j]=cou;
	  cou++;
	}
	else{
	  b[j]=a[s[j]-'a'+20];
	}
      }
      else{
	if(a[s[j]-'0']==-1){
	  a[s[j]-'0']=cou;
	  b[j]=cou;
	  cou++;
	}
	else{
	  b[j]=a[s[j]-'0'];
	}
      }
    }
    if(cou==1)cou=2;
    long long int ans=powl((long long int)cou,strlen(s)-1);
    //printf("%lld\n",ans);
    for(int j=1;j<strlen(s);j++){
      if(b[j]==1){
	ans+=0;
      }
      else if(b[j]==0){
	ans+=powl((long long int)cou,strlen(s)-1-j);
      }
      else{
	ans+=(long long int)b[j]*powl((long long int)cou,strlen(s)-1-j);
      }
      //printf("%lld\n",ans);
    }
    printf("Case #%d: %lld\n",i,ans);
  }

  return 0;
}
