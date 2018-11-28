#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <list>
#include <set>
#include <map>

using namespace std;

const int MAX_INT = 2147483647;
const int MAX_N = 1001;
int tbl[MAX_N][2];

int main(int argc, char* argv[])
{
	int tc;
    scanf("%d\n", &tc);
	for(int testnum=1; testnum<=tc; testnum++){
	    int i,j,k;
        int n;
		scanf("%d\n", &n);

		for(i=0; i<n; i++){
			scanf("%d%d\n", &tbl[i][0], &tbl[i][1]);
		}

		int ans = 0;
		for(i=0; i<n; i++){
			for(j=i+1; j<n; j++){
				if((tbl[i][0] > tbl[j][0] && tbl[i][1] < tbl[j][1]) || 
					(tbl[i][0] < tbl[j][0] && tbl[i][1] > tbl[j][1])){
						ans++;
				}				
			}
		}

		cout << "Case #" << testnum << ": " << ans << endl;
    }
    return 0;
}

