#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
char s[1001],ss[1001];
int tt[5];
int main()
{
	int n,k,i,j,flag=1,min,len;
	cin>>n;
	while(n--)
	{
		cin>>k>>s;
		for(i=0;i<k;i++)tt[i]=i;
		len=strlen(s);
		min=1;
		for(i=1;i<len;i++)
		{
			if(s[i]!=s[i-1])min++;
		}
		while(next_permutation(tt,tt+k))
		{
			int ts=len/k;
			for(i=0;i<ts;i++)
			{
				for(j=0;j<k;j++)
				{
					ss[i*k+j]=s[i*k+tt[j]];
				}
			}
			int temp=1;
			for(i=1;i<len;i++)
			{
				if(ss[i]!=ss[i-1])temp++;
			}
			if(temp<min)min=temp;
		}
		cout<<"Case #"<<flag++<<": ";
		cout<<min<<endl;
	}
	return 0;
}