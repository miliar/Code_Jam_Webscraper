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

int n;
char input[1000];
char output[1000];
char mmap[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
//#define home
//#define small
//#define large
int main() 
{
#ifdef home
    freopen("1.txt", "r", stdin);
#endif
#ifdef small
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-out-small", "w", stdout);
#endif
#ifdef large
    freopen("A-large.in", "r", stdin);
    freopen("A-out-large", "w", stdout);
#endif
    char str[26];

    scanf("%d", &n);
    getchar();
    int _case = 1;
    while(n--)
    {
        scanf("%[^\n]s", input);
        getchar();
        int i;
        for(i = 0;i < strlen(input);i++)
        {
            if(input[i] == ' ') output[i] = ' ';
            else
                output[i] = mmap[input[i]-'a'];
        }
        output[i] = '\0';
        printf("Case #%d: %s\n",_case++, output);
    }
}
