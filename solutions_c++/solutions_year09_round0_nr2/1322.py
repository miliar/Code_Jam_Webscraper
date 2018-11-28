#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
char c;
int n,m;
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
char rex(vector<vector<int> >&a,vector<vector<char> >&names,int x,int y){
	if(names[x][y]!='?')
		return names[x][y];
	int i,xx,yy;
	int mix=x;
	int miy=y;
	int mi=a[x][y];
	for(i=0;i<4;i++){
		xx=x+dx[i];
		yy=y+dy[i];
		if(xx>=0 && xx<n && yy>=0 && yy<m){
			if(a[xx][yy]<mi){
				mix=xx;
				miy=yy;
				mi=a[xx][yy];
			}
		}
	}
	if(mi!=a[x][y]){
		names[x][y]=rex(a,names,mix,miy);
		return names[x][y];
	}
	
	names[x][y]=c;
	c++;
	/*if(c>'z')
		c='a';*/
	return names[x][y];
	
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int t;
	cin>>t;
	int iii;
	for(iii=0;iii<t;iii++){
		cin>>n>>m;
		vector<vector<int> >a(n,vector<int>(m));
		vector<vector<char> >names(n,vector<char>(m,'?'));
		c='a';
		int i1,i2;
		for(i1=0;i1<n;i1++)
			for(i2=0;i2<m;++i2)
				scanf("%d",&a[i1][i2]);

		for(i1=0;i1<n;++i1)
			for(i2=0;i2<m;++i2)
				if(names[i1][i2]=='?')
					rex(a,names,i1,i2);

		cout<<"Case #"<<iii+1<<":"<<endl;
		for(i1=0;i1<n;++i1){
			for(i2=0;i2<m;++i2)
				printf("%c ",names[i1][i2]);
			printf("\n");
		}
	}
	/*int i;
	cout<<100<<endl;
	for(i=0;i<100;i++){
		int i1,i2;
		cout<<100<<' '<<100<<endl;
		for(i1=0;i1<100;i1++){
			for(i2=0;i2<100;i2++)
				cout<<rand()%10000<<' ';
			cout<<endl;
		}
	}*/
	return 0;
}