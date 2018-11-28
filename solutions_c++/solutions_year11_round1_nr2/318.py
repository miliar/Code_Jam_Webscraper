#include<iostream>
#include<string>
using namespace std;

typedef long long int64;


string D[1005],L[1005];

int N,M;
bool can[1005];
bool had[22];
int sum[30];

void minus(string s){
	for(int i=0;i<s.length();i++) sum[ s[i]-'a' ]--;
}

void elimnate(string s,char ch,bool hou){ //pos cannot be ch
	for(int i=1;i<=N;i++){
		if( can[i]==false ) continue;
		bool _can=true;
		for(int j=0;j<s.length();j++){

			if( had[j]==false && D[i][j]==ch ){
				can[i]=false;
				minus(D[i]);
				break;
			}

			if( had[j]==true && D[i][j]!=s[j] ) {
				can[i]=false;
				minus(D[i]);
				break;
			}
		}
	}
}

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);

	int Te=1,cas; cin>>cas;
	while( cas-- ){
		
		cin>>N>>M;
		for(int i=1;i<=N;i++) cin>>D[i];
		for(int i=1;i<=M;i++) cin>>L[i];

		printf("Case #%d:",Te++);
		for(int i=1;i<=M;i++){
			int lose=-1; string ans="";

			for(int j=1;j<=N;j++){
				int _lose=0;

				memset(can,true,sizeof(can));
				memset(had,false,sizeof(had));
				memset(sum,0,sizeof(sum));
				
				for(int k=1;k<=N;k++){
					if( D[k].length() != D[j].length() ) {
						can[k]=false; continue;
					}
					for(int p=0;p<D[k].length();p++)
						sum[ D[k][p]-'a' ]++;
				}

				for(int w=0;w<L[i].length();w++){
					if( sum[L[i][w]-'a' ]==0 ) continue;
					bool add=true;
					for(int p=0;p<D[j].length();p++){
						if( D[j][p] == L[i][w] ){
							add=false;
							had[p]=true;
						}
					}
					_lose+=add;

					elimnate(D[j],L[i][w],add);
				}
				//cout<<_lose<<' '<<D[j]<<endl;

				if( _lose > lose ){
					lose=_lose;
					ans=D[j];
				}
			}
			cout<<' '<<ans;
		}
		cout<<endl;
	}
}