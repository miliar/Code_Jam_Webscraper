#include<iostream>
#include<stdio.h>
#include <fstream>
using namespace std;
int main()
{
	char z,q[110];
		freopen("BotTrust.txt","w",stdout);
	int o[110],b[110],p[110],so,sb,n,m,i,j,k,s,x;
	cin>>n;
	x=0;
	while(n--)
	{
		x++;
		cin>>m;
		j=0;
		k=0;
		for(i=0;i<m;i++)
		{
			cin>>q[i]>>p[i];
		}
		s=0;
		so=1;
		sb=1;
		i=0;
		while(1)
		{
			if(i==m)break;
			if(q[i]=='O')
			{
				if(so==p[i])
				{
					s++;
					i++;
				}
				else if(so<p[i])
				{
					so++;
					s++;
				}
				else if(so>p[i])
				{
					so--;
					s++;
				}
				for(j=i;j<m;j++)
				{
					if(q[j]=='B')
					{
						if(sb==p[j])
						{
							;
						}
						else if(sb<p[j])
						{
							sb++;
						}
						else if(sb>p[j])
						{
							sb--;
						}
						break;
					}
				}
			}
			else if(q[i]=='B')
			{
				if(sb==p[i])
				{
					s++;
					i++;
				}
				else if(sb<p[i])
				{
					sb++;
					s++;
				}
				else if(sb>p[i])
				{
					sb--;
					s++;
				}
				for(j=i;j<m;j++)
				{
					if(q[j]=='O')
					{
						if(so==p[j])
						{
							;
						}
						else if(so<p[j])
						{
							so++;
						}
						else if(so>p[j])
						{
							so--;
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",x,s);
	}
	return 0;
}
