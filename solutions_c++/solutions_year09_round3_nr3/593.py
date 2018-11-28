#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<list>
#include<iterator>
#include<map>
#include<algorithm>
#include<cctype>
#include<cmath>
#include<numeric>
#include<strstream>


using namespace std;

#define FOR(i,a,b) for(long int i=a; i<b ; i++)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define VI vector<int>

int getBribe(vector<int> &v,int cell) {
	int bribe=0;
	FOR(i,cell+1,v.size()) {
		if(v[i] == 0)
			break;
		else bribe++;
	}
	for(int i=cell-1 ; i>0 ; i--) {
		if(v[i] == 0)
			break;
		else bribe++;
	}
	return bribe;

}

int main() {
	int N,caseN=0;
	for(cin >> N ; caseN<N; caseN++) {
		int P,Q;
		cin >> P >> Q;
		vector<int> p(Q,0);
		vector<int> v(P+1,1);
		FOR(i,0,Q)  { cin >> p[i];}
		int sum=0;
		int ret=100000;
		sort(p.begin(),p.end());
		do
		{
			
			FOR(i,0,p.size()) {
				//p[i] is released
				v[p[i]] = 0;
				sum += getBribe(v,p[i]);

			}
			ret = min(ret,sum);
			sum=0;
			FOR(i,0,v.size()) v[i]=1;


		}
		while (next_permutation(p.begin(),p.end()));
		cout << "Case #" << caseN+1 << ": " << ret << endl;
	}

	return 0;
}	