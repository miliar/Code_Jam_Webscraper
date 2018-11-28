#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	int cases = 0;
	vector<vector<int> > holder;
	int h =0;

	ifstream myfile;
	myfile.open("inps.txt");
	if(myfile.is_open())
	{
		myfile >> h;
		holder.resize(h+1);
		holder[0].push_back(h);

			for(int i=1; i<=holder[0][0]; i++)
			{
				myfile >> h;
				holder[i].push_back(h);
				myfile >> h;
				holder[i].push_back(h);
				myfile >> h;
				holder[i].push_back(h);
				for(int j=0; j<holder[i][0]; j++)
				{
					myfile >> h;
					holder[i].push_back(h);
				} 
			}
	}
	myfile.close();

	//actual algo
	vector<int> track(holder[0][0]+1);
	for(int p=1; p<=holder[0][0]; p++)
	{
		for(int e=3; e<holder[p].size(); e++)
		{
			if(holder[p][e] == 0 && holder[p][2] ==0 || holder[p][e]==1 && holder[p][2] ==1)
			{
				track[p] +=1;
			}
			else
			{
				int hs = holder[p][2];
				if(holder[p][e]>=holder[p][2])
				{
					holder[p][e] -= holder[p][2];
					if (holder[p][e] >=-1)
					{
						if(holder[p][2]!=0){holder[p][2]-=1;}
						holder[p][e] -= holder[p][2];
						if (holder[p][e] >=-1)
						{
							if(holder[p][2]!=0){holder[p][2]-=1;}
							holder[p][e] -= holder[p][2];
							if(holder[p][e]>0)
							{
								track[p] += 1;
							} 
							else if((holder[p][e]== 0 && holder[p][1]>=1) || (holder[p][e]==-1 && holder[p][1]>=1))
							{
								track[p] +=1;
								holder[p][1] -= 1;
							}
						}
					}	
				}
				holder[p][2] = hs;
			}
		}
	}

	for(int w=1; w<track.size(); w++)
	{
		cout << "Case #" << w << ": " << track[w] << endl;
	}
	return 0;
}
