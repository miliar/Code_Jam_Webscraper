#include <iostream>
#include <stdio.h>
#include <vector>
#include <memory.h>

using namespace std;

int canCombine[256][256];
bool isOpposed[256][256];


typedef vector<int>::iterator VI;

int main()
{
	int T;
	scanf("%d",&T);
	
	for(int t=0;t<T;t++)
	{
		memset(canCombine,-1,sizeof(canCombine));
		memset(isOpposed,false,sizeof(isOpposed));
		
		vector<int> v;
		
		int C;
		
		scanf("%d",&C);
		
		for(int n=0;n<C;n++)
		{
			char ch[5];
			scanf("%s",ch);
			
			int a= ch[0];
			int b=ch[1];
			int c=ch[2];
			
			canCombine[a][b]=c;
			canCombine[b][a]=c;
		}
		
		int D;
		scanf("%d",&D);
		
		
		for(int n=0;n<D;n++)
		{
			char ch[5];
			scanf("%s",ch);
			
			int a=ch[0];
			int b=ch[1];
			
			isOpposed[a][b]=true;
			isOpposed[b][a]=true;
		}
		
		char str[200];
		
		int N;
		scanf("%d",&N);
		
		scanf("%s",str);
		
		for(int n=0;n<N;n++)
		{
			int num = (int)str[n];
			
			if(v.size()==0)
			{
				v.push_back(num);
			}
			else if(canCombine[v.back()][num]!=-1)
			{
				int add = canCombine[v.back()][num];
				v.pop_back();
				v.push_back(add);
			}
			else
			{
				bool del = false;
				
				for(VI it =v.begin();it!=v.end();it++)
				{
					if(isOpposed[*it][num])
					{
						del =true;
						break;
					}
				}
				
				if(del)
				{
					v.clear();
				}
				else
				{
					v.push_back(num);
				}
				
			}
		}
		
		printf("Case #%d: ",t+1);
		
		printf("[");
		
		if(v.size()>0)
		{
			printf("%c",v[0]);
		}
		
		for(unsigned int i=1;i<v.size();i++)
		{
			printf(", %c",v[i]);
		}
		
		printf("]\n");
		
		
		
		
		
		
		
		
		
		
	}
}