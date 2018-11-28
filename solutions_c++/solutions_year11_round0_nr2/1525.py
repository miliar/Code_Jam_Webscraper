#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;


int combine[260][260];
int Clear[260][260];
string ans;
int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	//printf("Algorithm is Beautiful!\n");
	int T,C,D,N,casetest=1;
	cin>>T;
	while(T--)
	{
		cout<<"Case #"<<casetest++<<": [";
		memset(Clear,0,sizeof(Clear));
		memset(combine,0,sizeof(combine));
		ans.clear();
		cin>>C;
		string str;
		int sz;
		for(int i=1;i<=C;i++)
		{
			cin>>str;
			combine[str[0]][str[1]]=combine[str[1]][str[0]]=str[2];
		}
		cin>>D;
		for(int i=1;i<=D;i++)
		{
			cin>>str;
			Clear[str[0]][str[1]]=Clear[str[1]][str[0]]=1;
		}
		cin>>N;
		cin>>str;
		ans.push_back(str[0]);
		for(int i=1;i<N;i++)
		{
			if(ans.size()!=0 && combine[ans.back()][str[i]])
			{
				char temp=combine[ans.back()][str[i]];
				ans.erase(ans.end()-1,ans.end());
				ans.push_back(temp);
			}
			else
			{
				int sz=ans.size();
				if(sz==0)
				{
					ans.push_back(str[i]);
					continue;
				}
				int index=0;
				string::iterator iter=ans.begin();
				while(index!=sz)
				{
					if(Clear[ans[index]][str[i]])
					{
						//ans.erase(iter,ans.end());
						ans.clear();
						break;
					}
					index++;
					iter++;
				}
				if(index==sz)ans.push_back(str[i]);
			}
		}
		sz=ans.size();
		if(sz==0)cout<<"]"<<endl;
		else
		{
			for(int i=0;i<sz-1;i++)
				cout<<ans[i]<<", ";
			cout<<ans[sz-1]<<"]"<<endl;
		}

	}
	return 0;
}