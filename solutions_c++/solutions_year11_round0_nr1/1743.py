#include<iostream>
#include<cstdio>

using namespace std;

int o[101],b[101];
int x,t,n,opos,bpos,incB,incO,j,k,i,Time;
char c;

#define SIGN(x) (((x)<0)?(-1):(((x)>0)?(1):(0)))

main()
{
      
      scanf("%d",&t);
      int tc=1;
      while(t--){
         
         scanf("%d",&n);
         
         for(i=0;i<n;++i)
         {    //scanf("%c",&c);
              cin>>c;
              scanf("%d",&x);
              if(c=='O')
              {   o[i]=x; b[i]=-1;
              }
              else if(c=='B')
              {   o[i]=-1; b[i]=x;
              }
              //else cout<<"ERROR";         
         }
         
         for(j=0;o[j]==-1 && j<n;++j);
         for(k=0;b[k]==-1 && k<n;++k);
         
        // cout<<j<<"\t"<<k<<"\n";
         
         Time=0;
         opos=1; bpos=1;
         
         for(i=0;i<n;++i)
         {    if(i==j)
              {   //cout<<"in J : ";
                  incO=SIGN(o[j]-opos);
                  incB=SIGN(b[k]-bpos);
                  while(opos!=o[j]) 
                  {   opos+=incO; 
                      if(bpos!=b[k]) bpos+=incB;
                      Time++; 
                  }
                  
                  if(bpos!=b[k]) bpos+=incB;
                  for(j++;o[j]==-1 && j<n;++j);
                  Time++;
              }
              else if(i==k)
              {   //cout<<"in I : ";
                  incO=SIGN(o[j]-opos);
                  incB=SIGN(b[k]-bpos);
                  while(bpos!=b[k]) 
                  {   if(opos!=o[j]) opos+=incO; 
                      bpos+=incB;
                      Time++; 
                  }
                  
                  if(opos!=o[j]) opos+=incO;
                  for(k++;b[k]==-1 && k<n;++k);
                  Time++;
              }
              //cout<<"(i,j,k) : "<<"("<<i<<","<<j<<","<<k<<")\t";
            //  cout<<"Time : "<<Time<<"\n";
         }
         
         cout<<"Case #"<<tc<<": "<<Time<<"\n";
         tc++;
      }
}
