// Paste me into the FileEdit configuration dialog

#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <iostream>
#include <cmath>
#include <ctime>
#include <queue>

using namespace std;

const int MAX = 100;

char a[MAX][MAX];

int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_case_count;
	cin >> test_case_count;
	for (int test_case = 1; test_case<=test_case_count; ++test_case)
	{		 
		int r, c, d;		
		cin >> r >> c >> d;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)	
				cin >> a[i][j];
		int ans = -1;
		for (int size = min(r, c); size >= 3; --size)
		{
			
			for (int i = 0; i < r-size+1 && ans < 0 ; ++i)
				for (int j = 0; j < c-size+1 && ans < 0; ++j)
				{
					double sumx = 0, sumy = 0;			  
					double ccx = (i + (i + size))/2.0;
					double ccy = (j + (j + size))/2.0;
					for (int i1 = i; i1 < i+size; ++i1)
						for (int j1 = j; j1 < j+size; ++j1) 
						if (i1==i && j1 ==j || i1==i+size-1 && j1 ==j || i1==i+size-1 && j1 ==j+size-1 ||  i1==i && j1 ==j+size-1)
						{}
						else{
							sumx += a[i1][j1] * (i1 + 0.5 - ccx);
							sumy += a[i1][j1] * (j1 + 0.5 - ccy);
						}
					if (fabs(sumx) < 1e-10 && fabs(sumy) < 1e-10)
					{
						ans = size;	
					}
				}	
			if (ans > 0)
				break;

		}

		cout << "Case #" << test_case << ": ";
		if  (ans > 0)
			 cout << ans;
		else
			cout << "IMPOSSIBLE";
		cout << endl;

	}
	fclose(stdout);
}

