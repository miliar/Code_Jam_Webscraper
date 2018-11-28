 #include <iostream>
 #include <vector>
 #include <algorithm>
 #include <stdio.h>
 
 //using namespace std;
 FILE *f,*g;
 int L, D, N;
 char a[5010][17];
 char b[300];
 int i,j,k,p,total,final,r,aaa,nr=0;
 int main() {
     f=fopen("date.in","r");
     g=fopen("date.out","w");
 fscanf(f,"%d %d %d",&L,&D,&N);
 
 for(i=0;i<D; i++)
   fscanf(f,"%s",&a[i]);
   
  
   
 for(i=0;i<N;i++)
    {fscanf(f,"%s",&b);
     r=0; // indicele in b
     final=0;
     
    for (k=0;k<D;k++) //parcurg dictionarul
        { r=0;
         for ( p=0;p<L;p++) //cuvantul din dictionar
             {aaa=0;
             
              if(b[r]!='(')  //e litera simpla
                   { if (a[k][p]==b[r]) {aaa=1; r++;} 
                   else p=L+1;                    
                   } 
              else   //e cu paranteza
                   {         
                   while (b[r]!=')' )
                      {
                       if (b[r]=='(' || aaa==1) r++;
                       else if (a[k][p]==b[r]) {aaa=1; r++;}
                       else r++;
                       }
                    r++;
                    if (aaa==0) p=L+1;
                    }
                }
           if(p==L) final++;  
          }  
         nr++;  
       fprintf (g,"Case #%d: %d\n",nr, final);           
     
    
    }
 
  
  
  return 0;
 }
