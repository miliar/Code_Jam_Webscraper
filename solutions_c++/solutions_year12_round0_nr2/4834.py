#include<iostream>
using namespace std;
int num[300];
bool ans[300]={false};
 int n,s,p,arr[300];
 int put[300][2];
void recur(int i,int sumans,int pos)
{
     if(i==3)
     {
    // cout<<num[0]<<" "<<num[1]<<" "<<num[2]<<"\n";
    
    // system("pause");        
    
    
    if(abs(num[0]-num[1])>2  ||  abs(num[1]-num[2])> 2 || abs(num[0]-num[2])>2) 
    return ;
    if(abs(num[0]-num[1])==2  ||  abs(num[1]-num[2])== 2 || abs(num[0]-num[2])==2)
    if(s==0)
    return; 
    //bool diff=false;
    
    //diff=true;
    
    int sumans1=num[0]+num[1]+num[2];
    if(sumans1 !=sumans)
    return;
    
    
     
    
     
    
     int bestp=max(max(num[0],num[1]),num[2]);             
    //cout<<num[0]<<" "<<num[1]<<" "<<num[2]<<"\n";
     //system("pause");
    // put[pos][0]=true;         
     if(bestp >= p)
    { 
    //ans[k]=true;
    
     if((abs(num[0]-num[1])==2  ||  abs(num[1]-num[2])== 2 || abs(num[0]-num[2])==2) )
    put[pos][1]=true;
    else
    put[pos][0]=true;  
   // cout<<num[0]<<" "<<num[1]<<" "<<num[2]<<"\n";
     //system("pause");       
    
    }
   
     
     
     return ;
             
     }
     for(int j=0;j<=10;j++)
     {
     num[i]=j;
     recur(i+1,sumans,pos);        
     }
     
}


int main()
{
int t;
cin>>t;
int abc=1;
while(t--)
{
         
          cin>>n>>s>>p;
          int tot=0;
          for(int i=0;i<n;i++)
          {cin>>arr[i];
          
          recur(0,arr[i],i);
          }
          int surponly=0;
          
          //for(int i=0;i<n;i++)
          //cout<<put[i][0]<<"--"<<put[i][1]<<"\n";
          
          for(int i=0;i<n;i++)
          {if(put[i][0]==true)
          tot++;
          else if(put[i][1]==true)
          surponly++;
          }
          if(surponly<=s)
          tot=tot+surponly;
          else
          tot=tot+s;     
          cout<<"Case #"<<abc++<<": ";
          cout<<tot<<"\n";
          for(int i=0;i<n;i++)
          put[i][0]=put[i][1]=false;
          //system("pause");
          
          
          }    
    
}
