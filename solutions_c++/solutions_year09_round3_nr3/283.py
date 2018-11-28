#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std ;

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out.txt", "w", stdout);
	int T;
	int kase;
	int ans;
	int P, Q;
	
	cin >> T;
	for(kase = 1; kase <= T; kase ++)
	{
		vector<int> cell;
		int flag[105];
		cin >> P >> Q;
		int i, j, k;
		for(i = 0; i < Q; i ++)
		{
			cin >> j;
			cell.push_back(j);	
		}

		ans = -1;
		do
		{
			memset(flag, 0, sizeof(flag));
			flag[0] = -1;
			flag[P+1] = -1;
			
//			cout << "q" << endl;
			
			int cnt = 0;
			for(i = 0; i < Q; i ++)
			{
				flag[cell[i]] = -1;
				for(j = cell[i] - 1; j > 0; j --)
				{
					if(flag[j] == 0)
						cnt ++;
					else	break;	
				}	
				for(j = cell[i] + 1; j <= P; j ++)
				{
					if(flag[j] == 0)
						cnt ++;
					else break;	
				}
			}
			if(ans == -1)	ans = cnt;
			else
			{
				ans = ans < cnt ? ans : cnt;	
			}
			
		}while(next_permutation(cell.begin(), cell.end()));
	
		cout << "Case #" << kase << ": " << ans << endl;
	}
    return 0;
}


/*
Input 
   

   
2
8 1
3
20 3
3 6 14

Output 
Case #1: 7
Case #2: 35
 


*/
