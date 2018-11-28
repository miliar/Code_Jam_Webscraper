#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <list>
#include <bitset>
#include <cstring>
#include <sys/time.h>
#include <sys/signal.h>
#include <unistd.h>
#include <stack>
#include <cmath>
#include <map>
#include <streambuf>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
#define FOR(x,a,e) for( x=a; x<=(e); ++x)
#define FORL(x,a,e) for(int x=a; x<(e); ++x)
#define FORD(x,a,e) for(int x=a; x>=(e); --x)
#define FORDG(x,a,e) for(int x=a; x>(e); --x)
#define REP(x,n) for(int x =0;x<(n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second


int main()
{
	string pattern = "welcome to code jam";

	int i,n,t;

	string number;
	getline(cin, number);
	stringstream iss_n(number);
	iss_n >> n;

	FORL(t,0,n)
	{
    	string data;
    	getline(cin,data);

    	map<string, vector<int> > occurences;
    	FORL(i,0,SIZE(pattern))
    	{
    		stringstream iss;
    		iss << pattern[i];
    		string el;
    		iss >> el;
    		if ( occurences.find(el) == occurences.end() )
    		{
    			occurences[el] = vector<int>();
    			int j;
    			FORL(j,0,SIZE(data))
    			{
    				if (data[j] == pattern[i]) (occurences[el]).PB(j);
    			}
    		}
    	}

    	int level = 0;
    	int res = 0;
    	vector<vector<int>  >positions(19,vector<int>());
    	FOR(level,0,18)
    	{
    		stringstream iss;
			iss << pattern[level];
			string el;
			iss >> el;
    		if (level == 0)
    		{
    			vector<int> v;
    			FOREACH(it,occurences[el])
					v.PB(*it);
    			positions[0] = v;
    		}
    		else
    		{
    			vector<int> v;
    			FOREACH(it, positions[level-1])
    			{
    				FOREACH(it2, occurences[el])
    				{
    					if(*it2 > *it)
    						v.PB(*it2);
    				}
    			}
    			positions[level] = v;
    		}

    		/*cout<<"SIZE = "<<SIZE(positions[level])<<endl;
    		cout<<"ELEMENT `"<<el<<"` ON POSITIONS  :"<<endl;
    		FOREACH(it, positions[level])
    		{
    			cout<<*it<<endl;
    		}*/
    	}


    	res = SIZE(positions[18]) % 10000;
    	stringstream iss_res;
    	if (res < 10)
    		iss_res<<"000"<<res;
    	else if(res<100)
    		iss_res<<"00"<<res;
    	else if(res<1000)
    		iss_res<<"0"<<res;
    	else
    		iss_res<<res;

    	cout<<"Case #"<<t+1<<": "<<iss_res.str()<<endl;
	}
}
