// cj1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

struct node
{
	int ind;
	unsigned long long int wt;
};
unsigned long long int cal (struct node x[101],struct node y[101], int i, int j,unsigned long long int wi,unsigned long long int wj)
{
	unsigned  long long int max = 0;
	if(i == 0 || j == 0) return 0;
	if(x[i].ind == y[j].ind)
	{
		if(wi==wj)
		{
			max = wi +  cal (x, y, i-1, j-1, x[i-1].wt, y[j-1].wt);
		}
		else
		{
			if(wi > wj)
			{
				max = wj + cal (x, y, i, j-1, wi-wj, y[j-1].wt);
			}
			else
			{
				max = wi + cal (x, y, i-1, j, x[i-1].wt, wj-wi);
			}
		}
	}
	else
	{
		unsigned  long long int max1 = cal (x, y, i, j-1, wi, y[j-1].wt);
		unsigned long long int max2 = cal (x, y, i-1, j, x[i-1].wt, wj);
		max = (max1 > max2 ? max1 : max2);
	}
	return max;
}
int main()
{
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("C-small-attempt2.out", "w",stdout); 
    int T,n,m;
		struct node x[101],y[101];
		x[0].ind=y[0].ind = 0;
		x[0].wt=y[0].wt = -1;
		cin >> T;
		for(int tc=1;tc<=T;tc++) 
        { 
			cin >> n >>m;
			for(int i =1; i <=n;++i)
			{
				cin >> x[i].wt;
				cin >> x[i].ind;
			}
			for(int i =1; i <=m;++i)
			{
				cin >> y[i].wt;
				cin >> y[i].ind;
			}	
			
			cout << "Case #"<<tc<<": "<< cal(x, y, n, m, x[n].wt, y[m].wt) <<endl;
			
        } 
	fclose(stdin);
	fclose(stdout);
	return 0;
}

