#include<iostream>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<iomanip>
#include<algorithm>
#include<locale>
#include<cmath>
#include<cstdlib>

using namespace std;

int main()
{
	ifstream fin
	("files\\A2.in");
	ofstream fout
	("files\\A2.out");

	int use[] = {1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37};
	int N;
	fin>>N;
	set<char> ch;
	vector<char> ch2(100);
	vector<int> ch3(500);
	for(int i = 0; i < N; i++)
	{
		ch.clear();
		ch2.clear();
		ch3.clear();
		cout<<"=====Case #"<< i+1 <<"====="<<endl;
		string in;
		fin>>in;
		for(int j = 0; j < in.length(); j++)
		{
			if(ch.insert(in[j]).second)
			{
				ch2.push_back(in[j]);
				ch3[in[j]] = ch2.size()-1;
			}
		}
		int base = ch.size();
		base = max(2,base);
		cout<<base<<endl;
		unsigned long long result = 0;
		for(int j = 0; j < in.length(); j++)
		{
			result *= base;
			result += use[ch3[in[j]]];
		}

		fout<<"Case #"<< i+1 <<": "<<result<<endl;
		cout<<"Case #"<< i+1 <<": "<<result<<endl;
	}
}
