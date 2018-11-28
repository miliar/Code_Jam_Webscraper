#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
char mymap[]="yhesocvxduiglbkrztnwjpfmaq";
char g[200];
int main(){
#ifdef DEBUG
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
#endif
    int t,i,j,len;
    scanf("%d\n",&t);
    for(i=1;i<=t;i++){
        printf("Case #%d: ",i);
        gets(g);
        len=strlen(g);
        for(j=0;j<len;j++)
            if(isalpha(g[j])) g[j]=mymap[g[j]-'a'];
        puts(g);
    }
	return 0;
}
