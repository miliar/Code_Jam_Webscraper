
//#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <string.h>
#include <algorithm>
#include <stack>
#include <map>
#include <list>
#include <cmath>
#include <math.h>
#include <stdlib.h>
#include <vector>
using namespace std;

ifstream cin("E:\\Heyi\\pd\\GoogleJam\\Qualification2010.5.7\\Qualification\\C-large.in");
ofstream cout("E:\\Heyi\\pd\\GoogleJam\\Qualification2010.5.7\\Qualification\\C-large.out");
#define POUT(n,v){cout<<"Case #"<<(n+1)<<": "<<v<<endl;} 

#define MAX_NUM 1000
int v[MAX_NUM];
int sortV(const void* a,const void* b)
{
	return *(int*)a-*(int*)b;
}
int main()
{
	
	int T;
	cin>>T;
	for (int i=0;i<T;i++)
	{
		int N;
		cin>>N;
		memset(v,0,MAX_NUM);
		long l=0;
		long vv=0;
		for (int j=0;j<N;j++)
		{
			cin>>v[j];
			vv+=v[j];
			l^=v[j];
		}
		if (l!=0)
		{
			cout<<"Case #"<<(i+1)<<": NO"<<endl;
		}
		else
		{
			qsort(v,N,sizeof(int),sortV);
			cout<<"Case #"<<(i+1)<<": "<<(vv-v[0])<<endl;
		}


	}
	return 0;
}
