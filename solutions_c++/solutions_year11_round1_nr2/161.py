#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#pragma comment(linker, "/STACK:1760777216")

#define ll long long

using namespace std;

ll gcd(ll a,ll b) {return b==0 ? a : gcd(b,a%b);}

char words[10003][11]={0};
int len[10003]={0},res[10003]={0};

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		int n,m;
		cin >> n >> m;
		for(int i=0;i<n;i++)
		{
			cin >> words[i];
			len[i]=strlen(words[i]);
		}
		char al[28]={0};
		for(int e=0;e<m;e++)
		{
			cin >> al;
			for(int i=0;i<n;i++)
			{
				char cur[11]={0};
				int score=0,cnt=0;
				for(int j=0;j<26;j++)
				{
					bool poss=false;
					for(int r=0;r<n;r++)
					{
						if (len[r]==len[i])
						{
							bool norm=true;
							for(int k=0;k<len[r];k++)
							{
								if (cur[k]!='\0'&&cur[k]!=words[r][k])
								{
									norm=false;
									break;
								}
								if (cur[k]=='\0')
								{
									for(int y=0;y<len[i];y++)
										if (words[r][k]==cur[y])
										{
											norm=false;
											break;
										}
									for(int y=0;y<j;y++)
										if (words[r][k]==al[y])
										{
											norm=false;
											break;
										}
								}
							}
							if (norm)
							{
								for(int k=0;k<len[r];k++)
									if (al[j]==words[r][k])
									{
										poss=true;
										break;
									}
							}
						}
						if (poss) break;
					}
					if (poss)
					{
						bool was=false;
						for(int t=0;t<len[i];t++)
							if (words[i][t]==al[j]) cur[t]=al[j],was=true,cnt++;
						if (!was) score++;
					}
					if (cnt==len[i]) break;
				}
				res[i]=score;
			}
			int mn=res[0],ind=0;
			for(int i=0;i<n;i++)
				if (mn<res[i]) mn=res[i],ind=i;
			if (e==0) printf("%s",words[ind]);
			else printf(" %s",words[ind]);
		}
		printf("\n");
	}
	return 0;
}
