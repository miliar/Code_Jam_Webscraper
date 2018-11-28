#include <iostream>
#include <algorithm>
using namespace std;

inline int mmin(const int &a, const int &b){
	return a<b?a:b;
}

int S, R, RP[10];
bool released[101];
int test();

int main(){
	released[0]=1;
	int N, rst;
	cin>>N;
	for(int n=0; n<N; n++){
//		for(int i=1; i<=R; ++i)
//			released[i]=0;
		cin>>S>>R;
		rst=R*S;
		released[S+1]=1;
		for(int i=0; i<R; ++i){
			cin>>RP[i];
		}
		sort(RP, RP+R);
		rst=test();
		while(next_permutation(RP, RP+R)){
			rst=mmin(rst, test());
		}
		released[S+1]=0;
		cout<<"Case #"<<n+1<<": "<<rst<<'\n';
	}
	return 0;
}

int test(){
	int rst=0;
	for(int i=0; i<R; ++i){
		released[RP[i]]=1;
		for(int j=RP[i]-1; released[j]!=1; --j)
			++rst;
		for(int j=RP[i]+1; released[j]!=1; ++j)
			++rst;
	}
	for(int i=0; i<R; ++i){
		released[RP[i]]=0;
	}
	return rst;
}