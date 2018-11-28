#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <iostream>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define mp make_pair
#define pb push_back

typedef long long ll;

using namespace std;

void solve(int kase)
{

    int n;
    int value[50][50];
    int row[50];
    int count = 0;

    scanf("%d",&n);
    REP(i,n) {
        char buf[1024];
        scanf("%s",buf);
        row[i] = 0;
        REP(j,n) {
            value[i][j] = buf[j]-'0';
            if(value[i][j]) row[i] = j;
        }
//        printf("%d\n",row[i]);
    }

    REP(i,n) {
        for(int j=i; j<n; ++j) {
            if(row[j] <= i) {
                count += j-i;
                for(int k=j; k >= i+1; --k) {
                    swap(row[k],row[k-1]);
                }
                break;
            }
        }
    }

    printf("Case #%d: %d\n",kase,count);
}

int main()
{
    int t;
    scanf("%d",&t);
    REP(i,t) solve(i+1);

	return 0;
}
