#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>



int main()
{

FILE * f, * g;
f=fopen("D-small-attempt4.in","r");
g=fopen("output.out","w");


int T,H,W,D,i,j,x,y,px,py,up,down,left,right,total;

char ch;

fscanf (f,"%d",&T);

for (i=1;i<=T;i++)
    {
    
    total=0;
    
    fscanf(f,"%d",&H); 
    fscanf(f,"%d",&W);
    fscanf(f,"%d",&D);
    
    
    int m[H][W];
    
        
    for (y=0;y<H;y++)
        {
        for (x=0;x<W;)
            {
            fscanf(f,"%c",&ch);
            if (ch=='#') {
                         m[y][x]=1;
                         x++;
                         }
            else if (ch=='.') {
                              m[y][x]=0;
                              x++;
                              }
            else if (ch=='X') {
                              
                              py=y;
                              px=x;
                              
                              m[y][x]=2;
                              x++;
                              }            
            }         
        }     
        
    
    
    up=(py-0)*2-1;
    down=(H-1-py)*2-1;
    
    left=(px-0)*2-1;
    right=(W-1-px)*2-1;    
    
    
    int sizey,sizex;
    
    
    sizey=(D/(up+down)+1)*2*2+1;
    sizex=(D/(left+right)+1)*2*2+1;
    
    int vy[sizey];
    int vx[sizex];
    
    vy[0]=-(D/(up+down)+1)*(up+down);
    vy[1]=vy[0]+up;
    
    j=2;
    while (j<sizey)
          {
          vy[j]=vy[j-2]+(up+down);
          vy[j+1]=vy[j-1]+(up+down);
          j=j+2;
          }

    
    vx[0]=-(D/(left+right)+1)*(left+right);
    vx[1]=vx[0]+right;
    
    j=2;
    while (j<sizex)
          {
          vx[j]=vx[j-2]+(left+right);
          vx[j+1]=vx[j-1]+(left+right);
          j=j+2;
          }
    
    
    /*
    printf("\n\n");
    
    for (j=0;j<sizey;j++)
        printf ("%d ",vy[j]);
        
    printf("\n\n");
        
    for (j=0;j<sizex;j++)
        printf ("%d ",vx[j]);
    
    printf("\n\n"); 
    */
    
    
    
     int catex=0,catey=0;
     double dist;
     
     double s[sizex*sizey][3],panta,xxx,yyy;
     int si=0,iii,pp;
    
     for (x=0;x<sizex;x++)
         {
         for (y=0;y<sizey;y++)
             {
                             
             
             dist=sqrt(vx[x]*vx[x]+vy[y]*vy[y]);
             if (dist<=D) 
                          {
                                               
                          
                          if (vx[x]!=0 && vy[y]!=0)
                                                   {
                                                   panta=1.*vx[x]/vy[y];
                                                   // printf("\n\nPANTA %f %d %d\n\n",panta,vx[x],vy[y]);  
                                                   
                                                   
                                                   pp=0;
                                                   
                                                   
                                                   
                                                   if (vx[x]<0 ) xxx=-1;
                                                   else xxx=1;
                                                   
                                                   if (vy[y]<0) yyy=-1;
                                                   else yyy=1;
                                                   
                                                   /*
                                                   xxx=vx[x]/abs(vx[x]);
                                                   yyy=vy[y]/abs(vy[y]);
                                                   */
                                                   
                                                   
                                                   for (iii=0;iii<si;iii++)     
                                                       {
                                                       if (s[iii][0]==panta) 
                                                                           {
                                                                           if (xxx==s[iii][1] && yyy==s[iii][2])
                                                                              {
                                                                              pp=1; 
                                                                              //printf("\n conflict %d/%d = %f     %f %f \n",vx[x],vy[y],s[iii][0],s[iii][1],s[iii][2]);
                                                                              break;
                                                                              }
                                                                           }                         
                                                       }
                                                       
                                                   if (pp==0)
                                                             {
                                                             s[si][0]=panta;
                                                             s[si][1]=xxx;
                                                             s[si][2]=yyy;
                                                             
                                                             si++;
                                                             }
                                                   }
                          if (vx[x]==0 && vy[y]!=0) catey++;
                          if (vy[y]==0 && vx[x]!=0) catex++;
                          
                          }
             }
         }
         
     //for (iii=0;iii<si;iii++) printf("%d ",s[iii][0]);
         
     //printf("\n catey %d  catex %d  si %d \n",catey,catex,si);
     
     
     if (catey>2) catey=2;
     if (catex>2) catex=2;
     
     total = si + catex + catey;
    
    /*
    for (y=0;y<H;y++)
        {
        for (x=0;x<W;x++)
            {
            printf("%d ",m[y][x]);         
            }         
        printf("\n");
        }  
        
    printf("\n\nD %d  tot %d \n\n",D,total);
     
    getch();
    */
    

    fprintf(g,"Case #%d: %d \n",i,total);
    }
    
return 0;
}




