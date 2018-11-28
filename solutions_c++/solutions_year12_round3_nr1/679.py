#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

int main(){

  int T;cin>>T;
  for(int t=0;t<T;t++){//# of test;
    int data[1001][1001];memset(data,0,sizeof(data));
    int N;cin>>N;//# of classes;
    for(int i=1;i<=N;i++){
      int M;cin>>M;
      for(int k=1;k<=M;k++){
	int n;cin>>n;
	data[n][i]++;//# of path ([i] -> [n]);
      }
    }
    //topo;
    vector<int> order;
    bool used[1001];memset(used,true,sizeof(used));
    for(int n=0;n<N;n++){
      for(int i=1;i<=N;i++){
	if(!used[i])continue;
	int r=0;
	for(int k=1;k<=N;k++)if(used[k])r+=data[k][i];
	if(r==0){
	  order.push_back(i);
	  used[i]=false;
	  break;
	}
      }
    }
    
    reverse(order.begin(),order.end());
    //    for(int i=0;i<N;i++)cout<<order[i]<<'*';cout<<endl;
    //greedy;
    for(int i=0;i<N;i++){
      int n=order[i];
      for(int k=1;k<=N;k++){
	//nを子孫に持つkにnの子孫のデータを渡す。
	if(data[k][n]>0)for(int l=0;l<N;l++)data[k][l]+=data[n][l];
      }
    }
    bool ok=false;
    for(int i=1;i<=N;i++){
      for(int j=1;j<=N;j++){
	//	cout<<i<<"->"<<j<<' '<<data[i][j]<<endl;
	if(data[i][j]>1)ok=true;
      }
    }
    string g="Case #";
    int L=t+1;
    if(L<10)g+=(char)(L+'0');else{g+=(char)(L/10+'0');g+=(char)(L%10+'0');}
    g+=": ";
    cout<<g;
    if(ok)cout<<"Yes";else cout<<"No";
    cout<<endl;
  }
  return 0;
}
