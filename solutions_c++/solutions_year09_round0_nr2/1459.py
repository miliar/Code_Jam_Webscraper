#include<iostream>
#include<map>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int t=1; t<=T; t++){
		int H, W;
		cin>>H>>W;
		int ht[H][W];
		int h[H][W];
		int cnt=1;
		for(int i=0; i<H; i++) for(int j=0; j<W; j++){
			cin>>ht[i][j];
			h[i][j]=cnt++;
		}
		for(int k=0; k<W+H+1; k++)
			for(int i=0; i<H; i++) for(int j=0; j<W; j++){
				int cur=ht[i][j];
				if(i>0 && cur>ht[i-1][j]){ cur=ht[i-1][j]; h[i][j]=h[i-1][j]; }
				if(j>0 && cur>ht[i][j-1]){ cur=ht[i][j-1]; h[i][j]=h[i][j-1]; }
				if(j<W-1 && cur>ht[i][j+1]){ cur=ht[i][j+1]; h[i][j]=h[i][j+1]; }
				if(i<H-1 && cur>ht[i+1][j]){ cur=ht[i+1][j]; h[i][j]=h[i+1][j]; }
		}
		map<int, char> m;
		char next='a';
		cout<<"Case #"<<t<<":"<<endl;
		for(int i=0; i<H; i++){
			for(int j=0; j<W; j++){
				if(m[h[i][j]]==0) m[h[i][j]]=next++;
				cout<<m[h[i][j]];
				//cout<<h[i][j];
				if(j<W-1) cout<<" ";
			}
			cout<<endl;
		}
	}
	return 0;
}
