#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;


int main()
{
	
	int T,N,M;
	string tmp;
	int needed;
	cin >> T;
	vector< vector<string> > inp;
	for(int counter = 0; counter< T; counter++)
	{
		inp.clear();
		int tot=0;
		cin >> N >> M;
		for(int i=0; i<N; i++)
		{
			vector<string> push;
			cin >> tmp;
			string tmp2;
			int start=1;
			while(start<tmp.size())
			{
				tmp2="";
				for(int j= start; j<tmp.size(); j++)
				{
					if(tmp[j] == '/')
					{
						start = j+1;
						break;
					}
					start = j+1;
					tmp2+=tmp[j];
					
				}
				
				push.push_back(tmp2);
			}
			inp.push_back(push);
			push.clear();
			
		}
		for(int i=0; i<M; i++)
		{
			vector<string> push2;
			cin >> tmp;
			int start = 1;
			string tmp2;
			while(start<tmp.size())
			{
				tmp2="";
				for(int j= start; j<tmp.size(); j++)
				{
					if(tmp[j] == '/')
					{
						start = j+1;
						break;
					}
					
					tmp2+=tmp[j];
					start = j+1;
					
				}
				push2.push_back(tmp2);
			}	
			
			int minste=push2.size();
			for(int k=0; k<inp.size(); k++)
			{
				
				int m=0;
				while(m<push2.size() && m<inp[k].size() && inp[k][m] == push2[m])
				{
					m++;
				}
				
				int sums = push2.size() - m;
				
				minste = min(minste, sums);
			}
			if(inp.size() == 0)
				tot += push2.size();
			else {
				tot+=minste;
				
			}

			
			
			inp.push_back(push2);
			push2.clear();
		}
		
		
			
		cout << "Case #" << counter+1 << ": " << tot << endl;
	}
}
		
		
		
		
		
		
		