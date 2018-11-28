#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>

using namespace std;

struct data{
  set<double> i;
  int a;
  int b;
};

int main(){
  int T,N;
  data d[1000];
  cin >> T;
  for(int t=1;t<=T;t++){
    cin >> N;
    int p=0;
    int ans=0;
    for(int i=0;i<N;i++){
      int a,b,tmp;
      cin >> a >> b;
      d[p].a=a;
      d[p].b=b;
      d[p].i.clear();
      for(int j=0;j<p;j++){
	if( ( d[j].a - a ) * ( d[j].b - b )<0){
	  d[j].i.insert((double)(abs(d[j].b-b))/(abs(d[j].a-a)));
	  d[p].i.insert((double)(abs(d[j].b-b))/(abs(d[j].a-a)));
	}
      }
      p++;
    }
    for(int i=0;i<N;i++)
      ans+=d[i].i.size();
    printf("Case #%d: %d\n",t,ans/2);
  }
  return 0;
}
