#include<iostream>
#include<cstring>
using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		int p,q;
		cin>>p>>q;
		int s[102][102];
		int pos[102];
		memset(s,0,sizeof s);
		pos[0]=0;
		pos[q+1]=p+1;
		for(int j=1;j<=q;j++)
			cin>>pos[j];
		for(int j=1;j<=q;j++)
			s[j][j]=pos[j+1]-pos[j-1]-2;
		for(int j=2;j<=q;j++)
			for(int k=1;k<=q-j+1;k++){
				long min=s[k+1][k+j-1];
				for(int l=k;l<k+j;l++){
					long v=s[k][l-1]+s[l+1][k+j-1];
					if(v<min)min=v;
				}
				s[k][k+j-1]=min+pos[k+j]-pos[k-1]-2;
				//cerr<<k<<","<<k+j-1<<": "<<s[k][k+j-1]<<endl;
			}
		cout<<"Case #"<<i<<": "<<s[1][q]<<endl;
	}
	return 0;
}