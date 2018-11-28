#include<fstream>
#include<iostream>
using namespace std ;
#define fo(i, n) for (i=0 ; i < n ; i++)



int w[20] ;
int main()
{
	ifstream cin("input.in") ;
	ofstream cout("output.out") ;
	int T ;
	int N, z, i, j ;

	cin >> T ;

	fo(z, T)
	{
		cin >> N ;
		

		int TOT = 0 ;
		fo(i, N)
			cin >> w[i], TOT+=w[i];

		int ret = -1 ;

		fo(i, (1<<N)-1)
		{
			int tmp1 = 0, tmp2 = 0, tot=0 ;

			fo(j, N)
			{
				if (i & (1<<j))
				{
					tot+= w[j] ;
					tmp1^=w[j] ;
				}
				else
					tmp2^= w[j] ;
			}

			if (tmp1==tmp2)			
				ret = max(ret, tot) ;
		}

		cout << "Case #" << z+1 << ": " ;
		if (ret==-1)
			cout << "NO" << endl ;
		else
			cout << ret << endl ;
		
	}
}