#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <memory.h>

int main()
{

	freopen("A-small-attempt2.in","rt",stdin);
	freopen("A.out","wt",stdout);
    
    const char c[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l'
        ,'b','k','r','z','t','n','w','j','p','f','m','a','q'};

    int n;
    std::cin>>n;
    char t[11];
    std::cin.getline(t,10);
    for(int i=0;i<n;i++)
    {
        char in[200];
        memset(in,0x00,sizeof(in));
        std::cin.getline(in,200);
        std::string s(in);
        printf("Case #%d: ",i+1);
        for(int j=0;j<s.length();j++)
        {
            if (s.at(j)!=' ') 
                printf("%c", c[s.at(j)-0x61]);
            else 
                printf(" ");
        }
        printf("\n");
    }
	return 1;
}