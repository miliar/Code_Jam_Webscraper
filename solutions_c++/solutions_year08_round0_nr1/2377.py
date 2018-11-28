#include <algorithm>
#include <vector>
#include <string>
#include <fstream>
using namespace std;


int main()
{
	ifstream infile;
	infile.open("A-large.in.txt");
	ofstream outfile;
	outfile.open("A-large.out.txt");
	int N, S, Q;
	infile>>N;
	int i, j, k;

	vector<string> engine;
	vector<string> output;
	vector<int> index;
	string temp;

	i = 0;
	while (i < N)
	{
		index.clear();
		engine.clear();

		infile>>S;
		getline(infile,temp);
		for (j=0; j<S; j++)
		{
		
			getline(infile,temp);

			engine.push_back(temp);
		}
		
		infile>>Q;
		getline(infile,temp);
		for (j=0; j<Q; j++)
		{
			getline(infile,temp);
			engine.push_back(temp);
			for (k=0; k<S; k++)
			{
				if (engine[k] == temp)
				{
					index.push_back(k);
					break;
				}
			}
		}
		//deal the index sequence
		size_t m = 0;
		size_t num = index.size();
		int number = 0, va, count=0;
		
		char* flag = new char[S];
		memset(flag, '0', S);
		while (m < num)
		{
			va = index[m];
			if (flag[va] == '0')
			{
				flag[va] = '1';
				number++;
			}
			if (number == S)
			{
				count++;
				memset(flag, '0', S);
				number = 0;
				m--;
			}
			m++;
		}
		outfile<<"Case #"<<i+1<<": "<<count<<endl;
		delete[] flag;
	i++;
	}

	infile.close();
	outfile.close();
}

