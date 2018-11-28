#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <set>
using namespace std;

const int maxn=513;
int chess[maxn][maxn];
int r[maxn][maxn];
int c[maxn][maxn];
int s[maxn][maxn];
int row,col;
int ret[maxn];
int num[maxn][maxn];
bool flag[maxn][maxn];

struct data
{
	int r,c,size;
	bool operator < (const data& b) const
	{
		if(size!=b.size) return size>b.size;
		if(r!=b.r) return r<b.r;
		return c<b.c;
	}
};
set<data> st;

void input()
{
	int i,j,k,tmp;
	char str[maxn/4+1];
	memset(chess,0,sizeof(chess));
	scanf("%d%d",&row,&col);
	for(i=0;i<row;i++){
		scanf("%s",&str);
		for(j=0;j<col/4;j++){
			if(str[j]>='0'&&str[j]<='9') tmp=str[j]-'0';
			else tmp=str[j]-'A'+10;
			for(k=0;k<4;k++){
				chess[i+1][j*4+(3-k)+1]=((tmp&(1<<k))!=0);
			}
		}
	}
}

int lowbit(int x)
{
	return x&(x^(x-1));
}

void modify(int px,int py,int delt)
{
	int x=px, y;
	while(x<=row){
		y=py;
		while(y<=col){
			num[x][y]+=delt;
			y+=lowbit(y);
		}
		x+=lowbit(x);
	}
}

int query(int px,int py)
{
	int ret=0;
	int x=px, y;
	while(x>0){
		y=py;
		while(y>0){
			ret+=num[x][y];
			y-=lowbit(y);
		}
		x-=lowbit(x);
	}
	return ret;
}

void preproc()
{
	int i,j;
	memset(r,0,sizeof(r));
	memset(c,0,sizeof(c));
	memset(s,0,sizeof(s));
	for(i=1;i<=row;i++){
		r[i][1]=1;
		for(j=2;j<=col;j++){
			if(chess[i][j]!=chess[i][j-1]) r[i][j]=r[i][j-1]+1;
			else r[i][j]=1;
		}
	}
	for(i=1;i<=col;i++){
		for(j=1;j<=row;j++){
			if(chess[j][i]!=chess[j-1][i]) c[j][i]=c[j-1][i]+1;
			else c[j][i]=1;
		}
	}
	for(i=1;i<=row;i++){
		for(j=1;j<=col;j++){
			s[i][j]=1;
			if(i==1 || j==1) continue;
			if(chess[i][j]!=chess[i-1][j-1]) continue;
			s[i][j]=min(r[i][j],c[i][j]);
			s[i][j]=min(s[i][j],s[i-1][j-1]+1);
		}
	}
	st.clear();
	for(i=1;i<=row;i++){
		for(j=1;j<=col;j++){
			data d;
			d.r=i;
			d.c=j;
			d.size=s[i][j];
			st.insert(d);
		}
	}
	memset(num,0,sizeof(num));
	for(i=1;i<=row;i++){
		for(j=1;j<=col;j++){
			modify(i,j,1);
		}
	}
}

void setFlag(data d)
{
	int i,j;
	for(i=0;i<d.size;i++){
		for(j=0;j<d.size;j++){
			flag[d.r-i][d.c-j]=true;
			modify(d.r-i,d.c-j,-1);
		}
	}
}

int getNum(int x1,int y1,int x2,int y2)
{
	int ret=query(x2,y2);
	ret+=query(x1-1,y1-1);
	ret-=query(x2,y1-1);
	ret-=query(x1-1,y2);
	return ret;
}

bool check(data d)
{
	int ret=getNum(d.r-d.size+1,d.c-d.size+1,d.r,d.c);
	return ret==d.size*d.size;
}

data reset(data d)
{
	int left=1,right=d.size;
	int mid;
	while(left<right)
	{
		mid=(left+right+1)/2;
		data td=d;
		td.size=mid;
		if(check(td)){
			left=mid;
		}else{
			right=mid-1;
		}
	}
	data ret=d;
	ret.size=left;
	return ret;
}

void solve()
{
	preproc();
	memset(ret,0,sizeof(ret));
	memset(flag,0,sizeof(flag));
	while(!st.empty())
	{
		data d=*(st.begin());
		st.erase(st.begin());
		if(flag[d.r][d.c]==true) continue;
		if(check(d)==true){
			setFlag(d);
			ret[d.size]++;
		}else{
			d=reset(d);
			st.insert(d);
		}
	}
	int i,cot=0;
	for(i=maxn;i>0;i--){
		if(ret[i]>0) cot++;
	}
	printf("%d\n",cot);
	for(i=maxn;i>0;i--){
		if(ret[i]>0) printf("%d %d\n",i,ret[i]);
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		input();
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}