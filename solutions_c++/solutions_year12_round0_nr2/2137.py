#include<iostream>
using namespace std;
int t[200],answer;
void solve(int T)
{
	int N,S,P,i,tl,tr;
	answer=0;
	scanf("%d%d%d",&N,&S,&P);
	for(i=0;i<N;i++) 
	{
		scanf("%d",&t[i]);
		tl=P+2*max(0,P-1);	//tr=P+2*min(10,P+1);	
		if(tl<=t[i]) 
		{
			//ok
			answer++;
		}
		else
		{
			tl=P+2*max(0,P-2);	//tr=P+2*min(10,P+2);	
			if(tl<=t[i]&&S)
			{
				S--;
				answer++;
				//hm...
			}
			else
			{
				// :(
			}
		}
	}
	printf("Case #%d: %d\n",T,answer);
}
int main()
{
	int T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		solve(i);
	}
	return 0;
}