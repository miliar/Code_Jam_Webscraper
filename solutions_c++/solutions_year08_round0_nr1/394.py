#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int MAXS=101;
const int MAXQ=1002;
const int INFTY=10000000;

int f[MAXQ][MAXS];
vector<string> engine(0);
vector<string> query(0);
int ans;
int n,q,s;

int init(){
	engine.resize(0);
	query.resize(0);
	memset(f,0,sizeof(f));
	cin>>s;
	string tmp;
	getline(cin,tmp);
	for(int i=0;i<s;++i){
		getline(cin,tmp);
		engine.push_back(tmp);
	}
	cin>>q;
	getline(cin,tmp);
	for(int i=0;i<q;++i){
		getline(cin,tmp);
		query.push_back(tmp);
	}
	return 0;
}

int solve(){
	for(int i=1;i<=q;++i){
		for(int j=0;j<s;++j){
			f[i][j]=INFTY;
			if(query[i-1]==engine[j]) continue;
			for(int k=0;k<s;++k){
				if(k!=j && f[i-1][k]+1<f[i][j]){
					f[i][j]=f[i-1][k]+1;
				}
			}
			if(f[i-1][j]<f[i][j]){
				f[i][j]=f[i-1][j];
			}
		}
	}
	ans=INFTY;
	for(int i=0;i<s;++i){
		if(f[q][i]<ans) ans=f[q][i];
	}
	return 0;
}

int show(int n){
	cout<<"Case #"<<n<<": "<<ans<<endl;
	return 0;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>n;
	for(int i=0;i<n;++i){
		init();
		solve();
		show(i+1);
	}
	return 0;
}
