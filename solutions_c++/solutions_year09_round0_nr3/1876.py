#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

string s;
string w="welcome to code jam";
int r=0;

void findw(int i,int p){//текущая буква и текущая позиция
	int k=0;
	for (int j=i;j<s.size();j++){
		if (p==w.size()-1 && w[p]==s[j]) r=(r+1)%10000;
		if (w[p]==s[j]) findw(j,p+1);
	}
}


void getdata(){
	getline(cin,s);
}

int solve(){
	r=0;
	getdata();
	findw(0,0);
	return r;
}

void writedata(int r){
	if (r<10) printf("000%d\n",r); else 
	if (r<100) printf("00%d\n",r); else
	if (r<1000) printf("0%d\n",r); else
	if (r<10000) printf("%d\n",r);
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	for (int i=1;i<=t;i++){
		int r=solve();
		printf("Case #%d: ",i);
		writedata(r);
	}
	return 0;
}