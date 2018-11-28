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

using namespace std;
vector<vector<char>> voppose;
vector<vector<char>> vform;
vector<char> vdes;
vector<char> vsrc;
int C,D,N;
void solve()
{
	int spos = 0;
	int dlen = 0;
goto_p1:
	while (spos < vsrc.size())
	{
		vdes.push_back(vsrc[spos]);
		spos++;
		if (vdes.size() < 2)
		{
			continue;
		}
		dlen = vdes.size();
		for (int i =0;i<vform.size();i++)
		{
			if ((vdes[dlen-2] == vform[i][0] && vdes[dlen-1] == vform[i][1]) ||
				(vdes[dlen-1]== vform[i][0]&&vdes[dlen -2] == vform[i][1]))
			{
				vdes.pop_back();
				vdes.pop_back();
				vdes.push_back(vform[i][2]);
				goto goto_p1;
			}
		}
		for (int i=0;i<vdes.size()-1;i++)
		{
			for (int j=0;j<voppose.size();j++)
			{
				if ((vdes[i] == voppose[j][0] && vdes[dlen-1] == voppose[j][1]) ||
					(vdes[i] == voppose[j][1] && vdes[dlen-1] == voppose[j][0]))
				{
					//int k = dlen - i;
					//while(k){vdes.pop_back();k--;};
					vdes.clear();
					goto goto_p1;
				}
			}

		}
		
		
		
	}
	

}

int main()
{
	FILE *fp = NULL;

	//fp = freopen("B-small-attempt4.in","r",stdin);
	fp = freopen("B-large.in","r",stdin);
	fp = freopen("B-large.out","w",stdout);

	int T;
	cin>>T;
	char ch;
	vector<char> vtmp;
	for (int caseId=1;caseId<=T;caseId++)
	{
		vform.clear();
		voppose.clear();
		vsrc.clear();
		vdes.clear();

		cin>>C;
		
		for (int i=0;i<C;i++)
		{
			vtmp.clear();
			cin>>ch;
			vtmp.push_back(ch);
			cin>>ch;
			vtmp.push_back(ch);
			cin>>ch;
			vtmp.push_back(ch);
			vform.push_back(vtmp);
		}
		cin>>D;
		for (int i=0;i<D;i++)
		{
			vtmp.clear();
			cin>>ch;
			vtmp.push_back(ch);
			cin>>ch;
			vtmp.push_back(ch);
			voppose.push_back(vtmp);
		}
		cin>>N;
		for (int i=0;i<N;i++)
		{
			cin>>ch;
			vsrc.push_back(ch);
		}
		solve();
		cout<<"Case #"<<caseId<<": [";
		for(int i = 0;i<vdes.size();i++)
		{
			if (i < vdes.size() -1)
			{
				cout<<vdes[i]<<", ";
			}
			else
				cout<<vdes[i];
			
		}
		cout<<"]"<<endl;
		cerr<<caseId<<"/"<<T<<endl;
	}


	return 0;
}

