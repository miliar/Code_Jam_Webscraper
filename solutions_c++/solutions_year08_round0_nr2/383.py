#include<cstdio>
#include<algorithm>
using namespace std;
#define MINUTES (24*60)
bool dbg=0;

int readyA [MINUTES];
int readyB [MINUTES];
int leaveA [MINUTES];
int leaveB [MINUTES];
int na,nb,t;

int readTime()
{
    char s[10];
    scanf("%s",s);
    int time=((s[4]-'0')+10*(s[3]-'0')+60*(s[1]-'0')+600*(s[0]-'0'));
    if(dbg)printf("readTime(%s):%d\n",s,time);
    return time;
}

void readCase()
{
    scanf("%d%d%d",&t,&na,&nb);
    if(dbg)printf("t:%d, na:%d, nb:%d\n",t,na,nb);
    for(int i=0;i<MINUTES;i++)
    {
	readyA[i]=0;
	readyB[i]=0;
	leaveA[i]=0;
	leaveB[i]=0;
    }
    for(int i=0;i<na;i++)
    {
	int d,a;
	d=readTime();
	a=readTime();
	leaveA[d]++;
	readyB[a+t]++;
    }
    for(int i=0;i<nb;i++)
    {
	int d,a;
	d=readTime();
	a=readTime();
	leaveB[d]++;
	readyA[a+t]++;
    }
}

void solveCase(int cas)
{
    int A=0,B=0,minA=0,minB=0;
    for(int i=0;i<MINUTES;i++)
    {
	A=A-leaveA[i]+readyA[i];
	B=B-leaveB[i]+readyB[i];
	minA=min(A,minA);
	minB=min(B,minB);
    }
    printf("Case #%d: %d %d\n",cas,-minA,-minB);
}

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
	readCase();
	solveCase(i+1);
    }
    return 0;
}


