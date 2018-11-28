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
	class SpeakingTongues
	{
			struct Case
			{
				string m_Input;
				string m_Output;
			};
			vector <Case> m_Cases;
			hash_map <char, char> m_Map;
			vector <bool> m_InFlags;
			vector <bool> m_OutFlags;
			vector <string> m_Input;
			vector <string> m_Output;
			///////////////////////////////////////
			void readInput()
			{
				string path = dataFolder + "SpeakingTongues\\A-small.in";
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
					m_Cases[t].m_Input = line;
				}
				is.close();
			}
			void solveCase(Case& cs)
			{
				cs.m_Output.resize(cs.m_Input.size());
				for (int i = 0; i < cs.m_Input.size(); ++i)
				{
					if (m_Map.find(cs.m_Input[i]) == m_Map.end())
					{
						cout << "No letter: " << cs.m_Input[i] << endl;
						throw 1;
					}
					cs.m_Output[i] = m_Map[cs.m_Input[i]];
				}
			}
			void solveCases()
			{
				for (int t = 0; t < m_Cases.size(); ++t)
				{
					solveCase(m_Cases[t]);
				}
			}
			void saveOutput()
			{
				string path = dataFolder + "SpeakingTongues\\res.out";
				ofstream os;
				os.open(path.c_str());
				if (!os.is_open()) throw 1;
				///////////////////////////////////////////////
				for (int i = 0; i < m_Cases.size(); ++i)
				{
					os << "Case #" << i + 1 << ": " << m_Cases[i].m_Output << endl;					
				}
				///////////////////////////////////////////////
				os.close();
			}
			void addMapping(const string& s_in, const string& s_out)
			{
				if (s_in.length() != s_out.length()) throw 1;
				for (int i = 0; i < s_in.size(); ++i)
				{					
					m_Map[s_in[i]] = s_out[i];
					if (s_in[i] != ' ')
					{
						m_InFlags[s_in[i] - 'a'] = true;
						m_OutFlags[s_out[i] - 'a'] = true;
					}
				}
			}
			void finalizeMapping()
			{
				cout << "Map size: " << m_Map.size() << endl;
				int i_in = 0;
				int i_out = 0;
				while ((i_in < m_InFlags.size()) && (i_out < m_OutFlags.size()))
				{
					if (!m_InFlags[i_in])
					{
						while (m_OutFlags[i_out]) ++i_out;
						m_Map['a' + i_in] = 'a' + i_out;
						++i_in;
						++i_out;
					}
					else if (!m_OutFlags[i_out])
					{
						while(m_InFlags[i_in]) ++i_in;
						m_Map['a' + i_in] = 'a' + i_out;
						++i_out;
						++i_in;
					}
					else
					{
						++i_in;
						++i_out;
					}
				}
			}
			void initMapping()
			{
				m_InFlags.resize(26, false);
				m_OutFlags.resize(26, false);
				m_Input.resize(4);
				m_Output.resize(4);
				//////////////////////////////////////
				m_Input[0] = "y qee";
				m_Output[0] = "a zoo";								
				m_Input[1] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
				m_Output[1] = "our language is impossible to understand";
				m_Input[2] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
				m_Output[2] = "there are twenty six factorial possibilities";
				m_Input[3] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
				m_Output[3] = "so it is okay if you want to just give up";
				//////////////////////////////////////
				for (int i = 0; i < m_Input.size(); ++i)
					addMapping(m_Input[i], m_Output[i]);
				finalizeMapping();
			}
		public:
			void solve()
			{
				initMapping();
				readInput();
				solveCases();
				saveOutput();
			}
	};
}