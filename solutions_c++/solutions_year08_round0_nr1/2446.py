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
    map<string,int> sm;
    int noOfCases = readint();

    for(int i = 0; i < noOfCases; i++)
    {

        int sn = readint();
		int switcha = 0;
//        map<string, int> sem;
        for(int j=0; j < sn; j++)
        {
            string a;
            getline(cin, a);
            sm[a]=0;
        }
        int m = 0;
        int qn = readint();
        int count = 0;
		for(int j=0; j < qn; j++)
        {
            string a;
            getline(cin,a);
			if (sm.find(a) != sm.end())
			{
				if (sm[a]==1)
				{
					continue;
				}
				else
				{
					if (count >= sn -1)
			        {
						for(map<string,int>::iterator it= sm.begin(); it != sm.end(); it++)
						{
							it->second = 0;
						} 
						count = 1;
                        ++switcha;
					
					}
					else 
					{
						++count;
					}
					sm[a] = 1;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << switcha << endl;
	}
}