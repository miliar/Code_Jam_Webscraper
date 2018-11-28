#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	vector<string> words;
	vector<string> lang;

	int L = 0, D = 0, N = 0;
    infile >> L >> D >> N;
	int count = 0;
	int index1 = 0, index2 = 0;
	int index3 = 0;
	int n = 1;
	while(D-- > 0)
	{
		string temp;
		infile >> temp;
		words.push_back(temp);
	}
	while(N-- > 0)
	{
		string temp;
		infile >> temp;
		lang.push_back(temp);
	}

	for(vector<string>::iterator pos = lang.begin(); pos < lang.end(); ++pos)
	{
		count = 0;
		for(vector<string>::iterator iter = words.begin(); iter < words.end(); ++iter)
		{
			index1 = 0;
			index2 = 0;
			for(int num = 0; num < L; num++)
			{
				if((*pos)[index1] == '(')
				{
					index2 = pos->find(')', index1);
					index3 = pos->find((*iter)[num], index1);
					if(index3 == -1 || index3 > index2)
					{
						break;
					}
					index1 = index2 + 1;
				}
				else
				{
					if((*pos)[index1] == (*iter)[num])
					{
						index1++;
					}
					else
					{
						break;
					}
				}
			}
			if(num == L)
			{
				count++;
			}
		}
		outfile << "Case #" << n << ": " << count <<endl;
		n++;
	}
	return 0;
}