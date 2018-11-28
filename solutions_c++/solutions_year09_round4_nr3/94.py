#include<iostream>
#include<fstream>
using namespace std;

int n,m,r=0,k;
bool map[101][101];
int match[101];
bool fw[101];
int val[101][101];

bool search(int x)
{
for(int i=1;i<=m;i++)
if(map[x][i] && !fw[i])
{
fw[i]=1;
int t=match[i];
match[i]=x;
if(t<0 || search(t))
return 1;
match[i]=t;
}
return 0;
}

bool able(int a,int b)
{
	for(int i=1;i<=k;i++)
		if(val[a][i] <= val[b][i])
			return false;
		return true;
}


int main()
{
	ifstream cin("C.in");
	ofstream cout("C.out");
int T;
	cin>>T;
	for(int c=1;c<=T;c++)
	{
cin>>n>>k;
m=n;
memset(map,0,sizeof(map));
r=0;
		
for(int i=1;i<=n;i++)
	for(int j=1;j<=k;j++)
		cin>>val[i][j];
for(int i=1;i<=n;i++)
	for(int j=1;j<=n;j++)	
		if(able(i,j))
			map[i][j]=1;
	

for(int i=1;i<=100;i++)
match[i]=-1;



for(int i=1;i<=n;i++)
{
memset(fw,0,sizeof(fw));
if(search(i))
r++;
}
cout<<"Case #"<<c<<": "<<n-r<<endl;
}
return 0;
}
