/*
ID: ebappa11
PROG: solder
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>



#define MAXN 105
using namespace std;

int main() {
	ofstream out ("A-small.out");
	ifstream in ("A-small.in");


	int ts, N, pos[2], sec[2], n, s;
	char B;
	vector <int> seq, bot;

	in >> ts;

	for (unsigned int t = 0; t < ts; t += 1)
	{
		sec[0]=0;
		sec[1]=0;
		pos[1]=1;
		pos[0]=1;
		s=0;
		in >> N;

		for (unsigned int i = 0; i < N; i += 1)
		{
			in >> B >> n;
			if (B == 'O')
			{
				bot.push_back(0);
			}
			else	bot.push_back(1);

			seq.push_back(n);
		}

		for (unsigned int i = 0; i < N; i += 1)
		{
			
			s = (sec[bot[i]] + abs(seq[i] - pos[bot[i]]) >= s)?sec[bot[i]] + abs(seq[i] - pos[bot[i]]) + 1:s+1;
			//cout << abs(seq[i] - pos[bot[i]]) << ' ' <<bot[i] << ' ' << sec[bot[i]] << ' ' << s << "\n";
			sec[bot[i]] = s;
			pos[bot[i]]=seq[i];
			
		}

		out << "Case #" << t+1 << ": " << s << "\n";
		seq.clear();
		bot.clear();
	}
	
	return 0;
}








