#include<iostream>
#include<algorithm>
using namespace std;
int num=0,n,m,sum=0,ou;
int a[200][200],b[200][200];
char c[200][200];
int f[200],g[200];
void dfs(int i , int j ) 
{
	b[i][j]=1;
//	c[i][j]=(char)('a'+num);
	int t=1<<28,ii,jj;
	f[sum]=i;g[sum]=j;sum++;
	if ( i-1>=0&&t>a[i-1][j]) {t=a[i-1][j];ii=i-1;jj=j;}
	if ( j-1>=0&&t>a[i][j-1]) {t=a[i][j-1];ii=i;jj=j-1;}
	if ( j+1<m&&t>a[i][j+1]) {t=a[i][j+1];ii=i;jj=j+1;}
	if ( i+1<n&&t>a[i+1][j]) {t=a[i+1][j];ii=i+1;jj=j;}	
	if ( t < a[i][j] ) 
	{
		if ( b[ii][jj] ) 
		{
			c[i][j]=c[ii][jj];ou=c[ii][jj]-'a';return;
		}
		dfs(ii,jj);//f[sum]=i;g[sum]=j;sum++;
	}
}
void set( int v ) 
{

	for ( int i =0 ; i < sum ; i ++ ) c[f[i]][g[i]]=(char)(v+'a');
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i , j , kk , ii; 
	cin>>kk;
	for ( ii = 1 ;ii <= kk ; ii ++ ) 
	{
		num=0;
		memset(b,0,sizeof b);
		cin>>n>>m;
		for ( i = 0 ;i < n ; i ++ ) 
			for ( j = 0 ; j < m ; j ++ ) cin>>a[i][j];
		for ( i = 0 ;i < n ;i ++ ) 
			for ( j = 0 ;j < m ;j ++) 
			{
				if ( b[i][j] ) continue; 
				ou=-1;
				sum=0;
				dfs(i,j);
				if ( ou==-1) {set(num);num++;}
				else set(ou);
				
			}
		cout<<"Case #"<<ii<<":"<<endl;
		for ( i = 0 ;i < n ;i ++ ) 
		{
			cout<<c[i][0];
			for ( j = 1 ;j < m ;j ++) cout<<' '<<c[i][j];cout<<endl;
		}
	}
	return 0;
}