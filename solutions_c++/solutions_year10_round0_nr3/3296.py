#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>

long long int n, m, p;
long int r;
long long int a[1001][2],b[1001];
int main()
{
	char filename[32], infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); 
	strcpy(outfile, filename);
	strcat(infile, ".in"); 
	strcat(outfile, ".out");

	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
    fscanf(fp, "%ld", &r);
	
	for(long int i=1;i<=r;i++){
             
	long long int  j=0, dc=0,qe=1;
	long long int loc=0,sum=0,partial=0,gtot=0;
	long long int startpoint=1,endpoint=p;
    
    fscanf(fp, "%Lu%Lu%Ld", &n,&m,&p);
    
    for(j=0;j<p;j++) { 
                     fscanf(fp, "%d", &a[j][0]); 
                     a[j][1] = -1; 
                     gtot =gtot + a[j][0]; 
    }
    a[0][1]=1;
    b[0]=0;
    
    if(gtot < m){
            sum = gtot * n;
    }
    else{
         do{
            loc = loc + a[dc][0];   dc++;          
            dc = dc % p;
            if( m < loc + a[dc][0]){
                b[qe] =   loc;
                qe++;
                loc = 0;
                if(a[dc][1] == -1 )
                            a[dc][1] =  qe;
                else{
                     startpoint = a[dc][1]  ;
                     endpoint = qe-1; 
                     break;
                }
            }
         }while(1);
         if(n>=endpoint){
                         for(long int wq = startpoint ; wq <= endpoint; wq++)
                                  partial = partial + b[wq];
                         sum = sum + partial * ((n-startpoint+1)/(endpoint - startpoint + 1));
                         for(int we = 1 ; we <= startpoint-1; we++)
                                 sum = sum + b[we];
                                 long long int asd = (n-startpoint+1)%(endpoint - startpoint + 1);
                                 if(asd > 0){
                                        for(int we = startpoint ; we <= (startpoint + asd -1); we++)
                                                sum = sum + b[we];   
                                 } 
         }
         else{
              for(int we = 1 ; we <= n; we++)
                      sum = sum + b[we];  
         }
    }
    fprintf(ofp, "Case #%d: %Lu\n", i, sum);
    }
    return 0;
}
