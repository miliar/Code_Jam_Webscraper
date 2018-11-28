#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

int main(){

  int T;cin>>T;
  for(int t=0;t<T;t++){//# of test;
    int N;cin>>N;//# of vine;
    long long d[10000];
    long long l[10000];
    long long data[10000];
    for(int i=0;i<N;i++){
      cin>>d[i]>>l[i];data[i]=-1;
    }
    data[0]=d[0];
    long long D;cin>>D;
    //greedy?
    for(int i=0;i<N;i++){
      for(int k=i+1;k<N;k++){//move i to k;
	if(d[k] <= d[i]+data[i]){//can reach;
	  data[k]=max(data[k], min(l[k],d[k]-d[i]));
	}
      }
    }
    bool ok=false;
    for(int i=0;i<N;i++){//can goal?
      //     cout<<d[i]<<' '<<data[i]<<endl;
      if(d[i]+data[i]>=D)ok=true;
    }

    string g="Case #";
    int L=t+1;
    if(L<10)g+=(char)(L+'0');else{g+=(char)(L/10+'0');g+=(char)(L%10+'0');}
    g+=": ";
    cout<<g;
    if(ok)cout<<"YES";else cout<<"NO";
    cout<<endl;
  }
  return 0;
}
