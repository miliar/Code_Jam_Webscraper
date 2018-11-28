#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define oo 10005

string str[oo][27];
int a[27][oo],c[27][oo];
int N,M;
int T;

inline void Readin()
{
	memset(a,0,sizeof a);
	memset(c,0,sizeof c);

	cin >> N >> M;
	for (int i=1;i<=N;++i)
		cin >> str[i][26];
	
	//prepare
	for (int i=1;i<=N;++i)
		str[i][0]= string(str[i][26].size(),'*');
}

inline bool comp(int x,int y)
{
	return str[x][T] < str[y][T];
}

inline void Solve()
{
	string s;
	
	
	while (M--)
	{
		string ans="";
		int res=-1;
		
		cin >> s;
		
		for (int i=1;i<=N;++i)
		{
			int len= str[i][26].size();
			for (int j=0;j<25;++j)
			{
				str[i][j+1] = str[i][j];
				for (int k=0;k<len;++k)
					if (str[i][26][k] == s[j])
						str[i][j+1][k] = s[j];
			}
		}
		
		for (int i=1;i<=N;++i)
		{
			for (int j=0;j<=26;++j)
				a[j][i]=i;
		}
		for (int j=0;j<26;++j)
		{
			T= j;
			sort(a[j]+1,a[j]+1+N,comp);
		}
		
		for (int i=1;i<=N;++i)
			for (int j=0;j<26;++j)
				c[j][i] = str[i][j] != str[i][j+1];
		
		for (int j=0;j<26;++j)
		{
			int l=1,r=1;
			for (int i=2;i<=N+1;++i)
				if (i<=N && str[a[j][i]][j] == str[a[j][l]][j]) r=i;
				else{
					int cc=0;
					for (int k=l;k<=r;++k)
						cc |= c[j][a[j][k]];
					for (int k=l;k<=r;++k)
						c[j][a[j][k]]=cc;
					l=i;
					r=i;
				}
		}
		
		for (int i=1;i<=N;++i)
		{
			int x =0;
			for (char ch='a';ch<='z';++ch)
				if (str[i][26].find(ch)!= string::npos) x--;
				
			for (int j=0;j<26;++j)
				x += c[j][i];
			//cout << x << endl;
			if (x> res)
			{
				res=x;
				ans=str[i][26];
			}
		}
		
		cout << ' ' << ans;// <<  ':' << res;
	}
	
	cout << endl;
}

int main()
{
	//freopen("i.txt","r",stdin);
	int Test,Case=0;
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d:",++Case);
		Readin();
		Solve();
	}
	
	
	
	return 0;
}
