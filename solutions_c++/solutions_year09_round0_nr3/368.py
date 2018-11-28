#include<all>
string codejam="welcome to code jam";
int g[1000][100];
int search(string a, string b){
	memset(g,0,sizeof g);
	for(int i=0; i<(int)a.size(); i++){
		for(int j=0; j<(int)b.size(); j++){
			if(a[i]==b[j]){
				if(i&&j)
					g[i][j]+=g[i-1][j-1];
				if(j==0)
					g[i][j]+=1;
			}
			if(i)
				g[i][j]+=g[i-1][j];
			g[i][j]%=10000;
		}
	}
	return g[a.size()-1][b.size()-1];
}
int main(){
	int rr;
	cin >> rr;
	string s;
	getline(cin,s);
	for(int kase=1; kase<=rr; kase++){
		getline(cin,s);
		printf("Case #%d: %04d\n", kase,search(s,codejam));
	}
}

