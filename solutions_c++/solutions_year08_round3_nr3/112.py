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
typedef vector<long long> vl;

struct MyKey
{
  long long vals[2];
  bool operator()(const MyKey& s1, const MyKey& s2) const
  {
    return memcmp(s1.vals,s2.vals,sizeof(vals)) < 0;
  }
};

map<MyKey, long long, MyKey> memory;

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

long long  countSeqForCase(vl &speeds,int idx,long long lastSpeed)
{
	long long result=1;
	for (unsigned int speedId=idx;speedId<speeds.size();speedId++)
  {
		if (speeds[speedId]>lastSpeed)
		{
			MyKey key;
      key.vals[0]=speedId+1;
      key.vals[1]=speeds[speedId];

      map<MyKey, long long, MyKey>::iterator cur  = memory.find(key);
      if (cur!=memory.end())
      {
        result+=cur->second;
				result=result%1000000007;
      }
      else
      {
				long long temp=countSeqForCase(speeds,speedId+1,speeds[speedId]);
        result+=temp;
				result=result%1000000007;
        memory[key]=temp;
      }		
		}
	}
	return result;
}

long long  countSeq(vl &speeds)
{
	long long result=0;
	memory.clear();
	for (int i=0;i<speeds.size();i++)
	{
		result+=countSeqForCase(speeds,i,speeds[i]);
		result=result%1000000007;
	}
	return result;
}

int main() {
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	int caseCount; 
	cin >> caseCount;
	for(int caseId=1;caseId<=caseCount;caseId++) 
	{
		ll n, m, X, Y, Z;
		vl A;
		vl speeds;
		cin >> n >>  m >>  X >>  Y >> Z;
		A.clear();
		A.resize(m);
		for (int i=0;i<m;i++)
		{
			cin >> A[i];
		}

		speeds.resize(n);
		for (int i=0;i<n;i++)
		{
			speeds[i]=A[i%m];
			A[i%m] = (X * A[i%m] + Y * (i + 1))%Z;
		}

		long long result=(countSeq(speeds)%1000000007);
		cout << "Case #" << caseId << ": " << result << endl;
	}
	
	return 0;
}
