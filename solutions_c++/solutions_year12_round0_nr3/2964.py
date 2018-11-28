#include<string>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int T;
int A,B;
int Pow[20];
int wei(int A)
{
	int Cnt=0;
	while(A>0)
	Cnt++,A/=10;
	return Cnt;
}
void solve(int A,int B,int num)
{
	int Ans=0;
	int Cnt=wei(A);
	int now,temp;
	for(int i=A;i<=B;i++)
	{ 
		//int Scnt=0;
		for(int j=i+1;j<=B;j++)
		for(int k=1;k<Cnt;k++)
		{
			if(wei(i)!=wei(j))
			continue;
			now=i;
			temp=now%Pow[k];
			now/=Pow[k];
			now+=temp*Pow[Cnt-k];
			if(now==j)
			{
				Ans++;
				continue;
			}
		}
		//if(Scnt)
		//cout<<i<<" "<<Scnt<<endl;
	}
	printf("Case #%d: %d\n",num,Ans);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	Pow[0]=1;
	for(int i=1;i<=9;i++)
	Pow[i]=Pow[i-1]*10;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&A,&B);
		solve(A,B,tt);
	}
	return 0;
}