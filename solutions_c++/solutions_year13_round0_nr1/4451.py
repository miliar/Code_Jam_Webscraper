/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
* File Name : a.cpp
* Creation Date : 13-04-2013
* Last Modified : Saturday 13 April 2013 08:49:20 PM IST
* Created By :  Vishal Gupta
_._._._._._._._._._._._._._._._._._._._._.*/
                                   
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include<stack>
#include<vector>
#include<cstring>
#include<set>
#include<map>
#define sz(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traversing a container..works for any type of container
#define present(container, element) (container.find(element) != container.end())    //used for set...return 1 if el is ps 0 otherwise
#define cpresent(container, element) (find(all(container),element) != container.end())  //same as present...but is for vectors
#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define rep(i,n) 	FOR(i,0,n)
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d ",n)
#define pil(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
typedef long long int LL;
using namespace std;
int main()
{
	int t,T,countx,counto,flago,flagx,flagdot ,i,j;
	si(t);
	char a[5][5],m;
	rep(T,t)
	{
		flago=0; flagx=0; flagdot=0;
		for(i=0; i<4; i++)
		{
			ss(a[i]);
		}
		 scanf("%c",&m);
		for(i=0; i<4; i++)
		{
			counto=0; countx=0;
			for(j=0; j<4; j++)
			{
				if(a[i][j]=='.')
					flagdot=1;
				 if(a[i][j]=='X' || a[i][j]=='T')
					countx++;
				 if(a[i][j]=='O' || a[i][j]=='T')
					counto++;
			}
					if(countx==4)
			{ 
				flagx=1;
				break;
			}
			else if(counto==4)
			{
				flago=1;
				break;
			
			}
		}
		
		if(flagx==0 && flago==0)
		{
			for(j=0; j<4; j++)
			{
				counto=0; countx=0;
				for(i=0; i<4; i++)
				{


					if(a[i][j]=='X' || a[i][j]=='T')
						countx++;
					 if(a[i][j]=='O' || a[i][j]=='T')
						counto++;
				}
				
				if(countx==4)
				{ 
					flagx=1;
					 break;
				}
				else if(counto==4)
				{
					flago=1;
					break;
				}
			}
		}
		if(flagx==0 && flago==0) 
		{       countx=0; counto=0;
			for(i=0; i<4; i++)
			{
				if(a[i][i]=='X' || a[i][i]=='T')
					countx++;
				 if(a[i][i]=='O' || a[i][i]=='T')
					counto++;

			} 
				
			if(countx==4)
			{
				flagx=1;
			        		
			}
				else if(counto==4)
				{
					flago=1;
				}
	        }
		if(flagx==0 && flago==0) 
		{
			countx=0; counto=0;
			for(i=0; i<4; i++)
			{
				if(a[i][3-i]=='X' || a[i][3-i]=='T')
					countx++;
				 if(a[i][3-i]=='O' || a[i][3-i]=='T')
					counto++;
                                      
			} 
				
			if(countx==4)
			{
				flagx=1;
			
			}
				 if(counto==4)
				flago=1;
		}
		if(flago==1)
			printf("Case #%d: O won\n",T+1);
		 if(flagx==1)
			printf("Case #%d: X won\n",T+1);
		 if(flago==0 && flagx== 0)
		{
			if(flagdot==0)
				printf("Case #%d: Draw\n",T+1);		
			else
				printf("Case #%d: Game has not completed\n",T+1);		

		}
	}
	return 0;
}
