#include <iostream>
#include <map>
#include <windows.h>
using namespace  std;

INT64 L,t,N,C;
INT64 dis[2000];
INT64 compute() {
	map<INT64,INT64> SS;
	cin>>L>>t>>N>>C;
	for(INT64 i = 0;i<C;i++)
		cin>>dis[i];
	INT64 total = 0;
	for(INT64 i= 0;i<N;i++) {
		SS[dis[i%C]]++;
		total += dis[i%C];
	}
	if (t/2>=total) {//no light
		return total*2;
	}
	INT64 used = t/2;
	INT64 index = 0;
	while (used) {
		INT64 toreduce = dis[index%C];
		if (toreduce<=used) {
			used-= toreduce;
			SS[toreduce]--;
		} else {
			SS[toreduce]--;
			SS[toreduce-used]++;
			used = 0;
		}
		index++;
	}
	INT64 remain = L;
	INT64 acc = 0;
	INT64 ret = t;
	for(map<INT64,INT64>::reverse_iterator it = SS.rbegin();it!=SS.rend();it++) {
		INT64 d = it->first;
		INT64 count = it->second;
		ret += d*count*2;
		if (count>remain) {
			acc+=d*remain;
			remain=0;
		} else {
			remain-=count;
			acc+=d*count;
		}
	}
	ret-=acc;
	return ret;
}
int main() {
	int ncase;
	cin>>ncase;
	for(int i = 0;i<ncase;i++) {
		cout<<"Case #"<<i+1<<": ";
		cout<<compute();
		cout<<"\n";
	}
}