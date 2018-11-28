#include <iostream>
#include <fstream>
using namespace std;

int main(){
	int t;
	int n;
	long k;
	int bit[30];
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("ans1_large.txt");
	fin >> t;
	for (int i = 0; i < t; ++i)
	{
		fin >> n >> k;
		for (int j = 0; j < 30; ++j)
			bit[j] = 0;
		int temp=0;
		bool flag = true;
		while (k > 0)
		{
			bit[temp] = k % 2;
			k = k / 2;
			++temp;
		}
		for (int j = 0; j < n; ++ j)
			if (!bit[j])
			{
				flag = false;
				break;	
			}
		if (flag)
			fout << "Case #" << i+1 << ": ON" << endl;
		else fout << "Case #" << i+1 << ": OFF" << endl;
	}
	fin.close();
	fout.close();
	return 0;	
}
