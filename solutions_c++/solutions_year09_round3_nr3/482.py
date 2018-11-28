
#include "stdafx.h"
#include<algorithm>
#include<map>
#include<set>
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
using namespace std;
int cases,p,q;
int simulate(vector<int> );
int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}

int simulate(int order[])
{
		int states[104];
		memset(states,0,sizeof(states));
	int count=0;
    for(int i=0;i<q;i++)
	{
        states[order[i]]=1;
		
		for(int l=order[i]-1;l>0;l--)
			if(states[l]==0)
				count++;
			else
				break;
		for(int l=order[i]+1;l<=p;l++)
			if(states[l]==0)
				count++;
			else
				break;
		
	}
return count;
}



void main()
{

	
	ifstream cin("1.txt");
    ofstream cout("2.txt");
    
	string word;
	cin>>cases;

	
	for(int i=0;i<cases;i++)
	{
		int prisoner[105];	
	for(int l=0;l<105;l++)
		prisoner[l]=6000;
	
         cin>>p;
		 cin>>q;
		 int x;
		 for(int j=0;j<q;j++)
		 {
			 cin>>x;
			 prisoner[j]=x;
		 }
		
	
  

  sort (prisoner,prisoner+q);
int num=700000;
  do {
	  
	  if(simulate(prisoner)<num)
		  num=simulate(prisoner);
  } while ( next_permutation (prisoner,prisoner+q) );


		 cout<<"Case #"<<i+1<<": ";
		 cout<<num<<endl;
	}





}