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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


const int maxsize=500+5;

int n;
int pailie[maxsize][maxsize];

int mod=100003;

int result[maxsize][maxsize];
void init(){
    for(int i=0;i<maxsize;i++) {
        pailie[0][i]=1;
        pailie[i][i]=1;
    }
    for(int i=2;i<maxsize;i++){
        for(int j=1;j<i;j++){
            pailie[j][i]=(pailie[j][i-1]+pailie[j-1][i-1]) % mod;
        }
    }
}
int calc(int i,int j){
    if(i==1) return 1;
    int r=0;
    for(int t=1;t<i;t++){
        if(t<(2*i-j)) continue;
        r= (r+pailie[i-t-1][j-i-1]*result[t][i])%mod;
    }
    return r;
}
void calc(){
    for(int j=2;j<maxsize;j++){
        for(int i=1;i<j;i++){
            result[i][j]=calc(i,j);
        }
    }

}

int main()
{
    init();
    calc();
//	freopen("test1","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d",&n);
                int r=0;
                for(int i=1;i<n;i++){
                    r=(r+result[i][n])% mod;
                }
                printf("%d\n",r);
		fflush(stdout);
	}



	return 0;
}
