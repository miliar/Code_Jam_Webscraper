#include<iostream>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>

using namespace std;

char r[40];
char str[200];
bool ok[100];

void main(){

#ifdef INPUT_VAR
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	int n;
	scanf("%d\n",&n);
	string in="zejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvy qee";
	string ou="qour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upa zoo";
	for (int i=0;i<in.length();i++)
	{
		if (in[i]!=' ') 
		{
			r[in[i]-'a']=ou[i];
			ok[ou[i]-'a']=1;
		}
	}

	for (int i=1;i<=n;i++)
	{
		gets(str);
		printf("Case #%d: ",i);
		int j=0;
		while (str[j])
		{
			if (str[j]!=' ')
			{
				printf("%c",r[str[j]-'a']);
			}
			else
			{
				printf(" ");
			}
			j++;
		}
		printf("\n");
	}
}