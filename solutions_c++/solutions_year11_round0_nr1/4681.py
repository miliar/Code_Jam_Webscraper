#include<iostream.h>
#include<conio.h>
int T,N,i,j,ans[100],front,rear,count,temp,pos[2];
char c;

struct str
{
       int col,val;
       }st[100];
int main()
{ 
    cin>>T;
    
    for(i=1;i<=T;i++)
    {   pos[0]=1;
pos[1]=1;
                     cin>>N;
                     for(j=0;j<N;j++)
                     {  cin>>c;
                         if(c=='B') st[j].col=1;
                         else st[j].col=0;   
                         cin>>st[j].val;            
                     }
       // cout<<"\n TOSOLVE ";
             //   for(j=0;j<N;j++)
             //   cout<<st[j].col<<" "<<st[j].val<<" ";
                 
    rear=0;
    count=0;
    temp=0;
       while(1)
        {
    front=rear;
    while(st[front].col==st[rear].col)
          {
    rear++;if(rear==N)
              break;
          }        
            while(front != rear )
            {
            temp=abs(st[front].val-pos[st[front].col]);
            temp++;
            count+=temp;   // cout<<"\n temp = "<<temp<<" ";getch();
            pos[st[front].col]= st[front].val;
            if(rear!=N)
           { if(abs(st[rear].val-pos[st[rear].col])<=temp)
            {  pos[st[rear].col]=st[rear].val;  
            }
            else { 
                 if(st[rear].val>pos[st[rear].col])
                 pos[st[rear].col]+=temp;
                 else pos[st[rear].col]-=temp;
                 }       
                 }            
            front++;
            }
       if(rear==N)
       break;
    
         }
    //cout<<"\n Storinng "<<count<<" \n";
    ans[i]=count;
    }
    for(i=1;i<=T;i++)
    { cout<<"Case #"<<i<<": "<<ans[i]<<"\n";
                     
                     }
    getch();
   return 0;
    }
