#include<iostream>
#include<string>
#include<vector>
#include<cstring>

using namespace std;

int n,m;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d:",tt);
		cin>>n>>m;

		vector<pair<string,int> > D[10];

		for(int i=0;i<n;i++)
		{
			string s;
			cin>>s;
			D[s.length()-1].push_back(pair<string,int>(s,i));
		}

		for(int mm=0;mm<m;mm++)
		{
			string order;
			cin>>order;

			string ans = "";
			int maxCnt = -1;
			int maxIdx;

			for(int i=0;i<10;i++)
			{
				if (D[i].size()==0) continue;

				for(int j=0;j<D[i].size();j++)
				{

					vector<string> rem;
					for(int k=0;k<D[i].size();k++)
						if (k!=j)
							rem.push_back(D[i][k].first);

					string tans = D[i][j].first;
					int pt = 0;
					
					bool exist[26],correxist[26];
					memset(correxist,0,sizeof(correxist));
						for(int l=0;l<tans.length();l++)
							correxist[tans[l]-'a']=true;

					memset(exist,0,sizeof(exist));
					for(int k=0;k<rem.size();k++)
						for(int l=0;l<rem[k].length();l++)
							exist[rem[k][l]-'a']=true;
					for(int l=0;l<tans.length();l++)
							exist[tans[l]-'a']=true;

					for(int k=0;rem.size()>0;k++)
					{
						int c = order[k]-'a';
						if (!exist[c]) continue;
						if (correxist[c])
						{
							for(int l=0;l<rem.size();l++)
								for(int t=0;t<i+1;t++)
								{
									if (tans[t]==c+'a'&&rem[l][t]!=c+'a'||tans[t]!=c+'a'&&rem[l][t]==c+'a')
									{
										rem.erase(rem.begin()+l);
										--l;
										break;
									}
								}

							memset(exist,0,sizeof(exist));
							for(int k=0;k<rem.size();k++)
								for(int l=0;l<rem[k].length();l++)
									exist[rem[k][l]-'a']=true;
							for(int l=0;l<tans.length();l++)
									exist[tans[l]-'a']=true;
						}
						else
						{
							++pt;
							for(int l=0;l<rem.size();l++)
								for(int t=0;t<i+1;t++)
								{
									if (rem[l][t]==c+'a')
									{
										rem.erase(rem.begin()+l);
										--l;
										break;
									}
								}

							memset(exist,0,sizeof(exist));
							for(int k=0;k<rem.size();k++)
								for(int l=0;l<rem[k].length();l++)
									exist[rem[k][l]-'a']=true;
							for(int l=0;l<tans.length();l++)
									exist[tans[l]-'a']=true;
						}
					}

					if (pt>maxCnt||pt==maxCnt&&maxIdx>D[i][j].second) { maxIdx = D[i][j].second; maxCnt = pt; ans = tans; }
				}
			}
			
			printf(" %s",ans.c_str());
		}
		printf("\n");
	}

	return 0;
}

