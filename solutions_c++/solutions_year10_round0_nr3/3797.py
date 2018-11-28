#include<iostream>
using namespace std;
int main()
{
	int g[10000],r,k,n,t,temp[10000],ans[10000];
	int a,i,j;
	cin>>t;
	for(a=0;a<t;a++)
	{
		cin>>r>>k>>n;
		for(i=0;i<n;i++)
		{
			cin>>g[i];
		}
		int final=0,count1=0;
		for(j=0;j<n;j++)
		{
			count1=count1+g[j];
		}
		if(count1<=k)
			final=count1*r;
		else
		{
		while(r>0)
		{
			int count=0;
			for(j=0;j<n;j++)
			{
				count=count+g[j];
				if(count>k)
				{
					final=final+count-g[j];
					r--;
					break;
				}
				else if(count==k)
				{
					final=final+count;
					r--;
					j++;
					break;
				}
			}
			for(int z=0;z<n;z++)
				temp[z]=g[z];
			int l=0,y=0;
			for(int m=j;m<n;m++)
			{
				g[l]=temp[m];
				l++;
			}
			for(int x=0;x<j;x++)
			{
			       g[x+l]=temp[y];
			       y++;
			}

		}
		}
		ans[a]=final;
	}
	for(a=0;a<t;a++)
		cout<<"Case #"<<a+1<<": "<<ans[a]<<"\n";
}
