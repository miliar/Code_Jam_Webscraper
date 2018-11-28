#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <vector>
#define F(i,n) for(i=0;i<n;i++)
using namespace std;
int check(int s[])
{
	if(s['O']==4)
	return 1;
	if(s['X']==4)
	return 2;
	if(s['O']==3 && s['T']==1)
	return 1;
	if(s['X']==3 && s['T']==1)
	return 2;
	else
	return 3;
}
void setdigits(int s[])
{
	   s['.']=0;
	   s['O']=0;
	   s['T']=0;
	   s['X']=0;
}
int main()
{ string s[4];
	int t,l,n,i,j;
	cin>>t;
	for(l=1;l<=t;l++)
	{ int k[255],n=10;
	   setdigits(k);
		F(i,4)
		cin>>s[i];
		
		F(j,4)
		{setdigits(k);
		  F(i,4)
		   {
		    k[s[i][j]]++;
			}
		n=check(k);
		if(n<=2)
		goto X;
		}
	   //diag check
		setdigits(k);
		for(i=0,j=0;i<4;i++,j++)
		k[s[i][j]]++;
		n=check(k);
		if(n<=2)
		goto X;
	    setdigits(k);
		for(i=0,j=3;i<4;i++,j--)
		k[s[i][j]]++;
		n=check(k);
		if(n<=2)
		goto X;
		//rowcheck
		setdigits(k);
		 
		F(i,4)
		{ setdigits(k);
		F(j,4)
		{   
			k[s[i][j]]++;
			
		}
		n=check(k);
		if(n<=2)
		goto X;
		}
		X:
		if(n==1)
		printf("Case #%d: O won\n",l);
		else if (n==2)
		printf("Case #%d: X won\n",l);
		else if(k['.']>0)
		printf("Case #%d: Game has not completed\n",l);
		else
		printf("Case #%d: Draw\n",l);
	}
		return 0;
	}
