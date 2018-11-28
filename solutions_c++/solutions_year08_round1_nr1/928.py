#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>


using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;
typedef long double LD;


#define REP(i,n) for (int i=0; i<(n); ++i)


using namespace std;

int readint()
{
	string temp;
	int retVal;
	getline(cin, temp);
	stringstream ss(temp);
	ss>> retVal;
	return retVal;
}

int main()
{

	int noOfCases = readint();
    
	for(int i = 0; i < noOfCases; i++)
	{
        vector<int> v1;
        vector<int>  v2;
        __int64 x = 0;
        int numofVec;
        cin >> numofVec;
        REP(j,numofVec)
		{
		   int a;
           cin >> a;
           v1.push_back(a);
		}
        REP(j,numofVec)
		{
		   int a;
           cin >> a;
           v2.push_back(a);
		}
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        REP(j,numofVec)
		{
          x += v1[j]*v2[numofVec - j - 1];
		}
   
		cout << "Case #" << i + 1 << ": " << x << endl;
	}
}