#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

bool conf[30];
unsigned long long cnt;

void generate(int pos, int n)
{
	if(pos == n)
	{
		int c = 1+count(conf+2, conf+n, true);
		while(conf[c])
		{
			c = 1+count(conf+2, conf+c, true);
		}

		if(c == 1) 
		{
			++cnt;
			cnt = cnt % 100003;
		}
	}
	else
	{
		conf[pos] = true;
		generate(pos+1, n);
		conf[pos] = false;
		generate(pos+1, n);
	}
}

int main()
{
	int T;
	cin>>T;

	//conf[1] = true;
	for(int i = 0; i < T; ++i)
	{
		int n;
		cin>>n;

		generate(2, n);
		
		cout<<"Case #"<<i+1<<": "<<cnt%100003<<endl;

		cnt = 0;
		memset(conf, 0, 30*sizeof(bool));
	}
}