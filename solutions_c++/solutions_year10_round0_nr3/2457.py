
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
template<class T>
ostream& operator<<(ostream& out, const vector<T>& nums)
{
	out<<"[";
	for(vector<T>::const_iterator i=nums.begin(); i!=nums.end(); i++)
		out<<(*i)<<ends;
	out<<"]";
	return out;
}

int cj(const int R, const int k, const int N, int* g)
{
	int sum = 0;
	int cur = 0;
	for (int i=0; i<R; i++)
	{
		int people = 0;
		int group_count = 0;
		for(; group_count<N ;cur=(cur+1)%N)
		{
			people+=g[cur];
			group_count++;
			if (people>k)
			{
				people -= g[cur];
				break;
			}
		}
		sum +=people;
	}
	return sum;
}

const int MAX_N = 1001;
int main()
{
	int T, R, k, N;
	int g[MAX_N];
	cin>>T;
	int count=1;
	int i=0;
	for (; count<=T; count++)
	{
		cin>>R>>k>>N;
		for (i=0; i<N; i++)
			cin>>g[i];
		g[N] = 0;
		cout<<"Case #"<<(count)<<": "<<cj(R, k, N, g)<<endl;
	}
	return 0;
}

