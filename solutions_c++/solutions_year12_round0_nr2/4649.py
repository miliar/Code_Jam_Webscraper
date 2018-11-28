#include<iostream>

using namespace std;

int main()
{
    int n,s,p,t,d,r,count;
    
int x=1;
scanf("%d",&t);
//getchar();
while(t--)
{
cin>>n;
cin>>s;
cin>>p;

int a[n];

printf("Case #%d: ",x);
x++;
count=0;
int y=0;
for(int i=0;i<n;i++)
{      
        cin>>a[i];
        d=a[i]/3;
        r=a[i]%3;
        //cout<<"test"<<i<<"  "<<a[i];
        
        
        if(a[i]<=1)
        count++;
         if(r==1)
         {
         if((d+1)>=p)
         {//cout<<"x1";
         y++;
         }
         }
         else if(r==2)
         {
         if((d+1)>=p)
         {y++;
         //cout<<"y1";
         
         }
         else if(((d+2)>=p)&&s!=0)
         {//cout<<"y2";
         y++;
         s--;
         }
         }
         else if(a[i]>1&&r==0)
            {if(d>=p)
             {y++;
             //cout<<"z";
             }
             else
             {
             if((d+1)>=p&&s!=0)
              {//cout<<"z1";
                               y++;
              s--;
              }
              }
           }
           else if(a[i]<=1&&p<=1)
           {if(a[i]>=p)
               y++;
               }
}          
cout<<y;
cout<<"\n";
}         
return 0;
}
