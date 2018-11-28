#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <string>
using namespace std;
const int maxN = 20;
char str[maxN];
char dword[500+10];
map<string,int> p;
vector<char>table[maxN];
int l , d , n;
int ans;
FILE *fin = fopen("A-large.in","r");
FILE *fout = fopen("out.txt","w");

void DFS(int dep,string s)
{
	if(!p[s]) return ;
	if(dep == l)
	{
		if(p[s]) ++ans;
		//fprintf(fout,"%s\n",s);
		return ;
	}
	for(int i = 0 ; i < table[dep+1].size() ; ++i)
		DFS(dep+1,s+table[dep+1][i]);
}
int main()
{
	fscanf(fin,"%d%d%d",&l,&d,&n);
	while(d--)
	{
		fscanf(fin,"%s",str);
		p[str] = true;
		int len = strlen(str);
		char s[maxN] = {0};
		for(int tt = 0 ; tt+1 < len ; ++tt)
		{
				s[tt] = str[tt];
				s[tt+1] = '\0';
				p[s] = true;
		}
	}
	p[""] = true;
	for(int i = 1 ; i <= n ; ++i)
	{
		fscanf(fin,"%s",dword);
		int token = 0 , endtoken = 0;
		int len = strlen(dword);
		int group = 0;
		for(int t = 0 ; t < maxN ; ++t)table[t].clear();
		for(int k = 0 ; k < len ; ++k)
		{
			if(group > l) break;
			if(dword[k] == '(')
			{
				token = 1;
				++group;
			}else if(dword[k]==')')
			{
				token = 0;
			}
			else if(token)
			{
				table[group].push_back(dword[k]);
			}else if(!token)
			{
				++group;
				table[group].push_back(dword[k]);
			}
		}
		if(group > l) 
		{
			fprintf(fout,"Case #%d: 0\n",i);
			continue;
		}
		
		//debug
		/*for(int tt = 1 ; tt <= group  ; ++tt)
		{
			for(int kk = 0 ; kk < table[tt].size() ; ++kk)
				fprintf(fout,"%c",table[tt][kk]);
			fprintf(fout,"\n");
		}*/
		//end debug
		//±©Á¦Ã¶¾Ù
		ans = 0;
		DFS(0,"");
		fprintf(fout,"Case #%d: %d\n",i,ans);
	}
	return 0;
}
