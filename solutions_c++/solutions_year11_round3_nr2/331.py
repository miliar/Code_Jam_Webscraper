#include <iostream>
#include <math.h>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX(a, b) (((a)<(b))?(b):(a))
#define LL long long
LL L, t, N, C;
LL A[1000001];
LL P[1000001];
bool boosted[1000001];

LL getNeeded(void){
	LL total=0;
	for(int i=0;i<N;++i){
		LL req=P[i+1]-P[i];
		if(boosted[i]){//boosted
			if(t<=total){
				total+=req/2;
			}else if(t<total+req){
				total+=(t-total)+(req-(t-total))/2;
			}else{
				total+=req;
			}
		}else{
			total+=req;
		}
	}
	return total;
}

void solve(int c){
	P[0]=0;
	for(int i=1, prev=0;i<=N;++i, prev=(prev+1)%C){
		P[i]=P[i-1]+A[prev];
	}
	int first=N-1;
	LL total=0;
	for(int i=0;i<N;++i){
		LL req=P[i+1]-P[i];
		if(t<total+req){
			first=i;
			break;
		}
		total+=req;
	}
	vector<pair<LL, int> > v;
	v.push_back(make_pair((P[first+1]-P[first]-(t-total)), first));
	for(int i=first+1;i<N;++i){
		v.push_back(make_pair(P[i+1]-P[i], i));
	}
	sort(v.rbegin(), v.rend());
	memset(boosted,0, sizeof(boosted));
	for(int i=0;i<L && i<v.size();++i){
		boosted[v[i].second]=true;
	}
	LL sol=getNeeded();

	cout<<"Case #"<<c<<": "<<sol<<endl;
	

}


int main(int argc, char *argv){
	int numCases;
	cin>>numCases;
	for(int c=0;c<numCases;++c){
		cin>>L>>t>>N>>C;
		for(int i=0;i<C;++i){
			cin>>A[i];
			A[i]*=2;
		}
		solve(c+1);
	}
	return 0;
}
