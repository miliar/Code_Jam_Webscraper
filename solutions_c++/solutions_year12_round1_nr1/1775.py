#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

int getnum(int k) {
    char ch;
    for (;true;) {
        scanf("%c",&ch);
        if (ch>='0' && ch<='9') break;
    }
    int number=(ch-48)*10;
    scanf("%c",&ch);
    if (ch!='.') return number;
    for (;true;) {
        scanf("%c",&ch);
        if (ch>='0' && ch<='9') break;
    }
    char ch2;
    for (;true;) {
        scanf("%c",&ch2);
        if (ch2<'0' || ch2>'9') break;
    }
    return number+ch-48;
}
double getmin(double a,double b) {
    if (a<b) return a;
    return b;
}
int T,A,B;
double l[100005],ans;
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (int tsum=1;tsum<=T;tsum++) {
        scanf("%d%d",&A,&B);
        double lv=1.0;
        l[0]=0.0;
        double p;
        for (int i=1;i<=A;i++) {
            scanf("%lf",&p);
            l[i]=l[i-1]+lv*(1-p);
            lv=lv*p;
        }
        ans=(1-l[A])*(B-A+1)+l[A]*(B-A+1+B+1);
        ans=getmin(ans,B+2);
        for (int i=1;i<=A;i++) {
            ans=getmin(ans,l[A-1]*(A-i+1+B-i+2+B+1)+(1-l[A-1])*(A-i+1+B-i+2));
        }
        printf("Case #%d: %.6lf\n",tsum,ans);
    }  
    return 0;
}
