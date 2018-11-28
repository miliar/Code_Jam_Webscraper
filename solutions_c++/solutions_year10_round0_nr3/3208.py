#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
long long int n1, m1, p;
long int r;
long long int app[1001][2], bpp[1001];
int main()
{
char nameoffile[32];
char inputfile[32], outputfile[32];
scanf("%s", nameoffile);
strcpy(inputfile, nameoffile); strcpy(outputfile, nameoffile);
strcat(inputfile, ".in"); strcat(outputfile, ".out");

FILE *fp=fopen(inputfile, "r"), *ofp=fopen(outputfile, "w");
 

fscanf(fp, "%ld", &r);
for(long int i=1;i<=r;i++) 
{
long long int  j=0, cd1=0,me=1;
long long int location=0,sum=0,temp=0,ptree=0;
long long int begn=1,finish=p;
           fscanf(fp, "%Lu%Lu%Ld", &n1,&m1,&p);

for(j=0;j<p;j++) { fscanf(fp, "%d", &app[j][0]); app[j][1] = -1; ptree =ptree + app[j][0]; }
app[0][1]=1;
bpp[0]=0;
if(ptree < m1)
{
        sum = ptree * n1;
        }
        else
        {



do
{
   
   location = location + app[cd1][0];   cd1++;          
   cd1 = cd1 % p;
   if( m1 < location + app[cd1][0])
   {
   bpp[me] =   location;
   me++;
   location = 0;
   if(app[cd1][1] == -1 )
   app[cd1][1] =  me;
   else
   {
    begn = app[cd1][1]  ;
    finish = me-1; 
   break;
   
}
   }

}while(1);
if(n1>=finish){
for(long int wq = begn ; wq <= finish; wq++)
temp = temp + bpp[wq];
 sum = sum + temp * ((n1-begn+1)/(finish - begn + 1));
 for(int we = 1 ; we <= begn-1; we++)
sum = sum + bpp[we];
long long int asd = (n1-begn+1)%(finish - begn + 1);
if(asd > 0)
{
    for(int we = begn ; we <= (begn + asd -1); we++)
sum = sum + bpp[we];   
} 
}else
{
     
         for(int we = 1 ; we <= n1; we++)
sum = sum + bpp[we];  
     
     }




}
           fprintf(ofp, "Case #%d: %Lu\n", i, sum);
}
return 0;
}

