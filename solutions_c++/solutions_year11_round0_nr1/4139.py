#include <iostream>
#include <cmath>
using namespace std;

struct target{
    char color;
    int pos;
};

int main(){
    int n,t,waitO,waitB,posO,posB,out;      
    scanf("%d",&n);
    for (int z=0;z<n;z++){
        scanf("%d",&t);
        target seq[110];
        waitO=0;
        waitB=0;
        posO=1;
        posB=1;
        out=0;
        for (int y=0;y<t;y++)
            cin>>seq[y].color>>seq[y].pos;    
        for (int y=0;y<t;y++){
            if (seq[y].color=='O'){
                if (waitO>=abs(seq[y].pos-posO)){
                  out++;               
                  waitB++;
                  posO=seq[y].pos;
                  waitO=0;
                }
                else{
                  out+=abs(seq[y].pos-posO)-waitO;
                  out++;
                  waitB+=abs(seq[y].pos-posO)-waitO+1;
                  posO=seq[y].pos;
                  waitO=0;
                }
            }
            else{
                if (waitB>=abs(seq[y].pos-posB)){
                  out++;           
                  waitO++;
                  posB=seq[y].pos;
                  waitB=0;
                }
                else{
                  out+=abs(seq[y].pos-posB)-waitB;
                  out++;
                  waitO+=abs(seq[y].pos-posB)-waitB+1;
                  posB=seq[y].pos;
                  waitB=0;
                }
            }
        }
        printf("Case #%d: %d\n",z+1,out);                        
    }
}
