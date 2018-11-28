#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 1005;

int a[nmax],mas[nmax],b[nmax],c[nmax];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){

		memset(mas,0,sizeof(mas));

		int n;
		cin >> n;
		for (int i = 1;i <= n; ++i) cin >> b[i];
		for (int i = 1;i <= n; ++i) c[i] = b[i];

		sort(b+1,b+n+1);

		for (int i = 1;i <= n; ++i)
		{
			for (int j = 1;j <= n; ++j)
				if (c[i] == b[j])
				{
					a[i] = j;
					break;
				}
		}

		double sum = 0;

		for (int i = 1;i <= n; ++i)
		if (mas[i] == 0)
		{
			int len = 1;
			int pos = a[i];
			mas[i] = 1;
			while (mas[pos] != 1)
			{
				mas[pos] = 1;
				pos = a[pos];
				++len;
			}

			if (len > 1)sum += (double) len;
		}
		
		printf("Case #%i: %.6lf\n",test,sum);		
	}
	
	return 0;
}