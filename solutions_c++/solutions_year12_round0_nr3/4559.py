#include<iostream>

using namespace std;

bool camb(int a,int b)
{
	if(a<10 || b<10)
		return 0;
	int ta=0,tb=0;
	int tmp=b;
	while(tmp>0)
	{
		tb++;
		tmp=tmp/10;
	}
	tmp=a;	
	while(tmp>0)
	{
		ta++;
		tmp=tmp/10;
	}

	if(ta!=tb)
		return 0;
	
	if(ta==2)
	{
		if(a==((b%10)*10+b/10))
			return 1;
	}
	if(ta==3)
	{
		if(a==((b%100)*10+b/100))
			return 1;
		if(a==((b%10)*100+b/10))
			return 1;
	}
	if(ta==4)
	{
		if(a==(b%1000)*10+b/1000)
			return 1;
		if(a==(b%100)*100+b/100)
			return 1;
		if(a==(b%10)*1000+b/10)
			return 1;
	}
			
	return 0;
}

int main()
{
	int n;
	cin>>n;
	int s1,s2;
	for(int q=1;q<=n;q++)
	{
		cout<<"Case #"<<q<<": ";
		cin>>s1>>s2;
		int cont=0;
		for(int i=s1;i<s2;i++)
		{
			for(int j=i+1;j<=s2;j++)
			{
				if(camb(i,j))
				{
					cont++;
				}
			}
		}
		cout<<cont<<endl;		
	}
}
