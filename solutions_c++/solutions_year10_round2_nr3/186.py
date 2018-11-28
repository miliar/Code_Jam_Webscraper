#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>
#include<set>
#define md 100003

using namespace std;
vector<vector<int> > sav;
vector<vector<long long> > cc;

void do_cc(int n, int m){
	cc.clear(); cc.resize(m+1, vector<long long>(n+1, 0));
	for(int i=0; i<=n; i++){ cc[0][i]=1; }
	for(int i=1; i<=n; i++){
		for(int j=1; j<=i && j<=m; j++){
			cc[j][i] = (cc[j][i-1]+cc[j-1][i-1])%md;
		}
	}
}

int f(int n, int len){
	if(len==1)return 1;
//	cout<<n<<" "<<len<<" \n"; cout.flush();
	if(sav[n][len]>=0) return sav[n][len];

	int res=0;

	for(int i=1; i<len; i++){
		int nnum = n-len-1;
		int npos = len-i-1;
//		cout<<npos<<" "<<nnum<<"h\n";cout.flush();
		if(npos<=nnum){
			int tmp = (cc[npos][nnum]*f(len, i))%md;
			res+=tmp;
			res%=md;
		}
	}
	sav[n][len]=res;
	return res;
	
}
int main(){
	int C, n;
	cin>>C;
	do_cc(500, 500);
	for(int i=0; i<C; i++){
		//cin>>wrds[i]; 
		cin>>n;
		sav.clear(); sav.resize(n+1, vector<int> (n+1,-1));
		int res = 0;
		for(int j=1; j<n; j++){
			res+=f(n, j);
			res%=md;

		}
		cout<<"Case #"<<i+1<<": " <<res<<"\n";
	}
	
}
