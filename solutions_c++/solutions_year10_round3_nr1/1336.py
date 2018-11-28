#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<set>
#include<queue>
#include<string>
#include<cmath>
#include<algorithm>
#include<stdio.h>
using namespace std;

struct TA
{
	int x;
	bool right;
	int idx;
	TA (int x_, int right_, int idx_)
	{
		x=x_;
		right=right_;
		idx=idx_;
	}
	bool friend operator < (TA &a, TA &b)
	{
		if (a.x<b.x)
			return true;
		return false;
	}
};

int search(vector<TA> a,vector<TA>::iterator b)
{
	int count=0;
	vector<TA>::iterator tmp=b;
	tmp++;
	while (tmp->idx!=b->idx)
	{
		if (!tmp->right)
			count++;
		tmp++;
	}
	return count;
}

int is(int l[1000], int r[1000], int i, int j)
{
	if (l[i]<l[j] && r[i]>r[j])
		return 1;
	if (l[i]>l[j] && r[i]<r[j])
		return 1;
	return 0;
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int test,N_TESTS;
	in >> N_TESTS;

	for (test=0;test<N_TESTS;test++)
	{
		int N;
		in >> N;
		vector<TA> a,b;
		int l[1000],r[1000];
		for (int i=0;i<N;i++)
		{
			int l1,r1;
			in >> l1 >> r1;
			l[i]=l1;
			r[i]=r1;
		}
		//sort(a.begin(),a.end());
		/*int res=0;
		for (vector<TA>::iterator i=a.begin();i!=a.end();i++)
			if (!(*i).right)
				res+=search(a,i);*/
		int res=0;
		for (int i=0;i<N;i++)
			for (int j=0;j<N;j++)
				if (i!=j)
					res+=is(l,r,i,j);
		out << "Case #" << test+1 << ": " << res/2 << endl;
	}

	return 0;
}