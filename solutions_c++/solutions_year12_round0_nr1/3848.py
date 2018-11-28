#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

char s[10000];
char map[] = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
    int tt; scanf("%d",&tt); gets(s);
    for (int ti=1;ti<=tt;ti++){
        printf("Case #%d: ",ti);
        gets(s);
        for (int i=0;s[i];i++){
            if (s[i]>='a' && s[i]<='z'){
                s[i] = map[s[i]-97];
            }
        }
        puts(s);
    }
    return 0;
}

