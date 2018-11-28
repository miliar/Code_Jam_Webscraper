// Funny.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(char** argv)
{
	ifstream in("C-small.in");
	ofstream out("C-small.out");

	int T;

	in >> T;
	for(int t = 0; t < T; t++)
	{
		int R, k, N, temp;
		in >> R >> k >> N;
		vector<int> group;
		for(int i = 0; i < N; i++)
		{
			in >> temp;
			group.push_back(temp);
		}
		
		long long int res = 0;

		int s = 0;
		for(int r = 0; r < R; r++)
		{
			temp = 0;
			for(int i = 0; i < group.size(); i++)
			{
				if((temp + group[s]) > k) break;
				temp += group[s];
				s = (s + 1) % group.size();
			}
			res += temp;
		}

		out << "Case #" << t + 1 << ": " << res << endl;
	}
	return 0;
}
