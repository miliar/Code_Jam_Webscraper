#include<iostream>
using namespace std;

int main(){
	int x;cin>>x;
	int cnt=0;
	while(cnt<x){
		cout<<"Case #"<<++cnt<<": ";
		string mp[4];
		for(int i=0;i<4;i++)cin>>mp[i];
		int num=0;
		if(mp[0][0]!='.'){
			for(int i=0;i<4;i++){
				if(mp[0][0]==mp[i][i]||mp[i][i]=='T')num++;
			}
			if(num==4){
				cout<<(mp[0][0]=='T'?mp[1][1]:mp[0][0])<<" won"<<endl;
				continue;
			}
		}
		num=0;
		if(mp[0][3]!='.'){
			for(int i=0;i<4;i++){
				if(mp[0][3]==mp[i][3-i]||mp[i][3-i]=='T')num++;
			}
			if(num==4){
				cout<<(mp[0][3]=='T'?mp[3][0]:mp[0][3])<<" won"<<endl;
				continue;
			}
		}
		for(int i=0;i<4;i++){
			int numw=0,numh=0;
			for(int j=0;j<4;j++){
				if(mp[i][0]!='.'&&(mp[i][0]==mp[i][j]||mp[i][j]=='T'))numw++;
				if(mp[0][i]!='.'&&(mp[0][i]==mp[j][i]||mp[j][i]=='T'))numh++;
			}
			if(numw==4){
				cout<<(mp[i][0]=='T'?mp[i][1]:mp[i][0])<<" won"<<endl;
				goto end;
			}
			if(numh==4){
				cout<<(mp[0][i]=='T'?mp[1][i]:mp[0][i])<<" won"<<endl;
				goto end;
			}
		}
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(mp[i][j]=='.'){
					cout<<"Game has not completed"<<endl;
					goto end;
				}
			}
		}
		cout<<"Draw"<<endl;
end:;
	}
}
