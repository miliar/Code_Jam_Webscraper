#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
using namespace std;


int main()
{
	int tmax,c,d,n;
	char temp;
	char C[36][3],D[28][2];
	char str[6],s[102];
	bool pararc,parard;
	vector<char> e;
	ifstream input;
	ofstream output;
	
	input.open("B-large.in");
	output.open("output.dat");
	
	input>>tmax;
	
	for (int t1=1;t1<=tmax;t1++)
	{
		input>>c;
		for (int i=0;i<c;i++)
		{
			input>>str;
			C[i][0]=str[0]; C[i][1]=str[1];C[i][2]=str[2];
		}
		input>>d;
		for (int i=0;i<d;i++)
		{
			input>>str;
			D[i][0]=str[0]; D[i][1]=str[1];
		}
		
		input>>n>>s;
		e.push_back(s[0]);

		
		for (int i=1;i<n;i++)
		{
			temp=s[i];
			pararc=false;
			for (int j=0;j<c;j++)
			{ 
				if (e.back() == C[j][0] && temp==C[j][1])
				{
					e.back()=C[j][2]; 
					pararc=true;
					break;
				}
				if (temp == C[j][0] && e.back()==C[j][1])
				{
					e.back()=C[j][2]; 
					pararc=true;
					break;
				}
					
			}
			
		
			if (!pararc)
			{
				
				parard=false;
				for (int j=0;j<d;j++)
				{
					if (temp==D[j][0] || temp==D[j][1])
					{
						for (int k=0;k<e.size();k++)
						{
							if (e[k]!=temp && (e[k]==D[j][0] || e[k]==D[j][1]))
								{
									e.clear(); parard=true; 
								
								break;
								}
							
						}
								
					}
					if (parard) break;
				}
			}
			if (!(parard || pararc)) e.push_back(temp);
			
		}
		
		if (!e.empty())
		{
		output<<"Case #"<<t1<<": ["<<e[0];

		for (int j=1; j<e.size();j++)
			output<<", "<<e[j];
		output<<"]\n";
		}
		else
			output<<"Case #"<<t1<<": []\n";
		e.clear();
	}
	input.close();
	output.close();
	
	return 0;
}
