#include <stdio.h>
#include <stdlib.h>


int main () {
    
    int x,hasil,n,k,b,t,cou,te,z,max;
    int jarak[55];
    int kec[55];
    double waktu[55];
    scanf("%d",&x);
    for(int c=1; c<=x;c++) {
        hasil = 0;
        scanf("%d %d %d %d",&n,&k,&b,&t);
        for (int i=0;i<n;i++) {
            scanf("%d",&jarak[i]);
        }
        for (int i=0;i<n;i++) {
            scanf("%d",&kec[i]);
        }
        
        for(int i=0;i<n;i++) {
            waktu[i] = (double)(b-jarak[i])/(double)kec[i];
        }
           
        cou = 0;     
        for(int i=0;i<n;i++) {
            if(waktu[i] <= t) cou++;
            //printf("%d ",waktu[i]);
        }
        if(cou >= k) {
            cou = 0;           
            for(int i = n-1; i>=0; i--) {
                if(waktu[i] <= t) cou++;
                else break;
            }
            while(cou < k) {   
                for (int i=n-1;i>=0;i--) {
                    if(waktu[i] > t) {
                        for(int j=i-1;j>=0;j--) {
                            if(waktu[j] <= t) {
                                for(int zz=j; zz<i; zz++) {
                                    te = waktu[zz];
                                    waktu[zz] = waktu[zz+1];
                                    waktu[zz+1] = te;
                                    hasil++;
                                }
                                break;
                            }
                        }
                        break;
                    }
                }
                                
                cou = 0;                
                for(int i = n-1; i>=0; i--) {
                    if(waktu[i] <= t) cou++;
                    else break;
                }
            }            
            
            printf("Case #%d: %d\n",c,hasil);
        } else  printf("Case #%d: IMPOSSIBLE\n",c);
    }
    
    while (getchar()!=EOF);
    return 0;
}
