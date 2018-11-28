#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

double probA[99999];
int bitcheck[100001];

double solve(int a,int b,int c);

int main(){

  int T;cin>>T;
  for(int i=0;i<T;i++){
    memset(probA,0,sizeof(probA));
    int A,B;
    cin>>A>>B;
    for(int j=0;j<A;j++){
      cin>>probA[j];
    }

    double ans=(double)(B+2);
    for(int k=0;k<A;k++){
      ans=min(ans,solve(A,B,k));
    }

    cout<<"Case #"<<i+1<<": ";printf("%.6lf",ans);cout<<endl;
  }

  return 0;
}

double solve(int a,int b,int c){
  memset(bitcheck,0,sizeof(bitcheck));
  double res=0.0;

  for(int i=0;i<1<<a;i++){
    for(int j=0;j<a;j++)bitcheck[j]=i>>j&1;
    double tt=1.0;
    for(int k=0;k<a;k++){
      if(bitcheck[k]==1)tt*=probA[k];
      else tt*=(1.0-probA[k]);
    }

    int cnt=c+c+b-a+1;
    for(int s=0;s<c;s++){
      bitcheck[(a-1)-s]=1;
    }
    for(int t=0;t<a;t++){
      if(bitcheck[t]==0){cnt+=(b+1);break;}
    }
    res+=(cnt*tt);
  }

  return res;

}
