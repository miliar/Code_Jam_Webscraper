#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <ctime>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>
#include <cstring>
using namespace std;

#define fi first
#define se second
#define pb(a) push_back(a)
#define mp(a, b) make_pair(a, b)

map<char, char> M;
char S[10000];



int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output2.txt", "w", stdout);
    string F2 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string S2 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    for(int i = 0; i < F2.length(); i++)
    {
        M[F2[i]] = S2[i];
    }
    M['q'] = 'z';
    M['z'] = 'q';
    //printf("M.size = %d\n", M.size());
    int n;
    scanf("%d\n", &n);
    for(int test = 1; test <= n; test++)
    {

//        int len = 0;
//        char c = ' ';
//        while(c != '\n')
//        {
//            if(scanf("%c", &c) < 0)
//                break;
//            S[len++] = c;
//        }
//        if(len > 0)
//            len--;
//      //  printf("len = %d\n", len);
        gets(S);
       // printf("Case #%d: %s\n", test, S);
     //   S[len] = '\0';
        for(int i = 0; S[i] != '\0'; i++)
        {
            if(S[i]>= 'a' && S[i] <= 'z')
            {
                //printf("(%d)(%c)(s) ", i, S[i]);
                S[i] = M[S[i]];
            }
        }
        cout << "Case #"<< test<<": ";
        printf("%s\n", S);
    }
    return 0;
}
