#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <memory.h>
#include <iostream>
using namespace std;
typedef long long lint;
vector<lint> p;

int root(vector<int> & a, int i){
	vector<int > tmp;
	while (a[i]!=i){
		tmp.push_back(i);
		i = a[i];
	}
	for(int j = 0; j<tmp.size(); ++j)
		a[tmp[j]] = i;
	return i;
}
void merge (vector<int> & a, int i, int j){
	i = root(a,i);
	j = root(a,j);
	if (i!=j){
		a[i] = j;
	}
}
int main(){
	ifstream in("B-large.in");
	ofstream out("output.txt");
	int N;
	in >> N;
	p.push_back(2);
	for(int j = 3; j< 1000000; j+=2){
		int k = 1;
		while (k < (int)p.size() && p[k]*p[k] <= j && j%p[k]!=0)
			++k;
		if (k>=(int)p.size() || p[k]*p[k]>j)
			p.push_back(j);
	}
	cout<<p.size()<<endl;
	//return 0;
	for(int t = 0; t<N; ++t){
		cout<<"\t"<<t<<endl;
		lint A,B,P;
		in >> A >> B >> P;
		int T = B-A;
		int k = 0;
		while (k<(int)p.size() &&p[k]<P)
			++k;
		vector<int> g(B-A+1,-1);
		for(int i =0; i< g.size(); ++i)
			g[i] = i;
		for(int i = k; i<(int)p.size() && p[i]<= T; ++i){
			int n = (A/p[i])*p[i]-A;
			if (n<0) n+=p[i];
			int v = g[n];
			n+=p[i];
			while(n<g.size()){
				merge(g,g[n],v);
				n+=p[i];
			}
		}
		int ans = 0;
		for(int i =0; i< g.size(); ++i)
			if (root(g,i) == i) ++ans;
		out<<"Case #"<<t+1<<": "<<ans<<endl;
	}
	return 0;
}