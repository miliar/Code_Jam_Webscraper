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

bool check_filled(vector<bool> check)
{
	for(int i=0; i<(int)check.size(); i++)
	{
		if(check[i] == false)
			return false;
	}
	return true;
}


int main()
{
	string temp;
	int numCases;
	getline(cin, temp);
	stringstream ss(temp);
	ss >> numCases;

	for(int c=1; c<=numCases; c++)
	{
		int S, Q;
		getline(cin, temp);
		stringstream ss_in(temp);
		ss_in >> S;

		vector<string> SS;
		for(int i=0; i<S; i++)
		{
			getline(cin, temp);
			SS.push_back(temp);
		}

		getline(cin, temp);
		stringstream ss_in2(temp);
		ss_in2 >> Q;

		vector<string> QQ;
		for(int i=0; i<Q; i++)
		{
			string temp;
			getline(cin, temp);
			QQ.push_back(temp);
		}

		int ans = 0;
		vector<bool> check(S, false);

		for(int i=0; i<Q; i++)
		{
			for(int j=0; j<S; j++)
			{
				if(SS[j] == QQ[i])
				{
					check[j] = true;
					if(check_filled(check))
					{
						ans++;
						for(int ii=0; ii<S; ii++) check[ii] = false;
						check[j] = true;
					}
					goto endend;
				}
			}
endend:;
		}

		cout << "Case #" << c << ": " << ans << endl;
	}

	return 0;
}
