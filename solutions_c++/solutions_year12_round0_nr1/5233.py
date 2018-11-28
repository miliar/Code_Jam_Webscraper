/*
 * Author:  xioumu
 * Created Time:  2012-4-14 11:51:45
 * File Name: aa.cpp
 * solve: aa.cpp
 */
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
#define esp 1e-8
#define maxn 1007
typedef long long int64;
int z[maxn] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
};
string s;
int main(){
    int t;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d\n",&t);
    for(int ii= 1; ii<=t; ii++){
        getline(cin, s);
        //cout << s << endl;
        printf("Case #%d: ",ii);
        for(int i=0; i<s.size(); i++)
            if(s[i] == ' ') printf(" ");
            else printf("%c",z[ s[i] ]);
        if(ii != t) printf("\n");
    } 
    return 0;
}
