#include<iostream>
#include<vector>
#include<string>
#include <iomanip>

using namespace std;
int N, C;
vector<double > sav;
vector<vector<long long> > cc;

void do_cc(){
	cc.clear(); cc.resize(41, vector<long long>(41, 0));
	for(int i=0; i<41; i++){ cc[0][i]=1; cc[i][i]=1; }
	for(int i=2; i<41; i++){
		for(int j=1; j<i; j++){
			cc[j][i] = cc[j][i-1]+cc[j-1][i-1];
		}
	}
}

double rec(int L){
	if(L==0) return 0;
	if(sav[L]!=-1) return sav[L];
	double res=0;
	int start=0; long long div; double add;
	if(N>C-L){
		div = cc[N][C];
		add=1;
	}else{
		start=1;
		div = cc[N][C]-cc[N][C-L];
		add = (double)cc[N][C]/div;
	}
	for(int i=1; i<=N; i++){
		if(i>L || N-i>C-L) continue;
		res+=(double)cc[i][L]*cc[N-i][C-L]*rec(L-i);
	}
	res/=div; res+=add;
	
	sav[L]=res;
	return res;
}

int main(){
	int T;
	cin>>T;
	do_cc();
	for(int i=0; i<T; i++){
		double res = 0;
		cin>>C>>N;
		sav.clear(); sav.resize(C+1, -1);
		res = rec(C);
		cout<<"Case #"<<i+1<<": "<<res<<"\n";
	}
	
}
