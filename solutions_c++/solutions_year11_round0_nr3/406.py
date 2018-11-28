#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int Temp[1100];

int main(){
	
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int T,N,count=0,Ans,Res;
	cin>>T;
	while(T--){
		cin>>N;
		Ans=0;
		count++;
		Res=0;
		for(int i=1;i<=N;i++){
			cin>>Temp[i];
			Ans=Ans^Temp[i];
		}
		if(Ans!=0){
			cout<<"Case #"<<count<<": NO"<<endl;
		}else
		{
			sort(Temp+1,Temp+N+1);
			for(int k=2;k<=N;k++)
				Res+=Temp[k];
			cout<<"Case #"<<count<<": "<<Res<<endl;
		}
	}
	return 0;
}
