#include<iostream>
using namespace std;
struct aaa{
  int next;
  long long value;
}data[1000];
int g[1000];

int main(){
  int t;
  cin >> t;
  
  int x=0;
  for(;x<t;x++){
    int r,k,n;
    cin >> r >> k >> n;
    for(int i=0;i<n;i++){
      cin >> g[i];
      data[i].next=-1;
    }
    int start=0;
    long long ans=0;
    for(int i=0;i<r;i++){
      if(data[start].next!=-1){
	ans+=data[start].value;
	start=data[start].next;
      }else{
	int sum=0,j;
	for(j=start;;){
	  sum+=g[j];
	  if(sum!=g[start]&&j==start)break;
	  if(sum>k)break;
	  else j=(j+1)%n;
	}
	sum-=g[j];
	ans+=sum;
	data[start].value=sum;
	data[start].next=j;
	start=j;
      }
    }
    printf("Case #%d: ",x+1);
    cout << ans << endl;
  }

  return 0;
}
