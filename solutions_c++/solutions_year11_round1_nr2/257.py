#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int n,m,lose,Test,small;
string dic[20000],s,ans,a;
bool canUsed[20000];
bool wrong[300];
bool display[300];

int calc(){
	int tp = 0,lose= 0,flag = 0;
		for (int i = 1;i<=n;++i) {
			canUsed[i] = (a.size() == dic[i].size()) ;
		}
	for (int i = 0;i<a.size();++i) display[i] = 0;
	
		
	while (tp<26){
		
		for (int i = 'a';i<='z';++i) wrong[i] = 1;
		
		for (int i = 1;i<=n;++i)
		if (canUsed[i]){
			for (int j = 0;j<dic[i].size();++j) 
				wrong[ dic[i][j] ] = 0;
		}
		
		while (tp<26 && wrong[ s[tp] ]) ++tp;
		if (tp == 26) return lose;
		flag = 0;
		for (int i = 0;i<a.size();++i){
			if (a[i] == s[tp]) display[i] = 1,++flag;
		}
		++tp;
		if (flag == 0) ++lose; else{
			for (int i = 1;i<=n;++i) 
			if (canUsed[i]){
				for (int j = 0;j<a.size();++j)
				if (display[j] && a[j]!=dic[i][j]) {
					canUsed[i] = 0;break;
				}
			}
		}
		
	}
	return lose;
}
void work(){
	cin >> n >> m;
	
	for (int i = 1;i<=n;++i) 
	cin >> dic[i];
	for (int i = 1;i<=m;++i){
		if (i>1) printf(" ");
		cin >> s;
	
		for (int k = 1;k<=n;++k){
			a = dic[k];
			lose = calc();
			//cout << a <<endl;
			//cout << lose << endl;
			if (k == 1 || lose>small) {
				small = lose;
				ans = a;
			}
		}
		//cout << small << endl;
		cout << ans ;
	}
	printf("\n");
}

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin >> Test;
	for (int ii = 1;ii<=Test;++ii){
		printf("Case #%d: ",ii);
		work();
	}
	return 0;
}
