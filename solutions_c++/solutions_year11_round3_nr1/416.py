#pragma comment(linker,"/STACK:16777216")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<cstring>
#include<ctime>
#include<cmath>
#include<functional>

using namespace std;

#define ll long long
#define ld long double
#define si short int
#define pii pair<int,int>
#define vi vector<int>
#define vit vector<int>::iterator
#define sq(x) (x)*(x)
#define pil pair<ll, i>

char** mas;
int r,c;
void test(int T)
{
	printf("Case #%d:\n",T+1);
	scanf("%d%d",&c,&r);
	for(int i=1; i<=c; ++i)
		scanf(" %s",mas[i]+1);
	for(int i=1; i<=c; ++i)
		for(int j=1; j<=r; ++j)
			if(mas[i][j]=='#')
			{
				mas[i][j]='/';
				if(mas[i][j+1]=='#')
				{
					mas[i][j+1]='\\';
				}
				else
				{
					printf("Impossible\n");
					return;
				}
				if(mas[i+1][j]=='#')
				{
					mas[i+1][j]='\\';
				}
				else
				{
					printf("Impossible\n");
					return;
				}
				if(mas[i+1][j+1]=='#')
				{
					mas[i+1][j+1]='/';
				}
				else
				{
					printf("Impossible\n");
					return;
				}
			}
	for(int i=1; i<=c; ++i)
		printf("%s\n",mas[i]+1);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	mas=new char*[55];
	for(int i=0; i<55; ++i)
	{
		mas[i]=new char[55];
		for(int j=0; j<55; ++j)
			mas[i][j]=0;
	}
	int T;
	cin>>T;
	for(int t=0; t<T; ++t)
		test(t);
	return 0;
}