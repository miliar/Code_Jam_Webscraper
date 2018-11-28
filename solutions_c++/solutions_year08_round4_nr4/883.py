#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
#include<cstdio>
#include<cmath>
#include<fstream>
using namespace std;
#define pi 3.141592653589793

#define ABS(x) ((x)>0?(x):-(x))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define DIST(x,y) ABS((x)-(y))
int gcd(int x,int y){if(y==0)return x;else return(gcd(y,x%y));}

int getlen(string S, vector<int> v)
{
	int n = v.size();
	int len = S.length();
	string ans = S;
	for (int i = 0; i < len/n; i ++)
	{
		for (int j = 0; j < n; j ++)
		{
			ans[i*n + j] = S[i*n + v[j]]; 
		}
	}
	char prev,next;
	int ret = 1;
	for (int k =1; k < len; k++)
	{
		prev = ans[k-1];
		next = ans[k];
		if (next != prev)
			ret++;
	}
	return ret;
}
int main()
{
	int N;
	ifstream fin ("input.in");
	ofstream fout ("output.out");
	fin >> N;
	int k,len;
	vector <int> v;
	string S;
	int ans = 999999999;
	for (int i = 0; i < N; i ++)
	{
		v.clear();
		fin >> k;
		fin >> S;
		len = S.length();
		for (int j = 0; j < k; j++)
			v.push_back(j);
		ans = getlen(S,v);
		while ( next_permutation(v.begin(), v.end()) )
		{
			ans = MIN(ans,getlen(S,v));
		}
		fout << "Case #" << i + 1 << ": " <<ans <<endl;
	}
	
	return 0;	
}
