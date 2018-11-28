#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN=1000+10;
char s[MAXN];
char s1[MAXN];
int f(void)
{
	int res=1;
	int i;
	for(i=1;s1[i];i++)
		if(s1[i]!=s1[i-1]) res++;
	return res;
}
void solution(int num)
{
	printf("Case #%d: ",num);
	int k;
	scanf("%d",&k);
	scanf("%s",s);
	vector<int> a;
	int res=strlen(s);
	int i,j;
	for(i=0;i<k;i++) a.push_back(i);
	do
	{
		for(i=0;s[i];i+=k)
		{
			for(j=0;j<k;j++)
				s1[i+j]=s[i+a[j]];
		}
		s1[i]=0;
		if(f()<res) res=f();
	}while(next_permutation(a.begin(),a.end()));
	printf("%d\n",res);	
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
		solution(i+1);
	return 0;
}
