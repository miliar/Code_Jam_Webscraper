#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<map>
#include<algorithm>
#include<list>
#include<math.h>
#include<vector>
#include <stdint.h>

using namespace std;

int main()
{
	ifstream infile("C-small-attempt0.in");
	ofstream outfile("C-small-output.txt");
	
	if(!infile)
	{
		cout<<"Error opening inout file";
		return 1;
	}
	if(!outfile)
	{
		cout<<"Error opening output file";
		return 1;
	}
	int numTestCases;
	int num, k, R;
	int group[1000], temp;
	infile >> numTestCases;
	for(int i = 1; i<= numTestCases; i++)
	{
		//Input testcase
		infile >> R;
		infile >> k;
		infile >> num;
		cout<<" R, k, num are"<<R<<","<<k<<","<<num<<endl;
		for(int j =0; j<num; j++)
		{
			infile >> temp;
			group[j] = temp;
			cout<<group[j];
		}
		cout<<endl;

		//Process
		int num_grp=0, cur_grp = 0, tot_money=0, max_count=k;
		while(R>0)
		{
			while(max_count)
			{
				if((group[cur_grp] <= max_count) && (num_grp < num))
				{
					tot_money += group[cur_grp];
					max_count -= group[cur_grp];
					cur_grp = (cur_grp + 1)%num;
					num_grp++;
				}
				else
				{
					break;
				}
			}
			R--;
			max_count = k;
			num_grp=0;
		}
		
		//Output result
		outfile << "Case #"<< i <<": "<< tot_money<<"\n";
	}

}
