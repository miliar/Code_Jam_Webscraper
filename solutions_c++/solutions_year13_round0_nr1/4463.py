#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char ma[10][10];
int T;
int cc=1;
string s[4];
bool check(int curr,char c){
	int tt=0;
	for(int i=0;i!=4;i++){
		if(ma[curr][i]==c || ma[curr][i]=='T'){
			tt++;
		}
	}
	if(tt==4)
		return true;
	tt=0;
	for(int i=0;i!=4;i++){
		if(ma[i][curr]==c || ma[i][curr]=='T'){
			tt++;
		}
	}
	if(tt==4)
		return true;
	if(curr==0){
		int t=0;
		for(int i=0;i!=4;i++){
			if(ma[i][i]==c || ma[i][i]=='T'){
				t++;
			}
		}
		if(t==4) return true;
	}
	if(curr==3){
		int t=0;
		for(int i=0;i!=4;i++){
			if(ma[i][4-i-1]==c || ma[i][4-i-1]=='T'){
				t++;
			}
		}
		if(t==4) return true;
	}
	return false;
}
int main(){
#ifdef LOCAL
	freopen("a.txt","r",stdin);
	freopen("a.out","w",stdout);
#endif
	s[0]="X won";
	s[1]="O won";
	s[2]="Game has not completed";
	s[3]="Draw";
	cin>>T;
	while(cc<=T){
		for(int i=0;i!=4;i++){
			scanf(" %s",ma[i]);
			//printf("%s\n",ma[i]);
		}
		bool ans[4];
		memset(ans,0,sizeof(ans));
		for(int i=0;i!=4;i++){
			if(check(i,'X'))
				ans[0]=true;
			if(check(i,'O'))
				ans[1]=true;
		}
		for(int i=0;i<4;i++){
			for (int j = 0; j < 4; j++) {
				//cout<<ma[i][j]<<endl;
				if(ma[i][j]=='.'){
					ans[2]=true;
					break;
				}
			}
		}
		if(!(ans[0]||ans[1]||ans[2]))
			ans[3]=true;
		for(int i=0;i!=4;i++){
			if(ans[i]){
				cout<<"Case #"<<cc++<<": "<<s[i]<<endl;
				break;
			}
		}
	}
}
