#include "stdio.h"
#include "iostream"
#include "string.h"
#include "math.h"
#include "string"
#include "vector"
#include "set"
#include "map"
#include "queue"
#include "list"
#include "stack"

using namespace std;

int n;
char matr[45][45];
int col[45];
void init()
{
	cin>>n;
	int i,j;
	for(i=0;i<n;i++){
		col[i]=0;
		for(j=0;j<n;j++){
			cin>>matr[i][j];
			if(matr[i][j]=='1')
				col[i]=j+1;
		}
	}
}
void change(int a,int b)
{
	int i;
	char t;
	for(i=0;i<n;i++){
		t=matr[a][i];
		matr[a][i]=matr[b][i];
		matr[b][i]=t;
	}
	t=col[a];
	col[a]=col[b];
	col[b]=t;
}

void solve()
{
	int i,j;
	int ans=0;
	for(i=0;i<n;i++){
		if(col[i]<=i+1) continue;
		for(j=i+1;j<n;j++){
			if(col[j]<=i+1) break;
		}
		for(;j>i;j--){
			change(j,j-1);
			ans++;
		}
	}
	cout<<ans<<endl;
}
int main()
{

	freopen("out.txt","w",stdout);
	int cs;
	cin>>cs;
	for(int ii=1;ii<=cs;ii++){
		cout<<"Case #"<<ii<<": ";
		init();
		solve();
	}
}