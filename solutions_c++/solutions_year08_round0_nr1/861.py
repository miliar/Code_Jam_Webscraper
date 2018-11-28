#include <iostream>
#include <string>
#include <vector>

#define Inf (int)1e9

using namespace std;
vector<string> A,B;
int test,n,m;
string s;

int t[100][1000];
bool g[100][1000];
int fuck(int cur,int pos){
	if (pos>=m) return 0;
	if (t[cur][pos]<Inf) return t[cur][pos];
	if (g[cur][pos])	
	for (int i=0;i<n;i++)
		if (i!=cur){
			int top=1+fuck(i,pos+1);
			if (top<t[cur][pos]) t[cur][pos]=top;
		}
	if (!g[cur][pos]){
		int top=fuck(cur,pos+1);
		if (top<t[cur][pos]) t[cur][pos]=top;
	}
	return t[cur][pos];
}


int main(void){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%i\n",&test);
	for (int z=1;z<=test;z++){
		printf("Case #%i: ",z);
		A.clear();
		B.clear();
		scanf("%i\n",&n);
		for (int i=0;i<n;i++){
			getline(cin,s);
			A.push_back(s);
		}
		scanf("%i\n",&m);
		for (int i=0;i<m;i++){
			getline(cin,s);
			B.push_back(s);
		}
		int ans=Inf;
		for(int i=0;i<n;i++)
			for (int j=0;j<m;j++){
				t[i][j]=Inf;
				g[i][j]=(A[i]==B[j]);
			}
		for (int i=0;i<n;i++)
			ans=min(ans,fuck(i,0));
		printf("%i\n",ans);
	}

	return 0;
}
