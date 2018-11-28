#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
using namespace std;
int t,h,w;
int a[102][102]; 
char b[102][102];
int c[5][2]={{0,0},{-1,0},{0,-1},{0,1},{1,0}};
int d[102][102];
struct node
{
       int x,y;
       struct node *next; 
}e[10000];
int num;
char we[26];
char ew[26];
struct node*head;
int f(int j,int k)
{
   // struct node *temp=head;
    struct node *temp=&e[num++];
    temp->x=j;
    temp->y=k;
    temp->next=head;
    head=temp;
}
int main()
{   
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
          scanf("%d%d",&h,&w);
          for(int j=1;j<=h;j++)
          for(int k=1;k<=w;k++)
          scanf("%d",&a[j][k]);
          
          for(int j=1;j<=w;j++)
          a[0][j]=a[h+1][j]=10000;
          for(int j=1;j<=h;j++)
          a[j][0]=a[j][w+1]=10000;
          
          memset(b,0,sizeof(b));
          char t='a';
          num=0;
          head=NULL;
          for(int j=1;j<=h;j++)
          for(int k=1;k<=w;k++)
          {
                  int p=0;
                  int q=a[j][k];
                  for(int o=1;o<=4;o++)
                  if(a[j+c[o][0]][k+c[o][1]]<q)
                  {     
                        //cout<<a[j+c[o][0]][k+c[o][1]]<<" "<<q<<endl; 
                        p=o;
                        q=a[j+c[o][0]][k+c[o][1]];                       
                  }
                  if(p==0)
                  {      
                         // cout<<"haihao "<<j<<" "<<k<<endl;
                          b[j][k]=t;
                          t++;
                  }
                  else
                  {      
                         d[j][k]=p;
                         f(j,k);
                  }
          }
          //cout<<d[h][w]<<endl;
         // cout<<num<<endl;
         // cout<<"hao"<<endl;
          while(head!=NULL)
          {
                           struct node *p=head;
                           struct node *q=NULL;
                           while(p!=NULL)
                           {             
                                         char temp1=b[p->x+c[d[p->x][p->y]][0]][p->y+c[d[p->x][p->y]][1]];
                                         if(temp1!=0)
                                         {        
                                                  //if(p->x==h&&p->y==w)
                                                  //cout<<(p->x)<<"  "<<(p->y)<<" "<<temp1<<endl;
                                                 // num--;
                                                 // if(num==1) cout<<(p->x)<<"  "<<(p->y)<<" "<<temp1<<endl;
                                                  b[p->x][p->y]=temp1;
                                                  if(q!=NULL)
                                                  {
                                                  q->next=p->next;
                                                  p=p->next;
                                                  }
                                                  else head=p=p->next;
                                                  
                                                 // break;
                                                  
                                         }
                                         else
                                         {
                                         q=p;
                                         p=p->next;
                                         }
                           }
          }
          printf("Case #%d:\n",i);
          t='a';
          memset(we,0,sizeof(we));
          for(int j=1;j<=h;j++)
          for(int k=1;k<=w;k++)
          {
          if(!we[b[j][k]-'a'])
          {
                we[b[j][k]-'a']=1;
                ew[b[j][k]-'a']=t;
                t++;             
          }
          b[j][k]=ew[b[j][k]-'a'];
          }  
         
          //cout<<b[h][w]<<endl;
          for(int j=1;j<=h;j++)
          {
          for(int k=1;k<w;k++)
          {
          putchar(b[j][k]);
          putchar(' ');
          }
          //putchar(b[j][w]);
        printf("%c\n",b[j][w]);
          }
          
    }
   // system("pause");
    return 0;
}
