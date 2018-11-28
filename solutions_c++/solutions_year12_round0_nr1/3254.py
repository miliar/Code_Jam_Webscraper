#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;
char mp[26];
int main ()
{   string temp = "yhesocvxduiglbkrztnwjpfmaq";
    //freopen ("input.txt", "r", stdin);
    //freopen ("output.txt", "w", stdout);

    int T;


    scanf ("%d",&T);
    getchar();
    for (int p =0;p<T;p++)
    {   char s[105];
        char r[105];
        cin.getline(s,105);
        int n = strlen(s);
        for (int i=0;i<n;i++)
        {   if (s[i]>='a' && s[i]<='z')
                s[i] = temp[s[i]-'a'];
            else if (s[i]= ' ')
                s[i]=' ';
        }
        printf ("Case #%d: ",p+1);
        printf ("%s\n",s);

    }

return 0;
}
