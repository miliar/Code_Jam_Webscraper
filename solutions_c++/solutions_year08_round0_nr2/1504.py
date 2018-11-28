#include <stdio.h>
#include <stdlib.h>

typedef struct tim
{
       int start, stop, train,station;
       struct tim* next;
       } tim;

int compare (const void * a, const void * b)
{
     if( (*(tim*)a).start ==  (*(tim*)b).start  )      
         return ( (*(tim*)a).stop - (*(tim*)b).stop );
     return ( (*(tim*)a).start - (*(tim*)b).start );
}


int main()
{
    int m,n,na,nb;
    int i,j,k,q;
    int a,b,c,d,e;
    int tfa,tfb,time,tmp;

    FILE *f,*g;
    f = fopen("in.txt","r");
    g = fopen("out.txt","w");
    e =0;
    fscanf(f,"%d",&m);    
    for(i = 0; i < m; ++i)
    {
                tfa = tfb = 0; 
                
                fscanf(f,"%d",&n);    
                fscanf(f,"%d %d",&na,&nb);    
                tim *t =(tim*)calloc(na+nb,sizeof(struct tim)); 
                
                for(j = 0; j < na; ++j)
                {
                      fscanf(f,"%d:%d %d:%d",&a,&b,&c,&d);                                            
                      t[j].start = a * 60 +b;
                      t[j].stop = c * 60 +d;
                      t[j].station = 1;
               }
                for(k = 0; k < nb; ++k)
                {
                      fscanf(f,"%d:%d %d:%d",&a,&b,&c,&d);                                            
                      t[j+k].start = a * 60 +b;
                      t[j+k].stop = c * 60 +d;
                      t[j+k].station = 2;                    
                }   
                
             qsort(t,na+nb,sizeof(tim),compare);
   //          for(k=0;k<na+nb;k++)
  // /         {
    //                             printf("%d %d %d %d\n",t[k].start,t[k].stop,t[k].station,t[k].train);
          //   }
            e =0;  
              for(k=0;k<na+nb;k++)
              {
                        int st;
                        int j;
                        ++e;
                        if(t[k].train == 0)
                        {
                                    if(t[k].station == 1)
                                        ++tfa;
                                    else
                                        ++tfb;
                                    t[k].train = e;            
                        
                                    j = k+1;
                                    time = t[k].stop +n;
                                    st = t[k].station;
                       
                                    while(j<na+nb)
                                    {
                                        if((t[j].start >= time)&&(t[j].station!=st)&&t[j].train==0)
                                            {
                                               time = t[j].stop +n;
                                               t[j].train = e;
                                               st = t[j].station;
                                            }
                                        ++j;
                                    }
                        }
                         
              }
                      

              
              free(t);                 
              fprintf(g,"Case #%d: %d %d \n",i+1,tfa,tfb);
          
    }
        
    fclose(f);
    fclose(g);
    

    return 0;
}
