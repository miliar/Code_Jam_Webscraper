#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int cases,n,arr1[15][2],arr2[15][2],total,nextO,nextB,Next,o,b;
char c;

void advance()
{
	if(nextO < n && arr1[nextO][1] == Next)
	{
		if(o == arr1[nextO][0])
		{
			nextO++;
			Next++;
		}

		else if(o < arr1[nextO][0])
			o++;

		else
			o--;

		if(nextB < n)
		{
			if(b < arr2[nextB][0])
				b++;

			else if(b > arr2[nextB][0])
				b--;
		}
	}
	else
	{
		if(b == arr2[nextB][0])
		{
			nextB++;
			Next++;
		}

		else if(b < arr2[nextB][0]) // move forward
			b++;

		else
			b--;

		if(nextO < n)
		{
			if(o < arr1[nextO][0])
				o++;

			else if(o > arr1[nextO][0])
				o--;
		}
	}
}

int main()
{
	int ans;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>cases;
	for(int cc=0;cc<cases;cc++)
	{
		total=0;
		memset(arr1,-1,sizeof(arr1));
		memset(arr2,-1,sizeof(arr2));
		cin>>n;
		o=b=0;
		for(int i=0;i<n;i++)
		{
			cin>>c;
			if(c=='O')
			{
				cin>>arr1[o][0];
				arr1[o++][1]=i;
			}
			else
			{
				cin>>arr2[b][0];
				arr2[b++][1]=i;
			}
		}
		Next=0;
		nextO=nextB=0;
		o=b=1;

		ans=0;
		while(Next<n)
		{
			advance();
			ans++;
		}

		cout<<"Case #"<<cc+1<<": "<<ans<<endl;
	}
	return 0;
}