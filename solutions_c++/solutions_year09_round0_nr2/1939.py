 #include <iostream>
 #include <vector>
 #include <algorithm>
 #include <stdio.h>
 FILE *f,*g;
 int T,H,W;
 int undei, undej;
 int a[110][110];
 char b[110][110];
 int vect[2][10010];
 int i,j,p,pozi,pozj,l,c;
 
 
 void unde(int x,int y) //se varsa in undei si undej
 { int min=a[x][y];
 undei=0;
 undej=0;
 if(a[x-1][y]<min) {undei=x-1;undej=y; min=a[undei][undej];}
 if(a[x][y-1]<min) {undei=x;undej=y-1; min=a[undei][undej];}
 if(a[x][y+1]<min) {undei=x;undej=y+1; min=a[undei][undej];}
 if(a[x+1][y]<min) {undei=x+1;undej=y; min=a[undei][undej];}    
 }
 
 
 
 void minim()
 {int min=10010;
  vect[0][0]=0;
  vect[1][0]=0;
  for(i=1;i<=H;i++)
                     for(j=1;j<=W;j++)
                                      if(a[i][j]<min&&b[i][j]==0)
                                      {
                                      min=a[i][j];
                                      vect[0][0]=i;
                                      vect[1][0]=j;
                                      }     
     }
     
     
 
 int main() 
 {
     f=fopen("B-small.in","r");
     g=fopen("date.out","w");
     T=0;
     fscanf(f,"%d",&T);
    
     
for (p=1;p<=T;p++)
    {
    fscanf(f,"%d %d",&H,&W);
    for(i=1;i<=H;i++)
                     for(j=1;j<=W;j++)
                                     { fscanf(f,"%d",&a[i][j]);
                                     b[i][j]=0;}
                                   
    for(i=0;i<=W+1;i++) {a[0][i]=10010; a[H+1][i]=10010; b[0][i]=2; b[H+1][i]=2;}
    for(i=0;i<=H+1;i++) {a[i][0]=10010; a[i][W+1]=10010; b[i][0]=2; b[i][W+1]=2;}
    
    
    int eok=1;
    char litera='a'-1;
    while(eok==1)
    {
    minim();
    if (vect[0][0]==0) eok=0;
    else
        {int poz=0;
         litera++;
         pozi=vect[0][0];
         pozj=vect[1][0];
         b[pozi][pozj]=litera;
         int final=0;
         while(poz<=final&&final<1000)
                     {//studiez elementul de pe pozitia poz  din coada
                     pozi=vect[0][poz];
                     pozj=vect[1][poz];
                     if(b[pozi][pozj-1]==0) {unde(pozi,pozj-1); //toate 4 sunt identice +-1
                                              if(undei==pozi&&undej==pozj) 
                                                                           {final++;
                                                                            b[pozi][pozj-1]=b[pozi][pozj];          
                                                                            vect[0][final]=pozi;
                                                                            vect[1][final]=pozj-1;                                                                            
                                                                           }
                                              }
                      if(b[pozi-1][pozj]==0) {unde(pozi-1,pozj);
                                              if(undei==pozi&&undej==pozj) 
                                                                           {final++;
                                                                            b[pozi-1][pozj]=b[pozi][pozj]   ;          
                                                                            vect[0][final]=pozi-1;
                                                                            vect[1][final]=pozj;                                                                            
                                                                           }
                                              } 
                      if(b[pozi+1][pozj]==0) {unde(pozi+1,pozj);
                                              if(undei==pozi&&undej==pozj) 
                                                                           {final++;
                                                                            b[pozi+1][pozj]=b[pozi][pozj]   ;          
                                                                            vect[0][final]=pozi+1;
                                                                            vect[1][final]=pozj;                                                                            
                                                                           }
                                              } 
                       if(b[pozi][pozj+1]==0) {unde(pozi,pozj+1);
                                              if(undei==pozi&&undej==pozj) 
                                                                           {final++;
                                                                            b[pozi][pozj+1]=b[pozi][pozj]   ;          
                                                                            vect[0][final]=pozi;
                                                                            vect[1][final]=pozj+1;
                                                                            }
                                                                                                                          }                                                  
                     poz++; //elimin elementul studiat;
                     }
    
        }
   }
    
    
    //schimbat culori!!
   char curent='a';
    for(i=1;i<=H;i++)
         for (j=1;j<=W;j++)
              {if(b[i][j]>curent)
                                { char litera2=b[i][j];
                                     for(l=1;l<=H;l++)
                                                   for (c=1;c<=W;c++)
                                                   {
                                                   if(b[l][c]==litera2) b[l][c]=curent;
                                                   else if(b[l][c]==curent) b[l][c]=litera2;
                                                   }
                                                   
                                curent++;
                                }
              
               if(b[i][j]==curent) curent++;
               }
    
  
    fprintf(g,"Case #%d:\n",p);
        for(i=1;i<=H;i++)
         {
         for (j=1;j<=W;j++)
               fprintf(g,"%c ",b[i][j]);
          fprintf(g,"\n");
          }              
             
   }
 
 
}
