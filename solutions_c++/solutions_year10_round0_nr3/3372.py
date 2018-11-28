#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int testcases=0,rides=0,group=0,numg=0,temp=0,calc=0,ktemp=0,count=-1;
	
	vector< int > work;
	
	
    ofstream fout ("C-small-attempt0.out");
    ifstream fin ("C-small-attempt0.in");
	
	fin>>testcases;
	
	for(int i=0;i<testcases;i++)
	{
		work.clear();
		calc=0;
		fin>>rides>>group>>numg;

		for(int j=0;j<numg;j++)
		{
			fin>>temp;
			work.push_back(temp);
		}

		for(int n=0;n<rides;n++)
		{
			ktemp=group;
			count=-1;

			for(int a=0;a<work.size();)
			{
				count++;
				if(ktemp-work[a]>=0)
				{
					ktemp-=work[a];
					calc+=work[a];
					work.push_back(work[a]);
					work.erase(work.begin());
				}
				else
					break;

				if(count+1==work.size())
					break;
			}
			
		}

		fout<<"Case #"<<i+1<<": "<<calc<<endl;
		
	}
	
	
	return 0;
}

/*

  
	
*/