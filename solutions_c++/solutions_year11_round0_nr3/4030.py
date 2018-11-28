#include<iostream>
#include<stdio.h>


using namespace std;

void main(){
	freopen("input.txt","rb",stdin);
	freopen ("out.txt","w",stdout);
	
	int T;
	cin>>T;
	int u=T;
	while(u--){
		int n;
		unsigned __int64  N[100];
		cin>>n;
		for(unsigned __int64  i=0;i<n;i++)cin>>N[i];
		
		unsigned __int64  z=2<<(n-1);
		unsigned __int64 Max=0;
		for(int i=1;i<z-1;i++){
			unsigned __int64 k=i;
			unsigned __int64  X=0,A=0,Y=0;
			for(unsigned __int64  j=0;j<n;j++,k=k>>1){
				if(k%2==0)X^=N[j];
				else{
					Y^=N[j];
					A+=N[j];
				}
			}
			if(X==Y && A>Max)Max=A;
		}

		if(Max==0)printf("Case #%d: NO\n",T-u);
		else printf("Case #%d: %d\n",T-u,Max);
	}
}