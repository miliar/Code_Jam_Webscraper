#include <iostream>
#include <string>
using namespace std;

int how_many(const char* s,const char* q)
{
	if(*q==0)return 1;
	if(*s==0)return 0;
	int R=how_many(s+1,q);
	if(*s==*q)R+=how_many(s+1,q+1);
	return R;
}

char S[505]={0};

char* itoa4(int a)
{
	S[4]=0;
	S[3]=a%10+'0';
	a/=10;
	S[2]=a%10+'0';
	a/=10;
	S[1]=a%10+'0';
	a/=10;
	S[0]=a%10+'0';
	a/=10;
	return S;
}

int main()
{
	freopen("a.in","rt",stdin);
	freopen("a.ou","wt",stdout);
	int N,i;
	cin>>N;
	gets(S);
	for(i=1;i<=N;i++)
	{
		gets(S);
		printf("Case #%d: %s\n",i,itoa4(how_many(S,"welcome to code jam")));
	}
	return 0;
}
