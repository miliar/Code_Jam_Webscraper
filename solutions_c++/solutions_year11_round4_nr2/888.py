#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#define eps 1e-4

using namespace std;

struct wtf{
	long long mass;
	double x,y;
	wtf operator+(wtf &a){
		wtf res;
		res.x=x+(a.x-x)*a.mass/(mass+a.mass);
		res.y=y+(a.y-y)*a.mass/(mass+a.mass);
		res.mass=mass+a.mass;
		return res;
	}
	wtf operator-(wtf &a){
		wtf res;
		res.x=x+(x-a.x)*(a.mass)/(mass-a.mass);
		res.y=y+(y-a.y)*(a.mass)/(mass-a.mass);
		res.mass=mass-a.mass;
		return res;
	}
	wtf(wtf &w){
		mass=w.mass;
		x=w.x;
		y=w.y;
	}
	wtf(){
	}
	wtf(double i,double j,int m){
		x=i;
		y=j;
		mass=m;
	}
};


wtf a[501][501];
wtf b[501][501];
char s[501];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int Q;
	scanf("%d",&Q);

	for(int test=1;test<=Q;test++){
		int n,m,d;
		scanf("%d%d%d",&n,&m,&d);
		gets(s);
		for(int i=0;i<n;i++){
			gets(s);
			for(int j=0;j<m;j++)
				a[i][j]=wtf(i+.5,j+.5,d+s[j]-'0');
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				b[i][j]=a[i][j];
				if(i)b[i][j]=b[i][j]+b[i-1][j];
				if(j)b[i][j]=b[i][j]+b[i][j-1];
				if(i && j)b[i][j]=b[i][j]-b[i-1][j-1];
			}
		}
		int maxk=min(m,n);
		int ck=2;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				for(int k=ck+1;k<=n;k++){
					if(i+k>n || j+k>m)continue;
					else{
						wtf w=b[i+k-1][j+k-1];
						if(i)w=w-b[i-1][j+k-1];
						if(j)w=w-b[i+k-1][j-1];
						if(i && j)w=w+b[i-1][j-1];
						w=w-a[i][j];
						w=w-a[i+k-1][j];
						w=w-a[i][j+k-1];
						w=w-a[i+k-1][j+k-1];
						if(fabs(w.x-i-.5*k)<eps && fabs(w.y-j-.5*k)<eps)ck=k;
					}
				}
		if(ck!=2)printf("Case #%d: %d\n",test,ck);
		else printf("Case #%d: IMPOSSIBLE\n",test);
	}
	return 0;
}
