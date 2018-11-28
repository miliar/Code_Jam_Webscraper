#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define MAX_N 10100
bool answer;
int Finish,N;
int d[MAX_N],l[MAX_N];
int flag[MAX_N];
bool go(int CurL,int dd,int next)
{
	if(CurL+dd>=Finish) answer=true;
	if(answer) return true;
	int x;
	for(int i=next;i<N;i++)
	{
		if(CurL+dd>=d[i])
		{
			x=min(l[i],d[i]-dd);
			if(flag[i]&&flag[i]>=x) continue;
	//		flag[i]=x;
			if(go(x,d[i],i+1)) return true;
		}
		else break;
	}
	return false;
}
void solve(int T)
{

	answer=false;
	scanf("%d",&N);
	for(int i=0;i<N;i++)
		scanf("%d%d",&d[i],&l[i]);
	scanf("%d",&Finish);
	printf("Case #%d: ",T);

	if(go(d[0],d[0],1)) printf("YES\n");
	else printf("NO\n");
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) solve(i);
	return 0;
}