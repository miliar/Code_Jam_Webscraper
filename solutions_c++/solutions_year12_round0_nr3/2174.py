#include<iostream>
#include<map>
#include<ctime>
using namespace std;
map<int, map<int,bool> > flag;
char s[100];
int P[10];
int answer;
void init()
{
	P[0]=1;
	for(int i=1;i<=9;i++) P[i]=P[i-1]*10;
}
void check(int X,int MAX)
{
	int l,a,b,i,k;
	sprintf(s,"%d",X);
	l=strlen(s);
	for(i=1;i<l;i++)
	{
		a=X/P[l-i];
		b=X%P[l-i];
		if(s[i]!='0')
		{
			k=b*P[i]+a;
			if(k>X&&k<=MAX&&!flag[X][k])
			{
				flag[X][k]=true;
				answer++;
			}
		}
	}
}
void solve(int T)
{
	int A,B;
	flag.clear();
	scanf("%d%d",&A,&B);
	answer=0;
	for(int x=A;x<=B;x++) check(x,B);
	printf("Case #%d: %d\n",T,answer);
}
int main()
{
	init();
	int T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++) solve(i);
	return 0;
}