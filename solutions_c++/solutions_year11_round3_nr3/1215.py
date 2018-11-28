#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
using namespace std;
#define fo(A,S,D) for(int A=S;A<D;A++)

int hcf_function(int a,int b)
//int GCD(int a, int b) 
{ 
  if ( b == 0 )
    return a;
  return hcf_function ( b,a%b);
} 

int lcm_function(int m,int n)
{
	int lcm;
	lcm=m*n/hcf_function(m,n);
	return lcm;
}
int main(int argc, char **argv)
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T,array[100]={1,20,5,2},N,L,H;
	cin>>T;
	int f=1;
	fo(t,0,T){
		cin>>N>>L>>H;
		cout<<"Case #"<<t+1<<": ";
		fo(i,0,N)
			cin>>array[i];
		fo(i,L,H+1){
			f=0;
			fo(j,0,N){
				if(array[j]%i==0 || i%array[j]==0)
					f++;
			}
			if(f==N){
				f=-1;
				cout<<i<<endl;break;
			}
		}
		if(f!=-1) cout<<"NO\n";
		
/*		int lcm=array[0];
		for(int i=1;i<N;i++)
			lcm=lcm_function(lcm,array[i]);	
		//cout<<lcm;
		if(lcm<=H&&lcm>=L)
			cout<<lcm<<endl;
		else
			cout<<lcm<<"NO\n";*/
	}
	return 0;
}




