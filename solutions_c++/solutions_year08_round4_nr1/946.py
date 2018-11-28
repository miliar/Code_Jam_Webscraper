#include<iostream>
#include<vector>
using namespace std;

int main(){
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		int m,v;
		cin>>m>>v;
		vector<int> g(m+1),c(m+1),s(m+1),b(m+1);
		for(int j=1;j<=(m-1)/2;j++)
			cin>>g[j]>>c[j];
		for(int j=(m+1)/2;j<=m;j++)
			cin>>s[j];
		for(int j=(m+1)/2;j<=m;j++)
			b[j]=-1+(s[j]==v);
		for(int j=(m-1)/2;j>0;j--){
			int t=(s[j*2]==v)+(s[j*2+1]==v)+(g[j]!=v);
			if(t>1){
				s[j]=v;
				b[j]=0;
			}
			else{
				s[j]=!v;
				if(c[j]&&g[j]==v)
					if(t==1)
						b[j]=1;
					else if(s[j*2]!=v&&b[j*2]!=-1&&(s[j*2+1]==v||b[j*2+1]==-1||b[j*2]<b[j*2+1]))
						b[j]=b[j*2]+1;
					else if(s[j*2+1]!=v&&b[j*2+1]!=-1)
						b[j]=b[j*2+1]+1;
					else
						b[j]=-1;
				else if(t==0)
					if(b[j*2]==-1||b[j*2+1]==-1)
						b[j]=-1;
					else
						b[j]=b[j*2]+b[j*2+1];
				else if(s[j*2]!=v&&b[j*2]!=-1&&(s[j*2+1]==v||b[j*2+1]==-1||b[j*2]<b[j*2+1]))
					b[j]=b[j*2];
				else if(s[j*2+1]!=v)
					b[j]=b[j*2+1];
				else
					b[j]=-1;
			}
		}
		if(b[1]==-1)
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<i<<": "<<b[1]<<endl;
	}
	return 0;
}