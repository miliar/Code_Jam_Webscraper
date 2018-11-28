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

//bool cop(char a, char b)
//{
//
//}

int main()
{
	ifstream fin
	("files\\B2.in");
	ofstream fout
	("files\\B2.out");


	int N;
	fin>>N;

	for(int i = 0; i < N; i++)
	{
		cout<<"=====Case #"<< i+1 <<"====="<<endl;
		string input;
		fin>>input;
		bool ok = 0;
		int len = input.length();
		cout<<len<<endl;
		string output = input;
		while(next_permutation (output.begin(), output.end()))
		{
			if(output>input){ok = 1;break;}
		}
		if(!ok)
		{
			sort(output.begin(), output.end());
			if(output[0] == '0')
			{
				swap(output[output.find_first_not_of('0')], output[0]);
			}
			output.insert(1,"0");
		}

		fout<<"Case #"<< i+1 <<": "<<output<<endl;
		cout<<"Case #"<< i+1 <<": "<<output<<endl;
	}
}
