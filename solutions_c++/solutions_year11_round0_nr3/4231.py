#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define PB push_back
#define sz size()


/////////////////////////////////////////////////////////////////////////////////

int main()
{
	int T;
	cin >> T;
	REP(Case, T)
	{
		int N;
		cin>>N;
		vector<int> v;
		REP(i,N) {int tmp; cin>>tmp; v.PB(tmp); }
		sort(v.begin(), v.end());
		int t=0;
		REP(i,v.sz) t^=v[i];
		cout<<"Case #"<<Case+1<<": ";
		if(t)
			cout<<"NO"<<endl;
		else
		{
			int total=0;
			for(int i=1; i<v.sz; i++) total+=v[i];
			cout<<total<<endl;
		}
	}

	return 0;
}
