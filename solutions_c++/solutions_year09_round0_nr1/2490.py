#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>    
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits.h>
using namespace std;

char str[5001][16];
char temp[100];

int main(){
    int ts, l, d, n;

	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);

	scanf("%d %d %d",&l,&d,&n);
	for(int i=0;i<d;i++)
		scanf("%s",str[i]);
	for(int tt=0;tt<n;tt++){
		int ans = 0;

		scanf("%s",temp);

		int pnt = 0;
		bool mode = false, flag = true;
		for(int i=0;i<d;i++){
			pnt = 0;
			for(int j=0;j<strlen(temp);j++){
				if(temp[j] == '('){
					mode = true;
					flag = false;
					continue;
				}else if(temp[j] == ')'){
					if(!flag){
						break;
					}
					mode = false;
					pnt += 1;
					continue; 
				}

				if(!mode){
					if(str[i][pnt] != temp[j]){
						flag = false;
						break;
					}
					pnt += 1;
				}else{
					if(str[i][pnt] == temp[j])
						flag = true;
				}
			}
			if(flag)
				ans += 1;
		}
		printf("Case #%d: %d\n",tt+1,ans);
    } 
    return 0;
}
