#include<cstdio>
#include<iostream>
using namespace std;
int Ast,Aed,Bst,Bed;
bool win(int a,int b){
	if (a>b)
		return win(b,a);
	else if (a*2<=b)
		return 1;
	else
		return !win(a,b-a);
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++){
		cin>>Ast>>Aed>>Bst>>Bed;
		int ans=0;
		for (int i=Ast;i<=Aed;i++)
			for (int j=Bst;j<=Bed;j++)
				if (win(i,j))ans++;
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
