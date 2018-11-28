#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <iostream>
#include <cstdlib>
#include <list>
#include <vector>
#include <sstream>
using namespace std;
bool cmp(long long int a, long long int b)
{
	return a > b ; 
}
int main()
{
	int tn, n;
	long long int a[1000],b[1000];
	scanf("%d",&tn);
	int casen=1;
	while (tn--)
	{
		long long int ba=0;
		cin >> n ;
		for ( int i = 0 ; i< n;i++)
			cin >> a[i] ;
		for ( int i = 0 ; i< n;i++)
			cin >> b[i];
		sort(a,a+n);
		sort(b,b+n,cmp);
	//	for ( int i = 0 ; i< n;i++) cout << a[i] << endl;
	//	for ( int i = 0 ; i< n;i++) cout << b[i] << endl;
	//	cout << "ba" << endl;
		ba= 0 ; 
		for( int i= 0 ; i< n;i++)
		{
			ba+=(a[i]*b[i]);
	//		cout << ba << endl;
		}
		printf("Case #%d: ",casen++);
		cout << ba << endl; 
	}
	return 0 ;
	// biginteger  ;
}
