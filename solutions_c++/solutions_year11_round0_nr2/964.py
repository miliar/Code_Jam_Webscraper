#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <cassert>
#include <algorithm>
typedef long long LL;

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t;++i)
	{
		const int mMax='Z'-'A'+1;
		vector<vector<char> > combine(mMax,vector<char> (mMax,'-'));
		vector<vector<bool> > opp(mMax,vector<bool> (mMax,false));
		int C,D;
		cin >> C;
		for(int j=0;j<C;++j)
		{
			char tmpc1,tmpc2,tmpc3;
			cin >> tmpc1 >> tmpc2 >> tmpc3;
			combine[tmpc1-'A'][tmpc2-'A']=tmpc3;
			combine[tmpc2-'A'][tmpc1-'A']=tmpc3;
		}
		cin >> D;
		for(int j=0;j<D;++j)
		{
			char tmpc1,tmpc2;
			cin >> tmpc1 >> tmpc2;
			opp[tmpc1-'A'][tmpc2-'A']=true;
			opp[tmpc2-'A'][tmpc1-'A']=true;
		}
		int N;
		cin >> N;
		string s;
		cin >> s;
		assert(s.length()==N);
		deque<char> out;
		for(int j=0;j<s.length();++j)
		{
			if(out.empty())
			{
				out.push_back(s[j]);
			}
			else
			{
				if(combine[out.back()-'A'][s[j]-'A']!='-')
				{
					char tmpc=combine[out.back()-'A'][s[j]-'A'];
					out.pop_back();
					out.push_back(tmpc);
				}
				else
				{
					bool found=false;
					for(int k=0;k<out.size();++k)
					{
						if(opp[out[k]-'A'][s[j]-'A'])
						{
							found=true;
							break;
						}
					}
					if(found)
						out.clear();
					else
						out.push_back(s[j]);
				}
			}
		}
		cout << "Case #" << i << ": [";
		for(int j=0;j<out.size();++j)
		{
			if(j)
				cout << ", ";
			cout << out[j];
		}
		cout << "]"<< endl;
	}
	return 0;
}
