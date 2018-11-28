#include<iostream>
#include<cstdio>
using namespace std;
char a[4][4];
int x=0,o=0,d=0,d1=0;
int call()
{
	x=0;o=0;d=0;d1=0;
	for(int i=0;i<4;i++) scanf("%s",a[i]);
//	for(int i=0;i<4;i++) {for(int j=0;j<4;j++) cout<<a[i][j]<<" "; cout<<"\n";}
	for(int i=0;i<4;i++)
	{
		x=0;o=0;d=0;
		for(int j=0;j<4;j++)
		{
			x+=(a[i][j]=='X');
			o+=(a[i][j]=='O');
			d+=(a[i][j]=='.');
			cerr<<a[i][j]<<" ";
			cerr<<"x="<<x<<" ";
			cerr<<"o="<<o<<endl;
		}
		d1+=d;
		if(x==0&&d==0) {cout<<"O won"; return 0;}
		if(o==0&&d==0) {cout<<"X won"; return 0;}
		cerr<<"\n";
	}
	
	
	for(int j=0;j<4;j++)
	{
		x=0;o=0;d=0;
		for(int i=0;i<4;i++)
		{
			x+=(a[i][j]=='X');
			o+=(a[i][j]=='O');
			d+=(a[i][j]=='.');
			cerr<<a[i][j]<<" ";
			cerr<<"x="<<x<<" ";
			cerr<<"o="<<o<<endl;
		}
	if(x==0&&d==0) {cout<<"O won"; return 0;}
	if(o==0&&d==0) {cout<<"X won"; return 0;}
	}
	x=0;o=0;d=0;
	for(int i=0;i<4;i++)
	{
		x+=(a[i][i]=='X');
		o+=(a[i][i]=='O');
		d+=(a[i][i]=='.');
		cerr<<a[i][i]<<" ";
		cerr<<"x="<<x<<" ";
		cerr<<"o="<<o<<endl;
	}
	if(x==0&&d==0) {cout<<"O won"; return 0;}
	if(o==0&&d==0) {cout<<"X won"; return 0;}
	cerr<<endl;
	x=0;o=0;d=0;
	for(int i=0;i<4;i++)
	{
		x+=(a[i][3-i]=='X');
		o+=(a[i][3-i]=='O');
		d+=(a[i][3-i]=='.');
		cerr<<a[i][3-i]<<" ";
		cerr<<"x="<<x<<" ";
		cerr<<"o="<<o<<endl;
	}
	if(x==0&&d==0) {cout<<"O won"; return 0;}
	if(o==0&&d==0) {cout<<"X won"; return 0;}
	cerr<<endl;
	if(d1==0) cout<<"Draw";
	else cout<<"Game has not completed";
	return 0;
}

int main()
{
	int n;cin>>n;
	for(int i=0;i<n;i++)
	{
		cout<<"Case #"<<i+1<<": "; call();
		cout<<endl;
	}
	return 0;
}
