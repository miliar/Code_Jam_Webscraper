#include<iostream>

using namespace std;
int ans=-1;
int n;
int in[100];



void calc(int p,int sum1,int sum2,int sum3){
  
  if(p==n){
    if(sum1==sum2&&sum1!=0){
      if(sum3>ans)ans=sum3;
      return;
    }
  }else{
    calc(p+1,sum1^in[p],sum2,sum3+in[p]);
    calc(p+1,sum1,sum2^in[p],sum3);
  }
  return;
}

int main(){
  int t; cin >> t;
  for(int i=0;i<t;i++){
    cin >> n; for(int j=0;j<n;j++)cin>>in[j];
    ans=-1;
    calc(0,0,0,0);
    printf("Case #%d: ",i+1);
    if(ans==-1)puts("NO");
    else printf("%d\n",ans);
  }

  return 0;
  
}
