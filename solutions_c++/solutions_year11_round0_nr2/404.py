#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;

char Ans[1005];
string Cc[100],Dd[100],Temp;

int main(){
	
	freopen("B_small.in","r",stdin);
	freopen("B_small.out","w",stdout);
	
	int C,D,N,T;
	int count=0;
	
	cin>>T;
	
	while(T--){
		cin>>C;
		int cnt=0;
		for(int t=1;t<=C;t++)
			cin>>Cc[t];
			
		cin>>D;
		for(int t=1;t<=D;t++)
			cin>>Dd[t];
			
		cin>>N;
		
		cin>>Temp;
		count++;
		//int len=Temp.size();
		for(int i=0;i<N;i++){
			Ans[++cnt]=Temp[i];
			
			if (cnt>1)
			for(int j=1;j<=C;j++){
				if((Ans[cnt]==Cc[j][0]&&Ans[cnt-1]==Cc[j][1])||(Ans[cnt]==Cc[j][1]&&Ans[cnt-1]==Cc[j][0])){
					Ans[cnt-1]=Cc[j][2];
					--cnt;
				}
			}
			for(int k=1;k<=D;k++){
				for(int h=1;h<cnt;h++){
					if((Ans[h]==Dd[k][0]&&Ans[cnt]==Dd[k][1])||(Ans[h]==Dd[k][1]&&Ans[cnt]==Dd[k][0]))
						cnt=0;
				}
			}
		}
		cout<<"Case #"<<count<<": [";
		for(int l=1;l<cnt;l++)
			cout<<Ans[l]<<", ";
		
		if (cnt) cout<<Ans[cnt];
		cout <<"]"<<endl;
		
	}
	return 0;
} 
