#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <cmath>
#define NOTFOUND 4294967295
#define PI 3.1415926535897932384626433832795

using namespace std;

struct wire
{
	int a;
	int b;
	
	bool operator <(const wire &w)
	{
		return a<w.a;
	}
};

int main()
{
	ifstream fi("data.in");
	ofstream fo("data.out");

	int T,N;
	fi>>T;

	vector<wire> vec;

	for(int t=1; t<=T; t++)
	{
		fo<<"Case #"<<t<<": ";
		fi>>N;
		vec.clear();
		for(int i=0;i<N;i++)
		{
			wire neww;
			fi>>neww.a>>neww.b;
			vec.push_back(neww);
		}
		sort(vec.begin(),vec.end());

		int intsection=0;
		for(int i=0;i<N-1; i++)
		{
			for(int j=i+1; j<N; j++)
			{
				if(vec[j].b<vec[i].b)
					intsection++;
			}
		}
		fo<<intsection<<endl;
	}
}

			

