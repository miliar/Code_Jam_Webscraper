#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <cmath>
using namespace std;
char str[113];
int top=0;
char cmb[30][3];
int ccm;
char op[30][2];
int cop;

void provcmb(){
	if(top<2) return;
	for(int i=0; i<ccm; i++){
		if((str[top-1]==cmb[i][0] && str[top-2]==cmb[i][1]) || (str[top-2]==cmb[i][0] && str[top-1]==cmb[i][1])){
			top--;
			str[top-1]=cmb[i][2];
		}
	}
}

void dlop(){
	for(int j=0; j<cop; j++){
		//op[j][1]==str[top-1]
		for(int i=0; i<top-1; i++){
			if((str[i]==op[j][0] && op[j][1]==str[top-1]) || (str[top-1]==op[j][0] && op[j][1]==str[i])){
				top=0;
				return;
			}
		}
	}
}
void solve(){
	top=0;	
	cin>>ccm;
	for(int i=0; i<ccm; i++){
		for(int j=0; j<3; j++){
			cin>>cmb[i][j];
		}
	}
	cin>>cop;
	for(int i=0; i<cop; i++){
		for(int j=0; j<2; j++){
			cin>>op[i][j];
		}
	}
	int n;
	cin>>n;
	char ch;
	for(int i=0; i<n; i++){
		cin>>ch;
		str[top]=ch;
		top++;
		provcmb();
		dlop();
	}
	cout<<"[";
	for(int i=0; i<top; i++){
		if(i!=top-1){
			cout<<str[i]<<", ";
		}else{
			cout<<str[i];
		}
	}
	cout<<"]";
}
int  main(){
	int t;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin>>t;
	for(int i=0; i<t; i++){
		cout<<"Case #"<<i+1<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}