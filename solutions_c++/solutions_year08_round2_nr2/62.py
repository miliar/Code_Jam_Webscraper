#include <assert.h>
#include <iostream>
#include <ios>
#include <tr1/unordered_map>
#include <vector>
#include <fstream>
using namespace std;
using namespace std::tr1;

//ifstream in("B.ex");
istream& in = cin;
ostream& out = cout;

bool composites[1024 * 1024];

int color[1024 * 1024];
vector<int> lists[1024 * 1024];

void join(int i, int j)
{
	if(color[i] == color[j])
		return;

	if(lists[color[i]].size() > lists[color[j]].size())
		swap(i, j);
		
	lists[color[j]].insert(lists[color[j]].end(), lists[color[i]].begin(), lists[color[i]].end());
	
	int ci = color[i];
	int cj = color[j];
	for(int k = 0; k < lists[ci].size(); ++k)
		color[lists[ci][k]] = cj;
	lists[ci].clear();
	
	color[i] = cj;
}

int main(int argc, char** argv)
{
	for(int i = 2; i < 1024; ++i)
	{
		if(composites[i])
			continue;

		for(int j = i * i; j < 1024 * 1024; j += i)
		{
			composites[j] = true;
		}
	}
	
	int N;
	in >> N;
	for(int cas = 0; cas < N; ++cas)
	{
		long long A, B, P;
		
		in >> A >> B >> P;
		
		int l = B - A;
		
		for(int i = 0; i <= l; ++i)
		{
			lists[i].clear();
			lists[i].push_back(i);
			color[i] = i;
		}

		for(int i = 0; i <= l; ++i)
		{
			for(int j = i + 1; j <= l; ++j)
			{
				int d = __gcd(A + i, A + j);
				
				for(int k = P; k <= d; ++k)
				{
					if(!composites[k] && (d % k) == 0)
					{
						join(i, j);
					}
				}
			}
		}
		
		int colors = 0;
		for(int i = 0; i <= l; ++i)
		{
			if(lists[i].size())
				++colors;
		}
		
		cout << "Case #" << (cas + 1) << ": " << colors << endl;
	}
}

