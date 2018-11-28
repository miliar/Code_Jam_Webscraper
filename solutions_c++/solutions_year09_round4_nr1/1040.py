

#include <iostream>
using namespace std;

char r[45][45];
int end[45];
int n,sum;
void endCh()
{
	for(int i=1;i<=n;i++)
	{
		end[i]=0;
		for(int j=0;r[i-1][j];j++)
		{
			if(r[i-1][j]=='1')
				end[i]=j+1;
		}
	}
}
void chg(int x)
{
	int t=x,pos;
	for(int i=x;i<=n;i++)
	{
		if(end[i]<=t)
		{
			pos=i;
			break;
		}
	}
	for(int i=pos;i>x;i--)
	{
		swap(end[i],end[i-1]);
		sum++;
	}
}
int main()
{
	freopen("E://A-large.in","r",stdin);
	//freopen("E://yhy.txt","r",stdin);
	freopen("E://yyy.txt","w",stdout);
	int t=1,Y;
	cin>>Y;
	while(t<=Y)
	{
		cout<<"Case #"<<t++<<": ";
		int i;
		cin>>n;
		for(i=0;i<n;i++)
			scanf("%s",r[i]);
		endCh();
		sum=0;
		for(i=1;i<=n;i++)
		{
			if(i<end[i])
			{
				chg(i);
			}
		}
		cout<<sum<<endl;
	}
	return 0;
}