//============================================================================
// Name        : round1C_2.cpp
// Author      : Toqa Osama
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <list>

using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test,N,L,H;
	cin>>test;
	for(int t = 1;t<=test;t++)
	{
		int arr[101];
		cin>>N>>L>>H;
		for(int i = 0;i<N;i++)
		{
			cin>>arr[i];
		}
		bool f1 = false;
		cout<<"Case #"<<t<<": ";
		for(int i = L;i<=H;i++)
		{
			int f  = 0;
			for(int j = 0;j<N;j++)
			{
				if(arr[j]%i==0||i%arr[j]==0){
				f ++;
				}
			}
			if(f == N)
			{
				f1 = true;
				cout<<i<<endl;
				break;
			}
		}
		if(f1==false)
		{
			cout<<"NO\n";
		}
	}
	return 0;
}
