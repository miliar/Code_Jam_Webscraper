// google.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

std::string garbage;

void solve_case(int cas, std::ifstream & fs, std::ofstream & ofs)
{
	int n_s = 0;
	int n_q = 0;
	fs >> n_s;
	std::getline(fs, garbage);
	std::vector<std::string> eng(n_s);
	for(int i = 0; i != n_s; ++i)
	{
		std::getline(fs, eng[i]);
	}
	fs >> n_q;
	std::getline(fs, garbage);
	std::vector<std::string> que(n_q);
	for(int i = 0; i != n_q; ++i)
	{
		std::getline(fs, que[i]);
	}
	n_q = n_q;
	int qp = 0;
//	int prev_e = -1;
	int total_switches = 0;
	while( true )//qq != que.size() )
	{
		int best_e = 0;
		int best_q = 0;
		for(int e = 0; e != eng.size(); ++e)
		{
			std::string ce = eng[e];
//			if( prev_e == e )
//				continue; // Need to switch
			int q = qp;
			for( ;q != que.size(); ++q )
				if( que[q] == ce )
					break;
			if( q > best_q )
			{
				best_q = q;
				best_e = e;
			}
		}
		if( best_q == que.size() )
			break;
		total_switches += 1;
		qp = best_q;
		std::cout << qp << std::endl;
//		prev_e = best_e;
	}
	ofs << "Case #" << cas << ": " << total_switches << std::endl;
}

int main(int argc, char * argv[])
{
	std::ifstream fs("input.txt");
	std::ofstream ofs("output.txt");
	int n_cases = 0;
	fs >> n_cases;
	std::getline(fs, garbage);
	for(int c = 0; c != n_cases; ++c)
	{
		solve_case(c + 1, fs, ofs);
	}
	return 0;
}
