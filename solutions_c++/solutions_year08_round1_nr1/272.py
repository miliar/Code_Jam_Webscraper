#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
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

int main()
{
	ifstream fin ("input.in");
	ofstream fout ("output.out");
	int n,c,temp,ans = 0;
	vector <int> v1;
	vector <int> v2;
	fin >> n;
	for (int i = 0; i < n; i ++)
	{
		v1.clear();
		v2.clear();
		ans = 0;
		fin >> c;
		for (int j =0; j < c; j ++)
		{
			fin >> temp;
			v1.push_back(temp);
		}
		for (int k =0; k < c; k ++)
		{
			fin >> temp;
			v2.push_back(temp);
		}
		sort (v1.begin(),v1.end());
		for (int l = 0; l < c; l++)
		{
			ans = ans + v1[l]*v2[l];
		}

		while (next_permutation(v1.begin(),v1.end()))
		{
			temp = 0;
			for (int m = 0; m < c; m++)
			{
				temp = temp + v1[m]*v2[m];
			}
			ans = MIN(ans,temp);
		}
		fout << "Case #" << i + 1 << ": " <<ans << endl;

	}
	return 0;
}