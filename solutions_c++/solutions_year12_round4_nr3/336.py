/*
 * BingIt.cpp
 *
 *  Created on: May 20, 2012
 *      Author: carlosjosetoribio
 */

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>

using namespace std;

int X[2010];
int H[2010];
int sum = 0;
int check(int N,int &inc)
{
	for(int i = 0; i < N; ++i)
	{
		for(int j = i+1; j < N; ++j)
		{
			if(j==X[i])continue;
			if(j < X[i] && (H[j]-H[i])*(X[i]-i) >= (H[X[i]]-H[i])*(j-i) )
			{
				inc = H[X[i]];
				while((H[j]-H[i])*(X[i]-i) >= (inc-H[i])*(j-i))
				{
					inc++;
					sum++;
					if(sum > 4000000)break;
				}
				
				return X[i];
			}
			if(j > X[i] && (H[j]-H[i])*(X[i]-i) > (H[X[i]]-H[i])*(j-i))
			{
				inc = H[X[i]];
				while((H[j]-H[i])*(X[i]-i) > (inc-H[i])*(j-i))
				{
					inc++;
					sum++;
					if(sum > 4000000)break;
				}
				return X[i];
			}
		}
	}
	return -1;
}

void gen(int N)
{
	
	freopen("in.txt","w",stdout);
	cout << 1 << endl;
	cout << N << endl;
	int arr[2010];
	for(int i = 0; i < N; ++i)
	{
		int sz = rand()%1000;
		arr[i] = sz;
	}
	for(int i = 0; i < N-1; ++i)
	{
		int ma = i+1;
		for(int j = i+2; j < N; ++j)
		{
			if(  (arr[j]-arr[i])*(ma-i) > (arr[ma]-arr[i])*(j-i) )
				ma = j;
		}
		cout << ma+1 << " ";
	}
	cout << endl;
	for(int i = 0; i < N; ++i)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{
	cin.sync_with_stdio(false);

//	gen(10);return 0;
	freopen("/Users/carlosjosetoribio/Desktop/C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC; ++tc)
	{
		sum = 0;
		bool ok = true;
		int N;
		cin >> N;
		for(int i = 0; i < N-1; ++i)
		{
			cin >> X[i];
			X[i]--;
			if(X[i] <= i)ok = false;
		}
		cout << "Case #" << tc << ": ";
		if(!ok){cout << "Impossible" << endl;continue;}
		memset(H,0,sizeof(H));
		int t, cnt = 0;
		int inc;
		while(cnt < 1000 && (t=check(N,inc)) != -1)
		{
			H[t] = inc;
			cnt++;
		}
//		cout << cnt << endl;
		if(check(N,inc)==-1 && sum < 4000000)
		{
			for(int i = 0; i < N; ++i)
			{
				cout << H[i];
				if(i==N-1)cout<<endl;
				else cout << " ";
			}
		}
		else
			cout << "Impossible" << endl;
	}

	return 0;
}


