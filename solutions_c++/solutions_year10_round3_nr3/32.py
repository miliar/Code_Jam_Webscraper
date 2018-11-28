#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
using namespace std;
const int maxn=600;
const char vflag=9;
int n,m;
string str[maxn];
int Size[maxn];
int Numb[maxn];
int Cnt;

char bd[maxn][maxn];

char func(char ch,int mark)
{
	int val;
	if(ch<='9')val=ch-'0';
	else val=ch-'A'+10;
	return (mark&val)?1:0;
}

void disp()
{
	int i,j;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++)
			cout<<(int)bd[i][j];
		cout<<endl;
	}
	cout<<endl;
}

void trans()
{
	int i,j,k;
	memset(bd,0,sizeof(bd));
	for(i=0;i<n;i++){
		for(j=k=0;j<m/4;j++){
			bd[i][k++]=func(str[i][j],8);
			bd[i][k++]=func(str[i][j],4);
			bd[i][k++]=func(str[i][j],2);
			bd[i][k++]=func(str[i][j],1);
		}
	}
//	disp();
}

inline int find(const int &curx,const int &cury)
{
	int i,j,k,sz;
	for(sz=2;1;sz++){
		if(curx+sz>n || cury+sz>m)
			return sz-1;
		i=curx,j=cury+sz-1;
		if(bd[i][j]!=1-bd[i][j-1])
			return sz-1;
		for(k=curx+sz,i++;i<k;i++)
			if(bd[i][j]!=1-bd[i-1][j])
				return sz-1;
		for(i--,j--;j>=cury;j--)
			if(bd[i][j]!=1-bd[i][j+1])
				return sz-1;
	}
}

inline void color(const int &curx,const int &cury,const int &sz)
{
	int i,j;
	for(i=curx;i<curx+sz;i++)
		for(j=cury;j<cury+sz;j++)
			bd[i][j]=vflag;
}

void solve()
{
	trans();

	int i,j,k;
	int maxsize,x,y;
	for(Cnt=0;1;Cnt++){
		maxsize=0;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(bd[i][j]<=1){
					int sz=find(i,j);
					if(sz>maxsize){
						maxsize=sz;
						x=i;
						y=j;
					}
				}
		if(maxsize==0)break;

//		cout<<maxsize<<": "<<"("<<x<<","<<y<<")"<<endl;
		Size[Cnt]=maxsize;
		Numb[Cnt]=1;
		color(x,y,maxsize);

		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(bd[i][j]<=1){
					int sz=find(i,j);
					if(sz==maxsize){
						color(i,j,maxsize);
						Numb[Cnt]++;
					}
				}
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,ca,i;
	cin>>t;
	for(ca=1;ca<=t;ca++){
		cin>>n>>m;
		for(i=0;i<n;i++)
			cin>>str[i];
		solve();
		cout<<"Case #"<<ca<<": "<<Cnt<<endl;
		for(i=0;i<Cnt;i++)
			cout<<Size[i]<<" "<<Numb[i]<<endl;
//		cout<<endl;
	}
	return 0;
}