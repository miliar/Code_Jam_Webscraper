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
	const string dataFolderB = "C:\\Programming\\!Private\\ProblemSolver\\!Data\\Google Jam\\";
	class GoogleDancing
	{
			struct Case
			{
				int N, S, p, y;
				vector <int> m_Scores;
			};
			vector <Case> m_Cases;
			//////////////////////////////////////////////////////
			void readInput()
			{
				string path = dataFolderB + "GoogleDancing\\B-large.in";
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
					Case& cs = m_Cases[t];
					ist >> cs.N >> cs.S >> cs.p;
					cs.m_Scores.resize(cs.N);
					for (int i = 0; i < cs.N; ++i)
						ist >> cs.m_Scores[i];
				}
				is.close();
			}
			void saveOutput()
			{
				string path = dataFolderB + "GoogleDancing\\res.out";
				ofstream os;
				os.open(path.c_str());
				if (!os.is_open()) throw 1;
				///////////////////////////////////////////////
				for (int i = 0; i < m_Cases.size(); ++i)
				{
					os << "Case #" << i + 1 << ": " << m_Cases[i].y << endl;					
				}
				///////////////////////////////////////////////
				os.close();
			}
			void solveCase(Case& cs)
			{
				cs.y = 0;
				int lb, ub, sum;
				for (int i = 0; i < cs.N; ++i)
				{		
					sum = cs.m_Scores[i];
					if (sum == 0)
					{
						lb = ub = 0;
					}
					else if (sum == 1)
					{
						lb = ub = 1;
					}
					else
					{					
						lb = (sum + 2) / 3;
						ub = (sum + 4) / 3;
					}
					if (lb >= cs.p)
					{
						++cs.y;
					}
					else if ((cs.S > 0) && (ub >= cs.p))
					{
						++cs.y;
						--cs.S;
					}
				}
			}
			void solveCases()
			{
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