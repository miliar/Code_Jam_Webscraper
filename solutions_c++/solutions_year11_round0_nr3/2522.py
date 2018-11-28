#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <stdio.h>
#include <string.h>


using namespace std;


int main()
{
    long T, N;

    cin>>T;
    for (int cas=1;cas<=T;cas++){
        cin>>N;
        vector <long int> lt;
        long sum=0;
        long xorx = 0, num;
        while(N--){
            cin>>num;
            xorx = xorx^num;
            lt.push_back(num);
            sum+=num;
        }
        if (xorx != 0){
            printf("Case #%d: %s\n", cas, "NO");
            continue;
        }
        sort(lt.begin(), lt.end());
        printf("Case #%d: %d\n", cas, sum-lt[0]);
    }

}

