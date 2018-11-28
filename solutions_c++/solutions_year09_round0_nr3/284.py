#include<iostream>
#include<string>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
const int maxn=502;
int f[maxn][maxn],i,j,n,ca,ti;
string s=" welcome to code jam",t;
int main(){
	freopen("c2.in","r",stdin);
	freopen("c2.out","w",stdout);
	cin>>ca;
	getline(cin,t);
	fr(ti,1,ca){
		getline(cin,t);
		n=t.size();
		t=" "+t;
		fr(i,0,19)
			fr(j,0,n)
				if(i>j)
					f[i][j]=0;
				else
					if(i==0&&j==0)
						f[i][j]=1;
					else{
						f[i][j]=f[i][j-1];
						if(i&&s[i]==t[j])
							f[i][j]=(f[i][j]+f[i-1][j-1])%10000;
					}
		printf("Case #%d: %04d\n",ti,f[19][n]);
	}
}
