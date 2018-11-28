#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("2.out","w",stdout);
    int T;
    cin>>T;
    for (int _=1;_<=T;_++){
        int n,at=0,ap=1,bt=0,bp=1;
        cin>>n;
        while (n--){
              char ch=getchar();
              ch=getchar();
              int p;
              cin>>p;
              if (ch=='O'){
                  if (at<bt){
                      if (ap<p) ap=min(p,ap+bt-at); else ap=max(p,ap-bt+at);
                      at=bt;
                  }
                  at+=abs(p-ap)+1;
                  ap=p;
              }
              if (ch=='B'){
                  if (bt<at){
                      if (bp<p) bp=min(p,bp+at-bt); else bp=max(p,bp-at+bt);
                      bt=at;
                  }
                  bt+=abs(p-bp)+1;
                  bp=p;
              }
        }
        printf("Case #%d: %d\n",_,max(at,bt));
    }
//system("pause");
}
/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

*/
