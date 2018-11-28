#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define maxn 2010
#define maxe 1000100
#define INF 0x7fffffff
char s[maxn];
char mp[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	int i,j,n,tt=0,len;
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d",&n); gets(s);
	while(n--){
		printf("Case #%d: ",++tt);
		gets(s);
		len=strlen(s);
		for(i=0;i<len;i++){
			if(s[i]!=' ') printf("%c",mp[s[i]-'a']);
			else printf("%c",s[i]);
		}
		printf("\n");
	}
	return 0;
}