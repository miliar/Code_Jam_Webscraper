#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;

#ifndef ONLINE_JUDGE
#include<fstream>
  ifstream in("A-large.in.txt");
  ofstream out("a.out");
#define cin in
#define cout out
#endif

int main()
{
	int cs;
	cin>>cs;
	for(int ct = 1; ct <= cs; ct ++)
	{
		cout << "Case #"<<ct<<": ";
		int p, k, L;

		cin >> p >> k >> L;
		int a[1024];

		for(int i = 0; i < L; i ++)
			cin >> a[i];

		sort(a, a + L);
		reverse(a, a + L);
		
		long long ans = 0;
		for(int i = 0; i < L;  i++)
		{
			ans += (i / k + 1 ) * (long long)a[i];
		}
		cout << ans << endl;


	}
}
