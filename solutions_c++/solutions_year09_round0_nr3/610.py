#include<iostream>
#include<stdio.h>
using namespace std;

char s[]="welcome to code jam";
char t[600];
int map[501][20];

int main()
{
	int n;
	while(cin>>n)
	{
		cin.getline(t,501);
		for(int cas=0;cas<n;cas++)
		{
			cin.getline(t,501);
			int l=strlen(t);
			for(int i=0;i<=l;i++)
				for(int j=0;j<20;j++)
					map[i][j]=0;
			map[0][0]=1;
			for(int i=1;i<=l;i++)
			{
				for(int j=1;j<20;j++)
					if(t[i-1] == s[j-1])
					{
						for(int k=0;k<i;k++)
							map[i][j]=(map[i][j]+map[k][j-1])%10000;
					}
			}
			int sum=0;
			for(int i=0;i<=l;i++)
				sum=(map[i][19]+sum)%10000;
			cout<<"Case #"<<cas+1<<": "<<sum/1000<<(sum%1000)/100<<(sum%100)/10<<sum%10<<endl;
		}
	}
	return 0;
}
