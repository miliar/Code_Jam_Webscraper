#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
	ifstream infile("A-small-attempt0.in");
	ofstream outfile("output.txt");
	int i,j,z,count;
	int p,k,l,res;
	vector<int> alphalist,keylist;
	
	infile >> count;
	cout << "Total Cases: " << count << endl;
	for (i=0; i<count; i++)
	{
		cout << "Case " << i << " started !" << endl;
		infile >> p >> k >> l;
		alphalist.clear();
		keylist.clear();
		res = 0;
		for (j=0; j<l;j++)
		{
			alphalist.push_back(0);
			infile >> alphalist[j];
		}
		for (j=0; j<k;j++)
			keylist.push_back(0);

		sort(alphalist.begin(),alphalist.end());
		reverse(alphalist.begin(),alphalist.end());
		
		for (j=0; j<l;j++)
		{
			keylist[0]++;
			if (keylist[0] > p)
			{
//				impossible = true;
//				break;
			}
			res += alphalist[j] * keylist[0];
			sort(keylist.begin(),keylist.end());
		}		
		
		
		outfile << "Case #" << i+1 << ": " << res << endl;
	}
		
	
	infile.close();
	outfile.close();
}
