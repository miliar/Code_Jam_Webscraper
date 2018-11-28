#include <iostream>
#include <string>
#include <vector>
#include <conio.h>
#include <cmath>

int main(int argc, char* argv[])
{
	int T;
	std::cin >> T;
	for(int loop = 0; loop < T; ++loop)
	{
		int N;
		std::cin >> N;
		std::vector<std::pair<char,int> > seq;
		for(int i=0; i < N; ++i)
		{
			char c;
			int s;
			std::cin >> c >> s;
			seq.push_back(std::make_pair(c,s));
		}

		int po = 1, pb = 1;
		char lr = seq[0].first;
		int overlap = seq[0].second;
		int time = overlap;
		if(lr == 'O')
		{
			po = seq[0].second;
		}
		else
		{
			pb = seq[0].second;
		}

		std::vector<std::pair<char, int> >::iterator it = seq.begin();
		++it;
		for(std::vector<std::pair<char, int> >::iterator end=seq.end();
			it != end; ++it)
		{
			int dis;
			if(it->first == 'O')
			{
				dis = abs(po - it->second);
				po = it->second;
			}
			else
			{
				dis = abs(pb - it->second);
				pb = it->second;
			}

			if(lr == it->first)
			{
				overlap+= dis + 1;
				time += dis + 1;
			}
			else
			{
				int time_tmp = overlap >= dis ? 1 : (dis-overlap+1);
				overlap = time_tmp;
				time += time_tmp;
				lr = it->first;
			}
		}
		std::cout << "Case #" << loop+1 << ":" << " ";
		std::cout << time << std::endl;
	}
	return 0;
}

