#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main (int argc, char * const argv[]) {

	int T, n, result;

	ifstream fin ("/A-small-attempt0.in");
	ofstream fout ("/A-output.txt");

	fin >> T;
	
	for (int i=1; i <= T; i++)
	{
		result = 0;
		fin >> n;
		vector<int> v1(n);
		vector<int> v2(n);
		for (int j=0; j <n; j++) 
		{
			fin >> v1[j];
		}
		for (int j=0; j <n; j++) 
		{
			fin >> v2[j];
		}
		
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		
		reverse(v2.begin(), v2.end());
		for (int j=0; j <n; j++) 
		{
			result = result+(v1[j]*v2[j]);
		}
		
		fout << "Case #" << i << ": " << result << endl;
	}
    return 0;
}
