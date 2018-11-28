#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <list>
#include <iomanip>
#include <queue>
using namespace std;const int mx = 20000;int n, w, l;int r[mx];int id[mx], idd[mx];double x[mx], y[mx];queue<int> q;int cmp2 (int a, int b){	return id[a] < id[b];}int cmp (int a, int b){	return r[a] > r[b];}int check (int tt, double tx, double ty){	for (int i = 0; i < tt; i++)		if ( (sqrt((tx-x[id[i]])*(tx-x[id[i]]) + (ty-y[id[i]])*(ty-y[id[i]])))< r[id[tt]] + r[id[i]])			return 0;	return 1;}void outt(){	sort(idd, idd+n, cmp2);	for (int i = 0; i < n; i++)	{		printf(" %.3lf %.3lf", x[id[idd[i]]], y[id[idd[i]]]);	}}int main (){	//freopen("D:\\Visual Studio 2008\\Google Code Jam\\B-small-attempt0.in", "r", stdin ) ;

	//freopen("D:\\Visual Studio 2008\\Google Code Jam\\B-small-attempt0.out", "w", stdout ) ;	int T;	cin >> T;	for(int k = 1; k <= T; k++)	{		cin>>n>>w>>l;		for (int i = 0; i < n; i++)			{			scanf("%d", r+i), id[i] = i, idd[i] = i, x[i] = -1, y[i] = -1;		}		sort(id, id + n, cmp);		while (!q.empty())				q.pop();		int i = 0, pre = 0;			q.push(pre);		double x0 = 0, p = 0;		x[id[i]] = y[id[i]] = 0;		i++;		while (i < n)		{			p = p + r[id[i-1]] + r[id[i]];			if (p <=l)				{				x[id[i]] = x0;	y[id[i]] = p;				i++;			}			else				break;		}		while (true)		{			if (i >= n)				break;			x0 = x0 + r[id[pre]] + r[id[i]];				pre = i;				q.push(pre);			if (x0 > w)						break;			x[id[i]] = x0;			y[id[i]] = 0;			i++;			while (i < n)			{				double p = y[id[i-1]] + r[id[i-1]] + r[id[i]];				if (p <= l)				{					x[id[i]] = x0;						y[id[i]] = p;					i++;				}									elsebreak;			}		}		printf("Case #%d:", k);		outt();		cout<<endl;	}		return 0;}