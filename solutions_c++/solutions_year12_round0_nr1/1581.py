#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cassert>
#include<ctime>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>


#define PB push_back
#define M 100
#define N 500010
#define MOD 1000000007
#define MAX 18450000
#define MAX 18450000
//#define NMAX 101
//#define SRT 11
#define SRT 4300
#define LL long long
#define LLMAX 0x7fffffffffffffffLL

int main()
{
	char map[]="yhesocvxduiglbkrztnwjpfmaq",str[1000];
	int ti,i,j,tc;
	scanf("%d",&tc);
	gets(str);
	for(ti=1;ti<=tc;++ti)
	{
		gets(str);
		for(i=0;str[i]!=0;++i)
		{
			if(str[i]==' ')
			continue;
			j=str[i]-'a';
			str[i]=map[j];
		}
		printf("Case #%d: %s\n",ti,str);
	}
	return 0;
}