#include<iostream>
using namespace std;
int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int cs,c,com,opp,inv,p,i,j,ans[110],combine[30][30],occ[30];
	bool opposite[30][30];
	string s;
	cin>>cs;
	for (c=1;c<=cs;c++)
	{
		cin>>com;
		memset(combine,-1,sizeof(combine));
		for (i=0;i<com;i++)
		{
			cin>>s;
			combine[s[0]-'A'][s[1]-'A'] = s[2]-'A';
			combine[s[1]-'A'][s[0]-'A'] = s[2]-'A';
		}
		cin>>opp;
		memset(opposite,false,sizeof(opposite));
		for (i=0;i<opp;i++)
		{
			cin>>s;
			opposite[s[0]-'A'][s[1]-'A']=true;
			opposite[s[1]-'A'][s[0]-'A']=true;
		}
		cin>>inv>>s;
		p=-1;
		memset(occ,0,sizeof(occ));
		for (i=0;i<inv;i++)
		{
			p++;
			
			if (p>0 && combine[ans[p-1]][s[i]-'A']!=-1)
			{
				p--;
				occ[ans[p]]--;
				ans[p]=combine[ans[p]][s[i]-'A'];
			}
			else
			{
				ans[p]=s[i]-'A';
			}
			occ[ans[p]]++;
			
			for (j=0;j<26;j++)
				if (j!=ans[p] && occ[j]>0 && opposite[j][ans[p]] || j==ans[p] && occ[j]>1 && opposite[j][j])
				{
					p=-1;
					memset(occ,0,sizeof(occ));
					break;
				}
		}
		printf("Case #%d: [",c);
		for (j=0;j<=p;j++)
			if (j<p) printf("%c, ", ans[j]+'A');
			else printf("%c", ans[j]+'A');
		printf("]\n");
	}
	return 0;
}
