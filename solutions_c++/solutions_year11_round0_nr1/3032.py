#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int countO, countB;
	int newO, oldO, newB, oldB; 
	int testcases,i,k,n,j;
	char ch;
	ifstream fin("A-large.in");
	ofstream fout("A-large-out.in");
	
	fin>>testcases;
	for(k=1;k<=testcases;k++)
	{
		oldO = oldB = 1;
		countO = countB = 0;
		fin>>n;
		for(i=0;i<n;i++)
		{
			fin>>ch;
			fin>>j;
			if(ch=='O')
			{
				newO=j;
				if(newO>=oldO)
				 countO += newO-oldO+1;
			 else if(oldO >= newO)
			  	countO += oldO-newO+1;
				oldO = newO;
				if(countO <= countB)
					countO+=countB-countO+1;	
			}	
			else if(ch=='B')
			{
				newB=j;
				if(newB>=oldB)
				 countB += newB-oldB+1;
			 else if(oldB >= newB)
			  	countB += oldB-newB+1;
				oldB = newB;
				if(countB <= countO)
					countB+=countO-countB+1;	
			}
		}
		fout<<"Case #"<<k<<": "<<((countB>countO)?countB:countO)<<endl;
		}
		return 0;
}
