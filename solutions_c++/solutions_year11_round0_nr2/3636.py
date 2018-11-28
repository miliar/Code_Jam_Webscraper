#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
	int t;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	int n,size;
	vector<char> result;
	bool conflict[26][26];
	char combine[26][26];
	char one,two;
	string final,qwer;
	bool comb,conf;
	for(int j=0;j<t;j++)
	{
		result.clear();
		conf=false;	comb=false;
		for(int a=0;a<26;a++)
			for(int s=0;s<26;s++)
			{
				conflict[a][s] = false;
				combine[a][s] = NULL;
			}
		scanf("%d",&n);
		
		for(int i=0;i<n;i++)
		{
			cin>>qwer;
			combine[int(qwer[0])-65][int(qwer[1])-65] = qwer[2];
			combine[int(qwer[1])-65][int(qwer[0])-65] = qwer[2];
		}

		scanf("%d",&n);

		for(int i=0;i<n;i++)
		{
			cin>>qwer;
			conflict[int(qwer[0])-65][int(qwer[1])-65]=true;
			conflict[int(qwer[1])-65][int(qwer[0])-65]=true;
		}

		scanf("%d",&n);
		cin>>final;

		for(int i=0;i<n;i++)
		{
			result.push_back(final[i]);	size=result.size();	comb=false;

			if(result.size() >1)
			{
				if(combine[int(result[size-1])-65][int(result[size-2])-65] != NULL)
				{
					one = result[size-1];	two = result[size-2];
					result.pop_back();	result.pop_back();
					result.push_back(combine[int(one)-65][int(two)-65]);
					comb = true;
				}
				if(!comb)
				{
					for(int k=0;k<result.size();k++)
					{
						if(conflict[int(result[size-1])-65][int(result[k])-65])
						{
							result.clear();
							break;
						}
					}
				}
			}
		}
		
		size=result.size();
		printf("Case #%d: [",j+1);
		if(result.size()!=0)
		{
			cout<<result[0];
			for(int i=1;i<result.size();i++)
			{
				printf(", ");
				cout<<result[i];
			}
		}
		printf("]\n");
	}
		

	return 0;
}