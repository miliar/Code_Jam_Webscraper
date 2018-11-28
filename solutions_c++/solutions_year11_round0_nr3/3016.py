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
int s[20],m,p,sum;
int f[20];
int max(int x,int y)
{
	if(x>y)
		return x;
	else
		return y;
}
void fa(int n,int num2,int num,int e,int j)
{
    int i,num1,w,w1;
	if(e==0)
	{
             w=0;w1=0;
		for(i=0;i<m;i++)
		if(!s[i])
		{
		w^=f[i];
		w1+=f[i];
        }
       // cout<<num<<" "<<w<<" "<<w1<<endl;
       if(w==num)
       {
                 p=max(w1,num2);
                 if(p>sum)
                 sum=p;
       }	
		return ;
	}
	for(i=j;i<=m-e;i++)
	{
        //cout<<"sdjfhd"<<endl;
		if(!s[i])
		{
			s[i]=1;
			num1=num^f[i];
			fa(n,num2+f[i],num1,e-1,i+1);
			s[i]=0;
		}
	}
}
int main()
{
	int t,i,j,count=0;
    cin>>t;
	ofstream of("s.txt");
	while(t--)
	{
		count++;
		cin>>m;
		sum=0;
		memset(s,0,sizeof(s));
		for(i=0;i<m;i++)
			cin>>f[i];
		for(i=1;i<=m/2;i++)
		fa(i,0,0,i,0);			
		cout<<sum<<endl;
		of<<"Case #"<<count<<": ";
			if(sum==0)
				of<<"NO"<<endl;
			else
				of<<sum<<endl;

	}
    return 0;
}
