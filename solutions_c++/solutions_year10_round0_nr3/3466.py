#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int testcases=0,r=0,k=0,numg=0,temp=0,calc=0,ktemp=0,count=-1;
	
	vector< int > work;
	vector< int > ride;
	
	
    ofstream fout ("C-small-attempt2.out");
    ifstream fin ("C-small-attempt2.in");
	
	fin>>testcases;
	
	for(int i=0;i<testcases;i++)
	{
		work.clear();
		calc=0;
		fin>>r>>k>>numg;

		for(int j=0;j<numg;j++)
		{
			fin>>temp;
			work.push_back(temp);
		}

		for(int n=0;n<r;n++)
		{
			ktemp=k;
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
				if(a+1==work.size() || count+1==work.size())
					break;
			}
			
		}

		fout<<"Case #"<<i+1<<": "<<calc<<endl;
		
	}
	
	
	return 0;
}

/*

  
	
*/