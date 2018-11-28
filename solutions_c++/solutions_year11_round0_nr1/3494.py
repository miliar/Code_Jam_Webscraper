#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kCase=1;kCase<=T;kCase++)
    {
        int BPos = 1;
        int BTime = 0;
        int OPos = 1;
        int OTime = 0;
        int N;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
        {
            char color;
            int num;
            scanf(" %c %d",&color, &num);
            switch(color)
            {
                case 'B':
                    BTime += abs(num - BPos) + 1;
                    if(BTime<=OTime)
                    {
                        BTime = OTime+1;
                    }
                    BPos = num;
                    break;
                case 'O':
                    OTime += abs(num - OPos) + 1;
                    if(OTime<=BTime)
                    {
                        OTime=BTime+1;
                    }
                    OPos = num;
                    break;
            }
        }
        printf("Case #%d: %d\n",kCase, max(BTime,OTime));
    }
}















