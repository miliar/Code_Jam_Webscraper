#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


#define max(a,b) a>b?a:b
#define min(a,b) a<b?a:b



int **malloc2D(int Lines,int Columns) 
{
    int k,**matrix;
    matrix=(int**)malloc(Lines*sizeof(int*));
    for(k=0;k<Lines;k++) matrix[k]=(int*)malloc(Columns*sizeof(int));
    return matrix;
}

int *malloc1D(int n)
{
    int *array;
    array=(int*)malloc(n*sizeof(int));
    return array;
}




int T,N,**points,*cases;


void printer()
{
    int i;
    FILE *output;
    output=fopen("output.txt","w");
    for(i=0;i<T;i++)
        fprintf(output,"Case #%d: %d\n",(i+1),cases[i]);

    fclose(output);
}





int main()
{
    int i,j,k,l;
    FILE *input;
    char trash;
    int counter=0;
    input=fopen("A-large.in","r");
    
    fscanf(input,"%d",&T);
    fscanf(input,"%c",&trash);
    cases=malloc1D(T);
    
    for(i=0;i<T;i++)
    {
        fscanf(input,"%d",&N);
        fscanf(input,"%c",&trash);
        points=malloc2D(N,2);
        
        for(j=0;j<N;j++)
        {
            fscanf(input,"%d",&points[j][0]);
            fscanf(input,"%c",&trash);
            fscanf(input,"%d",&points[j][1]);
            fscanf(input,"%c",&trash);
        }
        for(j=0;j<N-1;j++)
            for(k=j+1;k<N;k++)
            {
                if(((points[j][0]>points[k][0])&&(points[j][1]<points[k][1]))||((points[j][0]<points[k][0])&&(points[j][1]>points[k][1])))
                counter++;
            }
            
        cases[i]=counter;
        counter=0;
    }
    fclose(input);
    printer();
    
    system("pause");
    
    return 0;
}
