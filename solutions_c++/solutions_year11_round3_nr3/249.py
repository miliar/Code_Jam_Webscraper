#include <iostream>
#include <stdio.h>
#include <fstream>
#include <algorithm>
#include <math.h>
using namespace std;

int gcd(int a, int b)
{
	if (b==0) return a;
	return gcd(b, a%b);
}

int nod(int a, int b)
{
	return a*b/gcd(a,b);
}

int main()
{
	int T,N,L,H;
	int A[101];

	int i,j,k;
	cin>>T;
	int opt;
	for (i=1;i<=T;i++)
	{
		cin >> N >> L >> H;
		for (j=0;j<N;j++) cin >> A[j];
		
		for (j=L;j<=H;j++)
		{
			opt = true;
			for (k=0;k<N;k++)
			{
				if (A[k]>j)
				{
					if (A[k]%j!=0) {
						opt = false;
						break;}
				}
				else
				{
					if (j%A[k]!=0) 
						{
						opt = false;
						break;}
				}
			}
			if (opt) break;
		}

		cout << "Case #" <<i<< ": ";
		if (opt) cout << j << endl;
		else cout << "NO" << endl;
	}
	return 0;
}