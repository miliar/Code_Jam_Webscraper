#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
using namespace std;

ifstream lettura ("input.txt");
ofstream scrittura ("output.txt");

char combine[256][256];
int opposed[256][256];

int main ()
{
	int t;

	lettura >> t;

	for (int i = 1; i <= t; i += 1)
	{
		memset (combine, 0, 256*256 * sizeof (char));
		memset (opposed, 0, 256*256 * sizeof (int));

		int c, d, n;
		string s;

		lettura >> c;

		for (int j = 0; j < c; j += 1)
		{
			lettura >> s;
			combine[s[0]][s[1]] = s[2];
			combine[s[1]][s[0]] = s[2];
		}

		lettura >> d;

		for (int j = 0; j < d; j += 1)
		{
			lettura >> s;
			opposed[s[0]][s[1]] = 1;
			opposed[s[1]][s[0]] = 1;
		}

		lettura >> n >> s;

		vector<char> seq;

		for (int j = 0; j < n; j += 1)
		{
			seq.push_back (s[j]);
			if (seq.size () >= 2)
			{
				if (combine[seq[seq.size()-1]][seq[seq.size()-2]] != 0)
				{
					char temp = combine[seq[seq.size()-1]][seq[seq.size()-2]];
					seq.pop_back ();
					seq.pop_back ();
					seq.push_back (temp);
				}
				else
				{
					for (int k = 0; k < seq.size ()-1; k += 1)
					{
						if (opposed[seq[seq.size()-1]][seq[k]] != 0)
						{
							seq.clear ();
							break;
						}
					}
				}
			}
		}

		scrittura << "Case #" << i << ": [";
		for (int j = 0; j < seq.size(); j += 1)
		{
			if (j != 0)
			{
				scrittura << ", ";
			}
			scrittura << seq[j];
		}
		scrittura << "]" << endl;
	}
}
