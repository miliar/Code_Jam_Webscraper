#include<stdio.h>
#include<conio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,n,p,po,pb;
    int dist,final,pro,prb;
    char r,prcol;
    int count=0;
    scanf("%d",&t);
    
    while(t>0)
    {
           count++;
           scanf("%d",&n);
           final=0;
           po=1;
           pb=1;
           prcol='\0';
           pro=0;
           prb=0;
           while(n>0)
           {
          /*  fflush(stdin);
            scanf("%c",&r);
            fflush(stdin);
            scanf("%d",&p); */
            cin>>r;
            cin>>p;
               
            if(r=='O')
            {
                      if(p>po)
                      dist=p-po+1;
                      else
                      dist=po-p+1;
                      
                      if(prcol!='B')
                      {
                                    final=final+dist; 
                      }
                
                      else
                      {
                                    if((pro+dist)>final)
                                    final=pro+dist;
                                    else
                                    {
                                        final=prb+1;
                                    }
                      }      
                      
            }
            if(r=='B')
            {
                      if(p>pb)
                      dist=p-pb+1;
                      else
                      dist=pb-p+1;
                      if(prcol!='O')
                      {
                                    final=final+dist;
                      }
                      else
                      {
                                    if((prb+dist)>final)
                                    final=prb+dist;
                                    else
                                    {
                                        final=pro+1;
                                    }
                      }
            }
            
            
            
            if(r=='O')
            { 
                      po=p;
                      pro=final;
                      prcol='O';
                      
            }
            else
            {
                      pb=p;
                      prb=final;
                      prcol='B';
            }
           
           n--;   
           }
                   
            printf("Case #%d: %d\n",count,final);  
    t--;          
    }
    
    getch();
 return 0;   
}
