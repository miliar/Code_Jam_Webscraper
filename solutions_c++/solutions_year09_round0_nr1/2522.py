#include<iostream>
#include<string>
using namespace std;
int main()
	{
	bool flag2=false, flag1=false;
	int i, L, D,N;
	char  a[5000][15];
	string  b;
	scanf("%d%d%d",&L,&D,&N);
	for(i=0; i<D; i++)
		scanf("%s",a[i]);
	for(i=0; i<N; i++)
		{
		cin>>b;
		int count=0, length = b.length();
		for(int j=0; j<D; j++)
			{
			int p=0;
			for(int k=0;k<length; k++)
				{
				if(b.at(k)=='(')
					flag2=true;
				else
					flag2=false;
					
				flag1=false;
				if(flag2==false)
					{
					if(b.at(k)==a[j][p])
						{
						  p++;
						flag1 = true;
						}
					else
						{
						flag1=false;
						break;
						}
				}
				else
					{
					while(b.at(k)!=')' && k<length)
						{
						if(b.at(k)==a[j][p])
							{
							if(flag1!=true)
								p++;
							flag1=true;
							}
						k++;
						}
					}
				if(flag1!=true)
					break;
				
				}
			if(flag1==true)
				count++;

			}
		printf("Case #%d: %d\n",i+1,count);
		}
	return 0;
	}
