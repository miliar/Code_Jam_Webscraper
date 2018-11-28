#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

#define N 201
int n;
char s[N][N];
int win[N],comp[N];
double wp[N],owp[N],oowp[N];

double cal(int k,const char*p)
{
	double A = 0 , B = 0;
	for (int i = 0; i < n; i++)
	 if (p[i] == '1') A++;
		else if (p[i] == '0') B++;
	win[k] = A;
	comp[k] = A + B;
	return A / (A + B);
}

double cal2(int k,const char *p)
{
	double tot = 0;
	for (int i = 0; i < n; i++)
	  if (p[i] != '.')
		tot += double(s[i][k] == '1' ? win[i] - 1: win[i]) / (comp[i] - 1);
	return tot / comp[k];
}

double cal3(const char *p)
{
	double tot = 0, num = 0;
	for (int i = 0; i < n; i++)
		if (p[i] == '1' || p[i] == '0')
		{
			tot += owp[i];
			num++;
		}
	return tot / num;
}

void init()
{
	scanf("%d",&n);
	for (int i = 0; i < n; i++)
	{
		scanf("%s",s[i]);
		wp[i] = cal(i,s[i]);
	}
	for (int i = 0; i < n; i++)
		owp[i] = cal2(i,s[i]);
	for (int i = 0; i < n; i++)
		oowp[i] = cal3(s[i]);
//	for(int i = 0; i < n; i++)
//	printf("%lf %lf %lf\n",wp[i],owp[i],oowp[i]);
}

int main() 
{
//	freopen("A.in","r",stdin);
//	freopen("A.ans","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; i++)
	{
		init();
		printf("Case #%d:\n",i);
		for (int j = 0; j < n; j++)
			printf("%0.8lf\n",0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]);
	}
}
