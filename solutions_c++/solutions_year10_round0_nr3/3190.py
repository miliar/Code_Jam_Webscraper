#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
long long int n, m, p;
long int r;
long long int a[1001][2],b[1001];
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");

	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
 

	fscanf(fp, "%ld", &r);
	
	for(long int i=1;i<=r;i++) 
{
	long int  j=0, dc=0,qe=1;
	long long int loc=0,sum=0,partial=0,tree=0;
	int start=1,endpoint=p;
           fscanf(fp, "%Ld%Ld%d", &n,&m,&p);

for(j=0;j<p;j++) { fscanf(fp, "%d", &a[j][0]); a[j][1] = -1; tree =tree + a[j][0]; }
a[0][1]=1;
b[0]=0;
if(tree < m)
{
        sum = tree * n;
        }
        else
        {



do
{
   
   loc = loc + a[dc][0];   dc++;          
   dc = dc % p;
   if( m < loc + a[dc][0])
   {
   b[qe] =   loc;
   qe++;
   loc = 0;
   if(a[dc][1] == -1 )
   a[dc][1] =  qe;
   else
   {
    start = a[dc][1]  ;
    endpoint = qe-1; 
   break;
   
}
   }

}while(1);
if(n>=endpoint){
for(int wq = start ; wq <= endpoint; wq++)
partial = partial + b[wq];
 sum = sum + partial * ((n-start+1)/(endpoint - start + 1));
 for(int we = 1 ; we <= start-1; we++)
sum = sum + b[we];
long long int asd = (n-start+1)%(endpoint - start + 1);
if(asd > 0)
{
    for(int we = start ; we <= (start + asd -1); we++)
sum = sum + b[we];   
} 
}else
{
     
         for(int we = 1 ; we <= n; we++)
sum = sum + b[we];  
     
     }




}
           fprintf(ofp, "Case #%d: %Ld\n", i, sum);
}
	return 0;
}
