#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <list>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<string> stringVec;

struct MyKey
{
  int vals[3];
  bool operator()(const MyKey& s1, const MyKey& s2) const
  {
    return memcmp(s1.vals,s2.vals,sizeof(vals)) < 0;
  }
};

map<MyKey, int, MyKey> memory;

/*MyKey key;
          key.vals[0]=engineId;
          key.vals[1]=queryId;
          key.vals[2]=switches;
          key.vals[3]=depth+1;
          map<MyKey, int, MyKey>::iterator cur  = memory.find(key);
          if (cur!=memory.end())
          {
            tempSwitches=cur->second;
          }
          else
          {
            tempSwitches=calculateSwitchesForSingleCase(queries,engines,engineId,queryId,switches,depth+1);
            memory[key]=tempSwitches;
          }		
    sort(array1.begin(), array1.end());
		sort(array2.begin(), array2.end(), greater<long long>());
          */

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	int caseCount; 
	cin >> caseCount;
	for(int caseId=1;caseId<=caseCount;caseId++) 
	{

		ll P,K,L;
		cin >> P >>K >>L;
		vi freq;
		freq.clear();
		freq.resize(L);
		for (int i=0;i<L;i++)
		{
			cin>>freq[i];
		}
		sort(freq.begin(), freq.end());
		long long result=0;
		int currentKey=1;
		int currentPos=1;
		for (int i=(freq.size()-1);i>=0;i--)
		{
			result+=(currentPos*freq[i]);
			currentKey++;
			if (currentKey>K)
			{
				currentKey=1;
				currentPos++;
			}
		}
		cout << "Case #" << caseId << ": " << result << endl;
	}
	
	return 0;
}
