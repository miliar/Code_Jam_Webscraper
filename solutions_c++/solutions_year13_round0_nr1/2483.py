#include<stdio.h>
int has(int a[17], int x,int s){
   int i=0;int f=0;
   for(;i<s;i++){
      if(a[i]==x) {f=1; break;}
      
   }
   return f;
}
void print(int x[],int s){
     int i;
     for(i=0;i<s;i++)     
                          printf("%d ",x[i]);
     printf("\n");
}
int main(){
    
    int t;
    scanf("%d",&t);
    int x[17];
    int o[17];
    char tp='t';
    int xc, oc,tc;
    int i=0,j=0,l=0;
    int so[10][4]={
                   {0,1,2,3},
                   {4,5,6,7},
                   {8,9,10,11},
                   {12,13,14,15},
                   
                   {0,4,8,12},
                   {1,5,9,13},
                   {2,6,10,14},
                   {3,7,11,15},
                   
                   {0,5,10,5},
                   {3,6,9,12}
                  };
    int cas=1;
    while(cas<=t){
               xc=0;oc=0,l=0;tc=0;
               scanf("%d",&tp);
               int mc=0;
           for(i=0;i<4;i++){    
               for(j=0;j<4;j++){
                    scanf("%c",&tp);
                    if(tp=='X') {

                                x[xc]=l;
                                l++;
                                xc++;
                                mc++;
                    }
                   else if(tp=='O'){
                                o[oc]=l;
                                l++;
                                oc++;
                                mc++;
                   }
                   else if(tp=='T'){
                               x[xc]=l;
                               o[oc]=l;
                               l++;
                               xc++;
                               oc++; 
              //                 tc++; 
                               mc++;   
                   }
                   else if(tp=='.') l++;
                }
                scanf("%c",&tp);
               }
               
               int xw=0;
               int ow=0;
               for(i=0;i<10;i++){
               
                            if(has(x,so[i][0],xc) && has(x,so[i][1],xc) && has(x,so[i][2],xc) && has(x,so[i][3],xc)){
                                xw=1;
                                break;
                            }
                            
               }
              
              if(xw){ printf("Case #%d: X won\n",cas);cas++;  continue;}
              for(i=0;i<10;i++){
               
                            if(has(o,so[i][0],oc) && has(o,so[i][1],oc) && has(o,so[i][2],oc) && has(o,so[i][3],oc)){
                                ow=1;
                                break;
                            }
                            
               }
              if(ow) { printf("Case #%d: O won\n",cas);}
              else  if(mc==16){
                      printf("Case #%d: Draw\n",cas);
              } else printf("Case #%d: Game has not completed\n",cas);
               
        cas++;                                     
    }
    
    return 0;
}
