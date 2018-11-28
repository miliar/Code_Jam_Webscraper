#include <iostream>
using namespace std;

const int MAX=100000;

int mini(int a,int b,int c){
int ans=a;
if(ans>b) ans=b;
if(ans>c) ans=c;
return ans;
}
int main(){

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int N;
	cin>>N;
	int cases;
	for(cases=1; cases <= N; ++ cases){
	
		int M;
		int V;
		cin>>M>>V;
		//int base;
		int G[5001][2];
		int C[10001];
		int i;
		int s[10001][2];
		for( i = 1 ; i <= (M-1)/2; ++i){
			cin>>G[i][0]>>G[i][1];
			s[i][0]=s[i][1]=MAX;
		}
		for( i =(M-1)/2+1 ; i <=M ; ++ i ){		
			cin>>C[i];
			s[i][C[i]]=0;
			s[i][1-C[i]]=MAX;
		}

		
		for(i=(M-1)/2;i>=1;--i){
			int L1=s[2*i][1];
			int L0=s[2*i][0];
			int R0=s[2*i+1][0];
			int R1=s[2*i+1][1];
			int tmp1,tmp0;
			//AND
			if(G[i][0]==1){
			
				//1
				tmp1=L1+R1;
				if(s[i][1]>tmp1)
					s[i][1]=tmp1;
				//0
				tmp0=mini(L1+R0,L0+R0,L0+R1);
					if(s[i][0]>tmp0)
					s[i][0]=tmp0;
			}
			//OR
			if(G[i][0]==0){
			
				//1
				tmp1=mini(L1+R0,L1+R1,L0+R1);
				if(s[i][1]>tmp1)
					s[i][1]=tmp1;
				//0
				tmp0=L0+R0;
					if(s[i][0]>tmp0)
					s[i][0]=tmp0;
			}

			//OR, change
			
			if(G[i][0]==0&&G[i][1]==1){
			
				//1
				tmp1=L1+R1+1;
				if(s[i][1]>tmp1)
					s[i][1]=tmp1;
				//0
				tmp0=mini(L1+R0,L0+R0,L0+R1)+1;
					if(s[i][0]>tmp0)
					s[i][0]=tmp0;
			}

			//AND, change
				if(G[i][0]==1&&G[i][1]==1){
			
				//1
				tmp1=mini(L1+R0,L1+R1,L0+R1)+1;
				if(s[i][1]>tmp1)
					s[i][1]=tmp1;
				//0
				tmp0=L0+R0+1;
					if(s[i][0]>tmp0)
					s[i][0]=tmp0;
			}


		
		}

		if(s[1][V]<MAX)
		cout<<"Case #"<<cases<<": "<<s[1][V]<<endl;
		else
		cout<<"Case #"<<cases<<": "<<"IMPOSSIBLE"<<endl;



	}
	return 0;
}