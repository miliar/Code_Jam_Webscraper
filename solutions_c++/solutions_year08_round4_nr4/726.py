#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define CLEAR(x,with) memset(x,with,sizeof(x))  

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
	string temp;
	int numCases;
	getline(cin, temp);
	stringstream ss(temp);
	ss >> numCases;

	for(int c=1; c<=numCases; c++)
	{
		int k;
		getline(cin, temp);
		stringstream ss(temp);
		ss >> k;

		string S;
		getline(cin, temp);
		stringstream ss_in(temp);
		ss_in >> S;

		vector<int> v; 

		 for(int i = 0; i < k; i++) { 
			  v.push_back(i); 
		 } 

		 int ans = 10000;

		 do
		 {
			 vector<int> SS;

			 for(int i=0; i<(int)S.size() / k; i++)
			 {
				 for(int j=0; j<k; j++)
				 {
					 SS.push_back( S[i * k + v[j]] );
				 }
			 }

			 int ansans = 0;
			 int prev = -1;

			 for(int i=0; i<(int)SS.size(); i++)
			 {
				 if(SS[i] == prev) continue;
				 else
				 {
					 prev = SS[i];
					 ansans++;
				 }
			 }
			 ans = min(ans, ansans);
			  
		 } while(next_permutation(all(v))); 
		

		cout << "Case #" << c << ": " << ans << endl;
	}

	return 0;
}
