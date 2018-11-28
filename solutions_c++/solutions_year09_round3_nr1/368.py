#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int data[36];
vector<int> res;

int main () {
    int t,i,j,l,x,val,min;
    long long num;
    string s;
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    scanf ("%d\n",&t);
    for (i=1;i<=t;i++) {
        res.clear();
        printf ("Case #%d: ",i);
        for (j=0;j<36;j++) data[j] = -1;
        getline(cin,s);
        l = s.length();
        res.resize(l);
        if (s[0]>='0' && s[0]<='9') data[s[0]-48] = 1;
        else data[s[0]-87] = 1;
        val = 0;
        for (j=1;j<l;j++) {
            if (s[j]>='0' && s[j]<='9') x = s[j]-48;
            else x = s[j]-87;
            if (data[x]!=-1) continue;
            else {
                 data[x] = val;
                 if (val==0) val = 2;
                 else val++;     
            }
        }
        if (val<=1) val = 2;
        for (j=0;j<l;j++) {
            if (s[j]>='0' && s[j]<='9') x = s[j]-48;
            else x = s[j]-87;
            res[j] = data[x];
        }
        num = 0;
        for (j=0;j<l;j++) 
            num = val*num + res[j];
        printf ("%I64d\n",num);
    }
    return 0;    
}
