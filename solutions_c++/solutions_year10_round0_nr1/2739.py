#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

string result[] = { "OFF", "ON" };

int remain(int a, double b)
{
	if(a < b) return 0;
	
	while(a > 0)
	{
		a -= b;
	}
	
	return a == 0 ? 1 : 0;
}

string test(int N, int K)
{
	//return result[(K + 1) % (int)pow(2.0, N) == 0];
	return result[remain(K + 1, pow(2.0, N))]; 
}

int main()
{
	ifstream fin("aa.in");
	ofstream fout("aa.out");
	
	int T, N, K;
	int i;
	
	fin >> T;
	
	for(i = 1; i <= T; i++)
	{
		fin >> N >> K;
				
		fout << "Case #" << i << ": " << test(N, K) << endl;
	}
}