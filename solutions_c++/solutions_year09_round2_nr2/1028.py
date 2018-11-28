#include<stdio.h>
#include<vector>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<string>
using namespace std;
int i,j,k,n,m,t,l,p;
double a,b;
string ans;
string Read;
vector<int> ogo;
void read()
{
	
	cin>>Read;
	
}

void work()
{
	int max = -1,maxJ= -1;
	bool have=false;
	bool bighave = false;
	for(j=Read.size()-1;j>=1;j--)
	{
		have = false;
		for(k=j-1;k>=0;k--)
		{
			if(Read[k]<Read[j])
			{
				have = true;
				break;
			}
		}
		if( bighave==false ) bighave = have;
		if(have)
		{
			if(max<k)
			{
				max = k;
				maxJ = j;
			}
		}
		

	}
	ans.clear();
	ogo.clear();
	k = max;
	j = maxJ;
	//cout<<k<<"\t"<<j<<"\n";
	if( bighave )
	{
		
		for(t=0;t<k;++t)
			ans.push_back(Read[t]);
		ans.push_back(Read[j]);
		for(t=k;t<Read.size();++t)
			if(t!=j)
				ogo.push_back(Read[t]);
		sort(ogo.begin(),ogo.end());
		for(t=0;t<ogo.size();++t)
			ans.push_back(ogo[t]);
	}
	else
	{
		for(t=0;t<Read.size();++t)
			ogo.push_back(Read[t]);
		sort(ogo.begin(),ogo.end());
		p=0;
		while(ogo[p++]=='0');
		ans.push_back(ogo[p-1]);
		ans.push_back('0');
		for(t=0;t<ogo.size();++t)
			if(t!=p-1)
				ans.push_back(ogo[t]);
	}
}

void write()
{

	cout<<"Case #"<<(i+1)<<": "<<ans<<"\n";
}


int main()
{
	scanf("%d",&n);
	for(i=0;i<n;++i)
	{
	read();
	work();
	write();
	}
	return 0;
}