#include<iostream>
#include<string>
using namespace std;
string s,ss="welcome to code jam";
int bw[1000][50];
int dp( int i , int j )
{
	if ( bw[i][j]!=-1) return bw[i][j];
	if ( j >= ss.length() ) return 1;
	if ( i >= s.length() ) return 0;
	if ( s[i]==ss[j]) return bw[i][j]=(dp(i+1,j+1)+dp(i+1,j))%10000;
	if ( s[i]!=ss[j]) return bw[i][j]=dp(i+1,j);
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,n;
//	int a[5];
	cin>>n;
	getchar();
	char ch[10000];
	for ( i = 1; i <= n ;i ++ ) 
	{
//		a[0]=a[1]=a[2]=a[3]=0;
		memset(bw,-1,sizeof bw);
		gets(ch);
		s=ch;
	//	cout<<s<<endl<<ss<<endl;
		int num = dp(0,0);
		cout<<"Case #"<<i<<": ";
		cout<<num/1000<<(num%1000)/100<<(num%100)/10<<(num%10)<<endl;
	}
	return 0;
}