#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

ifstream inf;
ofstream outf;
	
int n;
int a[2000];
int p[2000], used[2000];

double fact;
double randomanw[10000];
void help(int n )
{
	int cnt = 0;
	vector <int> pm(0);
	for (int i = 0; i <n; i++)
		pm.push_back(i);
	double sum = 0;
	int self = 0;
	do 
	{
		int cycle1 = 0, cycle2 = 0;
		for (int i = 0; i < n; i++) 
			if (pm[i] == i) cycle1++;
			else 
			if (pm[pm[i]] == i) cycle2++;		
		cycle2 /=2;
		cycle2 = 0;
		
		if (cycle1 + cycle2 == 0) 		
			self++;
		else
		{
			sum += cycle2 * 2.0 + 1 + randomanw[n - cycle1 - cycle2];
			if (cycle1  + cycle2*2 == n)
				sum -=1;
		}
		cnt++;
	}
	while (next_permutation(pm.begin(), pm.end()));
	double fcnt = double(cnt);//fact	
	randomanw[n] = (sum + self) / ((fcnt-self));


}
int main(void){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	randomanw[0] = 0.0;
	randomanw[1] = 0.0;
	randomanw[2] = 1.0;
	for(int i = 3; i <= 8; i++)
	{
		help(i);
		//outf << randomanw[i] << endl;
	}
	//return 0;
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++)
	{		

		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			a[i]--;
		}
		
		int cycle1 = 0, cycle2 = 0;
		for (int i = 0; i < n; i++) 
			if (a[i] == i) cycle1++;
			else 
			if (a[a[i]] == i) cycle2++;		
		
		cycle2 /=2;
		cycle2 = 0;
		double sum = 0;
		/*
		int self = 0;
		if (cycle1 + cycle2 == 0) 		
			self++;
		else
			sum += cycle2 * 2.0 + randomanw[n - cycle1 - cycle2];
		if (self)
			sum = randomanw[n];
		*/
		sum = n - cycle1;
		printf("Case #%d: %.9lf\n", test+1, sum);
			
		

	}

	outf.close();
	return 0;
}
