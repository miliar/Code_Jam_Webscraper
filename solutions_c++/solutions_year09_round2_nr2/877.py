/*
ID: frank44
PROG: the_next_number
LANG: C++
 */

#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>

using namespace std;

int main()
{
    freopen("data.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    char num[32];

    int t;
    scanf("%d", &t);

    for (int x=1; x<=t; x++)
    {
        scanf("%s", num);

        string str(num);

        bool flag = true;
        for (int i=0; i+1<str.length(); i++)
            if (str[i]<str[i+1]) flag = false;

        if (!flag)
        {
            next_permutation(num, num+str.length());
            printf("Case #%d: %s\n", x, num);
        }
        else
        {
            sort(num, num+str.length());
            str = string(num);

            int i = 0;
            while (str[0]=='0')
            {
                swap(str[0], str[i]);
                i++;
            }
            
            str.insert(1, "0");
            printf("Case #%d: %s\n", x, str.c_str());
        }
    }


}
