#include<stdio.h>

//int d[1000010];

int main(){
    int T, C;
    int g, r;
    int D;
    double s;
    double super;
    int P[205];
    int V[205];
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%d %d ", &C, &D);
        s=0;
        super=0;
        //printf("D = %lld\n", D);
        for(r=0; r<C; r++){
            scanf("%d %d ", &P[r], &V[r]);
            //printf("P V %d %d\n", P[r], V[r]);
            
            //printf("s = %llf\n", s); 
            
            if(r>=1){
                s = s + D -(P[r]-P[r-1]);
                if(s > super) super =s;
                if(s<0) s=0;
            }
            s = s + (V[r]-1)*D;
            if(s>super) super = s;
        }
        printf("Case #%d: ", g);
        
        
        printf("%llf\n", super/2);
    }
    return 0;
}
