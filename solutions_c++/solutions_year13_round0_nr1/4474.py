#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int row[4], col[4], diag[2];
	int T;
	char ch;
	bool done, more;
	cin>>T;
	for(int t=0; t<T; ++t){
		cout<<"Case #"<<t+1<<": ";
		memset(row, 0, sizeof(row));
		memset(col, 0, sizeof(col));
		memset(diag, 0, sizeof(diag));
		done = more = false;
		for(int i=0; i<4; ++i){
			for(int j=0; j<4; ++j){
				cin>>ch;
				if(ch=='T')continue;
				if(ch=='.') more=true;
				if(row[i]>=0){
					if(!row[i]&&ch!='.') row[i]=ch;
					else if(row[i]!=ch) row[i]=-1;
				}
				if(col[j]>=0){
					if(!col[j]&&ch!='.') col[j]=ch;
					else if(col[j]!=ch) col[j]=-1;
				}
				if(i==j && diag[0]>=0){
					if(!diag[0]&&ch!='.') diag[0]=ch;
					else if(diag[0]!=ch) diag[0]=-1;
				}
				if(i+j==3 && diag[1]>=0){
					if(!diag[1]&&ch!='.') diag[1]=ch;
					else if(diag[1]!=ch) diag[1]=-1;
				}
			}
		}
		for(int i=0; i<4 && !done; ++i){
			if(row[i]!=-1){
				cout<<(char)row[i]<<" won"<<endl;
				done=true;
			}
			else if(col[i]!=-1){
				cout<<(char)col[i]<<" won"<<endl;
				done=true;
			}
		}
		for(int i=0; i<2&&!done; ++i){
			if(diag[i]!=-1){
				cout<<(char)diag[i]<<" won"<<endl;
				done=true;
			}
		}
		if(!done&&more) cout<<"Game has not completed"<<endl;
		else if(!done) cout<<"Draw"<<endl;
	}
	return 0;
}