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
 char F[100];

//int matchit(char c1,char c2,char p);
 int M[26][26]={0};

//int ratchit(char c1,char c2);
 int R[26][26]={0};
 
 cin>>C;
 for(i=1;i<=C;i++)
 {cin>>T;M[T[0]-65][T[1]-65]=T[2]-65;M[T[1]-65][T[0]-65]=T[2]-65;}
 

 cin>>D;
 for(i=1;i<=D;i++)
 {cin>>B;R[B[0]-65][B[1]-65]=1;R[B[1]-65][B[0]-65]=1;}

 /*for(i=0;i<26;i++)
	{
	for(j=0;j<26;j++)
	{
		cout<<M[i][j]<<" ";
	}
	cout<<"\n";
	}
*/
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
                                 if(M[F[pointer]-65][c-65]) {F[pointer]=M[F[pointer]-65][c-65] + 65; check=1;}
				else
				{
                                 for(j=0;j<=pointer;j++)
                                 if(R[F[j]-65][c-65]) {pointer=-1;check=1;break;}
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
