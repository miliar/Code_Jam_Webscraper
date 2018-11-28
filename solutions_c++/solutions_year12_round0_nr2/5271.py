#include <algorithm>
#include <iostream>
#include <stdio.h>
//#include <string.h>
#include <vector>

using namespace std;

struct M
{
	int total;
	int s1;
	int s2;
	int s3;
	int smax;
	int nequalMax;
};

int main()
{
	int t, n, s, p;
	cin>>t;
	M* arr;
	for(int i = 0; i < t; i++)
	{
		cin>>n>>s>>p;
		arr = new M[n];
		M* w;
		for(int j = 0; j < n; j++)
		{
			w = &arr[j];
			cin>>w->total;
			int temp = w->total /3;
			if(w->total - (3*temp) == 0) {w->s1 = temp;w->s2 = temp;w->s3 = temp;w->smax = temp;w->nequalMax = 3;}
			else if(w->total - (3*temp) == 1) {w->s1 = temp;w->s2 = temp;w->s3 = temp+1;w->smax = temp+1;w->nequalMax = 1;}
			else if(w->total - (3*temp) == 2) {w->s1 = temp;w->s2 = temp+1;w->s3 = temp+1;w->smax = temp+1;w->nequalMax = 2;}
			else cout<<"ERROR";
		}
		int j = 0;
		int num = 0;
		while(j < n)
		{
			w = &arr[j];
			if(w->smax >= p) {num++;j++;}
			else if((w->smax+1) == p && w->nequalMax > 1 && w->smax >0 && s > 0) {num++;j++;s--;}
			else {j++;}
		}
		cout<<"Case #"<<(i+1)<<": "<<num<<"\n";
	}
	return 1;
}
