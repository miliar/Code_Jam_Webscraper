#include <cstdio>
#include <string>
#include <vector>
#define LEN 505

using namespace std;

int ncases, nways[LEN][25];
char text[LEN];
vector<int> pos[256];
string str="welcome to code jam";

void precomp()
{
	for(int i=0; i<str.size(); i++)
		pos[str[i]].push_back(i);
}

void godp()
{
	int sz=strlen(text);
	memset(nways, 0, sizeof(nways));
	for(int i=0; i<sz; i++)
	{
		if(text[i]=='w')
		{
			nways[i][0]=1;
			continue;
		}
		
		for(int j=0; j<pos[text[i]].size(); j++)
			for(int k=0; k<i; k++)
				if(str[pos[text[i]][j]-1]==text[k])
				{
					nways[i][pos[text[i]][j]]+=nways[k][pos[text[i]][j]-1];
					nways[i][pos[text[i]][j]]%=10000;
				}
	}
}

int main()
{
	scanf("%d", &ncases);
	getchar();
	precomp();
	for(int i=0; i<ncases; i++)
	{
		int sum=0;
		memset(text, 0, sizeof(text));
		fgets(text, 550, stdin);
		text[strlen(text)-1]='\0';
		godp();
		for(int j=0; j<strlen(text); j++)
		{
			sum+=nways[j][18];
			sum%=10000;
		}
		printf("Case #%d: %.4d\n", i+1, sum);
	}
}
