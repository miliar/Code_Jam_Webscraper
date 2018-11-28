#include <iostream>


using namespace std;
//int rem(int n,int d){return (n%d<0)?(n%d+d):n%d;};
int N;
long long X[100000];
long long Y[100000];
long long A,B,C,D,M;


int main(){
	int Ntc;
	cin>>Ntc;
	for(int tc=1;tc<=Ntc;tc++)
		{
       cin>>N;cin>>A;cin>>B;cin>>C;cin>>D;cin>>X[0];cin>>Y[0];cin>>M;
       long long x=X[0];long long y=Y[0];
       for(int i=1;i<N;i++)
           {
					X[i]=(A*x+B)%M;x=X[i];
               Y[i]=(C*y+D)%M;y=Y[i];
           }
       int res=0;
       for(int i=0;i<N-2;i++)
        for(int j=i+1;j<N-1;j++)
          for(int k=j+1;k<N;k++)
            {if((X[i]%3+X[j]%3+X[k]%3)%3==0 && 
                       (Y[i]%3+Y[j]%3+Y[k]%3)%3==0)res+=1;};
          cout<<"Case #"<<tc<<": "<<res<<"\n"; 
		}
}
