#pragma once

///////////////////////////////////////////////////
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <map>
#include <sstream>
#include <stack>
#include <set>
#include <math.h>
#include <limits>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <hash_map>
#include <hash_set>
using namespace std;
using namespace stdext;
////////////////////
#define i64 long long
///////////////////////////////////////////////////
namespace GoogleJam
{
	const string dataFolderC = "C:\\Programming\\!Private\\ProblemSolver\\!Data\\Google Jam\\";
	class Numbers
	{
			struct Case
			{
				int A, B;
				i64 m_Count;
			};
			vector <Case> m_Cases;
			vector <int> m_Powers;
			//////////////////////////////////////////////////////
			void readInput()
			{
				string path = dataFolderB + "Numbers\\C-large.in";
				ifstream is;
				is.open(path.c_str());
				if (!is.is_open()) throw 1;
				////////////////////////////////////////////////
				int T;
				string line;
				is >> T;				
				getline(is, line);
				m_Cases.resize(T);
				for (int t = 0; t < T; ++t)
				{
					getline(is, line);
					istringstream ist(line);
					ist >> m_Cases[t].A >> m_Cases[t].B;
				}
				is.close();
			}
			void saveOutput()
			{
				string path = dataFolderB + "Numbers\\res.out";
				ofstream os;
				os.open(path.c_str());
				if (!os.is_open()) throw 1;
				os.precision(20);
				///////////////////////////////////////////////
				for (int i = 0; i < m_Cases.size(); ++i)
				{
					os << "Case #" << i + 1 << ": " << m_Cases[i].m_Count << endl;					
				}
				///////////////////////////////////////////////
				os.close();
			}
			inline int getDigits(int n)
			{
				int d = 0;				
				while (n > 0)
				{
					++d;
					n /= 10;
				}
				return max(1, d);
			}
			int getPower(int k)
			{
				if (m_Powers[k] > 0) return m_Powers[k];
				m_Powers[k] = 1;
				for (int i = 0; i < k; ++i)
					m_Powers[k] *= 10;
				return m_Powers[k];
			}
			void solveCase(Case& cs)
			{
				cs.m_Count = 0;				
				int digits = getDigits(cs.A);
				int next = getPower(digits);
				for (int n = cs.A; n < cs.B; ++n)	
				{
					if (n >= next)
					{
						++digits;
						next = getPower(digits);
					}
					//////////////////////////////////////////////////
					hash_map <int, int> hm;
					for (int m = 1; m < digits; ++m)
					{
						int base = getPower(m);
						int x = n - (n / base) * base;
						if (x < getPower(m - 1)) continue;						
						int y = n / base;
						int f = x * getPower(digits - m) + y;
						if ((f > n) && (f <= cs.B))
						{
							if (hm[f] == 0)
							{
								++cs.m_Count;
								hm[f] = 1;
							}
						}
					}
				}
			}
			void solveCases()
			{
				m_Powers.resize(10, 0);
				for (int i = 0; i < m_Cases.size(); ++i)
					solveCase(m_Cases[i]);
			}
		public:
			void solve()
			{
				readInput();
				solveCases();
				saveOutput();
			}
	};
}