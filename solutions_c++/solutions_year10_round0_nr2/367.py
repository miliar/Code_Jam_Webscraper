/*
 * B.cpp
 *
 *  Created on: 2010-5-8
 *      Author: LK_TMP
 */

#include<iostream>
#include<cstdio>
using namespace std;
int a[1008],n;

int gcd(int a,int b)
{
	if (b==0) return a; else return (gcd(b,a%b));
}

int abs(int a)
{
	if (a>=0) return a; else return -a;
}

int main()
{
	int t;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	cin>>t;
	for (int test=1;test<=t;test++)
	{
		cin>>n;
		for (int i=0;i<n;i++) cin>>a[i];
		int q=abs(a[1]-a[0]);
		for (int i=2; i<n;i++)
			q = gcd(q, abs(a[i] - a[i - 1]));
		cout << "Case #"<<test<< ": "<< (q - a[0] % q) % q << endl;
	}
	fclose(stdin);  fclose(stdout);
	return 0;
}
