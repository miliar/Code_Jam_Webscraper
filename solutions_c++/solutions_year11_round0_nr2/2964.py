#include<iostream.h>
#include<stdio.h>
#include<fcntl.h>
int ccnt,dcnt,ncnt;
    int i,j,k,l,m,n;
    int t;
    int ptr;
    char comb[40][4],dest[40][3],inp[120];
    char out[120];
void chkcomb()
{
     int i,j;int tem;
     i=l-1;
     j=l-2;
     if(j>=0)
     {
      for(tem=0;tem<ccnt;tem++)
      {
       if((comb[tem][0]==out[i]&&comb[tem][1]==out[j])||(comb[tem][0]==out[j]&&comb[tem][1]==out[i]))                         
       {
       l--;                                                                                                                          
       out[l-1]=comb[tem][2];      
       break;                                                                                                              
       }                                                                                                                      
      }                         
     }       
}    
void chkdest()
{
     int i,j,k,m;
     for(j=0;j<l-1;j++)
     {
       for(i=0;i<dcnt;i++)
       if((dest[i][0]==out[j]&&dest[i][1]==out[l-1])||(dest[i][1]==out[j]&&dest[i][0]==out[l-1]))               
       l=0;
     }
}     
int main()
{
    cin>>t;
         freopen( "WIZ.txt", "w", stdout );
    for(i=0;i<t;i++)
    {
    ptr=l=0;              
    cin>>ccnt;
     for(j=0;j<ccnt;j++)
     cin>>comb[j];
    cin>>dcnt;
     for(j=0;j<dcnt;j++)
     cin>>dest[j];
    cin>>ncnt; 
    cin>>inp;
    while(ptr<ncnt)
    {
    out[l++]=inp[ptr++];
    chkcomb();
    chkdest();
    }
    cout<<"Case #"<<i+1<<": [";
    for(j=0;j<l;j++)
    {
    if(j!=0)
    cout<<" ";                
    cout<<out[j];
    if(j!=l-1)
    cout<<",";
    else
    cout<<"]";
    }
    if(l==0)
    cout<<"]";
    cout<<"\n";    
    }            
    return(0);
}
