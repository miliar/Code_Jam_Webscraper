#include <iostream>
using namespace std;

char a[5011][20];
bool b[20][30];
long l,d,n;

int main() {
//    freopen("a-small-attempt0.in","r",stdin);
    freopen("a-large.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>> l >> d >> n;
    
    for(long i=0; i<d; i++) scanf("%s\n",&a[i]);
    
    for(long test=0; test<n; test++) {
        long kq=0;
        
        memset(b,false,sizeof b);
        
        for(long i=0; i<l; i++) {
            char c;
            scanf("%c",&c);
            if (c!='(') {
                b[i][(long)c-'a']=true;
            } else do {
                scanf("%c",&c);
                if (c!=')') b[i][(long)c-'a']=true;
            } while (c!=')');
            scanf("\n");
        } //for i=0..l
        
        for(long i=0; i<d; i++) {
            bool gn=true;
            for(long j=0; j<l; j++)
                if (!b[j][(long)a[i][j]-'a']) {
                    gn=false;
                    break;
                }
            if (gn) kq++;
        } //for i=0..d
        
        cout<<"Case #"<<1+test<<": "<<kq<<"\n";
    } //for test
} //main
