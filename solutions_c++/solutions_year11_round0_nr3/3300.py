#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int min2(int a, int b)
{
	return a < b? a : b;
}

int min(vector<long int> v, int i,  int j)
{
	if(i == j)
		return v[i];		
	int mij = (i + j) / 2;
	return min2(min(v, i, mij), min(v, mij + 1, j));
		
}

long long sum(vector<long int> v)
{
	int n = v.size();
	long long sumS = 0, sumP = 0;
	for(int i = 0; i < n; i++){
		sumS += v[i];
		sumP ^= v[i];
	}	
	if(sumP != 0)
		return -1;
	else
		return sumS - min(v, 0, n - 1);
}

int main()
{
	ifstream in("C-large.in");
	ofstream out("output.txt");
	
	int T, N;
	long a;
	vector<long int> v;
	in >> T;
	for(int i = 0; i < T; i++) {
		in >> N;
		vector<long int> v;
		for(int j = 0; j < N; j++) {
			in >> a;
			v.push_back(a);		
		}
		long long rez = sum(v);
		if(rez < 0)
			out << "Case #" << i + 1 << ": NO\n"; 	
		else
			out << "Case #" << i + 1 << ": " << rez << "\n"; 	
			
	}	
	return 0;
}
