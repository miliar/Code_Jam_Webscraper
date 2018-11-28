#include<iostream>
#include<stdio.h>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

/*
 * This program reads from stdin and writes to stdout.
 * Run it with
 *     program < input.txt > output.txt
 */

char in[1000][1000];

double owpf(int n , int x , int N)
{
	int total = 0 , win = 0;
	for(int i = 0 ; i < N ; i++)
		if(i != x)
		{
			if(in[n][i] != '.')
				total++;
			if(in[n][i] == '1')
				win++;
		}
	return 1.0 * win / total;
}

double wp[1000] , owp[1000] , oowp[1000];

int main()
{
	int T;
	cin >> T;
	for(int t = 0 ; t < T ; t++)
	{
		cerr << "Test " << t << "\n";
		cout << "Case #" << t + 1 << ":\n";
		int N;
		cin >> N;
		for(int i = 0 ; i < N ; i++)
			cin >> in[i];
		for(int i = 0 ; i < N ; i++)
			wp[i] = owpf(i , -1 , N);
		for(int i = 0 ; i < N ; i++)
		{
			int cnt = 0;
			double total = 0;
			for(int j = 0 ; j < N ; j++)
				if(in[i][j] != '.')
				{
					cnt++;
					total += owpf(j , i , N);
				}
			owp[i] = total / cnt;
		}
		for(int i = 0 ; i < N ; i++)
		{
			int cnt = 0;
			double total = 0;
			for(int j = 0 ; j < N ; j++)
				if(in[i][j] != '.')
				{
					cnt++;
					total += owp[j];
				}
			oowp[i] = total / cnt;
		}
		for(int i = 0 ; i < N ; i++)
		{
			printf("%.10lf\n" , 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
}









