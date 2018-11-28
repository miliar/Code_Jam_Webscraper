#include <iostream>
using namespace std;

void solve(int casen){
    int n,br, time=0,ttime=0,stime=0;
    int poso=1, posb=1;
    char r,last='O';
    scanf("%d",&n);
    for (int k=0;k<n;++k){
        cin >> r >> br;
        if (r=='O'){
            
            if (last=='B'){
                ttime=abs(poso-br)+1-stime;
                if (ttime<=0) ttime=1;
                stime=ttime;
            
            }
            if (last=='O'){
                ttime=abs(poso-br)+1;
                stime+=ttime;
            }
            poso=br;
            last='O';
        }
        if(r=='B'){
            if (last=='O'){
                ttime=abs(posb-br)+1-stime;
                if (ttime<=0) ttime=1;
                stime=ttime;
            
            }
            if (last=='B'){
                ttime=abs(posb-br)+1;
                stime+=ttime;
            }
            posb=br;
            last='B';
        }
        time += ttime;
        //printf("%d\n", ttime);
    }
    printf("Case #%d: %d\n", casen,time);
    return;    
}


int main(void){
    int n;
    scanf("%d",&n);
    
    for (int k=0;k<n;++k)
        solve(k+1);
    
    //system("pause");
    return 0;
        
}
