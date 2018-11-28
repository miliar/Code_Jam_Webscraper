#include <stdio.h>
#include <stdlib.h>


double P[100010];
int main(){
    FILE *f = fopen("1.in","r");
    FILE *o = fopen("1.out","w");
    int T;
    fscanf(f,"%d",&T);
    for (int t = 1 ; t <= T ; t++){
        int A,B;
        fscanf(f,"%d %d",&A,&B);
        //printf("%d %d\n",A,B);
        for (int i = 1 ; i <= A ; i++){
            fscanf(f,"%lf",&P[i]);
            //printf("%lf ",P[i]);
        }
        //printf("\n");
        P[0] = 1;
        double ans,min=B+2;
        double p = 1;
        for (int i = 0 ; i <= A ; i++){
            p*=P[i];
            ans = ((A-i)+(B-i)+1)*p + (((A-i)+(B-i)+1) + B + 1)*(1-p);
            if (ans < min) min = ans;
        }
        fprintf(o,"Case #%d: %lf\n",t,min);
    }
    system("pause");
    fclose(f);
    fclose(o);
}
