#include<iostream>

using namespace std;

#define INF 0xffffff

int tree[20][20000],is_cng[20][20000],b0[20][20000],b1[20][20000];

int main(){
	int ncases; cin>>ncases;
	for(int icases=1;icases<=ncases;icases++){
		int M,V; cin>>M>>V;
		
		memset(tree,-1,sizeof(tree));
		memset(is_cng,-1,sizeof(is_cng));
		
		int depth;
		for(int i=0,m_cnt=0;m_cnt<M;i++){
			for(int j=0;j<(1<<i) && m_cnt<M;j++,m_cnt++){
				if((M-1)/2>m_cnt){
					cin>>tree[i][j]>>is_cng[i][j];
				}
				else{
					cin>>tree[i][j];
				}
			}
			depth=i;
		}
		/*
		for(int i=0,m_cnt=0;m_cnt<M;i++){
			for(int j=0;j<(1<<i) && m_cnt<M;j++,m_cnt++){
				cout<<tree[i][j]<<' ';
			}
			cout<<endl;
		}
		*/
		
		/*
		memset(b0,-1,sizeof(b0));
		memset(b1,-1,sizeof(b1));
		*/
		
		for(int i=0;i<20;i++){
			for(int j=0;j<10000;j++){
				b0[i][j]=b1[i][j]=INF;
			}
		}
		
		for(int i=depth;i>=0;i--){
			for(int j=0;j<(1<<i);j++){
				if(tree[i][j]==-1){
					continue;
				}
				if(is_cng[i][j]==-1){
					if(tree[i][j]==0){
						b0[i][j]=0;
					}
					else{
						b1[i][j]=0;
					}
					continue;
				}
				
				if(tree[i][j]==1 || (tree[i][j]==0 && is_cng[i][j]==1)){
					int cost=0;
					if(tree[i][j]==0 && is_cng[i][j]==1) cost=1;
					
					int a=b0[i+1][j*2]+b1[i+1][j*2+1];
					int b=b1[i+1][j*2]+b0[i+1][j*2+1];
					int c=b0[i+1][j*2]+b0[i+1][j*2+1];
					b0[i][j]=min(b0[i][j],min(a,min(b,c))+cost);
					b1[i][j]=min(b1[i][j],b1[i+1][j*2]+b1[i+1][j*2+1]+cost);
				}
				if(tree[i][j]==0 || (tree[i][j]==1 && is_cng[i][j]==1)){
					int cost=0;
					if(tree[i][j]==1 && is_cng[i][j]==1) cost=1;
					
					b0[i][j]=min(b0[i][j],b0[i+1][j*2]+b0[i+1][j*2+1]+cost);
					int a=b0[i+1][j*2]+b1[i+1][j*2+1];
					int b=b1[i+1][j*2]+b0[i+1][j*2+1];
					int c=b1[i+1][j*2]+b1[i+1][j*2+1];
					b1[i][j]=min(b1[i][j],min(a,min(b,c))+cost);
				}
			}
		}
		
		cout<<"Case #"<<icases<<": ";
		int ans;
		if(V==1){
			ans=b1[0][0];
		}
		if(V==0){
			ans=b0[0][0];
		}
		
		if(ans>=INF){
			cout<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<ans<<endl;
		}
	}
	
	return 0;
}
