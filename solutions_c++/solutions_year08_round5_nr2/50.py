#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for (int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}

const int MX[]={-1,1,0,0};
const int MY[]={0,0,-1,1};

int sizeX,sizeY,destX,destY,srcX,srcY;
char A[20][20];
int size;
vector<int> Q[5000000];
set<vector<int> > M;

bool valid(int x,int y)
{
	return x>=0 && x<sizeX && y>=0 && y<sizeY && A[x][y]!='#';
}
void addnode(vector<int> &data)
{
	if (M.find(data)!=M.end()) return;
	M.insert(data);
	if (size==5000000)
	{
		printf("BAD\n");
		exit(0);
	}
	Q[size++]=data;
}
int solve()
{
	for (int cl=0,dst=0;cl<size;dst++)
	{
		for (int pos=cl;pos<size;pos++)
		{
			vector<int> data=Q[pos];
//			string s;
//			vtos(data,s);
//			cout<<s<<endl;
			if (data[0]==destX && data[1]==destY) return dst;
			for (int dir=0;dir<4;dir++)
			{
				int x=data[0],y=data[1];
				for (;valid(x+MX[dir],y+MY[dir]);x+=MX[dir],y+=MY[dir]);
				for (int p=2;p<8;p+=3)
				{
					vector<int> newdata=data;
					newdata[p]=x;
					newdata[p+1]=y;
					newdata[p+2]=dir;
					if (newdata[2]==newdata[5] && newdata[3]==newdata[6] && newdata[4]==newdata[7])
						continue;
					addnode(newdata);
				}
			}
		}
		int t_size=size;
		for (int pos=cl;pos<t_size;pos++)
		{
			vector<int> data=Q[pos];
			if (data[0]==destX && data[1]==destY) return dst;
			if (data[2]<0 || data[5]<0) continue;
			for (int dir=0;dir<4;dir++)
			{
				vector<int> newdata=data;
				int x=data[0],y=data[1];
				int x2=x+MX[dir],y2=y+MY[dir];
				if (x==newdata[2] && y==newdata[3] && dir==newdata[4]) x2=newdata[5],y2=newdata[6];
				else if (x==newdata[5] && y==newdata[6] && dir==newdata[7]) x2=newdata[2],y2=newdata[3];
				if (valid(x2,y2))
				{
					newdata[0]=x2;
					newdata[1]=y2;
					addnode(newdata);
				}
			}
		}
		cl=t_size;
	}
	return -1;
}
int main()
{
//	freopen("input.txt","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d%d",&sizeX,&sizeY);
		for (int i=0;i<sizeX;i++) scanf("%s",A[i]);
		for (int i=0;i<sizeX;i++) for (int j=0;j<sizeY;j++)
			if (A[i][j]=='O') srcX=i,srcY=j;
			else if (A[i][j]=='X') destX=i,destY=j;
		vector<int> data;
		data.push_back(srcX);
		data.push_back(srcY);
		for (int i=0;i<6;i++) data.push_back(-1);
		M.clear();
		size=0;
		addnode(data);
		int result=solve();
		if (result<0)
			printf("THE CAKE IS A LIE\n");
		else
			printf("%d\n",result);
		fflush(stdout);
	}
	return 0;
}

