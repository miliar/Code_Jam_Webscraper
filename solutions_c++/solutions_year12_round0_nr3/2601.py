

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include<string.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int i,j,k;
	for(k=0;k<t;k++)
	{
		long long ans=0;
		int a,b;
		scanf("%d %d",&a,&b);
		for(i=a;i<b;i++)
		{
			stringstream s;
			s << i;
			string nstr = s.str();
			map<pair<int,int>,bool> mymap;
			for(j=1;j<nstr.size();j++)
			{
				if(nstr[j]<nstr[0]) continue;
				string temp;
				temp.assign(nstr,j,nstr.size()-j);
				string temp2;
				temp2.assign(nstr,0,j);
				string f = temp+temp2;
			//	cout << temp << " " << temp2 << " " << f << endl;
				int val = atoi(f.c_str());
				if(mymap.find(make_pair(i,val))!=mymap.end()) continue;

				stringstream l;
				l << val;
				string valstr = l.str();
				
				if(val>=a && val <=b && val>i  && valstr.size()==nstr.size() && mymap.find(make_pair(i,val))==mymap.end())
				{
					mymap[make_pair(i,val)]=true;
					ans++;
				}
			}
		}
		cout << "Case #" << k+1 <<": " << ans << endl;

	}
	return 0;
}
