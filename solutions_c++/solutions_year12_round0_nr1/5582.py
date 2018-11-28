using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

int main()
{
    char arr[222],res[222];
    int t,cs=1,l,i;
    char mai[30]="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d",&t);
    cin.ignore();
    while(t--)
    {
        cin.getline(arr,222);
        l=strlen(arr);
        for(i=0;i<l;i++)
        {
            if(arr[i]!=' ')
               res[i]=mai[arr[i]-'a'];
            else
              res[i]=' ';
        }
        res[i]='\0';
        printf("Case #%d: %s\n",cs,res);
        cs++;
    }
    return 0;
}
