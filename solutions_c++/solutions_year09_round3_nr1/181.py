#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <iostream>
using namespace std;

int a1[10],a2[30],a3[100];
char str[100];

long long p (int x,int y)
{
	long long ret;
	int i;
	ret=1;
	for(i=0;i<y;i++)
		ret*=x;
	return ret;
}

int main()
{
	FILE *fin,*fout;
	fin=fopen ("All Your Base.in","r");
	fout=fopen ("All Your Base.out","w");
	
	int T,t;
	fscanf (fin,"%d",&T);
	
	int e,i,j,k;
	long long ans;
	for(t=1;t<=T;t++)
	{
		memset (a1,-1,sizeof a1);
		memset (a2,-1,sizeof a2);
		fscanf (fin,"%s",str);
		e=strlen (str);
		j=0;
		if(str[0]>='0' &&str[0]<='9')
			a3[0]=a1[str[0]-'0']=1;
		if(str[0]>='a' &&str[0]<='z')
			a3[0]=a2[str[0]-'a']=1;
		for(i=1;i<e;i++)
		{
			if(str[i]>='0' &&str[i]<='9')
			{
				if(a1[str[i]-'0']!=-1)
					a3[i]=a1[str[i]-'0'];
				else
				{
					if(j==1)
						j++;
					a3[i]=a1[str[i]-'0']=j++;
				}
			}
			if(str[i]>='a' &&str[i]<='z')
			{
				if(a2[str[i]-'a']!=-1)
					a3[i]=a2[str[i]-'a'];
				else
				{
					if(j==1)
						j++;
					a3[i]=a2[str[i]-'a']=j++;
				}
			}
		}
		k=0;
		ans=0;
		j=max (j,2);
		//cout<<a3[0]<<a3[1]<<a3[2]<<a3[3]<<endl;
		for(i=0;i<e;i++)
		{
			ans=ans*j+a3[i];
			k++;
		}
		fprintf (fout,"Case #%d: %lld\n",t,ans);
	}
	//cin>>t;
	return 0;
}
