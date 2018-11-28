#include<iostream>
#include<string>
#include<fstream>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int dx[8]={-1,0,1,-1,1,-1,0,1};
int dy[8]={-1,-1,-1,0,0,1,1,1};

int getans(int x,int y,int k,int c,vector<string> rotate,int kk){
	int f=1;
	for(int i=0;i<kk;i++){
		//cerr<<k<<' '<<kk<<endl;
		//cerr<<x<<' '<<y<<endl;
		if(x<0 || x>=rotate.size())f=0;
		if(y<0 || y>=rotate.size())f=0;
		if(f==0)break;
		if(c==1 && rotate[x][y]!='R')f=0;
		if(c==0 && rotate[x][y]!='B')f=0;
		x+=dx[k];
		y+=dy[k];
	}
	return f;
}

int main(){
	int tn;cin>>tn;
	for(int ttn=1;ttn<=tn;ttn++){
		int n,m;cin>>n>>m;
		string s[n];
		for(int i=0;i<n;i++)cin>>s[i];
		vector<string> rotate(n);
		for(int i=0;i<n;i++){
			int cnt=0;
			for(int j=n-1;j>=0;j--){
				if(s[i][j]!='.'){
					rotate[i]+=s[i][j];
				}
				else{
					cnt++;
				}
			}
			for(int j=0;j<cnt;j++){
				rotate[i]+='.';
			}
			//cerr<<rotate[i]<<endl;
		}
		//for(int i=0;i<rotate.size();i++)cout<<rotate[i]<<endl;
		int b=0;
		int r=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				for(int k=0;k<8;k++){
					b|=getans(i,j,k,0,rotate,m);	
					r|=getans(i,j,k,1,rotate,m);	
				}
			}
		}
		cout<<"Case #"<<ttn<<": ";
		if(b && r)cout<<"Both"<<endl;
		if(b==0 && r==0)cout<<"Neither"<<endl;
		if(b==0 && r==1)cout<<"Red"<<endl;
		if(b==1 && r==0)cout<<"Blue"<<endl;
	}
	return 0;
}
