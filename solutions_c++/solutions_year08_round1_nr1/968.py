#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <stack>
#include <fstream>
#include <math.h>
#include <map>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

#define FOR0(i,b)	for(int i=0,_b=(int)(b);i<_b;i++)
#define FOR1(i,b)	for(int i=1,_b=(int)(b);i<=_b;i++)
#define LOG(s,ss)	cout<<s<<""<<ss<<endl;
#define Rep(e,c,Ty) vector<Ty*>::iterator e;for(e=(c).begin();e!=(c).end();e++)
#define MINVALUE(a,b) ((a)=((a)>(b))?(b):(a))

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

char buf[1024*1024];
int a[1000];
int b[1000];

__int64 scalar(int *a, int *b, int n)
{
	double value = 0.0;
	FOR0(i,n) value+=((double)a[i])*((double)b[i]);
	return (__int64)value;
}

void main()
{
	//freopen("E:\\workspace\\Round1\\debug\\input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
	ifstream input("E:\\workspace\\Round1\\debug\\input.txt");
	int t;
	input >> t;
	FOR1(z,t)
	{
		int n;
		input >> n;
		FOR0(i,n) input>>a[i];//scanf("%d", &a[i]);
		FOR0(j,n) input>>b[j];//scanf("%d", &b[j]);
		sort(a, a+n);
		__int64 minV = scalar(a, b, n);
		while (next_permutation(a,a+n)) minV = MINVALUE(minV, scalar(a,b,n));
		printf("Case #%d: %d\n", z, minV);
	}
	
}


