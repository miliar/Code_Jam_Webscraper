#include<algorithm>
#include<bitset>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>

#define pi 2*acos(0.0)
#define SIZE 110
#define ROOT 1000010

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T, t=0, n, s, p, N[110], tot;

	scanf("%d",&T);
	while(T--){
	    tot = 0;
	    scanf("%d%d%d",&n,&s,&p);
	    int k=0, x;
        for(int i=0; i<n; i++){
            scanf("%d",&x);
            if(x%3==0){
                if(x/3>=p){
                    tot++;
                }
                else N[k++] = x;
                }
            else if(x/3+1>=p){
                tot++;
            }
            else N[k++] = x;
        }
        if(s>0){
            sort(N, N+k);
            for(int i=1; i<=s && k-i>=0; i++){
                if((N[k-i]>=p) && (N[k-i]-2)/3>=p-2){
                    tot++;
                }
            }
        }

	    printf("Case #%d: %d\n",++t, tot);
	}


	return 0;
}
