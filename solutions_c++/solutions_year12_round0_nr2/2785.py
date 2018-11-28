#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;


int main()
{
 int surprise,gooctr,lines,i=1,answer,j;
 double p;
 double googlers[1000];
 ifstream infile ("input.in");
 ofstream outfile;
 outfile.open ("out.txt");
 infile>>lines;
 cout<<lines;
 while(lines>0)
 {
	answer=0;
	outfile<<"Case #"<<i<<": ";
	infile>>gooctr;
	infile>>surprise;
	infile>>p;
	for(j=0;j<gooctr;j++)
	infile>>googlers[j];
 	for(j=0;j<gooctr;j++)
	{
		if((googlers[j]/3)>(p-1))
		{
			answer++;
		}
		else
		{
			if(surprise>0)
			{
				if((googlers[j]/3)>(p-2) && googlers[j]!=0)
				{
					answer++;
					surprise--;
				}
			}
		}
	}
	outfile<<answer<<"\n";
	lines--;
	i++;
 }

 outfile.close();
}
