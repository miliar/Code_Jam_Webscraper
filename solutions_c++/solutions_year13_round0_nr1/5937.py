#include<iostream>
#include<iomanip>
#include<cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>

using namespace std;
#define f(i,a,b) for (int i = a; i < b; i++ )
#define rf(i,a,b) for (int i = a; i > =b; i-- )

int main()
{
	int t,n;
    	scanf("%d",&t);
    	string state[4];
    	for(int q=1;q<=t; q++)
    	{
    		int doti[4]={0};
    		int xi[4]={0};
    		int oi[4]={0};
    		int ti[4]={0};
        	int dotj[4]={0};
    		int xj[4]={0};
    		int oj[4]={0};
    		int tj[4]={0};
    		int countx=0;
    		int county=0;
    		int dot=0;
        	int flag=0;
        	f(i,0,4)
           	{
           		cin>>state[i];
           		f(j,0,4)
           		{
       				if(state[i][j]=='.')
       				{
           				doti[i]++;
           				dotj[j]++;
           				dot++;
           			}
           			else
           			{
           				if(state[i][j]=='X')
           				{	
           					xi[i]++;
           					xj[j]++;
           					countx++;
           				}
           				if(state[i][j]=='O')
           				{
           					oi[i]++;
           					oj[j]++;
           					county++;
           				}
           				if(state[i][j]=='T')
           				{
           					ti[i]++;
           					tj[j]++;
           				}
           			}
           		}			
           	}
           	
           	int turn=(countx-county);
           	if(turn==1) 
           	{
           		f(i,0,4)
           		{
                		if(xi[i]==4||(xi[i]==3 && ti[i]==1))
                		{	
                			printf("Case #%d: X won\n",q);
                			flag=1;
                			break;
                		}
                		else if(xj[i]==4||(xj[i]==3 && tj[i]==1))
                		{	
                			printf("Case #%d: X won\n",q);
                			flag=1;
                			break;
                		}
                	}
                	if(flag)
                		continue;
                	
                	int c1=0;
           		f(i,0,4)
           		{
           			
           			if(state[i][i]=='X'||state[i][i]=='T')
           				c1++;
           			else
           				break;
           		}
           		if(c1==4)
                	{	
                		printf("Case #%d: X won\n",q);
                		continue;
                	}
                	
                	c1=0;
                	f(i,0,4)
           		{
           			
           			if(state[i][3-i]=='X'||state[i][3-i]=='T')
           				c1++;
           			else
           				break;
           		}
           		if(c1==4)
                	{	
                		printf("Case #%d: X won\n",q);
                		continue;
                	}
                	
           		if(dot==0)
                	{
                		printf("Case #%d: Draw\n",q);
                		continue;
                	}
                	printf("Case #%d: Game has not completed\n",q);
                	continue;
                		
           	}
           	if(turn==0) 
           	{
           		f(i,0,4)
           		{
                		if(oi[i]==4||(oi[i]==3 && ti[i]==1))
                		{	
                			printf("Case #%d: O won\n",q);
                			flag=1;
                			break;
                		}
                		else if(oj[i]==4||(oj[i]==3 && tj[i]==1))
                		{	
                			printf("Case #%d: O won\n",q);
                			flag=1;
                			break;
                		}
                	}
                	if(flag)
                		continue;
                	
                	int c1=0;
           		f(i,0,4)
           		{
           			
           			if(state[i][i]=='O'||state[i][i]=='T')
           				c1++;
           			else
           				break;
           		}
           		if(c1==4)
                	{	
                		printf("Case #%d: O won\n",q);
                		continue;
                	}
                	
                	c1=0;
                	f(i,0,4)
           		{
           			
           			if(state[i][3-i]=='O'||state[i][3-i]=='T')
           				c1++;
           			else 
           				break;
           		}
           		if(c1==4)
                	{	
                		printf("Case #%d: O won\n",q);
                		continue;
                	}
                	
           		if(dot==0)
                	{
                		printf("Case #%d: Draw\n",q);
                		continue;
                	}
                	printf("Case #%d: Game has not completed\n",q);
                	continue;
                		
           	}                           	
    	}
    	return 0;
}
