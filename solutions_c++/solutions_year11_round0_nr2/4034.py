#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
 
 int k,test;
 cin>>test;
 
 for(k=1;k<=test;k++)
 {
 int N,pointer=-1,C,D,i,j;
 char T[3]={'0','0','0'};
 char B[2]={'0','0'};
 char F[10];
 cin>>C;
 if(C==1) cin>>T;
 //cout<<T[0]<<T[1]<<T[2]<<" ";

 cin>>D;
 if (D==1) cin>>B;
 //cout<<B[0]<<B[1]<<" ";

 cin>>N;
 
 char c;
 
 for(i=1;i<=N;i++)
 {
                  cin>>c;
		          //cout<<"c is :"<<c<<" ";
                  if(pointer==-1)
                  {
                                 F[++pointer]=c;
                                 }
                  else
                  {
                                 int check=0;
                                 if((F[pointer]==T[0] && c==T[1])) {F[pointer]=T[2];check=1;}
                                 else if((F[pointer]==T[1] && c==T[0])) {F[pointer]=T[2];check=1;}
                                 else if(c==B[1]) {
                                                  for(j=0;j<=pointer;j++)
                                                          if(F[j]==B[0]) {pointer=-1;check=1;break;}
                                                  }
                                 else if(c==B[0]) {
                                                  for(j=0;j<=pointer;j++)
                                                          if(F[j]==B[1]) {pointer=-1;check=1;break;}
                                                  }                
                                 if(check==0) {F[++pointer]=c;}
                  }
                 
                 
  }

	cout<<"Case #"<<k<<": ";
    cout<<"[";
    for(j=0;j<pointer;j++)
                  {cout<<F[j]<<", ";}
    if(pointer>=0)cout<<F[pointer];
    cout<<"]";
        
    cout<<"\n";
}
    return 0;
   
}

