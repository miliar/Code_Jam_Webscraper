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
  long long vals[2];
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
char temp[1000];
long long getUglys(char *p, int len,long long res,bool first)
{
	long long result=0;
	if (len==0)
	{
		if (res%2==0)
			return 1;
		if (res%3==0)
			return 1;
		if (res%5==0)
			return 1;
		if (res%7==0)
			return 1;
		if (res==0)
			return 1;
	}
	else
	{
	for (int i=1;i<=len;i++)
	{
		memcpy(temp,p,i);
		temp[i]=0;
		long long num=0;
		sscanf(temp,"%lld",&num);
		MyKey key;
    key.vals[0]=len-i;
    key.vals[1]=res+num;
    map<MyKey, int, MyKey>::iterator cur  = memory.find(key);
    if (cur!=memory.end())
    {
       result+=cur->second;
    }
    else
    {
      long long temp=getUglys(p+i,len-i,res+num,false);
      memory[key]=temp;
			result+=temp;
		}		

		if (!first)
		{
			key.vals[0]=len-i;
			key.vals[1]=res-num;
			cur  = memory.find(key);
			if (cur!=memory.end())
			{
				 result+=cur->second;
			}
			else
			{
				long long temp=getUglys(p+i,len-i,res-num,false);
				memory[key]=temp;
				result+=temp;
			}		
		}
	}
	}
	return result;
}

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	int caseCount; 
	cin >> caseCount;
	char string[2000];
	for(int caseId=1;caseId<=caseCount;caseId++) 
	{
		cin >> string;
		/*cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    */
		memory.clear();
		long long result=getUglys(string,strlen(string),0,true);
		cout << "Case #" << caseId << ": " << result << endl;
	}
	
	return 0;
}
