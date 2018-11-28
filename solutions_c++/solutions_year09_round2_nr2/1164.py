#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <functional>

using namespace std;

#define REP(i,a,b) for(i=(a); i<(b); ++i)
#define Rep(i,n) REP(i,0,n)
#define Vs vector<string>
#define Vsi vector<string>::iterator
#define Vi vector<int>
#define Vii vector<int>::iterator
#define Wilv(v,iter,iter_end) (iter)=(v).begin(),(iter_end)=(v).end();while( (iter)!=(iter_end) )

typedef map<string, string> PMap;

inline int sq(int n)
{
    return n*n;
}

inline int next(int num, int base)
{
    int ret=0;
    while(num>0) {
        ret += sq(num%base);
        num /= base;
    }
    return ret;
}



int main()
{
    int N;
    freopen("..\\in.txt", "r", stdin);
    freopen("..\\out.txt", "w", stdout);

    scanf("%d", &N);

    for(int ncase=1; ncase<=N; ncase++) {
        char a[30];
        char f[10]={0};
        scanf("%s", a);

        int len=0;
        while(a[len]!=0) {
            len++;
        }
        int i,j;
        for(i=len-1; i>=1; i--) {
            f[a[i]-'0']=i;
            if(a[i]>a[i-1]){
                for(j=a[i-1]-'0'+1; j<10; j++) {
                    if(f[j]){
                        int tmp = a[i-1];
                        a[i-1]=a[f[j]];
                        a[f[j]] = tmp;
                        break;
                    }
                }
                sort(a+i,a+len);
                break;
            }
        }

        if(i==0 || a[0]=='0') {
            a[len] = '0'; a[++len]=0;
            sort(a, a+len);
            Rep(i,len) {
                if(a[i]!='0'){
                    a[0] = a[i];
                    a[i] = '0';
                    break;
                }
            }
        }

        printf("Case #%d: %s\n", ncase, a);
    }

    return 0;
}

