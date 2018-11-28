#include<iostream>
#include<string>
#include<vector>
#include<cstring>

using namespace std;

char rc[256][256];
bool rd[256][256];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		memset(rc,-1,sizeof rc);
		memset(rd,0,sizeof rd);

		int nr;
		cin>>nr;
		for(int i=0;i<nr;i++)
		{
			string scr;
			cin>>scr;
			rc[scr[0]][scr[1]] = rc[scr[1]][scr[0]] = scr[2];
		}

		int nd;
		cin>>nd;
		for(int i=0;i<nd;i++)
		{
			string sdr;
			cin>>sdr;
			rd[sdr[0]][sdr[1]] = rd[sdr[1]][sdr[0]] = true;
		}

		int n;
		cin>>n;
		string s;
		cin>>s;

		vector<char> ans;

		for(int i=0;i<s.length();i++)
		{
			if (ans.size()==0) { ans.push_back(s[i]); continue; }
			char x=s[i],y=ans[ans.size()-1];

			if (~rc[x][y]) ans[ans.size()-1] = rc[x][y];
			else
			{
				ans.push_back(x);
				for(int j=0;j<ans.size()-1;j++)
				{
					if (rd[ans[j]][x])
					{
						ans.clear();
						break;
					}
				}
			}
		}

		printf("Case #%d: [",tt);
		for(int i=0;i<ans.size();i++)
			printf("%c%s",ans[i],i!=ans.size()-1?", ":"");
		printf("]\n");
	}

	return 0;
}

