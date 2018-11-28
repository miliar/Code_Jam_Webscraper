#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

string S[109];
int D[109],XO,TO,XB,TB,Tt;

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int N,T;
	
	
	cin>>T;
	int count=0;
	//for(int i=1;i<T;i++)
	while(T--){
		cin>>N;
		Tt=0;
		count++;
		XO=1,TO=0;
		XB=1,TB=0;
		
		for(int i=1;i<=N;i++){
			cin>>S[i];
			cin>>D[i];
			
			if(S[i]=="O"){
				Tt=max(abs(D[i]-XO)+TO,Tt)+1;
				XO=D[i];
				TO=Tt;
			}
			else if(S[i]=="B"){
				Tt=max(abs(D[i]-XB)+TB,Tt)+1;
				XB=D[i];
				TB=Tt;
			}
		}
		cout<<"Case #"<<count<<": "<<Tt<<endl;	
	}
	return 0;
}
