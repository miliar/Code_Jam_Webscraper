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

char buff[105];

const int maxb=105;
long long arr[maxb];

int main(){
    int test;
    scanf("%d",&test);
    
    arr[0]=1;
    arr[1]=0;
    for(int i=2;i<maxb;i++)
        arr[i]=i;
    
    for(int t=1;t<=test;t++){
        printf("Case #%d: ",t);
        map<char,long long> m;
        
        
        scanf("%s",buff);
        long long b=0;
        for(int i=0,sz=strlen(buff);i<sz;i++){
            if(!m.count(buff[i])){
                m[buff[i]]=arr[b];
                b++;
            }
        }
        
        if(b==1) {b=2;}
        
        long long res=0;
        for(int i=0,sz=strlen(buff);i<sz;i++)
            res=res*b+m[buff[i]];
        
        printf("%I64d\n",res);
    }
    return 0;
}
