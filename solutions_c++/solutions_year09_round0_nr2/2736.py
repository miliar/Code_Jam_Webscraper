#include <stdio.h>
#include<stdlib.h>
main()
{
      int alt[102][102];
      char bin[102][102];
      FILE *fi,*fo;
      fi=fopen("B-small-attempt2.in","r");
      fo=fopen("B-small-attempt2.out","w");
      int L,B,small[3],num=96,n;
      fscanf(fi,"%d",&n);
     for(int t =0;t<n;t++)
      {
      num=96;
      fscanf(fi,"%d",&L);
      fscanf(fi,"%d",&B);
      for(int a=1;a<=L;a++)
      {
              for (int b=1;b<=B;b++)
              {
                  fscanf(fi,"%d",&alt[a][b]);
                  bin[a][b]='\0';
                  
              }
      }
      for (int b=0;b<=B+1;b++)
      {
                  alt[0][b]=999999;
                  alt[L+1][b]=999999;
                  
      }
      for (int b=0;b<=L+1;b++)
      {
                  alt[b][0]=999999;
                  alt[b][B+1]=999999;
                  
      }
      
     //bin[1][1]='a';
      
      for(int a=1;a<=L;a++)
      {
              for (int b=1;b<=B;b++)
              {
                  small[0]=alt[a][b];
                  small[1]=a;
                  small[2]=b;
                  if(alt[a-1][b]<small[0])
                  {
                      small[0]=alt[a-1][b];
                      small[1]=a-1;
                      small[2]=b;
                  }
                  if(alt[a][b-1]<small[0])
                  {
                      small[0]=alt[a][b-1];
                      small[1]=a;
                      small[2]=b-1;
                  }
                  if(alt[a][b+1]<small[0])
                  {
                      small[0]=alt[a][b+1];
                      small[1]=a;
                      small[2]=b+1;
                  }
                  if(alt[a+1][b]<small[0])
                  {
                      small[0]=alt[a+1][b];
                      small[1]=a+1;
                      small[2]=b;
                  }
                  if(small[0]<alt[a][b])
                  {
                                        if(bin[a][b]=='\0')
                                        {
                                        if(bin[small[1]][small[2]] == '\0')
                                        {
                                             num=num+1;                      
                                             bin[small[1]][small[2]]=(char)(num);
                                             bin[a][b] =bin[small[1]][small[2]];
                                        }
                                        }
                                        if(bin[a][b]!='\0')
                                        {
                                        if(bin[small[1]][small[2]] == '\0')
                                        {
                                             bin[small[1]][small[2]]=bin[a][b];
                                             
                                        }
                                        }
                                        if(bin[a][b]=='\0')
                                        {
                                        if(bin[small[1]][small[2]] != '\0')
                                        {
                                            bin[a][b]= bin[small[1]][small[2]];
                                             
                                        }
                                        }
                                         if(bin[a][b]!='\0')
                                        {
                                        if(bin[small[1]][small[2]] != '\0')
                                        {
                                                                  // printf("##########\n");
                                           int x,y,z,sml,otr,aw;
                                           x=bin[a][b];
                                           y=bin[small[1]][small[2]];
                                           if(x<y)
                                           {
                                                  sml=x;
                                                  otr=y;
                                           }else
                                           {
                                                sml=y;
                                                otr=x;
                                                }
                                           
                                           if(x!=y)
                                           {
                                                  bin[small[1]][small[2]] = (char)sml;
                                                  bin[a][b]= (char)sml;
                                                  for(int p=1;p<=a;p++)
                                                  {
                                                  for(int q=1;q<=b;q++)
                                                      {
                                                        z=bin[p][q];
                                                        if(z==otr)
                                                        {
                                                                bin[p][q]=(char)sml;
                                                        }
                  
                                                       }
                                                   }
                                                   for(int w=otr ;w<=num;w++)
                                                   {
                                                   for(int p=1;p<=L;p++)
                                                  {
                                                  for(int q=1;q<=B;q++)
                                                      {
                                                        z=bin[p][q];
                                                        if(z==w)
                                                        {
                                                                aw=w-1;
                                                                bin[p][q]=(char)aw;
                                                        }
                  
                                                       }
                                                   }
                                                   }
                                                   num=num-1;
                                                  
                                                  }     
                                           
                                             
                                        }
                                        }
                                                                   
                                                                   
                                          
                  
                  }
                  if(small[0]==alt[a][b]&&bin[a][b]=='\0')
                  {
                    num=num+1;                      
                    bin[a][b]=(char)(num);   
                   }
              }
      }
      fprintf(fo,"Case #%d:\n",t+1);
      for(int a=1;a<=L;a++)
      {
              for (int b=1;b<=B;b++)
              {
                  fprintf(fo,"%c",bin[a][b]);
                  if(b!=B)
                  {
                          fprintf(fo," ");
                  }        
              }
             
                  {
                          fprintf(fo,"\n");
                  } 
      }
      }
      //scanf("%d",&L);
      
}

      
      
      
