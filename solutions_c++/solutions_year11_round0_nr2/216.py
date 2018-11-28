#include <iostream>
#include <string>
using namespace std;
char c[26][26];
bool d[26][26];
int C,D,N;
string s;

inline void Readin()
{
	memset(c,0,sizeof c);
	memset(d,0,sizeof d);
	
	string str;
	cin >> C;
	for (int i=1;i<=C;++i)
	{
		cin >> str;
		c[str[0]-'A'][str[1]-'A']=str[2];
		c[str[1]-'A'][str[0]-'A']=str[2];
	}
	
	cin >> D;
	for (int i=1;i<=D;++i)
	{
		cin >> str;
		d[str[0]-'A'][str[1]-'A']=true;
		d[str[1]-'A'][str[0]-'A']=true;
	}
	cin >> N >> s;
}

inline void Solve()
{
	string ans="";
	for (int i=0;i<s.size();++i)
	{
		ans += s[i];
		if (ans.size()>=2 && c[ans[ans.size()-2]-'A'][ans[ans.size()-1]-'A'])
			ans = ans.substr(0,ans.size()-2) + c[ans[ans.size()-2]-'A'][ans[ans.size()-1]-'A'];
		for (int j = 0;j <ans.size() -1;++j)
			for (int k =j+1; k<ans.size();++k)
				if (d[ans[j]-'A'][ans[k]-'A'])
				{
					ans="";
					goto End;
				}
		End: ;
	}
	
	printf("[");
	for (int i =0;i<ans.size();++i)
	{
		if (i) printf(", ");
		printf("%c",ans[i]);
	}
	puts("]");
}

int main()
{
	//freopen("i.txt","r",stdin);
	int Test,Case=0;
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
