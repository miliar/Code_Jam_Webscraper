#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

int N,T;

int gcd(int a,int b){
  if(b==0)return a;
  else return gcd(b,a%b);
}

int main(){
  int k;
  for(k=1,scanf("%d",&T);k<=T;k++){
    scanf("%d",&N);

    vector<long long int> t;
    long long int m=(long long int)1e12;
    for(int i=0;i<N;i++){
      long long int tmp;
      scanf("%lld",&tmp);
      m = min(tmp,m);
      t.push_back(tmp);
    }

    sort(t.begin(),t.end());

    for(int i=0;i+1<t.size();i++)
      t[i]=t[i+1]-t[i];

    int i;
    for(i=0;i+2<t.size();i++){
      t[i+1]=gcd(t[i],t[i+1]);
    }
 
    long long int ans=(bool)i?t[i]:t[0];
 
    ans = m%ans?ans-(m%ans):0 ;

    printf("Case #%d: %lld\n",k,ans);
  }
  return 0;
}
