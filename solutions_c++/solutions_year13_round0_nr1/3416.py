#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

char map[4][4];
int T;
bool label, hasT;

bool findans(char mark){
	bool issame;
	for (int i=0;i<=3;i++){
		issame=true;
		for (int j=0;j<=3;j++)
			if (map[i][j]!=mark) {issame=false;break;}
		if (issame) {cout<<mark<<" won"<<endl;return true;}
	}
	for (int j=0;j<=3;j++){
		issame=true;
		for (int i=0;i<=3;i++)
			if (map[i][j]!=mark) {issame=false;break;}
		if (issame) {cout<<mark<<" won"<<endl;return true;}
	}
	issame=true;
	for (int i=0;i<=3;i++)
		if (map[i][i]!=mark) {issame=false;break;}
	if (issame) {cout<<mark<<" won"<<endl;return true;}
	issame=true;
	for (int i=0;i<=3;i++)
		if (map[i][3-i]!=mark) {issame=false;break;}
	if (issame) {cout<<mark<<" won"<<endl;return true;}
	return false;
}

bool findpoint(void){
	for (int i=0;i<=3;i++)
		for (int j=0;j<=3;j++)
			if (map[i][j]=='.') {return true;}
	return false;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("std.out","w",stdout);
	cin>>T;
	for (int h=1;h<=T;h++){
		label=false;hasT=false;
		cout<<"Case #"<<h<<": ";
		for (int i=0;i<=3;i++)
			for (int j=0;j<=3;j++) cin>>map[i][j];
		for (int i=0;i<=3;i++)
			for (int j=0;j<=3;j++)
				if (map[i][j]=='T'){
					hasT=true;
					map[i][j]='X';label=findans('X');
					if (!label) {map[i][j]='O';label=findans('O');}
					if (!label){
						if (findpoint()) 
							{cout<<"Game has not completed"<<endl;}
						else
							{cout<<"Draw"<<endl;}
					}
				}
		if (!hasT){
			label=findans('X');
			if (!label) {label=findans('O');}
			if (!label) {
				if (findpoint()) 
					{cout<<"Game has not completed"<<endl;}
				else
					{cout<<"Draw"<<endl;}
			}
		}
	}
	return 0;
}
