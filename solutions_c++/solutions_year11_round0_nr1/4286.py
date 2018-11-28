#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
     int a[110][2]={0}; int order[110];int c[2]={1,1}; int count[110]={0}; int time; int t; int n; char ch; int x;
    cin>>t;
    for(int i=0; i<t;i++)
    {
           int k=0; int l=0; time=0;
           cin>>n;
           for(int j=0; j<n;j++)
           {
           
           cin>>ch;
           if(ch=='O')
           {           cin>>a[k][0]; k++; order[j]=0;}
           else if(ch=='B')           
           {      cin>>a[l][1]; l++; order[j]=1;}
           }// end of for j
          
                   
           
           int j=0; time=0; int flag0,flag1;  k=0;l=0; int ct=0;
           while(j<n)
           {
                     
                     flag0=0;flag1=0;
                     time++; ct++;
                     x=order[j];
                     if(x==0&&c[0]==a[k][0])
                     {   flag0=1;    j++; k++;}                  
                     else if(x==1&&c[1]==a[l][1])
                     {   flag1=1;    j++; l++;}
                     
                     if(c[0]>a[k][0]&&flag0==0)
                                     c[0]--;
                     else if(c[0]<a[k][0]&&flag0==0)
                                     c[0]++;
                                     
                     if(c[1]>a[l][1]&&flag1==0)
                                     c[1]--;
                     else if(c[1]<a[l][1]&&flag1==0)
                                     c[1]++;
                                     
                    
           }
           count[i]=time;
           time=0;
           
           for(int j=0;j<100;j++)
           {       a[j][0]=a[j][1]=0; }
           c[0]=c[1]=1;
           
    }//end of main for
    
  
           
          
    for(int i=0;i<t;i++)
            cout<<"Case #"<<i+1<<": "<<count[i]<<endl;
            
            getchar();
            getchar();
            getchar();
        
  
            
    return 0;
}
