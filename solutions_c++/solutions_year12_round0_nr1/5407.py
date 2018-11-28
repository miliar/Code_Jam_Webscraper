#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
char str1[1000];
char str2[1000];
char str[1000];
map<char,char> m;
int solve()
{

	for(int i = 0;str1[i] != '\0';i++)
	{
		m[str1[i]] = str2[i];
	}
	return 0;
}
void output()
{
	FILE* fp = fopen("index.txt","w");
	map<char,char>::iterator ite;
	for(ite = m.begin();ite != m.end();++ite)
	{
		char s = ite->first;
		char t = ite->second;
		fprintf(fp,"%c %c\n",s,t);
	}
	fclose(fp);
}
int main()
{
	m['q'] = 'z';
	m['z'] = 'q';
	freopen("1.txt","r",stdin);
	while( fgets(str1,1000-1,stdin))
	{
		fgets(str2,1000-1,stdin);
		solve();
	}
	output();
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,n = 0;
	scanf("%d",&T);
	getchar();
	while(n < T)
	{
		n++;
		fgets(str,1000-1,stdin);
		//printf("%s",str);
		printf("Case #%d: ",n);
		int i = 0;
		while(str[i] != '\0')
		{
			if(str[i] >= 'a' && str[i] <= 'z')
				printf("%c",m[str[i]]);
			else 
				printf("%c",str[i]);
			i++;
		}
	}
	return 0;
}