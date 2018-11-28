#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

int main(){

  int T;cin>>T;
  for(int t=0;t<T;t++){//# of test;
    int N;cin>>N;//# of students;
    long long W;long long l; cin>>W>>l;//w,l;
    long long r[1000];
    vector<long long>d;
    for(int i=0;i<N;i++){cin>>r[i];d.push_back(r[i]);}
    sort(d.begin(),d.end(),greater<long long>());
    long long x[1000];long long y[1000];
    x[0]=0;y[0]=0;
    
    int n=1;//now;
    long long c=0;//center;
    long long nc=d[0];//next center - d[i];
    long long nw=d[0];//now x;
    while(n<N){
      if(nw+d[n]<=W){
	x[n]=nw+d[n];y[n]=c;
	nw+=2*d[n];n++;
      }
      else{nw=-d[n];c=nc+d[n];nc=c+d[n];}
    }

    long long resx[1000];long long resy[1000];
    bool used[1000];memset(used,true,sizeof(used));
    for(int i=0;i<N;i++){
      for(int k=0;k<N;k++){
	if(used[k] && d[i]==r[k]){
	  used[k]=false;
	  resx[k]=x[i];
	  resy[k]=y[i];
	  break;
	}
      }
    }

    string g="Case #";
    int L=t+1;
    if(L<10)g+=(char)(L+'0');else{g+=(char)(L/10+'0');g+=(char)(L%10+'0');}
    g+=":";
    cout<<g;
    for(int i=0;i<N;i++){cout<<' '<<resx[i]<<' '<<resy[i];}
    cout<<endl;
  }
  return 0;
}
