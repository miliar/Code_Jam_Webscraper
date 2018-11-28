#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector< vector<int> > dp;

char word[] = "welcome to code jam";

int main () {
    int i,j,k,n,l,res;
    string str;
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    scanf ("%d\n",&n);
    for (i=0;i<n;i++) {
        dp.clear(); dp.resize(20);
        getline (cin,str);
        l = str.length();
        for (j=0;j<=19;j++) {
            dp[j].resize(l+1);       
            for (k=0;k<=l;k++) dp[j][k] = 0;
        }
        dp[0][0] = 1;
        for (j=0;j<=19;j++) {
            for (k=1;k<=l;k++) {
                if (j==0) {
                   dp[j][k] = 1;
                   continue;   
                }
                dp[j][k] = dp[j][k-1];
                if (word[j-1]==str[k-1]) {
                   dp[j][k] = (dp[j][k]+dp[j-1][k-1])%1000;
                }
            }    
        }
        printf ("Case #%d: ",i+1);
        res = dp[19][l];
        if (res<10) printf ("000%d\n",res);
        else if (res<100) printf ("00%d\n",res);
        else if (res<1000) printf ("0%d\n",res);
        else printf ("%d\n",res);
    }
    return 0;    
}
