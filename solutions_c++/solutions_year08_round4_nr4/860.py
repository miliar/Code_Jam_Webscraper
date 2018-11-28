#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <map>
#include <set>
#include <cassert>
#include <list>
#include <deque>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <queue>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b)) 
using namespace std;

int get(string S)
{
	int i;
	int ret=1;
	//cout<<S<<endl;
	for(i=1;i<S.size();i++)
	{
		if(S[i]!=S[i-1])
			ret++;
	}
	return ret;
}

int main()
{
	int N;
	int count=1;
	cin>>N;
	while(N--)
	{
		int k;
		string S;
		cin>>k>>S;
		int i;
		int min=999999999;
		vector <int> V(k);
		for(i=0;i<k;i++)
			V[i]=i;
		do
		{
			string temp=S;
			for(i=0;i<S.size();i++)
			{
				temp[i]=S[(i/k)*k+V[i%k]];
			}
			min=MIN(min,get(temp));
		}while(next_permutation(V.begin(),V.end()));
		cout<<"Case #"<<count<<": "<<min<<endl;
		count++;
	}
	return 0;
}




