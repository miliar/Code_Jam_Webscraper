
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
 
using namespace std;

vector<string> engine;
vector<string> queries;
map<string,int> mapping;

int solve(string current,int index,int cnt)
{
	if(current.compare(queries[index])!=0)
	{
		if(index == (queries.size()-1))
			return cnt;
		return solve(current,index+1,cnt);
	}
	else
	{
		int d[100];
		for(int i=0;i<engine.size();i++)
			d[i] = 0;

        d[mapping[(char*)current.c_str()]] =-1;
		//cout <<mapping[current.c_str()]<<endl;
			for(int j=index;j<queries.size();j++)
				if(d[mapping[queries[j]]]==0)
					d[mapping[queries[j]]] = j-index;
			int m=0;
			int n=0;
			for(int k=0;k<engine.size();k++)
			{
				if(d[k] ==-1)
					continue;
				if(d[k] ==0 )
					return cnt+1;
                if(d[k]>=m)
				{
					m = d[k];
					n=k;
				}
			}
			return solve(engine[n],index+m,cnt+1);
	}
	return cnt;

}
	

int main()
{
	string s;
    ofstream outfile ("output.txt");
    int N;
    getline(cin,s);
	sscanf(s.c_str(),"%i",&N);
	int c=1;
	while(c<=N)
	{
		mapping.clear();
		engine.clear();
		queries.clear();

		int ans =65533;
		int n,q;
		getline(cin,s);
		sscanf(s.c_str(),"%i",&n);
		for(int i=0;i<n;i++)
		{
			string tmp;
			getline(cin,tmp);
			engine.push_back(tmp);
			mapping[engine.back()] = i;
			//cout << mapping["Googol Sweden"] << endl;
		}
	    getline(cin,s);
		sscanf(s.c_str(),"%i",&q);
		if(q==0)
		{
			ans=0;
			goto end;
		}
		for(int i=0;i<q;i++)
		{
			string tmp2;
			getline(cin,tmp2);
			queries.push_back(tmp2);
		}
		for(int i=0;i<engine.size();i++)
		{
			if(engine[i].compare(queries[0])==0)
				continue;
			ans = min(ans,solve(engine[i],0,0));
		}
end:
	    char str[255];
		sprintf(str,"Case #%i: %i\n",c,ans);
		outfile.write(str,strlen(str));
		c++;
	}
    outfile.close();
    return 0;
}
