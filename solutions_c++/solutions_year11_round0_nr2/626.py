#include <cstdio>
#include <stack>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int t,ca=1;
	int c,d,n;

	scanf("%d",&t);
	while(t--)
	{
		typedef map<pair<char,char>, char> MM;
		typedef set<pair<char,char> > SS;
		MM m;
		SS s;
		scanf("%d",&c);
		int i;
		for(i=0;i<c;i++)
		{
			char cc[10];
			scanf("%s",cc);
			m[make_pair(cc[0],cc[1])]=cc[2];
			m[make_pair(cc[1],cc[0])]=cc[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			char opp[10];
			scanf("%s",&opp);
			s.insert(make_pair(opp[0],opp[1]));
			s.insert(make_pair(opp[1],opp[0]));
		}

		char el[200];
		scanf("%d%s",&n,el);
		vector<char> ans;
		for(i=0;i<n;i++)
		{
			if(!ans.empty() && m.find(make_pair(ans[ans.size()-1],el[i])) != m.end())
			{
				ans[ans.size()-1]=m[make_pair(ans[ans.size()-1],el[i])];
				continue;
			}
			size_t j,len=ans.size();
			for(j=0;j<len;j++)
			{
				if(s.find(make_pair(el[i],ans[j])) != s.end())
				{
					ans.clear();
					break;
				}
			}
			if(j<len) continue;
			ans.push_back(el[i]);
		}
		printf("Case #%d: [",ca++);
		size_t len = ans.size();
		if(len>0)
		{
			for(i=0;i<len-1;i++)
				printf("%c, ",ans[i]);
			printf("%c",ans[i]);
		}
		printf("]\n");
	}

	return 0;
}