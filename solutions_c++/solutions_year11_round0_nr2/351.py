// gcj B
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<map>
#include<string>
#include<cmath>
#include<set>
using namespace std;
typedef long long LL;
const int MAX=200;

int C,D,N;
string comb[MAX],tmp;
bool opp[MAX][MAX];

int stk[1000],top;
bool joycom()
{
	if(top<=1) return 0;
	for(int i=1;i<=C;i++)
	{
		if(stk[top]==comb[i][0]-'A'&&stk[top-1]==comb[i][1]-'A')
		{
			top--;
			stk[top]=comb[i][2]-'A';
			return 1;
		}
		if(stk[top-1]==comb[i][0]-'A'&&stk[top]==comb[i][1]-'A')
		{
			top--;
			stk[top]=comb[i][2]-'A';
			return 1;
		}
	}
	
	return 0;
}

bool joyopp()
{
	for(int i=1;i<=top;i++)
	{
		for(int j=i+1;j<=top;j++)
		{
			if(opp[stk[i]][stk[j]]) return 1;
		}
	}
	return 0;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int T;scanf("%d",&T);
	int CN=0;
	
	while(T--)
	{
		memset(opp,0,sizeof(opp));
		
		scanf("%d",&C);
		for(int i=1;i<=C;i++) cin>>comb[i];
		
		scanf("%d",&D);
		for(int i=1;i<=D;i++)
		{
			cin>>tmp;
			int xx=tmp[0]-'A',yy=tmp[1]-'A';
			opp[xx][yy]=opp[yy][xx]=1;
		}
		
		scanf("%d",&N);
		cin>>tmp;
		top=0;
		for(int i=0;i<N;i++)
		{
			stk[++top]=tmp[i]-'A';
			while(joycom()) ;
			
			if(joyopp()) top=0;
		}
		printf("Case #%d: [",++CN);
		if(top>=1) printf("%c",stk[1]+'A');
		for(int i=2;i<=top;i++) printf(", %c",stk[i]+'A');
		printf("]\n");
	}
	
	return 0;
}
