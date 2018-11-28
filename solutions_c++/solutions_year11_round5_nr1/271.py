#include<stdio.h>
#include<string>
#include<vector>
#include<math.h>
using namespace std;

double EPS = 0.00001;

int W, L, U, G;

int lowx[105];
int lowy[105];

int upx[105];
int upy[105];

double baixo[1005];
double alto[1005];
double dif[1005];
double area[1005];
double areatot;
int main(){
    int T, g;
    int i, k;
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%d %d %d %d ", &W, &L, &U, &G);    
        for(i=0; i<L; i++)
            scanf("%d %d ", &lowx[i], &lowy[i]);
        for(i=0; i<U; i++)
            scanf("%d %d ", &upx[i], &upy[i]);
        
 
        for(i=0; i<L-1; i++){
            for(k=lowx[i]; k<=lowx[i+1]; k++){
                baixo[k] = (double)lowy[i] + ( (double)k-(double)lowx[i] )*( ((double)lowy[i+1] - (double)lowy[i])/ ((double)lowx[i+1]-(double)lowx[i]) );
                //printf("baixo[%d]=%llf\n", k, baixo[k]);
             }    
        }
        for(i=0; i<U-1; i++){
            for(k=upx[i]; k<=upx[i+1]; k++){
                alto[k] = (double)upy[i] + ( (double)k-(double)upx[i] )*( ((double)upy[i+1] - (double)upy[i]) / ((double)upx[i+1] -(double)upx[i]) );
                //printf("alto[%d]=%llf\n", k, alto[k]);
            }
        }
        
        for(i=0; i<=W; i++)
            dif[i] = alto[i]-baixo[i];
        
        areatot=0.0;
        double areacul[1005];
        for(i=0; i<W; i++){
            area[i]= (dif[i]+dif[i+1])/2;
            areatot += area[i];
            areacul[i+1] = areatot;
            //printf("area[%d]=%llf\n", i, area[i]);
        }
        //printf("areatot=%llf\n", areatot);
        
        printf("Case #%d:\n", g);
        double acul = 0.0;
        i=0;
        k=0;
        while(k<W){
            double target = (areatot/(double)G)*(double)(i+1);
            double aux = areacul[k];
            acul= areacul[k+1];
            //printf("i=%d k=%d target=%llf, acul=%llf, aux=%llf\n", i, k, target, acul, aux);
            if(acul > target +EPS){//prestar atencao aqui!!!!!
                double isso =target - aux;
                //printf("isso=%llf\n", isso);
                double m;
                double aa = dif[k+1]-dif[k];
                double bb = 2*dif[k];
                double cc = -2*isso;
                double delta = sqrt(bb*bb - 4*aa*cc);
                double mlinha=5;
                if(aa>EPS || aa< -EPS){
                    m = (-bb + delta)/(2*aa);
                    //printf("bb = %llf, delta=%llf aa =%llf\n", bb, delta, aa);
                    mlinha = (-bb-delta)/(2*aa);
                    //printf("m=%llf, mlinha=%llf\n", m, mlinha);

                }
                else{
                    m = isso/dif[k];
                }
                if(m>=0-EPS && m<1) 
                    printf("%llf\n", m+(double)k);
                else if(mlinha >=0-EPS && mlinha<1)
                    printf("%llf\n", mlinha+(double)k);
                i++;
                
                if(i>=G-1) break;
            }
            else{
                k++;
            }
        }
        
        
    }
    
    return 0;
}
