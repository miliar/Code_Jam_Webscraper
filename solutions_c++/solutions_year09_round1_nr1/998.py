//////////////////////////////////////////////////////////////////////////
// Correct for small and large testsets
//////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;


int main()
{
	ifstream cin("A-small-attempt1.in");
	ofstream out("output.txt");

	int T,i,j;
	string line;
	vector<int> bases;
	cin>>T;
	cin.ignore();
	for(i=1; i<=T; i++)
	{
		bases.clear();
		getline(cin, line);
		stringstream sin(line);
		while(sin>>j)
			bases.push_back(j);

		for(j=2; ;j++)
		{
			bool flag = true;
			
			for(int k=0; k<bases.size(); k++)
			{
				bool flag1 = false;
				int temp = j;
				vector<int> nums;
				while(1)
				{
					nums.push_back(temp);
					//represent in base k
					int sum = 0;
					while(temp>0)
					{
						sum+=(temp%bases[k])*(temp%bases[k]);
						temp/=bases[k];
					}
					if(sum==1)
					{
						flag1 = true;
						break;
					}
					else if(find(nums.begin(), nums.end(), sum)!=nums.end())
					{
						flag1 = false;
						break;
					}

					temp = sum;
				}

				if(!flag1)
				{
					flag = false;
					break;
				}
			}

			if(flag)
			{
				out<<"Case #"<<i<<": "<<j<<endl;
				break;
			}
		}
	}

	//getchar();
	return 0;
}