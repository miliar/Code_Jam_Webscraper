/*
 * R2A.cpp
 *
 *  Created on: Sep 26, 2009
 *      Author: A.M.Sadek
 */

#include <iostream>
using namespace std;

#define MAX 45

int b[MAX];

int main() {
//	freopen("r2a.in","rt",stdin);
	//freopen("A-small-attempt1.in","rt",stdin);
	//freopen("A-small-attempt1.out","wt",stdout);
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);

	int tt;
	cin >> tt;
	for ( int t = 1 ; t <= tt ; t++)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			string s;
			cin >> s;
			int j;
			for (j = s.size() -1 ; j >= 0 ; j -- )
				if ( s[j] == '1')
					break;
			b[i] = j;
		}
/*
		cout << "====\n";
		for ( int i = 0 ; i < n ; i ++ )
			cout << b [i] << endl;
		cout << "====\n";
*/

		int i, j;

		int swaps = 0;
		for (i = 0; i < n; i++)
		{

			for ( j = i ; j < n ; j ++ )
				if ( b[j] <= i)
					break;

			swaps += j-i;
			for (int k = j; k > i ; k-- )
			{
				{
					int temp = b[k];
					b[k] = b[k-1];
					b[k-1] = temp;
					//swaps ++;
				}

			}
		}
		printf("Case #%d: %d\n",t,swaps);
	}
	return 0;
}
