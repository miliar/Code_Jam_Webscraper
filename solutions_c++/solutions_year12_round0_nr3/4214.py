//
#include<stdio.h>
#include<fstream.h>
#include<conio.h>
char* strsh(char sip[10],int sh,int len)
{
      int i;
      char sop[10];
      sop[len]='\0';
      for(i=0;i<sh;i++)
      {
                       sop[i]=sip[len-sh+i];
      }
      for(i=sh;i<len;i++)
      {
                       sop[i]=sip[i-sh];
      }
      return sop;
}
int main()
{
     int t,i,j,k,len,T,A,B,cnt[50];
     char si[10],sj[10],shs[10];
     freopen("C-small-attempt0.in","r",stdin);
     freopen("Outputcs.out","w",stdout);
     scanf("%d",&T);
     for(t=0;t<T;t++)
     {
                     scanf("%d %d",&A,&B);
                     cnt[t]=0;
                     for(i=A;i<=B;i++)
                     {
                                      itoa(i,si,10);
                                      len=strlen(si);
                                      for(j=A;j<=B;j++)
                                      {
                                                       itoa(j,sj,10);
                                                       if(len!=strlen(sj) || i==j)
                                                       {
                                                                          continue;
                                                       }
                                                       for(k=1;k<len;k++)
                                                       {
                                                                         strcpy(shs,strsh(sj,k,len));
                                                                         //printf("%s %s %d\n",si,shs,strcmp(si,shs));
                                                                         if(strcmp(si,shs)==0)
                                                                         {
                                                                                                          cnt[t]++;
                                                                                                          break;
                                                                         }
                                                       }
                                      }
                     }
     }
     for(t=0;t<T;t++)
     {
                     printf("Case #%d: %d\n",t+1,cnt[t]/2);                                                                                                                                                                
     }
     getch();
}
