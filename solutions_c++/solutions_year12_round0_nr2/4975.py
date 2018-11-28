#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
using namespace std;

int max(int a,int b)
{
	if(a>=b)
		return a;
	else 
		return b;
}

int max(int a, int b, int c)
{
	if(a>=b && a>=c)
		return a;
	else if(b>=c && b>=a)
		return b;
	else
		return c;
}

void getbest(int total, int *notsurprising, int *surprising)
{
	int bests=-1;
	int bestns=-1;
	for(int i=0;i<=10;i++)
	{
		for(int j=0;j<=10;j++)
		{
			for(int k=0;k<=10;k++)
			{
				if(i+j+k==total)
				{
					if(abs(i-j)<2 && abs(i-k)<2 && abs(k-j)<2)
                      bestns=max(bestns,max(i,j,k));
					else if(abs(i-j)<=2 && abs(i-k)<=2 && abs(k-j)<=2)
                      bests=max(bests,max(i,j,k));
				}
			}
		}
	}
	notsurprising[total]=bestns;
	surprising[total]=bests;
}



void main()
{
	int notsurprising[31];
	int surprising[31];
	for(int i=0;i<31;i++)
		getbest(i,notsurprising,surprising);
    int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin>>t;
	int numberofsurprising;
	int numberofgooglers;
	int p;
	int total;
    int ssatisfies;//number that satisfy only in suprising case
	int nssatisfies;//number that satisfy only in the non suprising case
	int bothsatisfy;
	int result;
	int losers;
	for(int i=1;i<=t;i++)
	{
      fin>>numberofgooglers>>numberofsurprising>>p;
	  ssatisfies=0;
	  bothsatisfy=0;
	  nssatisfies=0;
	  for(int j=0;j<numberofgooglers;j++)
	  {
		  fin>>total;
		  if(surprising[total]>=p && notsurprising[total]>=p)
			  bothsatisfy++;
		  else if(notsurprising[total]>=p)
			  nssatisfies++;
		  else if(surprising[total]>=p)
			  ssatisfies++;

	  }
	  losers=numberofgooglers-(ssatisfies+nssatisfies+bothsatisfy);
	  if(ssatisfies>=numberofsurprising)
	    result=nssatisfies+numberofsurprising+bothsatisfy;
	  else if(ssatisfies+bothsatisfy>=numberofsurprising)
		result=nssatisfies+bothsatisfy+ssatisfies;
	  else if(losers>=numberofsurprising-ssatisfies-bothsatisfy)
		  result=nssatisfies+bothsatisfy+ssatisfies;
	  else 
		  result=bothsatisfy+ssatisfies+nssatisfies-(numberofsurprising-ssatisfies-bothsatisfy-losers);
	  if(result<0)
		  result=0;	
	  fout<<"Case #"<<i<<": "<<result<<endl;
	}

}