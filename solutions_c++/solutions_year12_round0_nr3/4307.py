#include <stdio.h>
#include <math.h>
#include <string.h>
#include <set>

using namespace std;

int bit1[10];
bool judge(int a,int b) {
  int fucka=a;
  if(a<10)return false;
  set<int>myset;
  int i=0;
  while(b>0) {
    bit1[i++]=b%10;
    myset.insert(b%10);
    b/=10;
  }
  while(a>0) {
    int tmp=a%10;
    if(tmp!=0&&!myset.count(tmp))return false;
    a/=10;
  }
  myset.clear();
  for(int k=1;k<i;k++) {
    int tmp=bit1[0];
    for(int l=0;l<i-1;l++)bit1[l]=bit1[l+1];
    bit1[i-1]=tmp;
    tmp=0;
    for(int l=i-1;l>=0;l--) {
      tmp*=10;
      tmp+=bit1[l];
    }
    myset.insert(tmp);
  }
  if(myset.count(fucka))return true;
  else return false;
}
int main() {
  int cas,a,b;
  freopen("C.in","r",stdin);
  freopen("C.out","w",stdout);
  scanf("%d",&cas);

  for(int t=1;t<=cas;t++) {
    scanf("%d%d",&a,&b);
    //memset(flag,false,sizeof(flag));
    int res=0;
    for(int i=a;i<=b;i++) {
      for(int j=i+1;j<=b;j++) {
        if(judge(i,j))res++;
      }
    }
    printf("Case #%d: %d\n",t,res);
  }
  //printf("%d\n",judge(12,21));
  return 0;
}
