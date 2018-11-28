#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <math.h>
#include <stdio.h>
using namespace std;

int t;

int main(){
    scanf("%d",&t);
    for (int c1=0;c1<t;c1++){
        int c,d,n;
        char p[100][3];
        char o[100][2];
        scanf("%d",&c);
        for (int i=0;i<c;i++) scanf("%s",p[i]);
        scanf("%d",&d);
        for (int i=0;i<d;i++) scanf("%s",o[i]);
        vector<char> res;
        scanf("%d",&n);
        char s[1000];
        scanf("%s",s);
        for (int i=0;i<n;i++){
            if (res.size()>0){
                bool B=false;
                for (int j=0;j<c;j++){
                    if ((s[i]==p[j][0]&&res[res.size()-1]==p[j][1])||(s[i]==p[j][1]&&res[res.size()-1]==p[j][0])) {
                        B=true;
                        res.pop_back();
                        res.push_back(p[j][2]);
                        break;
                        }
                    }
                bool B1=false;
                if (!B){
                    for (int j=0;j<res.size();j++){
                        for (int k=0;k<d;k++){
                            if((res[j]==o[k][0]&&s[i]==o[k][1])||(res[j]==o[k][1]&&s[i]==o[k][0])){
                                B1=true;
                                res.clear();
                                break;
                                }
                            }
                        if (B1) break;
                        }

                    }
                if (!B1&&!B) res.push_back(s[i]);
                } else res.push_back(s[i]);
            }
        printf("Case #%d: [",c1+1);
        for(int i=0;i<res.size();i++){
            if (i!=0) printf(", %c",res[i]); else printf("%c",res[i]);
            }
        printf("]\n");
        }
    return 0;
    }
