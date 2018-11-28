#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int testcases=0,snapp=0,num ;

	vector< pair <int , int> > work;
	pair <int , int> temp;


    ofstream fout ("A-small-attempt4.out");
    ifstream fin ("A-small-attempt4.in");

	fin>>testcases;

	for(int i=0;i<testcases;i++)
	{
		work.clear();

		fin>>num>>snapp;

		for(int j=0;j<num;j++)
		{
			temp.first=0;
			temp.second=0;
			work.push_back(temp);
		}

		work[0].first=1;

		for(int u=0;u<snapp;u++)
		{
			if(work[0].second==0)
			{
				work[0].second=1;

				for(int h=1;h<work.size();h++)
				{
					if(work[h-1].second==1 && work[h-1].first==1)
					{
							work[h].first=1;
					}
						
				}

			}

			else
			{
				for(int h=1;h<work.size();h++)
				{
					if(work[h].first==1)
					{
						if(work[h].second==0)
						{
							work[h].second=1;
						}
						else
						{
							work[h].second=0;
						}

						work[h].first=0;
					}

						
				}

				work[0].second=0;
			}

		}

		bool flag=true;

		for(int o=0;o<work.size();o++)
		{
			if(work[o].second==0)
			{
				flag=false;
				break;
			}

		}

		if(flag)
		{
			fout<<"Case #"<<i+1<<": ON\n";
		}
		else
		{
			fout<<"Case #"<<i+1<<": OFF\n";
		}




	}


	return 0;
}

/*

 

*/