#include <string.h>
#include<iostream>
#define lowbit(x) ((x)&((x)^((x)-1)))
#define MAXN 100
typedef int elem_t;
using namespace std;

struct sum{  //维护和查询复杂度均为O(logm*logn),数组内容保存在sum.a[][]中
	elem_t a[MAXN][MAXN],c[MAXN][MAXN],ret;
	int m,n,t;
	void init(int i,int j){memset(a,0,sizeof(a));memset(c,0,sizeof(c));m=i,n=j;}
	void update(int i,int j,elem_t v){  //a[i][j]修改为v,矩阵若有初值也这样一个个赋值
		for (v-=a[i][j],a[i++][j++]+=v,t=j;i<=m;i+=lowbit(i))
			for (j=t;j<=n;c[i-1][j-1]+=v,j+=lowbit(j));
	}
	elem_t query(int i,int j){  //求sum{a[0..i-1][0..j-1]}
		for (ret=0,t=j;i;i^=lowbit(i))
			for (j=t;j;ret+=c[i-1][j-1],j^=lowbit(j));
		return ret;
	}
};
int main()
{
	int x;
	while(cin>>x)
	{
		cout<<lowbit(x)<<endl;
	}
}
	