
#include <iostream>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	double val1,val2,val3;
	ifstream in("D:\\A-large.in");
	if(!in) 
	{
		cout << "Cannot open input file.\n";
		return 1;
	}
	char str[1000];
	string str2;
	in.getline(str,1000);
	istringstream iss(str,istringstream::in);
	iss >> val1;
	cout << val1 << endl;
	int thecase = 0;
	while (thecase < val1)
	{
		in.getline(str,1000);
		istringstream iss2(str,istringstream::in);
		iss2 >> val2;

		string *listNames = new string[val2];
		for (int i =0; i < val2; i++)
		{
			in.getline(str,1000);
			listNames[i] = str;
		}
		in.getline(str,1000);
		istringstream iss3(str, istringstream::in);
		iss3 >> val3;
		
		string *searches = new string[val3];
		for (int i = 0; i<val3; i++)
		{
			in.getline(str,1000);
			searches[i] = str;
		}
		int *marker = new int[val2];
		for (int i = 0; i < val2; i++)
		{
			marker[i] = false;
		}
		int j = 0;
		int changes = 0;
		string currentname = "asegasdf";

		int counter = 0;
		int position = 0;
		while( j < val3)
		{
			int k = 0;
			while ( k < val2 )
			{
				/*if (searches[j] == currentname)
				{
					for (int m = 0; m < val2; m++)
					{
						marker[m] = 1;
						position = m;
					}
					break;
				}*/
				if (searches[j] == listNames[k])
				{
					marker[k] = 1;
					break;
				}
				k++;
				if (k == val2)
				{
					cout << "no change needed";
				}
			}
			//checking markers
			int sum = 0;
			for (int m = 0; m < val2; m++)
			{
				sum = sum + marker[m];
			}
			if (sum == val2)
			{
				currentname=listNames[position];
				for (int m = 0; m < val2; m++)
				{
					marker[m] = 0;
				}
				counter++;
				j--;
			}
			j++;
		}
			

		cout << "Case #" << thecase+1 <<": " << counter << endl;
		thecase++;
	}
	in.close();
}