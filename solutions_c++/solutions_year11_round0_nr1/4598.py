#include<iostream>
//#include<conio.h>
#include<cmath>
using namespace std;
int main()
{
    int T,k=0,n,i,ar1[102],ar2[102],t;
    int z0=1,z1=1,y1=0,y2=0,q1,q2; 
    char ch[202],x;
    //freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    cin>>T;
    while(T)
    {
      cin>>n;
      k++;
      y1=0,y2=0,t=0;
      for(i=0;i<n;i++)
       {cin>>ch[i];
        if(ch[i]=='O')
         cin>>ar1[y1++];
        else
         cin>>ar2[y2++];
       }
     z0=1,z1=1,y1=0,y2=0;
    /*cout<<"\n";
     for(i=0;i<y1;i++)
      cout<<ar1[y1]<<" ";
     cout<<"\n";
     for(i=0;i<y2;i++)
      cout<<ar2[y2]<<" ";   
     cout<<"t="<<t<<"\n";  */
     for(i=0;i<n;i++)
     {
      if(ch[i]=='O')
       {
        t+=abs((ar1[y1]-z0))+1;
        
        q1=z1+abs((ar1[y1]-z0))+1;
        q2=z1-abs((ar1[y1]-z0))-1;
        int h=min(abs(q1-ar2[y2]),abs(q2-ar2[y2]));
       // cout<<"\nh="<<h;
        if(h==abs(q1-ar2[y2]))
        {
         z1+=abs((ar1[y1]-z0))+1;                     
           if(z1>ar2[y2])
              z1=ar2[y2];
         //cout<<"\nhere1z1="<<z1;     
        }      
        else
        { z1-=abs((ar1[y1]-z0))+1; 
           if(z1<ar2[y2])
              z1=ar2[y2];
          //cout<<"\nhere2z1="<<z1;     
        }    
        z0=ar1[y1++];
       }
      else if(ch[i]=='B')
       {
        t+=abs((ar2[y2]-z1))+1;
        
        q1=z0+abs((ar2[y2]-z1))+1;
        q2=z0-abs((ar2[y2]-z1))-1;
        int h=min(abs(q1-ar1[y1]),abs(q2-ar1[y1]));
        if(h==abs(q1-ar1[y1]))
        {
         z0+=abs((ar2[y2]-z1))+1;                     
           if(z0>ar1[y1])
              z0=ar1[y1];
        }      
        else
        { z0-=abs((ar2[y2]-z1))+1; 
           if(z0<ar1[y1])
              z0=ar1[y1];
        }    
        z1=ar2[y2++];
       }
      //cout<<"\n z0="<<z0<<" z1="<<z1<<" t="<<t;
       //getch(); 
     }
     cout<<"Case #"<<k<<": "<<t<<"\n";
     T--;
  }
  return 0;
}  
