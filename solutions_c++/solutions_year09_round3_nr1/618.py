#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

struct point{
	int i, j;
	point (int ii=0,int jj=0){
		i=ii;j=jj;
	}
};
char s[100];
int col[256];
int r[100];
__int64 res(int base){
	__int64 ret=0;
	for(int i=0;s[i];i++)
		ret=ret*base+r[i];
	return ret;
}
int main(){
	int t;
	freopen("A-large.in","r",stdin); freopen("A-large.out", "w", stdout);
	
	scanf("%d", &t);
	for(int x=1;x<=t;x++){
		scanf("%s", s);
		memset(col, -1, sizeof(col));
		int len=strlen(s);
		int num=0;
		col[s[0]]=1;
		for (int i=0;i<len;i++){
			if(col[s[i]]==-1)col[s[i]]=num++;
			if(num==1)num++;
		}
		for(int i=0;i<len;i++){
			r[i]=col[s[i]];
		}
		if(num<2) num=2;
		__int64 ret=res(num);
		printf("Case #%d: %I64d\n",x,ret);

	}
	return 0;
}