#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,curB,curO;
	char ch;
	int m,n,ca=1;
	char arr[128];
	scanf("%d",&t);
	while(t--)
	{
		queue <int> OR;
		queue <int> BL;
		scanf("%d",&n);
		getchar();
		for(int i=0,k=0;i<n;i++)
		{
			scanf("%c%d",&ch,&m);
			getchar();
			arr[k++]=ch;
			if(ch=='O') OR.push(m);
			else BL.push(m);
		}
		curB=1;curO=1;
		int cnt=0;
		for(int i=0;i<n;i++)
		{
			bool flag=false;
			while(true)
			{
				cnt++;
				//move b
				if(BL.empty()==false  && curB<BL.front()) curB++;
				else if(BL.empty()==false && curB>BL.front()) curB--;
				else if(BL.empty()==false && curB == BL.front() && arr[i]=='B')
				{
					BL.pop();
					flag=true;
				}
				
				//move o
				if(OR.empty()==false && curO < OR.front()) curO++;
				else if(OR.empty()==false && curO>OR.front()) curO--;
				else if(!OR.empty() && curO==OR.front() && arr[i]=='O')
				{
					OR.pop();
					flag=true;
				}
				if(flag==true) break;
			}
		}
		printf("Case #%d: %d\n",ca++,cnt);
	}
	return 0;
}
