#include<iostream>
#include<cstdio>
using namespace std;
char comb[128][128];

int main()
{
	int t;
	cin>>t;
	int c,d,n,index;
	char temp[100+10],oppose[3], output[100+10]	;
	bool flag;
	
	for(int z=1;z<=t;z++)
	{
		
		scanf("%d",&c);
		for(int i=0;i<c;i++)
		{
			scanf("%s",temp);
			comb[temp[0]][temp[1]]=temp[2];
			comb[temp[1]][temp[0]]=temp[2];
		}
		scanf("%d",&d);
		for(int i=0;i<d;i++)
		{
			scanf("%s",oppose);
		}
		scanf("%d %s",&n,temp);
		index=1;
		output[0]=temp[0];
		for(int cur=1;cur<n;cur++)
		{
			flag=0;
			//combinaiton
			if(comb[temp[cur]][output[index-1]]!=0)
			{
				//char find;
				output[index-1]=comb[temp[cur]][output[index-1]];
				/*if(output[index-1]==oppose[0] || output[index-1]==oppose[1])
				{
				if(output[index-1]==oppose[0])
				find=oppose[1];
				else 
				output[index-1]=oppose[0];
				for(int t=0;output[t];t++)
				{
					if(output[t]==find)
					{
						flag=1;
						index=0;
						output[index]=0;
						break;
					}
				}
				}*/
				continue;
			}
			else if(temp[cur]==oppose[0] || temp[cur]==oppose[1])
			{
				char find;
				if(temp[cur]==oppose[0])
				find=oppose[1];
				else 
				find=oppose[0];
				for(int t=0;output[t];t++)
				{
					if(output[t]==find)
					{
						flag=1;
						for(int i=0;i<index;i++)
						output[i]=0;

						index=0;
						output[index]=0;
						break;
					}
				}
			}
			if(flag==0)
			{
				
				output[index]=temp[cur];
				index++;
			}
		
		}
		output[index]=0;
		cout<<"Case #"<<z<<": [";
		for(int i=0;output[i];i++)
		{
			cout<<output[i];
			if(i<index-1)
			cout<<", ";
		}
		cout<<"]"<<endl;
		for(int i=0;i<128;i++)
			for(int j=0;j<128;j++)
				comb[i][j]=0;
		for(int i=0;i<110;i++)
		output[i]=0;
		oppose[0]=oppose[1]=oppose[2]=0;	
	}
	

}
