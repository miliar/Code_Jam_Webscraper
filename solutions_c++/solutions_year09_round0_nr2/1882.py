#include<iostream>
#include<cstring>
using namespace std;

int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};

unsigned int s[102][102];
int rx[102][102],ry[102][102];

int main(){
	int t;
	cin>>t;
	for(int orz=1;orz<=t;orz++){
		int h,w;
		char l[102][102],cur;
		cur='a';
		memset(s,255,sizeof s);
		memset(l,0,sizeof l);
		cin>>h>>w;
		for(int i=1;i<=h;i++)
			for(int j=1;j<=w;j++)
				cin>>s[i][j];
		for(int i=1;i<=h;i++)
			for(int j=1;j<=w;j++){
				int tx=i,ty=j;
				for(int k=0;k<4;k++)
					if(s[tx][ty]>s[i+dx[k]][j+dy[k]]){
						rx[i][j]=tx=i+dx[k];
						ry[i][j]=ty=j+dy[k];
						
					}
				if(tx==i&&ty==j){
					rx[i][j]=i;
					ry[i][j]=j;
				}
			}
		cout<<"Case #"<<orz<<":"<<endl;
		for(int i=1;i<=h;i++)
			for(int j=1;j<=w;j++){
				int tx=i;
				int ty=j;
				while(rx[tx][ty]!=tx||ry[tx][ty]!=ty){
					int ttx=rx[tx][ty];
					ty=ry[tx][ty];
					tx=ttx;
				}
				int cx=i,cy=j;
				while(rx[cx][cy]!=cx||ry[cx][cy]!=cy){
					int ttx=rx[cx][cy];
					int tty=ry[cx][cy];
					rx[cx][cy]=tx;
					ry[cx][cy]=ty;
					cx=ttx;
					cy=tty;
				}
				if(l[tx][ty]=='\0')
					l[tx][ty]=cur++;
				cout<<l[tx][ty];
				if(j==w)
					cout<<endl;
				else
					cout<<" ";
			}

	}
	return 0;
}