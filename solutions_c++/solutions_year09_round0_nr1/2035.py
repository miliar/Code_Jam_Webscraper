#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int L,D,N;
	string str;
	vector<string> V;
	scanf("%d %d %d",&L,&D,&N);
	for(int i=0;i<D;i++)
	{
		cin>>str;
		V.push_back(str);
	}
	for(int i=0;i<N;i++)
	{
		printf("Case #%d: ",i+1);
		int count = 0,l=0;
		bool arr[15][26]={false};
		cin>>str;
		for(int j=0;j<str.size();j++)
		{
			if(str[j]!='(')
				arr[l][str[j]-'a']=true;
			else
			{
				j++;
				for(;str[j]!=')';j++)
					arr[l][str[j]-'a']=true;
			}
			l++;
		}
		for(int j=0;j<D;j++)
		{
			bool flag=true;
			for(int k=0;k<L;k++)
				if(arr[k][V[j][k]-'a']==false)
				{
					flag=false;
					break;
				}
			if(flag)
				count++;
		}
		cout<<count<<endl;
	}
}
