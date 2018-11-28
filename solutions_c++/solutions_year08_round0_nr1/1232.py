#include<algorithm>
#include<vector>
#include<string.h>
#include<sstream>
#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int main(void)
{
	string str;
	int N=0, NSE=0,Q=0,caseno=0,NSwitch=0,skip=-1;
	vector < string > SEN;
	vector < int > trac;
	ifstream file("input.in");
	ofstream outputfile("output");

	if(file.is_open())
	{	file>>N;
		getline(file,str);//<<endl;					//reads in no of test cases....then endl.....

		while((++caseno)<=N)
		{
			file>>NSE;							//reads in no of search engine per case.....then endl.....
			getline(file,str);

			for(int i=0;i<NSE;i++)
			{
					getline(file,str);
					SEN.push_back(str);			//fills vector wid search engine names....
					trac.push_back(i);
			}
			file>>Q;								//reads the query from here on.......
			getline(file,str);
			int queryproc=0;
				
				while(queryproc<Q)
				{
					getline(file,str);	
					queryproc++;
					
					for(int i=0;(i<trac.size());i++)
					{
						if(trac.size()==1) skip=trac[i];
						
						if(str==SEN[trac[i]])
						{
							trac.erase(trac.begin()+i,trac.begin()+i+1); 
							i--;
							break;
						}					

					}

					if(trac.size()==0)
						{
						NSwitch++;
						for(int k=0;(k<NSE);k++)
						{		if(k!=skip)
								trac.push_back(k);
						}
						}
				
				}	//end of while
		//	}
			
			SEN.clear();							//purges the string for next iteration
			trac.clear();
		outputfile<<"Case #"<<caseno<<": "<< NSwitch<<"\n";
		NSwitch=0; skip=-1;
		}//end of case			

	}	
	else cout<<"Error opening file";
	file.close();
	outputfile.close();
	return 0;
}
