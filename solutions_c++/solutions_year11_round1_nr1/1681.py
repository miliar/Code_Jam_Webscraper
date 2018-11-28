#include<iostream>
using namespace std;

int gcd(int x, int y) {
    if (x%y==0) return y;
    return gcd(y,x%y); }

int main() {
    int t,i,n,pd,pg;
    
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    
    cin>>t;
    for (int y=1; y<=t; y++) {
        int md=1,mg=1,d,g,ld,lg,td,tg;
        cin>>n>>pd>>pg;
        bool bisa=1;
        
        if (pd==0) d=1;
        else d=100/gcd(100,pd); td=d;
        if (pg==0) g=1;
        else g=100/gcd(100,pg); tg=g; //cout<<gcd(100,56)<<' '<<gcd(100,50)<<' ';
        if (g==0&&d==0) goto hell;
        else if (d==0) {bisa=0; goto hell;}
        while(g<d) g+=tg;
        md=d*pd/100;
        mg=g*pg/100;
        while (mg<md&&mg!=0) {
              g+=tg; mg=g*pg/100;
              }                   
        lg=g-mg;
        ld=d-md;
        if (d>n||ld>lg) bisa=0; //cout<<g<<" "<<d;
        hell:
        printf("Case #%d: ",y);
        if (bisa) printf("Possible\n");
        else printf("Broken\n");
        }
    //system("pause");
}
