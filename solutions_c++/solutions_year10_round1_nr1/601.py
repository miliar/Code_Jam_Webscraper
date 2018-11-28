#include <iostream>
#include <cstdio>
#include <string>
#define MAX 59

using namespace std;
string str;
string vc[MAX],m[MAX];

class est{public:
	int iz,ab,di,di2;
	est(){}
	est(int a,int b,int c,int d){
		iz=a;
		di=b;
		ab=c;
		di2=d;
	}
};

est dp[MAX][MAX];
int busca(int y,int n){
	for(int i=n-1;i>=0;i--)
		if(vc[y][i]!='.')
			return i;
	return 0;
}
int N;
bool valido(int y,int x){
	return y>=0 and x>=0 and y<N and x<N;
}
void resuelva(){
	getline(cin,str);
	int n,k;
	sscanf(str.c_str(),"%d %d" ,&n,&k);
	N=n;
	//cout<<n<<" "<<k<<endl;
	for(int i=0;i<n;i++){
		getline(cin,vc[i]);
		m[i]=vc[i];
		for(int j=0;j<n;j++)
			m[i][j]='.';
		//cout<<vc[i]<<endl;
	}
	for(int i=0;i<n;i++){
		int y=busca(i,n);
		int k=0;
		//cout<<y<<endl;
		for(int j=y;j>=0;j--){
				m[k][n-i-1]=vc[i][j];
				if(vc[i][j]!='.')
					k++;
		}

	}
	//cout<<endl;
	//for(int i=0;i<n;i++)
	//	cout<<m[i]<<endl;

	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			dp[i][j]=est(1,1,1,1);
	bool winb=false,winr=false;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){

			if(m[i][j]=='.')
				continue;

			int y=i,x=j-1;//izquierda
			if(valido(y,x)){
				char c=m[i][j];
				if(m[y][x]==c){
					dp[i][j].iz=dp[y][x].iz+1;
				}else
					dp[i][j].iz=1;
				if(dp[i][j].iz>=k){
					if(c=='R')
						winr=true;
					else
						winb=true;
				}
			}
			y=i-1;x=j-1;//diagonal
			if(valido(y,x)){
				char c=m[i][j];
				if(m[y][x]==c){
					dp[i][j].di=dp[y][x].di+1;
				}else
					dp[i][j].di=1;
				if(dp[i][j].di>=k){
					if(c=='R')
						winr=true;
					else
						winb=true;
				}
			}
			y=i-1;x=j;
			if(valido(y,x)){
				char c=m[i][j];
				if(m[y][x]==c){
					dp[i][j].di2=dp[y][x].di2+1;
				}else
					dp[i][j].di2=1;
				if(dp[i][j].di2>=k){
					if(c=='R')
						winr=true;
					else
						winb=true;
				}
			}
			y=i-1;x=j+1;
			if(valido(y,x)){
				char c=m[i][j];
				if(m[y][x]==c){
					dp[i][j].ab=dp[y][x].ab+1;
				}else
					dp[i][j].ab=1;
				if(dp[i][j].ab>=k){
					if(c=='R')
						winr=true;
					else
						winb=true;
				}
			}
		}
	}
	if(winr and winb)
		printf("Both\n");
	else if(winr)
		printf("Red\n");
	else if(winb)
		printf("Blue\n");
	else
		printf("Neither\n");

}
int main(){
	int n;
	//scanf("%d",&n);
	getline(cin,str);
	sscanf(str.c_str(),"%d",&n);
	for(int i=1;i<=n;i++){
		printf("Case #%d: ",i);
		resuelva();
	}
}
