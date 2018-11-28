#include <iostream>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

int mat[20][30];
int L,D,N;
char str[5100][20];
 
int suitable(int cnt) {
	for(int i = 0;i < L;++i) {
		if(!mat[i][str[cnt][i] - 'a']) {
			return 0;
		}
	}
	return 1;
}

int solve(char var[1000]) {
	int cnt = 0,len = strlen(var);
	memset(mat,0,sizeof(mat));
	bool mk = 0;
	for(int i = 0;i < len;++i) {
		if(var[i] == '(') {
			mk = 1;
			continue;
		}
		if(var[i] == ')') {
			mk = 0;
			cnt++;
			continue;
		}
		mat[cnt][var[i] - 'a'] = 1;
		if(!mk)cnt++;
	}
	int ans = 0;
	for(int i = 0;i < D;++i) {
		if(suitable(i))ans++;
	}
	return ans;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	while(cin>>L>>D>>N) {
		for(int i = 0;i < D;++i) {
			cin>>str[i];
		}
		int cas = 1;
		while(N--) {
			char temp[1000];
			cin>>temp;
			cout<<"Case #"<<cas++<<": "<<solve(temp)<<endl;
		}
	}
	return 0;
}
