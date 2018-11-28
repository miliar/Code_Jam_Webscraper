#include <stdio.h>
#include <string.h>
#include <memory.h>
#include <vector>
#include <algorithm>

#pragma optimize("O2",on)
using namespace std;

char s[1100],t[1100];

int main() {
#ifndef ONLINE_JUDGE
    freopen("D-small.in","r",stdin);
    freopen("D-small.out","w",stdout);
	//ifstream cin("A-small.in");
    //ofstream cout("A-small.out");
#endif
    int T; scanf("%d",&T);
    for (int o=1; o<=T; o++) {
        int k=0; scanf("%d\n",&k);
        gets(s);  int l=strlen(s);
        vector<int> a; int c=1;
        for (int i=1; i<=k; i++)
            {c*=i; a.push_back(i-1);}
        int res=1000000;
        for (int q=1; q<=c; q++) {
            for (int i=0; i<=l; i++)
                t[i]=s[i-i%k+a[i%k]];
            int cur=0;
            for (int i=1; i<=l; i++)
                if (t[i]!=t[i-1])
                    cur++;
            if (cur<res) res=cur;
            next_permutation(a.begin(),a.end());
        }
        printf("Case #%d: %d\n",o,res);
    }
	return 0;
}