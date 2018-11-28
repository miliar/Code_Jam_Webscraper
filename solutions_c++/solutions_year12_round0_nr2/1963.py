#include <iostream>
#define N 3

using namespace std;

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int max,min,mod,total;
    int c,n,s,p,y;
    scanf("%i",&c);
    for(int i=0;i<c;i++){
        y=0;
        scanf("%i %i %i",&n,&s,&p);
        for(int j=0;j<n;j++){
            scanf("%i",&total);
            mod=total%N;
            min=total/N;
            max=(mod==0)?(min):(min+1);
            if(max>=p){
                y++;
            }else if(s>0 && (mod==0 || mod==2) && max+1 == p && total>1 ){
                y++;
                s--;
            }
        }
        printf ("Case #%i: %i",i+1,y);
        if(i+1!=c)  printf("\n");
    }
    return 0;
}
