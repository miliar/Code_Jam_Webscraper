#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int L, D, N;
	cin >> L >> D >> N;

	vector<string> dict(D);

	for(int i=0;i<D;i++)
	{
		cin >> dict[i];
	}

	for(int i=0;i<N;i++)
	{
		int poss = 0;
		vector<string> tokens(L);

		string temp;
		cin >> temp;

		bool inside = false;
		int index = 0;
		for(int j=0;j<temp.size();j++)
		{
			if(temp[j] == ')')
			{
				inside = false;
				index++;
			}
			else if(temp[j] == '(')
			{
				inside = true;
			}
			else
			{
				tokens[index] += temp[j];
				if(!inside)
				{
					index++;
				}
			}
		}

		for(int j=0;j<dict.size();j++)
		{
			bool valid = true;
			for(int k=0;k<dict[j].size() && valid;k++)
			{
				if(tokens[k].find(dict[j][k]) == string::npos)
				{
					valid = false;
				}
			}
			if(valid)
			{
				poss++;
			}
		}		

		cout << "Case #" << i+1 << ": " << poss << endl;
	}
	return 0;
}
