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
int gcd(int a,int b){
	return b?gcd(b,a%b):a;
}

using namespace std;
int main(){
    int tt;
    long long N,pd,pg;
    freopen("111.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&tt);
    for (int tcas = 1;tcas<=tt;tcas++){
        printf("Case #%d: ",tcas);
        cin>>N>>pd>>pg;
        if (pg==100&&pd!=100){
                             printf("Broken\n");
                             continue;
                             }
        if (pg==0&&pd!=0){
                        printf("Broken\n");
                             continue;
                             }  
        if (pd==0){
               printf("Possible\n");
                             continue;
        }     
        long long tmp = gcd(pd,100);
        long long a = pd/tmp,b = 100/tmp;
        if (N/b>=1) printf("Possible\n");
        else printf("Broken\n");
    }
}
