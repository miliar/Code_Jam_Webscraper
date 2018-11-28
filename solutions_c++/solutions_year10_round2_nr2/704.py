#include<stdio.h>
#include <iostream>
#include<memory.h>
#include<string.h>
#include<math.h>
#include<conio.h>


int main()
{
	char filename[32], infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); 
	strcpy(outfile, filename);
	strcat(infile, ".in"); 
	strcat(outfile, ".out");

	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int count =0;
	int sum =0;
	int scount=0;
	int j=0;
	long long int b;
int n,k,c,tt;
long long int x[50];
int v[50];

    fscanf(fp, "%d", &c);
	
	for(int i=1;i<=c;i++){
        
        count =0 ;
        scount=0;
        sum=0;
                     
        fscanf(fp, "%d %d", &n,&k);
                fscanf(fp, "%Ld", &b);
                        fscanf(fp, "%d", &tt);
        for(j=0;j<n;j++) { 
                     fscanf(fp, "%Ld", &x[j]); 
        }
        for(j=0;j<n;j++) { 
                       fscanf(fp, "%d", &v[j]); 
        }      
        for(j=n-1;j>=0;j--){
                            //fprintf(ofp, "Before cal #%d: %d %d %Ld %Ld \n",i,tt, v[j], b,x[j]);
                            //fprintf(ofp, "%Ld \n",x[j]);
                           if(  (long int)(tt*v[j]) >= (long int)(b-x[j]) ){
                                         scount++;
                                         
                                         sum = sum +count;               
                                         if(scount>=k){
                                                       break;
                                                       }
                                }
                                else{
                                     count++;
                              //       fprintf(ofp, "Case #%d: %d %d\n",i, scount, count);
                                     if(count > (n-k))
                                              break;
                                     }
                                     
        }          
    
    
        if(scount >= k){
                  fprintf(ofp, "Case #%d: %d\n", i, sum);
        }
        else{
             fprintf(ofp, "Case #%d: IMPOSSIBLE\n", i);
        }
    }
    return 0;
}
