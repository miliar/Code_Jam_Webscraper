#include<iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <vector>
#include <cstdio>
#include <fstream>
using namespace std;
char s1[40][4],s2[40][3],s[105],s3[105];
int d[105],f;
int main()
{
	int t,i,j,n,m,k,e,count=0;
	cin>>t;
	ofstream of("s.txt");
	while(t--)
	{
		count++;
		memset(d,0,sizeof(d));
		cin>>n;
		for(i=0;i<n;i++)
			cin>>s1[i];
		cin>>m;
		for(i=0;i<m;i++)
			cin>>s2[i];
		cin>>k;
			cin>>s;
		for(i=1;i<k;i++)
		{
			for(j=i-1;j>=0;j--)
				if(!d[j])
					break;
			//cout<<j<<endl;
			if(j>=0)
			for(e=0;e<n;e++)
			if(s[j]==s1[e][0]&&s[i]==s1[e][1]||s[j]==s1[e][1]&&s[i]==s1[e][0])
			{
				d[j]=1;
				s[i]=s1[e][2];
				//cout<<i<<" "<<s[i]<<endl;
				continue;
			}
			for(e=0;e<m;e++)
			if(s[i]==s2[e][0]||s[i]==s2[e][1])
			{
				if(s[i]==s2[e][0])
				{
					j=i-1;
					while(j>=0)
					{
						if(s[j]==s2[e][1]&&!d[j])
							break;
						j--;
					}
					if(j>=0)
                    for(j=0;j<=i;j++)
                    d[j]=1;
				}
				if(s[i]==s2[e][1])
				{
				   j=i-1;
					while(j>=0)
					{
						if(s[j]==s2[e][0]&&!d[j])
							break;
						j--;
					}
					if(j>=0)
                    for(j=0;j<=i;j++)
                    d[j]=1;
				}
			}
		}
        printf("Case #%d: [",count);
		of<<"Case #"<<count<<": [";
		for(j=k-1;j>=0;j--)
		{
			if(!d[j])
				break;
		}
		for(i=0;i<j;i++)
			if(!d[i])
			{
				cout<<s[i]<<", ";
				of<<s[i]<<", ";
			}
		if(j>=0)
        {
			cout<<s[j];
			of<<s[j];
		}
		cout<<"]"<<endl;
		of<<"]"<<endl;
	}
    return 0;
}
