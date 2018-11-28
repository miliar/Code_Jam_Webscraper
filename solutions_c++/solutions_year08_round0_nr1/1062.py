#include<iostream>
#include<map>
#include<string>
using namespace std;
map<string,int> seen;
bool check[100];
int main()
{
	int n,s,q,i,j,tt,flag,res,casee=1;
	char nnn[101];
	string name;
	cin>>n;
	while(n--)
	{
		cin>>s;
		getchar();
		for(i=0;i<s;i++)
		{
			cin.getline(nnn,sizeof(nnn));
			name=nnn;
			seen[name]=i;
		}
		cin>>q;
		getchar();
		for(i=0;i<s;i++)check[i]=0;
		flag=0;
		res=0;
		if(q==0)goto label;
		i=0;
		while(1)
		{
			while(flag<s)
			{
				cin.getline(nnn,sizeof(nnn));
				name=nnn;
				i++;
				tt=seen[name];
				if(!check[tt])
				{
					check[tt]=1;
					flag++;
				}
				if(i==q)
				{
					if(flag==s)
					{
						res++;
					}
					goto label;
				}
			}
			res++;
			flag=1;
			for(j=0;j<s;j++)check[j]=0;
			check[tt]=1;
		}
label:  cout<<"Case #"<<casee++<<": "<<res<<endl;
	}
	return 0;
}
