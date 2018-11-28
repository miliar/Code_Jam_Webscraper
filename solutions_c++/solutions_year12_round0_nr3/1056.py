#include <string>
#include <vector>
#include <stdint.h>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <cassert>
#include <cstdio>
#include <list>
#include <cmath>
#include <climits>
#include <stack>

#define ASSERT(statement, obj) { typeof(obj) x=(statement); if(x!=(obj)){std::cout<<x<<std::endl;assert(false);}}
#define FOR(index, from, to) for (typeof(to) index=from; index<(to); ++index)
#define VFOR(index, v) for (typeof(v.size()) index=0; index<(v.size()); ++index)
#define ITER(it, list) for(typeof(list.begin()) it=list.begin(); it!=list.end();++it)
#define PRINT_VECTOR_INT(v) FOR(i, 0, v.size())cout<<v[i]<<" "
#define PBK push_back

using namespace std; 


int main()
{
	string line;
	int T=0;
	getline(cin, line);
	{
		stringstream ss(line);
		ss >> T;
	}

	FOR(i, 0, T)
	{
		int A, B, C = 0;
		{
			getline(cin, line);
			stringstream ss(line);
			ss >> A >> B;
		}
		string BB;
		{
			stringstream ss;
			ss << B;
			BB = ss.str();
		}

		FOR(n, A, B+1)
		{
			stringstream ss;
			ss << n;
			string str = ss.str();
			char* move = new char[str.length()*2+2];
			memset(move, 0, str.length()*2+2);
			strcpy(move, str.c_str());
			char* head = move;
			map<int, int> mp;

			FOR(m, 0, str.length()-1)
			{
				head[str.length()] = *head;
				++head;
				
				if (strcmp(head, str.c_str()) > 0 && strcmp(head, BB.c_str()) <= 0)
				{
					stringstream sss(head);
					int h;
					sss >> h;
					if (mp.find(h) == mp.end())
					{
	  					C++;
						mp[h] = -1;
						//cout<<str<<"  "<<head<<endl;
					}
				}
			}
			delete move;
		}

		printf("Case #%d: %d\n", i+1, C);
		//cout<<"===================\n";
	}
}

