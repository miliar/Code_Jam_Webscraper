#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

int main() {
    int Test; cin >> Test;
    char arr[1000],carr[1000];
    for(int tst=1; tst<=Test;tst++) {
            printf("Case #%d: ",tst);
            cin >> arr;
//            strcpy(carr,arr);
            int len = strlen(arr);
            if(next_permutation(arr,arr+len))
               printf("%s",arr);
            else { sort(arr,arr+len);
 //                printf("%c0",arr[0]); if(len>1) printf("%s",arr+1);
                   int idx=0;
                   while(arr[idx]=='0') idx++;
                   char ch=arr[idx]; arr[idx]='0';
                   printf("%c%s",ch,arr);
                   
                 }
            printf("\n");
    }
            
    
       
    return 0;
}
