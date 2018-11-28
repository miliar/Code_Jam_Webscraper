#include<stdio.h>
#include<stdlib.h>

int main()
{
    FILE* input=fopen("input.in","r");
    FILE* output=fopen("output.out","w");
    
    int triplets[100][4];
    int T,S,p,N;
    fscanf(input,"%d",&T);
    
    for(int k=0; k<T; k++)
    {
                    
         fscanf(input,"%d",&N);
         fscanf(input,"%d",&S);
         fscanf(input,"%d",&p);
         for(int i=0; i<N; i++)
         {
             int temp,mod,x,y;
             x=0;y=0;
             fscanf(input,"%d",&temp);
             //printf("%d",temp);
             mod=temp%3;
             temp=temp/3;
             if(mod==2){x=1; y=1;}
             else if(mod==1) { x=1; y=0; }
             triplets[i][0]=temp+x;
             triplets[i][1]=temp+y;
             triplets[i][2]=temp;
             triplets[i][3]=mod;
         }
         int count=0;
         
         for(int i=0; i<N; i++)
         {
       
         if( triplets[i][0]>=p){ count++; }
         else if(triplets[i][3]!=1 && triplets[i][0]==p-1 && triplets[i][0]>0 && S>0) {  printf("%d\n",k);count++; S--;}
          
         }
         
         fprintf(output,"Case #%d: %d\n",k+1,count);
    }
    fclose(output);
    //system("PAUSE");
    return 0;   
}
