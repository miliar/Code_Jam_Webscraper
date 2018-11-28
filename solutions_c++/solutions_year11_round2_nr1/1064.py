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

char **mas;
int n;

double chis[105];
double znam[105];
double *wp;
double *owp;
double *oowp;

void calcWP(int pos)
{
	double sum=0;
	int cnt=0;
	wp[pos]=0.0;
	for(int i=0; i<n; ++i)
	{
		if(mas[pos][i]!='.')
		{
			++cnt;
			sum+=mas[pos][i]-'0';
		}
	}
	if(cnt>0)
		wp[pos]=sum/cnt;
	chis[pos]=sum;
	znam[pos]=cnt;
}

void cowp(int pos)
{
	double sum=0;
	int cnt=0;
	owp[pos]=0.0;
	for(int i=0; i<n; ++i)
	{
		if(mas[pos][i]!='.')
		{
			++cnt;
			sum+=(chis[i]-mas[i][pos]+'0')/(znam[i]-1);
		}
	}
	if(cnt>0)
		owp[pos]=sum/cnt;
}

void calcOWP(int pos, double* wp, double* owp)
{
	double sum=0;
	int cnt=0;
	owp[pos]=0.0;
	for(int i=0; i<n; ++i)
	{
		if(mas[pos][i]!='.')
		{
			++cnt;
			sum+=wp[i];
		}
	}
	if(cnt>0)
		owp[pos]=sum/cnt;
}

void test(int T)
{
	scanf("%d",&n);
	for(int i=0; i<n; ++i)
	{
		scanf("%s",mas[i]);
	}
	for(int i=0; i<n; ++i)
		calcWP(i);
	for(int i=0; i<n; ++i)
		cowp(i);
	for(int i=0; i<n; ++i)
		calcOWP(i,owp,oowp);
	printf("Case #%d:\n",T);
	for(int i=0; i<n; ++i)
		printf("%.7lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	mas=new char*[105];
	for(int i=0; i<105; ++i)
		mas[i]=new char[105];
	wp=new double[105];
	owp=new double[105];
	oowp=new double[105];
	int T;
	scanf("%d",&T);
	for(int t=0; t<T; ++t)
		test(t+1);
	return 0;
}