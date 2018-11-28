#include <vector>
#include <string>
#include <map>
#include <set>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cassert>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef map<int,int> MII;
typedef pair<int,int> PII;
typedef vector<PII>  VPII;
typedef set<int> SI;



LL doit(){
	LL cnt=0;
	int p,k,l;
	scanf("%d %d %d",&p,&k,&l);
	VPII v;
	for(int i=0;i<l;i++){
		int in;
		scanf("%d",&in);
		v.push_back(PII(-in,i));
	}
	sort(v.begin(),v.end());
	VI vi(k,0);
	for(int i=0;i<l;i++){
		vi[i%k]++;
		int erg=vi[i%k]*(-v[i].first);
		cnt+=(LL)erg;
	}
	return cnt;
}	

int main(){
	int num_cases;
	cin >> num_cases;
	for(int kase=1;kase<=num_cases;kase++){
		cout << "Case #"<<kase<<": "<< doit()<<endl; 
	}	
	return 0;
}	
