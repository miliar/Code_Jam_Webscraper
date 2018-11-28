#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int find_engine(vector<string>& engine, string& name, int S);

int main()
{
	// read file
	ifstream infile("A-large.in");
	ofstream outfile("result.out");

	int N, S, Q;

	infile >> N;
	vector<string> engine;
	string tmp;
	int i, j;
	int qnum;
	int point;
	
	int switch_num;

	for(i = 0; i < N; i++)
	{
		switch_num = 0;

		// every case
		infile >> S;
		engine.clear();
		engine.reserve(S);
		qnum = 0;
		
		int* flag = new int[S];
		// memset(flag, 0, sizeof(flag));
		for ( j = 0; j < S; j++)
		{
			flag[j] = 0;
		}

		getline(infile, tmp);  // eat space
		// store engines
		for (j = 0; j < S; j++)
		{
			//infile.getline(tmp, 100);
			getline(infile, tmp);
			engine.push_back(tmp);
		}
		
		infile >> Q;
		// query
		getline(infile, tmp);  // eat space
		for (j = 0; j < Q; j++)
		{
			getline(infile, tmp);
			if (qnum < S-1)
			{
				point = find_engine(engine, tmp, Q);
				if (flag[point] == 0)
				{
					qnum++;
					flag[point] = 1;
				}
			}
			else if(qnum == S-1)  // the last one
			{
				point = find_engine(engine, tmp, Q);
				if (flag[point] == 0)  // this time, swithing is coming
				{
					switch_num++;

					qnum = 1;
					//memset(flag, 0, sizeof(flag)); // zeros
					for (int k = 0; k < S; k++)
					{
						flag[k] = 0;
					}
					
					flag[point] = 1;
				}
			}
		}

		outfile << "Case #" << i+1 << ": " << switch_num << endl;

		delete []flag;
	}

	infile.close();
	outfile.close();
	return 0;
}

int find_engine(vector<string>& engine, string& name, int S)
{
	for (int i = 0; i < S; i++)
	{
		if (name == engine[i])
			return i;
	}
	return -1;
}