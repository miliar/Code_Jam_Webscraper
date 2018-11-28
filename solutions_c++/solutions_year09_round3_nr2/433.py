#include <stdio.h>
#include <math.h>

int m[3],v[3];
long double ma[3],ve[3],x,t,time,mass;

int main()
{
    FILE *in,*out;
    int casen,T,i,j,k,n;
    
    
    in = fopen("in.txt","r");
    out = fopen("out.txt","w");
    
    fscanf(in,"%d\n",&T);
    for (casen = 1; casen <= T; casen++) {
        for (i=0; i<3; i++)
            ma[i] = ve[i] = 0;
        
        fscanf(in,"%d\n", &n);
        for (i=0; i<n; i++) {
            fscanf(in,"%d%d%d%d%d%d",m,m+1,m+2,v,v+1,v+2);
            for (j=0; j<3; j++) {
                ma[j] += m[j];
                ve[j] += v[j];
            }
        }
        for (i=0; i<3; i++) {
            ma[i] /= n;
            ve[i] /= n;
        }
        
        
        x = t = mass = 0;
        for (i=0; i<3; i++) {
            x += ma[i] * 2 * ve[i];
            t += 2 * ve[i]* ve[i]; 
        }
        
        time = -x / t;
        time = time > 0 ? time : 0;
        
        for (i=0; i<3; i++) 
            mass += (ma[i] + ve[i] *time) * (ma[i] + ve[i] *time);
        
        
        
        fprintf(out,"Case #%d: %.8lf %.8lf\n", casen,(double) sqrt(mass), (double)time);
    }
    
    fclose(in);
    fclose(out);
}
