#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
using namespace std;
int main(){
  long long l[3][3];
  long long N,n,A,B,C,D,x,y,M;
  int c=1;
  cin>>N;
  while(N--){
    cin>>n>>A>>B>>C>>D>>x>>y>>M;
    for(int i=0; i<3; i++)
      for(int j=0; j<3; j++)
	l[i][j]=0;
    l[x%3][y%3]=1;
    long long a=x,b=y;
    for(int i=1; i<n; i++){
      a=((A%M*a%M)%M+B%M)%M;
      b=((C%M*b%M)%M+D%M)%M;
      // cout<<a<<" "<<b<<endl;
      l[a%3][b%3]++;
    }
    /*
    for(int i=0; i<3; i++){
      for(int j=0; j<3; j++)
        cout<<l[i][j]<<" ";
      cout<<endl;
      }*/

    long long r=0;

    for(int i=0; i<3; i++){
      for(int j=0; j<3; j++){
	if(l[i][j]==3)
	  r++;
	if(l[i][j]>3)
	  r+=l[i][j]*(l[i][j]-1)*(l[i][j]-2)/6;
      }
    }
   long long z=0;
    for(int i=0; i<3; i++)
      for(int j=0; j<3; j++)
	for(int k=0; k<3; k++)
	  for(int s=0; s<3; s++)
	    for(int t=0; t<3; t++)
	      for(int m=0; m<3; m++)
		if(!(i==k&&j==s)&& !(i==t&&j==m)&& !(k==t&&s==m) 
		   && (i+k+t)%3==0 && (j+s+m)%3==0)
		  z+=l[i][j]*l[k][s]*l[t][m];
    r+=z/6;
    cout<<"Case #"<<c++<<": "<<r<<endl;
  }
  
}
