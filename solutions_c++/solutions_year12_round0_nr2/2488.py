#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	ifstream fi("data.txt");
	ofstream fo("output.txt");
	int lines;
	fi >> lines;
	int* da;
	da = new int[lines];
	for(int i=0; i<lines;i++)
	{
		da[i] = 0;
		int n;
		int s;
		int p;
		int scores;
		fi >> n >> s >> p;
		cout << n << " " << s << " " << p << " ";
		int* mm;
		mm = new int[n];
		scores = (p-1)*3;
		for(int j=0;j<n;j++)
			{
				fi >> mm[j];
				cout << mm[j] << " ";
				if(mm[j] > scores)
					da[i]++;
				else if((mm[j] > scores -2) && (s>0) && (mm[j] >0))
				{
					da[i]++;
					s--;
				}
			}
		cout << "Case #" << i+1 << ": " << da[i];
		fo << "Case #" << i+1 << ": " << da[i] << endl;
		cout << endl;
		delete[] mm;
	}
	fi.close();
	fo.close();
	return 0;
}