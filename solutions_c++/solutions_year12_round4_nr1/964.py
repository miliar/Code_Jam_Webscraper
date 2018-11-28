#include<iostream>
#include<vector>
#include<queue>
#include<string>
#include<algorithm>
using namespace std;

#define LL long long
#define MP make_pair

int T,N,D;
int ma[20000];
int d[20000];
int l[20000];
int main(){
	cin>>T;
	for(int ca=1; ca<=T; ca++){
		cout<<"Case #"<<ca<<": ";
		cin>>N;
		for(int i=0; i<N; i++)
			cin>>d[i]>>l[i];
		cin>>D;	
		bool suc=false;
		for(int i=0; i<N; i++)
			ma[i] = 0;
		queue<int> q;
		q.push(0);
		q.push(d[0]);
		ma[0] = d[0];	
		while(!q.empty()){
			int pos=q.front();q.pop();	
			int dis=q.front();q.pop();	
			if(d[pos] + dis >= D){
				suc = true;
				break;
			} 
			for(int i=pos+1; i<N; i++){
				if(d[pos]+dis>=d[i]){
					int nd=min(l[i],d[i] - d[pos]);
					if(nd>ma[i]){
						ma[i] = nd;
						q.push(i);
						q.push(nd);
					}
				}
			}
		}
		if(suc)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}
