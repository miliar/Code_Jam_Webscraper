/*
name:ca
By Tony
2011-5-22 обнГ05:00:17
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <string>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>

using namespace std;
const int maxn=100;
char p[maxn][maxn];


int main()
{
#ifndef ONLINE_JUDGE
    freopen("ca","r",stdin);
	freopen("ca.out","w",stdout);
#endif
    int r,c;
    int cas,icas=0;
    cin>>cas;
    while(cas--){
    	icas++;
    	printf("Case #%d:\n",icas);

    	cin>>r>>c;
    	int i,j;
    	for (i = 0; i < r; ++i) {
			for (j = 0; j < c; ++j) {
				cin>>p[i][j];
			}
		}
    	bool flag=true;

    	for (i = 0; i < r; ++i) {
    		if(!flag) break;
			for (j = 0; j < c; ++j) {
				if(!flag) break;
				if(p[i][j]=='#'){
					if(i+1<r && j+1<c &&p[i+1][j]=='#' && p[i][j+1]=='#' && p[i+1][j+1]=='#' )
					{
						p[i][j]='/';p[i][j+1]='\\';
						p[i+1][j]='\\';p[i+1][j+1]='/';
					}else{
						flag=false;
						break;
					}
				}
			}
		}

    	if(!flag)
    		printf("Impossible\n");
    	else{
        	for (i = 0; i < r; ++i) {
    			for (j = 0; j < c; ++j) {
    				printf("%c",p[i][j]);
    			}
    			printf("\n");
    		}
    	}





    }


	return 0;
}
