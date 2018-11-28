#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<algorithm>
#include<functional>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;
int gcd( int a, int b ) {  if( !b ) return a;  return gcd( b, a % b ); }

int main()
{
	char a[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	   
	string s="";
	int t,i;
	scanf("%d",&t);
	char c;
	scanf("%c",&c);
	int j=1;
	while(t--)
	{
	getline(cin,s);
	printf("Case #%d: ",j);
	for(i =0; s[i] != '\0';  i++)
	{
		if(s[i] == ' ')
		{
			printf(" ");
			continue;
		}
		printf("%c",a[s[i]%97]);
	}
	printf("\n");
	j++;
	}
	return 0;
}   
 
 

