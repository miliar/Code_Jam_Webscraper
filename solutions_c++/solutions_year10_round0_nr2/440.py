#include <stdio.h>
#include <iostream>
#include"algorithm"
#include <string>
#include <vector>
#include <map>
#include <math.h>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
VI  number;
int GCD(int a,int b)
{
	if(a<b)
		swap(a,b);
	if(a%b==0)
		return b;
	else
		return GCD(b,a%b);
	return 0;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,Case,num,n,ans;
	cin>>Case;
	num=1;
	while (Case--)
	{	
		cin>>n;
		number.resize(n);
		for(i=0;i<n;i++)
		{
			cin>>number[i];
		}
		sort(number.begin(),number.end());
		if(n==3)
		{
			if(number[0] == number[1] && number[1] == number[2] )
			{
				ans =0;
			}
			else if(number[0] == number[1] || number[1] == number[2] )
			{
				number[1]=number[2];
				n=2;
			}
			else
			{
				ans=GCD(number[2]-number[1],number[1]-number[0]);
				if(ans==1)
				{
					ans =0;
				}
				else if(ans!=0)
				{
					if(number[0]%ans ==0)
					{
						ans = 0;
					}
					else
					{
						ans=ans-(number[0]%ans);
					}
				}
				
			}
			
		}
		if(n==2)
		{
			ans=number[1]-number[0];
			if(ans==1)
			{
				ans =0;
			}
			else if(ans>1)
			{
				if(number[0]%ans ==0)
				{
					ans = 0;
				}
				else
				{
					ans=ans-(number[0]%ans);
				}
			}
		}
		printf("Case #%d: %d\n",num++,ans);		
	}
	return 0; 
}
