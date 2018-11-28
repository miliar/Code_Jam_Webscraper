#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

struct T 
{
	int a;
	int b;
};

const bool peresek(const T &p1, const T &p2)
{
	return 
		(p1.a>p2.a && p1.b<p2.b) ||
		(p1.a<p2.a && p1.b>p2.b);
}

int main()
{
	int i, j, k, t, n;
	int res;
	vector<T> data;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >>t;
	for(k=1; k<=t; ++k)
	{
		res= 0;
		cin >>n;
		data.resize(n);
		for(i=0; i<n; ++i)
			cin >>data[i].a >>data[i].b;
		for(i=0; i<n; ++i)
			for(j=i+1; j<n; ++j)
				if (peresek(data[i], data[j]))
					res++;
		cout <<"Case #" <<k <<": " <<res <<endl;
	}
	return 0;
}