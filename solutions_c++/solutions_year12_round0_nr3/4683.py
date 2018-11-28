#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <map>
#include <cstring>
#include <math.h>
using namespace std;

#define fin(i,T) for(i = 0; i < T; i++)
#define abs(x) (x<0) ? x : -x

int hund(int x)
{
	if(x < 10) return 10;
	else if(x < 100) return 100;
	else if(x < 1000) return 1000;
	else if(x < 10000) return 10000;
	else if(x < 100000) return 100000;
	else if(x < 1000000) return 1000000;
	else if(x < 10000000) return 10000000;
}

int main()
{
	string line;
	int i;
	
	int T;
	
	ifstream infile("C-small-attempt0.in");
	
	ofstream outfile ("output.txt");
	
	if (infile.is_open() && outfile.is_open()) 
	{
		infile >> T;
		getline(infile, line);
		istringstream iss(line);
		
		fin(i,T)
		{
			int A,B;
			
			getline(infile, line);
			istringstream iss(line);
			
			iss >> A;
			iss >> B;
			
			int c = 0;
			
			for(int j=A; j<B; ++j)
			{
				for(int k=j+1; k<=B; ++k)
				{
					for(int l=1; l<=6; ++l)
					{
						//cout << "A/(10*l) = " << A/(10*l) << endl;
						//if((int)floor(((double)j)/(10*l)) > 0)
						int mod = j % (int)pow(10,l);
						if(hund(mod) == hund(j)) continue;
						if(mod == j)
							break;
						else
						{
							int fl = (int)floor(((double)j)/pow(10,l));
							int nr = mod * hund(fl) + fl;
							//cout << "j=" << j << " nr=" << nr << " k=" << k << endl;
							if(nr == k && nr > j)
							{
								c++;break;
								//cout << c << ": j=" << j << "  " << mod << " " << fl << " = " << k << endl;
							}
						}
					}
				}
			}
			
			outfile << "Case #" << (i+1) <<": " << c << endl;
		}
		infile.close();
		outfile.close();
	}

	return 0;
}
