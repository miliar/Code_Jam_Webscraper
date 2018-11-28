#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

struct S
{
	vector <int> a;
	vector <int> b;
	vector <int> c;
};
int glrs;
int sur;
int Max = 0;
int p;
vector <S> Set (31);

void getmax( vector <int> scores, int googler, int Sur, int M)
{
	if (googler == scores.size() && sur == Sur)
	{
		if (M > Max)
			Max = M;
		return;
	}
	if (Sur > sur || googler == scores.size())
		return;
	else
	{
		for (int i = 0;i < Set[scores[googler]].a.size(); i++)
		{
			if (Set[scores[googler]].c[i] - Set[scores[googler]].a[i] != 2)
			{
				if (Set[scores[googler]].c[i] >= p)
					getmax(scores, googler+1, Sur, M+1);
				else
					getmax(scores, googler+1, Sur, M);
			}
			else
			{
				if (Set[scores[googler]].c[i] >= p)
					getmax(scores, googler+1, Sur+1, M+1);
				else
					getmax(scores, googler+1, Sur+1, M);
			}
		}
	}
}

int main()
{
	ifstream fin ("in.txt");
	ofstream fout ("out.txt");
	for (int i = 0; i <= 30; i ++)
	{
		for (int j = 0; j <= i; j++)
		{
			for (int k = j; k <= j+2; k++)
			{
				for (int l = j; l <= j+2 && l <= k+2; l++)
				{
					if (j + k + l != i) continue;
					if (l < k || l < j || k < j) continue;
					Set[i].a.push_back(j);
					Set[i].b.push_back(k);
					Set[i].c.push_back(l);
				}
			}
		}
	}
	int n;
	fin>>n;
	for (int i = 1; i <= n; i ++)
	{
		fin>>glrs>>sur>>p;
		vector <int> scores(glrs);
		for (int i = 0 ; i < glrs; i++)
			fin>>scores[i];
		getmax(scores, 0, 0, 0);
		fout<<"Case #"<<i<<": "<<Max<<endl;
		Max = 0;
	}
	return 0;
}