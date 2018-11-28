#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <bitset>
#include <string>
#include <algorithm>
using namespace std;
typedef long long LL;
const int maxn = 1005;

char c[maxn];
void translate()
{
	int i,l;
	l = strlen(c);
	for(i = 0;i < l;i ++)
	{
		if(c[i] == ' ') continue;
		switch(c[i])
		{
		case 'a':
			c[i] = 'y';
			break;
		case 'b':
			c[i] = 'h';
			break;
		case 'c':
			c[i] = 'e';
			break;
		case 'd':
			c[i] = 's';
			break;
		case 'e':
			c[i] = 'o';
			break;
		case 'f':
			c[i] = 'c';
			break;
		case 'g':
			c[i] = 'v';
			break;
		case 'h':
			c[i] = 'x';
			break;
		case 'i':
			c[i] = 'd';
			break;
		case 'j':
			c[i] = 'u';
			break;
		case 'k':
			c[i] = 'i';
			break;
		case 'l':
			c[i] = 'g';
			break;
		case 'm':
			c[i] = 'l';
			break;
		case 'n':
			c[i] = 'b';
			break;
		case 'o':
			c[i] = 'k';
			break;
		case 'p':
			c[i] = 'r';
			break;
		case 'q':
			c[i] = 'z';
			break;
		case 'r':
			c[i] = 't';
			break;
		case 's':
			c[i] = 'n';
			break;
		case 't':
			c[i] = 'w';
			break;
		case 'u':
			c[i] = 'j';
			break;
		case 'v':
			c[i] = 'p';
			break;
		case 'w':
			c[i] = 'f';
			break;
		case 'x':
			c[i] = 'm';
			break;
		case 'y':
			c[i] = 'a';
			break;
		case 'z':
			c[i] = 'q';
			break;
		}
	}
}
int main()
{
	int t,ncase = 0;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&t);
	gets(c);
	while(t --)
	{
		gets(c);
		translate();
		ncase ++;
		printf("Case #%d: %s\n",ncase,c);
	}
	return 0;
}
/*
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
#define __abs(x) (x)>0 ? (x):(-(x))
typedef long long LL;



LL A,B,a,b,c,d,x,y;

LL __extend_gcd(LL a,LL b,LL &x,LL & y)
{
	LL t,ret;
	if(b == 0)
	{
		x = 1;
		y = 0;
		return a;
	}
	ret = __extend_gcd(b,a%b,x,y);
	t = x; x = y; y = t - a/b*y;
	return ret;
}
int main()
{
	int t;
	LL dis,ans,tmp,maxd;
	scanf("%d",&t);
	while(t --)
	{
		scanf("%lld%lld%lld%lld",&A,&B,&a,&b);
		if(a > b)
			swap(a,b);
		dis = __abs(A-B);
		d = __extend_gcd(a,b,x,y);
		if(dis%d != 0)
			ans = -1;
		else
		{
			//a+b + b
			ans = -1;
			maxd = dis/(a+b);
			tmp = dis - (dis/(a+b))*(a+b);
			if(tmp%b == 0)
			{
				maxd += tmp/b;
				ans = maxd;
			}
			//a+b + a;
			maxd = dis/(a+b);
			tmp = dis - (dis/(a+b))*(a+b);
			if(tmp%a == 0)
			{
				maxd += tmp/a;
				if(ans == -1)
					ans = maxd;
				else
					ans = min(ans,maxd);
			}

			//a-b + a;
			maxd = (dis+a-1)/a;
			tmp = dis - (dis+a-1)/a*a;
			if(b != a && tmp%(b-a) == 0)
			{
				maxd += tmp/(b-a);
				if(ans == -1)
					ans = maxd;
				else
					ans = min(ans,maxd);
			}

			//b-a + b;
			maxd = (dis+a-1)/b;
			tmp = dis - (dis+a-1)/b*b;
			if(b != a && tmp%(b-a) == 0)
			{
				maxd += tmp/(b-a);
				if(ans == -1)
					ans = maxd;
				else
					ans = min(ans,maxd);
			}

		}
		printf("%lld\n",ans);
	}
	return 0;
}
/*
const int maxn = 100005;

int n;
struct Node{
	int h,pos;
};
Node mat[maxn];
bool comp(const Node & t1,const Node & t2)
{
	if(t1.h != t2.h)
		return t1.h > t2.h;
	return t1.pos < t2.pos;
}
int main()
{
	int t,ncase = 0,ans = 1,i;
	int h,pos;
	scanf("%d",&t);
	while(t --)
	{
		scanf("%d",&n);
		for(i = 0;i < n;i ++)
		{
			scanf("%d",&mat[i].h);
			mat[i].pos = i;
		}
		sort(mat,mat+n,comp);
		if(n >= 1) ans = 1;
		h = mat[0].h;
		pos = mat[0].pos;

		for(i = 1;i < n;i ++)
		{
			if(h > mat[i].h)
			{
				ans = max(ans,pos-mat[i].pos+1);
			}
			if(pos < mat[i].pos)
			{
				pos = mat[i].pos;
				h = mat[i].h;
			}
		}
		ncase ++;
		

		printf("Case %d: %d\n",ncase,ans);
	}
	return 0;
}
/*
#define inf 0.00000001
int flag;
typedef long long LL;
#define FF(i,A,s) for(int i = A[s];i != s;i = A[i])
const int maxm = 100400;
const int maxn = 206;
struct DLX{
	int R[maxm],L[maxm],U[maxm],D[maxm];
	int col[maxm],row[maxm];
	int s[maxn];bool hash[maxn]; //重复覆盖
	int pre,first,sz,NV,limit;
	void init(int n)  //列的数目
	{
		int i;
		for(i = 0;i <= n;i ++)
		{
			U[i] = i;D[i] = i;
			col[i] = i;   //
			L[i] = i-1,R[i] = i+1;
		}
		NV = n;sz = n+1;pre = -1;first = 0;
		memset(s,0,sizeof(s));
	}
	void insert(int i,int j)    //一行一行的插入数据i行j列
	{
		if(i != pre)  //pre表示前一行，如果不同，就更新前面那行的左右
		{
			R[sz-1] = first;L[first] = sz -1;
			pre = i;first = sz;
		}
		L[sz] = sz - 1;R[sz] = sz+1;  //可以将j列看做矩阵的最底部.
		D[U[j]] = sz;
		D[sz] = j;U[sz] = U[j];U[j] = sz;
		row[sz] = i,col[sz] = j,s[j] = 1;
		sz ++;
	}
	void finish() { R[sz-1] = first;L[first] = sz - 1;}
	void EXremove(int c){    //删除c列,而且与c有重复的行精确覆盖
		L[R[c]] = L[c];R[L[c]] = R[c];
		FF(i,D,c) FF(j,R,i) U[D[j]] = U[j],D[U[j]] = D[j],--s[col[j]];
	}
	void EXresume(int c){   //恢复c列,而且与c有重复的行
		FF(i,U,c) FF(j,L,i) ++s[col[j]],U[D[j]] = j,D[U[j]] = j;
		L[R[c]] = c;R[L[c]] = c;
	}
	//选择行，使每一列仅有一个
	bool dfs(const int &k) //精确覆盖，选择了k行了。
	{
		if(k >= flag) return false;
		if(R[0] == 0)
		{
			if(flag > k) flag = k;
			return true;
		}
		//if(R[0] == 0) return true; //找到解
		int idx = R[0],i;
		for(i = R[0] ;i != 0;i = R[i]) if(s[idx] > s[i]) idx = i;
		EXremove(col[idx]);
		FF(i,D,idx){
			FF(j,R,i) EXremove(col[j]);
			dfs(k+1);  //查找下一个。
			FF(j,L,i) EXresume(col[j]);
		}
		EXresume(col[idx]);
		return false;
	}
	//重复覆盖,选择最少行，所有的列被覆盖,后来添加的。
	void remove(int & c) { FF(i,D,c) L[R[i]] = L[i],R[L[i]] = R[i]; } //去掉某列
	void resume(int & c) { FF(i,U,c) L[R[i]] = i,R[L[i]] = i; }
	int h(){  //f启发函数
		int ret = 0;
		memset(hash,false,sizeof(hash));
		for(int c = R[0];c != 0;c = R[c]) if(!hash[c]){ //可以修改c !=  0部分
			hash[c] = true;  ret ++;
			FF(i,D,c)
				FF(j,R,i) hash[col[j]] = true;
		}
		return ret;
	}
	//重复覆盖，只删除列不删除行
	bool dfs(const int & k,int & limit)
	{
		if(k+h() >= limit) return false;
		if(R[0] == 0)
		{
			if(k < limit) limit = k; return true;
		}
		int idx = R[0],i;
		for(i = R[0] ;i != 0;i = R[i]) if(s[idx] > s[i]) idx = i;
		FF(i,D,idx){
			remove(i);
			FF(j,R,i) remove(j);
			if(dfs(k+1,limit)) return true;
			FF(j,L,i) resume(j);
			resume(i);
		}
		return false;
	}
	int astar()  //or 二分。
	{
		limit = h();
		while(!dfs(0,limit)) limit ++;  //修改点，limit最后期限
		return limit;
	}
};
struct Node{
	double x,y,r;
};
Node mat[maxn];

double dist(const Node & t1,const Node & t2)
{
	return sqrt((t1.x-t2.x)*(t1.x-t2.x)+(t1.y-t2.y)*(t1.y-t2.y));
}

int n;
DLX dlx;
int main()
{
	int i,j,ans;
	double r;
	
	while(scanf("%d",&n)!=EOF)
	{
		dlx.init(n);
		for(i = 0;i < n;i ++)
		{
			scanf("%lf%lf%lf",&mat[i].x,&mat[i].y,&mat[i].r);
		}
		for(i = 0;i < n;i ++)
		{
			for(j = 0;j < n;j ++)
			{
				r = dist(mat[i],mat[j]);
				if(r + inf <= mat[i].r)
				{
					dlx.insert(i+1,j+1);
				}
			}
		}
		dlx.finish();
		ans = dlx.astar();
		printf("%d\n",ans);
	}
	return 0;
}
/*
const int maxn = 1050;

int l;
char c[maxn],cc[50];
double Exception();
double Term();
double Factor();

/*
E = T | E + T | E - T
T = F | T * F | T / F
F = (E) | i


void __strrev(char *cc)
{
	char tmp;
	int i,l;
	for(i = 0,l = strlen(cc)-1;i < l;i ++,l --)
	{
		tmp = cc[i];
		cc[i] = cc[l];
		cc[l] = tmp;
	}
}
double Exception()
{
	double t = Term(),e;
	l --;
	if(c[l] == '+')
	{
		e = Exception();
		return t + e;
	}else if(c[l] == '-')
	{
		e = Exception();
		return e - t;
	}else{
		l ++;
		return t;
	}
}

double Term()
{
	double f = Factor(),t;
	l --;
	if(c[l] == '*')
	{
		t = Term();
		return t*f;
	}else if(c[l] == '/')
	{
		t = Term();
		return t/f;
	}else{
		l ++;
		return f;
	}
}

double Factor()
{
	int i;
	double f;
	l --;
	if((c[l] >= '0' && c[l] <= '9') || c[l] == '.')
	{
		i = 0;
		while((c[l] >= '0' && c[l] <= '9') || c[l] == '.')
			cc[i++] = c[l--];
		l ++;
		cc[i] = '\0';
		__strrev(cc);
		sscanf(cc,"%lf",&f);
		return f;
	}else if(c[l] == ')')
	{
		f = Exception();
		l --;
		return f;
	}
}
int main()
{
	int t;
	scanf("%d",&t);
	while(t --)
	{
		scanf("%s",c);
		l = strlen(c)-1;
		printf("%.2lf\n",Exception());
	}
	return 0;
}
/*
E = T|E+T|E-T
T = F|T*F|T/F
F = (E)|i
*/

/*
typedef long long LL;
#define INF 1000000000000LL
const int maxn = 200005;

LL a[maxn];
int n,k;
int heap[maxn],pre[maxn],next[maxn],link[maxn],len;

void swap(int  x,int  y)
{
	int tm;
	link[heap[x]] = y;
	link[heap[y]] = x;
	tm = heap[x];
	heap[x] = heap[y];
	heap[y] = tm;
}

void Up(int k)
{
	while(k != 1 && a[heap[k>>1]] > a[heap[k]])
	{
		swap((k>>1),k);
		k >>= 1;
	}
}

void Down(int k)
{
	int j;
	while(heap[k<<1] + heap[(k<<1)+1] != 0)
	{
		j = k << 1;
		if(heap[j] == 0) j ++;
		if(a[heap[(k<<1)+1]] < a[heap[j]] && heap[(k<<1)+1] != 0)
			j = (k << 1) + 1;
		if(a[heap[j]] < a[heap[k]])
			swap(k,j);
		else break;
		k = j;
	}
}

void Add(int x)
{
	len ++;
	heap[len] = x;
	link[x] = len;
	Up(len);
}

void Del(int x)
{
	x = link[x];
	link[heap[len]] = x;
	heap[x] = heap[len];
	Down(x);
	Up(x);
	heap[len] = 0;
	len --;
}

int main()
{
	LL ans;
	int i,j,t,pos;
	while(scanf("%d%d",&n,&k)!=EOF)
	{
		len = 0;
		for(i = 1;i <= n;i ++)
			scanf("%lld",&a[i]);
		sort(a+1,a+n+1);
		n --;
		for(i = 1;i <= n;i ++)
		{
			a[i] = a[i+1] - a[i];
			pre[i] = i-1;
			next[i] = i+1;
			Add(i);
		}
		ans = 0;
		for(i = 1;i <= k;i ++)
		{
			pos = heap[1];
			ans += a[pos];
			if(pre[pos] != 0 && next[pos] <= n)
			{
				Del(pre[pos]);
				Del(next[pos]);
				Del(pos);
				a[pos] = a[pre[pos]] + a[next[pos]] - a[pos];
				a[pre[pos]] = INF;
				a[next[pos]] = INF;
				Add(pos);
				pre[pos] = pre[pre[pos]];
				next[pre[pos]] = pos;
				next[pos] = next[next[pos]];
				pre[next[pos]] = pos;
			}else{
				Del(pos);
				if(pre[pos] == 0)
				{
					Del(next[pos]);
					pre[next[next[pos]]] = 0;
				}else if(next[pos] == n+1)
				{
					Del(pre[pos]);
					next[pre[pre[pos]]] = n+1;
				}
			}
		}		
		printf("%lld\n",ans);
		memset(heap,0,sizeof(heap));
	}
	return 0;
}


/*
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;
typedef __int64 LL;
#define INF 1000000000000
const int maxn = 100005;

LL a[maxn];
int n,k;
int heap[maxn],pre[maxn],next[maxn],link[maxn],len;

void swap(int & x,int & y)
{
	int tm;
	link[heap[x]] = y;
	link[heap[y]] = x;
	tm = heap[x];
	heap[x] = heap[y];
	heap[y] = heap[x];
}

void Up(int k)
{
	while(k != 1 && a[heap[k>>1]] > a[heap[k]])
	{
		swap(heap[k>>1],heap[k]);
		k >>= 1;
	}
}

void Down(int k)
{
	int j;
	while(heap[k<<1] + heap[(k<<1)+1] != 0)
	{
		j = k << 1;
		if(heap[j] == 0) j ++;
		if(a[heap[(k<<1)+1]] < a[heap[j]] && heap[(k<<1)+1] != 0)
			j = k << 1 + 1;
		if(a[heap[j]] < a[heap[k]])
			swap(k,j);
		else break;
		k = j;
	}
}

void Add(int x)
{
	len ++;
	heap[len] = x;
	link[x] = len;
	Up(x);
}

void Del(int x)
{
	x = link[x];
	link[heap[len]] = x;
	heap[x] = heap[len];
	Down(x);
	Up(x);
	heap[len] = 0;
	len --;
}

int main()
{
	LL ans;
	int i,j,t,pos;
	while(scanf("%d%d",&n,&k)!=EOF)
	{
		len = 0;
		for(i = 1;i <= n;i ++)
			scanf("%I64d",&a[i]);
		sort(a+1,a+n+1);
		n --;
		for(i = 1;i <= n;i ++)
		{
			a[i] = a[i+1] - a[i];
			pre[i] = i-1;
			next[i] = i+1;
			Add(i);
		}
		ans = 0;
		for(i = 1;i <= k;i ++)
		{
			pos = heap[1];
			ans += a[pos];
			if(pre[pos] != 0 && next[pos] <= n)
			{
				Del(pre[pos]);
				Del(next[pos]);
				Del(pos);
				a[pos] = a[pre[pos]] + a[next[pos]] - a[pos];
				a[pre[pos]] = INF;
				a[next[pos]] = INF;
				Add(pos);
				pre[pos] = pre[pre[pos]];
				next[pre[pos]] = pos;
				next[pos] = next[next[pos]];
				pre[next[pos]] = pos;
			}else{
				Del(pos);
				if(pre[pos] == 0)
				{
					Del(next[pos]);
					pre[next[next[pos]]] = 0;
				}else if(next[pos] == n)
				{
					Del(pre[pos]);
					next[pre[pre[pos]]] = n;
				}
			}
		}		
		printf("%I64d\n",ans);
	}
	return 0;
}
/*
typedef __int64 LL;
const int maxn = 355;

int num[maxn];
bool panduan(int n,int k)
{
	int len = 0,i,ans,t;
	while(n)
	{
		num[len] = n%k;
		n /= k;
		len ++;
	}
	ans = 0;
	for(i = 0;i < len;i ++)
	{
		ans ^= num[i];
	}
	for(i = t = 0;i < len;i ++)
	{
		if(num[i] > (ans^num[i]))
			t ++;
	}
	if(t) return true;
	return false;
}
int main()
{
	int n,k,t,tm;
	LL i;
	scanf("%d",&t);
	while(t --)
	{
		scanf("%d%d",&n,&k);
		if(k == 1 || n < k)
		{
			if(n&1) printf("1\n");
			else printf("0\n");
			continue;
		}
		if(panduan(n,k))
		{
			for(i = 1;i < n;i *= k)
			{
				tm = n-i;
				if(!panduan(tm,k)) break;
			}
			if(i <= n) printf("%d\n",i);
			else printf("0\n");
		}else printf("0\n");
	}
	return 0;
}
/*
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <ctime>
#include <queue>
#include <cstring>
using namespace std;
typedef __int64 LL;
const int maxn = 100005;

struct Node{
	int x,y;
};
Node mat[maxn];
LL xcross(const Node &t,const Node & t1,const Node & t2)
{
	return (LL) (t1.x-t.x)*(t2.y-t.y) - (LL) (t1.y-t.y)*(t2.x-t.x);
}
int n,m;
bool check(Node tmp)
{
	if(xcross(tmp,mat[1],mat[0]) <= 0) return false;
	if(xcross(tmp,mat[0],mat[n-1]) <= 0) return false;
	int l,r,mid,best;
	l = 0;r = n-1;
	best = 0;
	while(l <= r)
	{
		mid = (l+r)>>1;
		if(xcross(tmp,mat[mid],mat[0]) >= 0)
		{
			best = mid;
			l = mid + 1;
		}
		else r = mid - 1;
	}
	l = best;
	r = l+1;
	if(xcross(tmp,mat[l],mat[r]) >= 0) return false;
	return true;
}
int main()
{
	int i,j,ans;
	Node tmp;
	scanf("%d",&n);
	for(i = 0;i < n;i ++)
		scanf("%d%d",&mat[i].x,&mat[i].y);
	scanf("%d",&m);
	ans = 0;
	for(i = 0;i < m;i ++)
	{
		scanf("%d%d",&tmp.x,&tmp.y);
		if(check(tmp)) ans ++;
	}
	if(ans == m) printf("YES\n");
	else printf("NO\n");
	return 0;
}

/*
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;
const int maxn = 1000005;

int a[maxn];
int main()
{
	int n,p;
	int i,j,s;
	//freopen("G.in","w",stdout);
	for(n = 10;n <= maxn;n *= 10)
	{
		do{
			p = abs(rand()*rand()*rand())%n+1;
		}while(n%p == 0);
		printf("%d %d\n",n,p);
		a[0] = abs(rand()*rand()*rand())%1000000000 + 1;
		for(s = 1;s*p < n;s ++)
		{
			a[s] = abs(rand()*rand()*rand())%1000000000 + 1;
		}
		printf("%d",a[0]);
		for(j = 0;j < p;j ++)
		{
			for(i = 1;i < s;i ++)
				printf(" %d",a[i]);
		}
		j = n%p - 1;
		for(i = 0;i < j;i ++)
			printf(" %d",a[0]);
		printf("\n");
	}
	return 0;
}
/*
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <ctime>
#include <queue>
#include <cstring>
using namespace std;
typedef __int64 LL;
const int maxn = 1005;

LL dp[maxn][maxn];
int main()
{
	int t,i,j;
	int n,m,x1,x2,y1,y2;
	scanf("%d",&t);
	while(t --)
	{
		memset(dp,0,sizeof(dp));
		scanf("%d%d",&n,&m);
		dp[n][m] = 1;

	}
	return 0;
}
/*
typedef __int64 LL;
const int maxn = 100005;

struct Shoe{
	int c,s;
};
Shoe mat[maxn];
bool comp(const Shoe & s1,const Shoe & s2)
{
	return s1.si < s2.si;
}
LL dp[maxn][2];
int n,m;
int bfind(int val)
{
	int l,r,mid;
	l = 0;r = n-1;
	while(l <= r)
	{
		mid = (l+r)>>1;
		if(mat[mid].s == val) return mid;
		else if(mat[mid].s < val) l = mid + 1;
		else r = mid - 1;
	}
	return -1;
}
struct Customer{
	int d,l;
};
Customer cus[amxn];

int main()
{
	int i,j,p;
	scanf("%d",&n);
	for(i = 0;i < n;i ++)
		scanf("%d%d",&mat[i].c,&mat[i].s);
	scanf("%d",&m);
	for(i = 0;i < m;i ++)
		scanf("%d%d",&cus[i].d,&cus[i].l);
	sort(mat,mat+n,comp);
	for(i = 0;i < m;i ++)
	{
		p = bfind(cus[i].l);
		
	}
	return 0;
}
/*
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <ctime>
#include <queue>
#include <cstring>
using namespace std;
typedef long long LL;
const int maxn = 100010;
struct Shoe{
	int c,s;
};
int n,m;
Shoe mat[maxn];
bool comp(const Shoe & s1,const Shoe & s2)
{
	return s1.s < s2.s;
}
int bfind(int val)
{
	int l,r,mid;
	l = 0;r = n-1;
	while(l <= r)
	{
		mid == (l+r)>>1;
		if(mat[mid].s == val) return mid;
		else if(mat[mid].s < val) l = mid + 1;
		else r = mid - 1;
	}
	return -1;
}
struct Customer{
	int d,l;
};
Customer cus[maxn];
bool comp2(const Customer & c1,const Customer & c2)
{
	if(c1.d != c2.d) return c1.d < c2.d;
	return false;
}
int main()
{
	int i,p1,p2,p;
	LL ans = 0;
	scanf("%d",&n);
	for(i = 0;i < n;i ++)
	{
		scanf("%d%d",&mat[i].c,&mat[i].s);
	}
	sort(mat,mat+n,comp);
	scanf("%d",&m);
	for(i = 0;i < m;i ++)
		scanf("%d%d",&cus[i].d,&cus[i].l);
	sort(cus,cus+m,comp2);
	for(i = 0;i < m;i ++)
	{
		p1 = bfind(cus[i].l);
		
		p2 = bfind(cus[i].d);
		if(p1 == -1) p = p2;
		el
		if(p2 == -1) p = p1;
		if(p == -1) continue;

	}
	printf("%I64d\n",ans);
	return 0;
}
/*
const int maxn = 50;
typedef __int64 LL;
LL dp[maxn][maxn],n,m,k;
int a[maxn];
int main()
{
	int i,j;
	LL tmp;
	while(scanf("%I64d%I64d%I64d",&n,&m,&k)!=EOF)
	{
		for(i = 0;i <= n;i ++)
			for(j = 0;j <= m;j ++)
				dp[i][j] = 0;
		for(i = 0;i < m;i ++)
			scanf("%d",&a[i]);
		sort(a,a+m);
		if(n == 1){
			if(m >= k) printf("%d\n",a[k-1]);
			else printf("-1\n");
		}else{
			for(j = 0;j < m;j ++)  //康托数学原理 11有应该会
				dp[n-1][j] = 1;
			for(i = n-2;i >= 0;i --)
			{
				tmp = 0;
				for(j = 0;j < m;j ++)
					tmp += dp[i+1][j];
				for(j = 0;j < m;j ++)
					dp[i][j] = tmp;
			}
			tmp = 0;

			if(a[0] != 0) //没有开头是0的
				tmp += dp[0][0];
			for(i = 1;i < m;i ++) tmp += dp[0][i];
			if(tmp < k) printf("-1\n");
			else{
				for(i = 0;i < n;i ++)
				{
					for(j = 0;j < m;j ++)
					{
						if(i == 0 && j == 0 && a[0] == 0) continue;
						if(dp[i][j] >= k) break;
						k -= dp[i][j];
					}
					printf("%d",a[j]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
/*
const int maxn = 100005;
const int maxe = 500005;

struct Node{
	int v,sign,d,next;
};
int m,n;
int ma[maxn];
Node mat[maxe*2];
int bit[maxe],maxd;
int num[maxn];
int eda[maxe],len;
int a[maxn],b[maxn];
void addeda(int u,int v,int s)
{
	mat[len].v = v; mat[len].next = eda[u];
	mat[len].sign = s;
	eda[u] = len ++;
	swap(u,v);
	mat[len].v = v; mat[len].next = eda[u];
	mat[len].sign = s;
	eda[u] = len ++;
}

void Add(int pos,int val)
{
	while(pos <= maxd)
	{
		bit[pos] += val;
		pos += lowbit(pos);
	}
}

int Getsum(int pos)
{
	int ans = 0;
	while(pos > 0)
	{
		ans += bit[pos];
		pos -= lowbit(pos);
	}
	return ans;
}

int main()
{
	int i,j,u,v,tmp,ans = 0;
	scanf("%d%d",&m,&n);
	for(i = 0;i < n;i ++)
	{
		scanf("%d",&ma[i]);
		if(ma[i] > maxd) maxd = ma[i];
		eda[i+1] = -1;
	}
	len = 0;
	for(i = 0;i < m;i ++)
	{
		scanf("%d%d",&a[i],&b[i]);
		addeda(a[i],b[i],i);
	}
	for(i = 0;i < n;i ++)
	{
		num[i] = Getsum(ma[i]) - bit[ma[i]];
		for(j = eda[i];j != -1;j = mat[j].next)
		{
			v = mat[j].v;
			if(v-1 < i)
			{
				Add(a[i],1);
				tmp = Getsum(ma[v]) - bit[ma[v]];
				mat[j].d = tmp;
				Add(a[i],-1);
			}else{
				tmp = Getsum(ma[v]) - bit[ma[v]];
				mat[j].d = tmp;
			}
		}
		Add(ma[i],1);
	}
	
	for(i = 0;i < m;i ++)
	{
		printf("%d\n",ans);
	}
	return 0;
}


/* 1001
const int maxn = 1050000;

int n,k;
int a[maxn];
int qmax[maxn],qmaxs,qmaxe;
int qmin[maxn],qmins,qmine;

int main()
{
	int i,j,ans,s;
	LL tmp;
	while(scanf("%d%d",&n,&k)!=EOF)
	{
		for(i = 0;i < n;i ++)
			scanf("%d",&a[i]);
		qmaxs = qmaxe = 0;
		qmins = qmine = 0;
		qmax[0] = qmin[0] = 0;
		ans = 1;
		s = 0;
		for(i = 1;i < n;i ++)
		{
			while(qmaxs <= qmaxe)
			{
				if(a[qmax[qmaxe]] <= a[i])
					qmaxe --;
				else break;
			}
			qmaxe ++;
			qmax[qmaxe] = i;

			while(qmins <= qmine)
			{
				if(a[qmin[qmine]] >= a[i])
					qmine --;
				else break;
			}
			qmine ++;
			qmin[qmine] = i;

			while((LL)a[qmax[qmaxs]] - a[qmin[qmins]] > k)
			{
				if(qmax[qmaxs] > qmin[qmins])
				{
					s = qmin[qmins] + 1;
					qmins ++;
				}else
				{
					s = qmax[qmaxs] + 1;
					qmaxs ++;
				}
			}
			if(i-s+1 > ans) ans = i-s+1;
		}
		printf("%d\n",ans);
	}
	return 0;
}
/*
const int maxn = 32768;

int n,l,u;
int s[maxn];
int que[maxn],qs,qe;
int main()
{
	int i,j;
	while(scanf("%d",&n),n)
	{
		scanf("%d%d",&l,&u);
		for(i = 1;i <= n;i ++)
			scanf("%d",&s[i]);
		for(i = 1;i <= n;i ++)
			s[i] += s[i-1];
		qs = qe = 0;
		que[qs] = n;
		for(i = n-1;i >= n-l;i --)
		{
			while(qe >= qs)
			{
				if(s[i] <= s[que[qe]]) qe --;
				else break;
			}
			qe ++;
			que[qe] = i;
		}
		for(i = n-l-1;i >= 0;i --)
		{

		}
	}
	return 0;
}
/*1000
#define inf 0.000001
const int maxn = 20;

struct Node{
	char name[100];
	int rs;
};
bool operator < (const Node & t1,const Node & t2)
{
	return strcmp(t1.name,t2.name) > 0;
}
char name[maxn][100];
int val[maxn],num[maxn],p[maxn];
double rep[maxn][16];
priority_queue<Node> pq;
int x,n;
int main()
{
	int i,j,d,s;
	Node tmp;
	scanf("%d",&x);
	scanf("%d",&n);
	for(i = 0;i < n;i ++)
		num[i] = 0;
	for(i = 0;i < n;i ++)
	{
		scanf("%s%d",&name[i],&val[i]);
		if((val[i]*1.0)/x - 0.05 >= -inf)
		{
			for(j = 1;j <= 14;j ++)
			{
				rep[i][j] = (val[i]*1.0)/j;
			}
		}else 
		{
			for(j = 1;j <= 14;j ++)
				rep[i][j] = -1.000;
		}
		p[i] = 1;
	}
	for(i = 1;i <= 14;i ++)
	{
		double maxf = 0;
		int pos;
		for(j = 0;j < n;j ++)
		{
			if(rep[j][p[j]] > maxf)
			{
				maxf = rep[j][p[j]];
				pos = j;
			}
		}
		num[pos] = 1;
		p[pos] = 1;
	}
	for(i = 0;i < n;i ++)
	{
		if(rep[i][1] > 0)
		{
			strcpy(tmp.name,name[i]);
			tmp.rs = num[i];
			pq.push(tmp);
		}
	}
	while(!pq.empty())
	{
		tmp = pq.top();
		printf("%s %d\n",tmp.name,tmp.rs);
		pq.pop();
	}
	return 0;
}
/* 1002
typedef long long LL;
const int maxn = 1000003;
#define lowbit(x) ((x)&(-x))
int n,m;

int x[maxn],y[maxn];
LL xl[maxn],yl[maxn];

int findl(int *c,int val)
{
	int l,r,mid,best;
	l = 0;r = n-1;
	best = n;
	while(l <= r)
	{
		mid = (l+r)>>1;
		if(c[mid] >= val)
		{
			best = mid;
			r = mid - 1;
		}else l = mid + 1;
	}
	return best;
}

void add(LL *c,int val,int pos)
{
	while(pos <= n)
	{
		c[pos] += val;
		pos += lowbit(pos);
	}
}

LL getsum(LL *c,int pos)
{
	LL ans = 0;
	while(pos > 0)
	{
		ans += c[pos];
		pos -= lowbit(pos);
	}
	return ans;
}

char c[300100];
int main()
{
	int k,i,dx,dy,tx,ty;
	LL ansx,ansy,ans,tmp;
	scanf("%d%d",&n,&m);
	for(i = 0;i < n;i ++)
	{
		scanf("%d%d",&x[i],&y[i]);
	}
	sort(x,x+n);
	sort(y,y+n);
	for(i = 1;i <= n;i ++)
	{
		add(xl,x[i-1],i);
		add(yl,y[i-1],i);
	}
	scanf("%s",c);
	for(i = 0,dx = dy = 0;i < m;i ++)
	{
		if(c[i] == 'S')
		{
			dy ++;
		}else if(c[i] == 'J')
		{
			dy --;
		}else if(c[i] == 'I')
		{
			dx ++;
		}else if(c[i] == 'Z')
		{
			dx --;
		}
		tx = findl(x,dx);
		ansx = getsum(xl,n) - getsum(xl,tx);
		ansx -= (LL) dx*(n-tx);
		ansx += (LL) dx*tx - getsum(xl,tx);
		ty = findl(y,dy);
		ansy = getsum(yl,n) - getsum(yl,ty);
		ansy -= (LL) dy*(n-ty);
		ansy += (LL) dy*ty - getsum(yl,ty);
		ans = ansx + ansy;
		printf("%lld\n",ans);
	}
	return 0;
}
/*
typedef int u64;
const int maxn = 36400;
bool noprim[maxn] = {0};
int prim[4800],len;
void init()
{
     int i,j;
     prim[0] = 2;len = 1;noprim[0] = noprim[1] = true;
     for(i = 4;i < maxn;i += 2) noprim[i] = true;
     for(i = 3;i < maxn;i += 2)
     {
           if(!noprim[i])
           {
              for(j = i*2;j < maxn;j += i) noprim[j] = true;
              prim[len] = i;len ++;
           }
     }
}

int p,q;
void fenjie(int n)
{
	int i,j;
	p = 1;
	for(i = 0;i < len;i ++)
	{
		if(n%prim[i] == 0) break;
	}
	if(i < len)
	{
		p = prim[i];
		q = n/prim[i];
	}else
	{
		p = 1;
		q = n;
	}
}

u64 extend_gcd(u64 a,u64 b,u64 &x,u64 &y)
{
    u64 t,ret;
    if(!b)
    {
        x = 1;y = 0; return a;
    }
    ret = extend_gcd(b,a%b,x,y);
    t = x;x = y; y = t - a/b*y;
    return ret;
}

int main()
{
	init();
	int x,y,t1,t2;
	int t,n;
	scanf("%d",&t);
	while(t --)
	{
		scanf("%d",&n);
		fenjie(n);
		if(n == 2){
			printf("0 1\n");
			continue;
		}else
		{
			printf("0 1");
			extend_gcd(p,q,x,y);
			t1 = (x*p+n)%n;
			t2 = (y*q+n)%n;
			if(t1 > t2) swap(t1,t2);
			printf(" %d %d\n\n",t1,t2);
		}
	}
	return 0;
}
/*
const int maxn=8000000;
struct Node
{
	int maxd,val;
};
Node Tree[maxn];
int n,m;

void change(int rootx,int Lx,int Ly,int Rx,int Ry,int x1,int y1,int x2,int y2,int maxd)
{
	if(Lx == x1 && Ly == y1 && Rx == x2 && Ry == y2)
	{
		Tree[rootx].val = maxd;
		Tree[rootx].maxd = maxd;
	}else
	{
		if(Tree[rootx].val != 0)
		{
			Tree[rootx*4+1].val = Tree[rootx].val;
			Tree[rootx*4+1].maxd = Tree[rootx].val;
			Tree[rootx*4+2].val = Tree[rootx].val;
			Tree[rootx*4+2].maxd = Tree[rootx].val;
			Tree[rootx*4+3].val = Tree[rootx].val;
			Tree[rootx*4+3].maxd = Tree[rootx].val;
			Tree[rootx*4+4].val = Tree[rootx].val;
			Tree[rootx*4+4].maxd = Tree[rootx].val;
		}
		Tree[rootx].val = 0;
		int midx,midy;
		midx = (Lx+Rx)>>1;
		midy = (Ly+Ry)>>1;
		if(x1 <= midx && y1 <= midy)
			change(rootx*4+1,Lx,Ly,midx,midy,x1,y1,min(midx,x2),min(midy,y2),maxd);
		if(x2 > midx && y1 <= midy)
			change(rootx*4+2,midx+1,Ly,Rx,midy,max(x1,midx+1),y1,x2,min(midy,y2),maxd);
		if(x1 <= midx && y2 > midy)
			change(rootx*4+3,Lx,midy+1,midx,Ry,x1,max(y1,midy+1),min(x2,midx),y2,maxd);
		if(x2 > midx && y2 > midy)
			change(rootx*4+4,midx+1,midy+1,Rx,Ry,max(x1,midx+1),max(y1,midy+1),x2,y2,maxd);
		Tree[rootx].maxd = max(max(Tree[rootx*4+1].maxd,Tree[rootx*4+2].maxd),max(Tree[rootx*4+3].maxd,Tree[rootx*4+4].maxd));
	}
}

int Queue(int rootx,int Lx,int Ly,int Rx,int Ry,int x1,int y1,int x2,int y2)
{
	int maxd = 0;
	if(Lx == x1 && Ly == y1 && Rx == x2 && Ry == y2)
	{
		return Tree[rootx].maxd;
	}else
	{
		if(Tree[rootx].val != 0) return Tree[rootx].val;
		int midx,midy;
		midx = (Lx+Rx)>>1;
		midy = (Ly+Ry)>>1;
		if(x1 <= midx && y1 <= midy)
			maxd = max(maxd,Queue(rootx*4+1,Lx,Ly,midx,midy,x1,y1,min(midx,x2),min(midy,y2)));
		if(x2 > midx && y1 <= midy)
			maxd = max(maxd,Queue(rootx*4+2,midx+1,Ly,Rx,midy,max(x1,midx+1),y1,x2,min(midy,y2)));
		if(x1 <= midx && y2 > midy)
			maxd = max(maxd,Queue(rootx*4+3,Lx,midy+1,midx,Ry,x1,max(y1,midy+1),min(x2,midx),y2));
		if(x2 > midx && y2 > midy)
			maxd = max(maxd,Queue(rootx*4+4,midx+1,midy+1,Rx,Ry,max(x1,midx+1),max(y1,midy+1),x2,y2));
		return maxd;
	}
}


int main()
{
	int i,j,c;
	int a,b,h,x,y,x2,y2,tmp;
	while(scanf("%d%d%d",&n,&m,&c)!=EOF)
	{
		memset(Tree,0,sizeof(Tree));
		int s1 = sizeof(Tree);
		int s3 = sizeof(Tree[0]);
		int s2 = sizeof(Tree[0])*n*m;
		for(i = 0;i < c;i ++)
		{
			scanf("%d%d%d%d%d",&a,&b,&h,&x,&y);
			x ++;y ++;
			if(a >= 1) x2 = x+a-1;
			else x2 = x;
			if(b >= 1) y2 = y+b-1;
			else y2 = y;
			tmp = Queue(0,1,1,n,m,x,y,min(x2,n),min(y2,m));
			change(0,1,1,n,m,x,y,min(x2,n),min(y2,m),tmp+h);
		}
		printf("%d\n",Tree[0].maxd);
	}
	return 0;
}

/*1004
const int maxn = 1005;
const int inf = 1100000000;
struct Node{
	int pos,e;
};
Node mat[maxn],mat2[maxn];
int len;
int main()
{
	int i,j,k;
	int z;
	int c,t,l,e,p;
	scanf("%d",&z);
	while(z --)
	{
		scanf("%d%d%d",&c,&t,&l);
		for(i  = 0;i < t;i ++)
		{
			scanf("%d%d",&p,&e);
			mat[i].pos = p;
			mat[i].e = e+p;
		}
		for(i = 1;i < c;i ++)
		{
			for(j = 0;j < t;j ++)
			{
				scanf("%d%d",&p,&e);
				mat2[j].pos = p;
				mat2[j].e = inf;
				for(k = 0;k < t;k ++)
				{
					mat2[j].e = min(mat2[j].e,mat[k].e+e+abs(mat[k].pos-mat2[j].pos));
				}
			}
			for(j = 0;j < t;j ++)
				mat[j] = mat2[j];
		}
		int minsum = inf;
		for(i = 0;i < t;i ++)
			if(minsum > mat[i].e+l-mat[i].pos)
				minsum = mat[i].e+l-mat[i].pos;
		printf("%d\n",minsum);
	}
	return 0;
}
/*a
const int maxn = 250000;
struct Node{
	int v,d,next;
};
Node mat[maxn];
int eda[maxn],len;
int n;

void add(int u,int v,int c)
{
	mat[len].v = v; mat[len].d = c;
	mat[len].next = eda[u];
	eda[u] = len ++;
	swap(u,v);
	mat[len].v = v; mat[len].d = c;
	mat[len].next = eda[u];
	eda[u] = len ++;
}
int ca[maxn],dfn[maxn];
int dfs(int u,int fa)
{
	int sum = 0;
	if(fa == -1) dfn[u] = 0;
	int i,v;
	for(i = eda[u];i != -1;i = mat[i].next)
	{
		v = mat[i].v;
		if(v == fa) continue;
		dfn[v] = dfn[u]+mat[i].d;
		sum += mat[i].d*2;
		sum += dfs(v,u);
	}
	return sum;
}
int main()
{
	int i,j;
	int a,b,c,sum,mind,k;
	scanf("%d",&n);
	for(i = 0;i <= n;i ++)
	{
		scanf("%d",&ca[i]);
	}
	len = 0;
	for(i = 0;i <= n;i ++) eda[i] = -1;
	for(i = 0;i < n;i ++)
	{
		scanf("%d%d%d",&a,&b,&c);
		add(a,b,c);
	}
	sum = dfs(0,-1);
	k = 0;
	mind = ca[0] - dfn[0];
	for(i = 1;i <= n;i ++)
	{
		if(mind > ca[i]-dfn[i])
		{
			k = i;
			mind = ca[i]-dfn[i];
		}
	}
	printf("%d\n",sum+mind);
	return 0;
}

/*d
#define lowbit(x) ((x)&(-x))
#define inf 0.000001
const int maxn = 35000;
typedef struct Point point;

struct Node{
	double y1,y2;
};
double lx,rx;
int n,pl;
Node p[maxn];
bool comp(const Node & t1,const Node &t2)
{
	if(fabs(t1.y1-t2.y1) >= inf) return t1.y1 < t2.y1;
	else return t1.y2 < t2.y2;
}
double sp[maxn];
int find(double val)
{
	int l,r,mid;
	l = 0;r = n-1;
	while(l <= r)
	{
		mid = (l+r)>>1;
		if(fabs(sp[mid]-val) <= inf)
		{
			return mid;
		}else if(sp[mid]-val > inf)
			r = mid - 1;
		else l = mid+1;
	}
}
int num[maxn];
void add(int v)
{
	while(v <= n)
	{
		num[v] += 1;
		v += lowbit(v);
	}
}

int getsum(int v)
{
	int s = 0;
	while(v > 0)
	{
		s += num[v];
		v -= lowbit(v);
	}
	return s;
}
int main()
{
	int i,j,sum,pos,jd;
	double k,b;
	while(scanf("%lf%lf",&lx,&rx)!=EOF)
	{
		scanf("%d",&n);
		for(i = 0;i <= n;i ++) num[i] = 0;
		for(i = 0;i < n;i ++)
		{
			scanf("%lf%lf",&k,&b);
			p[i].y1 = lx*k+b;
			p[i].y2 = rx*k+b;
			sp[i] = p[i].y2;
		}
		sort(p,p+n,comp);
		sort(sp,sp+n);
		sum = 1;
		for(i = 0;i < n;i ++)
		{
			pos = find(p[i].y2)+1;
			if(pos < n) jd = getsum(n)-getsum(pos);
			else jd = 0;
			add(pos);
			sum += jd;
			sum ++;
		}
		printf("%d\n",sum);
	}
	return 0;
}
/* c
const int maxn = 15500;
int seg[maxn];
struct Node{
	int l,r,d;
};
Node mat[maxn];
int L,len;
bool comp(const Node & t1,const Node & t2)
{
	if(t1.l != t2.l) return t1.l < t2.l;
	else return t1.r < t2.r;
}
int main()
{
	int i,j,maxd;
	int s,e,d;
	while(scanf("%d",&L)!=EOF)
	{
		for(i = 0;i <= L;i ++)
			seg[i] = 0;
		len = 0;
		while(scanf("%d%d%d",&s,&e,&d)==3)
		{
			if(s < 0) break;
			mat[len].l = s; mat[len].r = e;
			mat[len++].d = d;
		}
		sort(mat,mat+len,comp);
		for(i = 0;i < len;i ++)
		{
			seg[mat[i].l] += mat[i].d;
			seg[mat[i].r+1] -= mat[i].d;
		}
		maxd = seg[0];
		for(i = 1;i <= L;i ++)
		{
			 seg[i] += seg[i-1];
			 if(seg[i] > maxd) maxd = seg[i];
		}
		for(i = 0;i <= L;i ++)
			if(maxd == seg[i])
			{
				printf("%d",i);
				break;
			}
		for(i = L;i >= 0;i --)
			if(maxd == seg[i])
			{
				printf(" %d\n",i);
				break;
			}
	}
	return 0;
}
/* h
const int maxn=9000000;
struct Node
{
	int maxd,val;
};
Node Tree[maxn];
int n,m;

void change(int rootx,int Lx,int Ly,int Rx,int Ry,int x1,int y1,int x2,int y2,int maxd)
{
	if(Lx == x1 && Ly == y1 && Rx == x2 && Ry == y2)
	{
		Tree[rootx].val = maxd;
		Tree[rootx].maxd = maxd;
	}else
	{
		if(Tree[rootx].val != 0)
		{
			Tree[rootx*4+1].val = Tree[rootx].val;
			Tree[rootx*4+1].maxd = Tree[rootx].val;
			Tree[rootx*4+2].val = Tree[rootx].val;
			Tree[rootx*4+2].maxd = Tree[rootx].val;
			Tree[rootx*4+3].val = Tree[rootx].val;
			Tree[rootx*4+3].maxd = Tree[rootx].val;
			Tree[rootx*4+4].val = Tree[rootx].val;
			Tree[rootx*4+4].maxd = Tree[rootx].val;
		}
		Tree[rootx].val = 0;
		int midx,midy;
		midx = (Lx+Rx)>>1;
		midy = (Ly+Ry)>>1;
		if(x1 <= midx && y1 <= midy)
			change(rootx*4+1,Lx,Ly,midx,midy,x1,y1,min(midx,x2),min(midy,y2),maxd);
		if(x2 > midx && y1 <= midy)
			change(rootx*4+2,midx+1,Ly,Rx,midy,max(x1,midx+1),y1,x2,min(midy,y2),maxd);
		if(x1 <= midx && y2 > midy)
			change(rootx*4+3,Lx,midy+1,midx,Ry,x1,max(y1,midy+1),min(x2,midx),y2,maxd);
		if(x2 > midx && y2 > midy)
			change(rootx*4+4,midx+1,midy+1,Rx,Ry,max(x1,midx+1),max(y1,midy+1),x2,y2,maxd);
		Tree[rootx].maxd = max(max(Tree[rootx*4+1].maxd,Tree[rootx*4+2].maxd),max(Tree[rootx*4+3].maxd,Tree[rootx*4+4].maxd));
	}
}

int Queue(int rootx,int Lx,int Ly,int Rx,int Ry,int x1,int y1,int x2,int y2)
{
	int maxd = 0;
	if(Lx == x1 && Ly == y1 && Rx == x2 && Ry == y2)
	{
		return Tree[rootx].maxd;
	}else
	{
		if(Tree[rootx].val != 0) return Tree[rootx].val;
		int midx,midy;
		midx = (Lx+Rx)>>1;
		midy = (Ly+Ry)>>1;
		if(x1 <= midx && y1 <= midy)
			maxd = max(maxd,Queue(rootx*4+1,Lx,Ly,midx,midy,x1,y1,min(midx,x2),min(midy,y2)));
		if(x2 > midx && y1 <= midy)
			maxd = max(maxd,Queue(rootx*4+2,midx+1,Ly,Rx,midy,max(x1,midx+1),y1,x2,min(midy,y2)));
		if(x1 <= midx && y2 > midy)
			maxd = max(maxd,Queue(rootx*4+3,Lx,midy+1,midx,Ry,x1,max(y1,midy+1),min(x2,midx),y2));
		if(x2 > midx && y2 > midy)
			maxd = max(maxd,Queue(rootx*4+4,midx+1,midy+1,Rx,Ry,max(x1,midx+1),max(y1,midy+1),x2,y2));
		return maxd;
	}
}


int main()
{
	int i,j,c;
	int a,b,h,x,y,x2,y2,tmp;
	while(scanf("%d%d%d",&n,&m,&c)!=EOF)
	{
		memset(Tree,0,sizeof(Tree));
		for(i = 0;i < c;i ++)
		{
			scanf("%d%d%d%d%d",&a,&b,&h,&x,&y);
			x ++;y ++;
			if(a >= 1) x2 = x+a-1;
			else x2 = x;
			if(b >= 1) y2 = y+b-1;
			else y2 = y;
			tmp = Queue(0,1,1,n,m,x,y,min(x2,n),min(y2,m));
			change(0,1,1,n,m,x,y,min(x2,n),min(y2,m),tmp+h);
		}
		printf("%d\n",Tree[0].maxd);
	}
	return 0;
}

/*
using namespace std;
const int inf = 1000000000;
const int maxn = 100500;
#define maxh 18
const int maxe = 250000;

int n;
struct Node{
	int u,v,d,next;
};
Node mat[maxe];
int len;
int fax[maxn];
bool comp(const Node & t1,const Node & t2)
{
	return t1.d < t2.d;
}

int findfa(int u)
{
	if(fax[u] != u) fax[u] = findfa(fax[u]);
	return fax[u];
}

void Unit(int x,int y)
{
	if(x > y) fax[x] = y;
	else fax[y] = x;
}

void add(int u,int v,int d)
{
	mat[len].u = u;
	mat[len].v = v;
	mat[len].d = d;
	len ++;

	swap(u,v);
	mat[len].u = u;
	mat[len].v = v; 
	mat[len].d = d;
	len ++;
}

struct CNode{
	int v,d,next;
};
CNode cmat[maxn*2];
int ceda[maxn],clen;
int dis[maxn];

int fa[maxh][maxn],h,height[maxn],pos[maxn],s;
const int bath[] = {1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072};


void addc(int u,int v,int d)
{
	cmat[clen].v = v; cmat[clen].next = ceda[u];
	cmat[clen].d = d;
	ceda[u] = clen ++;
	swap(u,v);
	cmat[clen].v = v; cmat[clen].next = ceda[u];
	cmat[clen].d = d;
	ceda[u] = clen ++;
}

struct BNode{
	int bs,u;
};
BNode bs[maxn];
void dfs(int u,int f)
{
	int i,v;
	fa[0][s] = u;
	pos[u] = s++;
	for(i = ceda[u];i != -1;i = cmat[i].next)
	{
		v = cmat[i].v;
		if(f == v) continue;
		height[v] = height[u] + 1;  
		bs[v].bs = i;
		bs[v].u = u;
		dfs(v,u);
		fa[0][s++] = u;
	}
}

void InitRMQ()
{
	int i,j,k,n;
	n = s;
	for(h = 0;bath[h] <= n;h ++);
	h --;
	for(i = 1;i <= h;i ++)
	{
		for(j = 1;j+bath[i]-1 <= n;j ++)
		{
			if(height[fa[i-1][j]] > height[fa[i-1][j+bath[i-1]]])
				fa[i][j] = fa[i-1][j+bath[i-1]];
			else 
				fa[i][j] = fa[i-1][j];
		}
	}
}

int lcp(int x,int y)
{
	int t1,t2,d,i,h;
	if(x == y) return 0;
	t1 = pos[x]; t2 = pos[y];
	if(t1 > t2) swap(t1,t2);
	d = t2-t1+1;
	for(h = 0;bath[h] <= d;h ++);
	h --;
	if(height[fa[h][t1]] < height[fa[h][t2-bath[h]+1]])
		return fa[h][t1];
	else return fa[h][t2-bath[h]+1];
}

int Queue(int x,int y)
{
	int ans,u,id;
	ans = 0;
	int fx = lcp(x,y);
	while(x != fx)
	{
		id = bs[x].bs;
		u = bs[x].u;
		if(cmat[id].d > ans) ans = cmat[id].d;
		x = u;
	}
	while(y != fx)
	{
		id = bs[y].bs;
		u = bs[y].u;
		if(cmat[id].d > ans) ans = cmat[id].d;
		y = u;
	}
	return ans;
}
int main()
{
	int si,ti,ans,m,q,i,j,ncase;
	int fx,fy,bs;
	int u,v,d;
	scanf("%d",&ncase);
	while(ncase --)
	{
		scanf("%d%d",&n,&m);
		len = clen = bs = 0;
		for(i = 1;i <= n;i ++)
		{
			ceda[i] = -1,fax[i] = i;
		}
		for(i = 0;i < m;i ++)
		{
			scanf("%d%d%d",&u,&v,&d);
			add(u,v,d);
		}
		sort(mat,mat+len,comp);
		for(i = 0;i < len;i ++)
		{
			fx = findfa(mat[i].u);
			fy = findfa(mat[i].v);
			if(fx != fy)
			{
				Unit(fx,fy);
				addc(mat[i].u,mat[i].v,mat[i].d);
				bs ++;
				if(bs >= n-1) break;
			}
		}
		s = 1;
		height[1] = 0;
		dfs(1,-1);
		InitRMQ();
		scanf("%d",&q);
		for(i = 0;i < q;i ++)
		{
			scanf("%d%d",&si,&ti);
			printf("%d\n",Queue(si,ti));
		}
	}
	return 0;
}
/*
const int maxn = 1005;

char c[maxn];
int num[26][maxn];  //将某个数更改，增加的数目
int jnum[maxn];
int onum[maxn];
int main()
{
	int n,ans,tmp,tmp2;
	int i,j,k,len,cs,s,t,maxd;
	scanf("%d",&n);
	while(n --)
	{
		scanf("%s",c);
		for(len = 0;c[len] != '\0';len ++);
		
		for(i = 0;i < 26;i ++)
			for(j = 0;j < len;j ++)
				num[i][j] = 0;
		ans = 0;
		for(i = 0;i < len;i ++)
		{
			//奇数情况
			tmp = cs = 0;
			s = -1;t = -1;
			for(j = 0;i+j < len && i-j >= 0;j ++)
				if(c[i-j] != c[i+j])
				{
					s = i-j; t = i+j;
					break;
				}else if(cs == 0) tmp ++;
			jnum[i] = tmp;
			ans += tmp;
			tmp2 = tmp;
			for(;i+j < len && i-j >= 0;j ++)
				if(c[i-j] != c[i+j])
				{
					if(cs >= 1) break;
					tmp2 ++;
					cs ++;
				}else tmp2 ++;
			if(s != -1)
			{
				num[c[t]-'a'][s] += tmp2-tmp;	
				num[c[s]-'a'][t] += tmp2-tmp;;
			}
			//偶数情况
			tmp = cs = 0;
			s = -1;t = -1;
			for(j = 1;i+j < len && i-j+1 >= 0;j ++)
				if(c[i-j+1] != c[i+j])
				{
					s = i-j+1; t = i+j;
					break;
				}else if(cs == 0) tmp ++;
			onum[i] = tmp;
			ans += tmp;
			tmp2 = tmp;
			for(;i+j < len && i-j+1 >= 0;j ++)
				if(c[i-j+1] != c[i+j])
				{
					if(cs >= 1) break;
					tmp2 ++;
					cs ++;
				}else tmp2 ++;
			if(s != -1)
			{
				num[c[t]-'a'][s] += tmp2-tmp;
				num[c[s]-'a'][t] += tmp2-tmp;
			}
		}
		maxd = 0;
		for(i = 0;i < len;i ++)  //剪掉更改后丢失的回文串
		{
			tmp = 0;
			for(j = 0;j < 26;j ++) if(num[j][i] > tmp) tmp = num[j][i];
			if(tmp == 0) continue;
			for(j = 0;j < len;j ++)
			{
				//偶数
				if(j-onum[j]+1 <= i && j+onum[j] >= i)
					tmp -= min(i-(j-onum[j]+1)+1,j+onum[j]-i+1);
				//奇数
				if(i == j) continue;
				if(j-jnum[j]+1 <= i && j+jnum[j] - 1 >= i)
					tmp -= min(i-(j-jnum[j]+1)+1,j+jnum[j] - 1-i+1);
			}
			if(tmp > maxd) maxd = tmp;
		}
		printf("%d\n",ans+maxd);
	}
	return 0;
}
/*lca + rmq
const int maxn = 100005;
#define maxh 18
#define less(a,b) a>b?b:a

int n;
struct Node{
	int v,next;
};
Node mat[maxn*2];
int eda[maxn],len,num[maxn];

void add(int u,int v)
{
	mat[len].v = v; mat[len].next = eda[u];
	eda[u] = len ++;
	swap(u,v);
	mat[len].v = v; mat[len].next = eda[u];
	eda[u] = len ++;
}
int fa[maxh][maxn],h,height[maxn],pos[maxn],s;
const int bath[] = {1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072};
int dp[maxn];

void dfs(int u,int f)
{
	int i,v;
	fa[0][s] = u;
	pos[u] = s++;
	for(i = eda[u];i != -1;i = mat[i].next)
	{
		v = mat[i].v;
		if(f == v) continue;
		height[v] = height[u] + 1;  //
		dp[v] = num[v] + dp[u];
		dfs(v,u);
		fa[0][s++] = u;
	}
}

void InitRMQ()
{
	int i,j,k,n;
	n = s;
	for(h = 0;bath[h] <= n;h ++);
	h --;
	for(i = 1;i <= h;i ++)
	{
		for(j = 1;j+bath[i]-1 <= n;j ++)
		{
			if(height[fa[i-1][j]] > height[fa[i-1][j+bath[i-1]]])
				fa[i][j] = fa[i-1][j+bath[i-1]];
			else 
				fa[i][j] = fa[i-1][j];
		}
	}
}

int lcp(int x,int y)
{
	int t1,t2,d,i,h;
	if(x == y) return 0;
	t1 = pos[x]; t2 = pos[y];
	if(t1 > t2) swap(t1,t2);
	d = t2-t1+1;
	for(h = 0;bath[h] <= d;h ++);
	h --;
	if(height[fa[h][t1]] < height[fa[h][t2-bath[h]+1]])
		return fa[h][t1];
	else return fa[h][t2-bath[h]+1];
}

int main()
{
	int m,i,j,k,l;
	int x,y,z;
	while(scanf("%d%d",&n,&m)!=EOF)
	{
		len = 0;
		for(i = 1;i <= n;i ++) eda[i] = -1;
		for(i = 1;i < n;i ++)
		{
			scanf("%d%d",&x,&y);
			add(x,y);
		}

		for(i = 1;i <= n;i ++)
			scanf("%d",&num[i]);
		dp[1] = num[1];
		height[1] = 0;
		s = 1;
		dfs(1,0);
		InitRMQ();
		for(i = 1;i <= m;i ++)
		{
			scanf("%d%d",&x,&y);
			if(x == y) printf("%d\n",num[x]);
			else
			{
				z = lcp(x,y);
				printf("%d\n",dp[x]-dp[z]+dp[y]-dp[z]+num[z]);
			}
		}
	}
	return 0;
}

/* h
const int inf = 300000;
const int maxn = 220;
const int maxe = 44000;

struct Node{
	int v,l,c,next;
};
Node mat[maxe];
int eda[maxn],len,dis[4][maxn],sign[maxn],co[maxn],ans;

void add(int u,int v,int l,int c)
{
	mat[len].v = v; mat[len].l = l;
	mat[len].c = c; mat[len].next = eda[u];
	eda[u] = len ++;
}

struct CNode{
	int v,color,d;
};
bool operator < ( const CNode & t1, const CNode & t2)
{
 	 if( t1.d > t2.d) return true;
 	 return false;
} 


void dijk(int n)
{
	CNode tmp,tm;
	int i,j,u,v,maxd,t;
	for(i = 1;i <= n;i ++) dis[1][i] = dis[2][i] = dis[3][i] = inf;
	priority_queue<CNode> pq;
	tmp.color = 0;tmp.v = 1;tmp.d = 0;
	pq.push(tmp);
	while(!pq.empty())
	{
		tmp = pq.top();pq.pop();
		u = tmp.v;
		for(i = eda[u];i != -1;i = mat[i].next)
		{
			v = mat[i].v;
			if(mat[i].c != tmp.color)
			{
				if(dis[mat[i].c][v] > tmp.d + mat[i].l)
				{
					dis[mat[i].c][v] = tmp.d+mat[i].l;
					tm.color = mat[i].c; tm.d = dis[mat[i].c][v];
					tm.v = v;
					pq.push(tm);
				}
			}
		}
	}
	ans = inf;
	ans = min(min(dis[1][n],dis[2][n]),dis[3][n]);
}

int main()
{
	int n,m,i,j;
	int x,y,l,c;
	while(scanf("%d%d",&n,&m)!=EOF)
	{
		len = 0;
		for(i = 1;i <= n;i ++) eda[i] = -1;
		for(i = 0;i < m;i ++)
		{
			scanf("%d%d%d%d",&x,&y,&l,&c);
			add(x,y,l,c);
		}
		dijk(n);
		if(ans >= inf) printf("-1\n");
		else	printf("%d\n",ans);
	}
	return 0;
}
/* g
const int inf = 9100000;
const int maxn = 400;
const int maxe = 20010;

int mat[maxn][maxn],dis[maxn][maxn];
int main()
{
	int i,j,k,u,v,d,n,m,ans;
	while(scanf("%d%d",&n,&m)!=EOF)
	{
		for(i = 1;i <= n;i ++)
			for(j = 1;j <= n;j ++)
				mat[i][j] = dis[i][j] = inf;
		for(i = 0;i < m;i ++)
		{
			scanf("%d%d%d",&u,&v,&d);
			mat[u][v] = mat[v][u] = d;
			dis[u][v] = dis[v][u] = d;
		}
		ans = inf;
		for(k = 1;k <= n;k ++)
		{
			for(i = 1;i < k;i ++)
			 for(j = i+1;j < k;j ++)
			 {
				
				if(dis[i][j]+mat[i][k]+mat[k][j] < ans || ans == -1)
					ans = dis[i][j]+mat[i][k]+mat[k][j];
			 }
			 for(i = 1;i <= n;i ++)
				 for(j = 1;j <= n;j ++)
					 dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j]);
		}
		if(ans >= inf) printf("-1\n");
		else	printf("%d\n",ans);
	}
	return 0;
}
/*
const int maxn = 1005;

char c[maxn];
int hash[30],num[30],nl;
int dp[maxn],dpl,ndpl;
int main()
{
	int i,j,n,len,ans,tmp,tmpans;
	int k,l,ncase = 0;
	scanf("%d",&n);
	while(n --)
	{
		scanf("%s",c);
		nl = 0;
		ncase ++;
		for(len = 0;c[len] != '\0';len ++)
		{
			if(hash[c[len]-'a'] != ncase)
			{
				num[nl++] = c[len]-'a';
				hash[c[len]-'a'] = ncase;
			}
		}
		ans = len;
		//奇数情况
		for(k = 0;k < len;k ++)
			dp[k] = k;
		dpl = k;
		for(k = 1;k*2 < len;k ++)
		{
			for(l = 0,ndpl = 0;l < dpl;l ++)
			{
				if(dp[l] - k < 0) continue;
				if(dp[l] + k >= len) break;
				if(c[dp[l]-k] == c[dp[l]+k])
				{
					dp[ndpl++] = dp[l];
					ans ++;
				}
			}
			if(ndpl == 0) break;
			dpl = ndpl;
		}

		//偶数情况
		for(k = 0,dpl = 0;k < len-1;k ++)
			if(c[k] == c[k+1])
			{
				dp[dpl++] = k;
				ans ++;
			}
		for(k = 1;k*2 <= len;k ++)
		{
			for(l = 0,ndpl = 0;l < dpl;l ++)
			{
				if(dp[l]-k < 0) continue;
				if(dp[l]+k+1 >= len) break;
				if(c[dp[l]-k] == c[dp[l]+k+1])
				{
					dp[ndpl++] = dp[l];
					ans ++;
				}
			}
			if(ndpl == 0) break;
			dpl = ndpl;
		}
		for(i = 0;i < len;i ++)
		{
			tmp = c[i]-'a';
			for(j = 0;j < nl;j ++)
			{
				tmpans = len;
				if(num[j] == tmp) continue;
				c[i] = num[j] + 'a';
				//奇数情况
				for(k = 0;k < len;k ++)
					dp[k] = k;
				dpl = k;
				for(k = 1;k*2 < len;k ++)
				{
					for(l = 0,ndpl = 0;l < dpl;l ++)
					{
						if(dp[l] - k < 0) continue;
						if(dp[l] + k >= len) break;
						if(c[dp[l]-k] == c[dp[l]+k])
						{
							dp[ndpl++] = dp[l];
							tmpans ++;
						}
					}
					dpl = ndpl;
				}

				//偶数情况
				for(k = 0,dpl = 0;k < len-1;k ++)
					if(c[k] == c[k+1])
					{
						dp[dpl++] = k;
						tmpans ++;
					}
				for(k = 1;k*2 <= len;k ++)
				{
					for(l = 0,ndpl = 0;l < dpl;l ++)
					{
						if(dp[l]-k < 0) continue;
						if(dp[l]+k+1 >= len) break;
						if(c[dp[l]-k] == c[dp[l]+k+1])
						{
							dp[ndpl++] = dp[l];
							tmpans ++;
						}
					}
					dpl = ndpl;
				}
				if(tmpans > ans) ans = tmpans;
			}
			c[i] = tmp+'a';
		}
		printf("%d\n",ans);
	}
	return 0;
}
/*
const int maxn = 10000;

int num[maxn];
int main()
{
	int n,i,j;
	while(scanf("%d",&n)!=EOF)
	{
		if(n == 0) break;
		for(i = 0;i < n;i ++)
			scanf("%d",&num[i]);
		sort(num,num+n);
		for(i = 1;i < n;i ++)
			if(num[i] - num[i-1] > 200) break;
		if(i < n) printf("IMPOSSIBLE\n");
		else
		{
			if((1422-num[n-1])*2 <= 200) printf("POSSIBLE\n");
			else printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
/*
const int maxn = 110;

int num[maxn],mat[maxn];
int main()
{
	int n,w,i,maxd,mored;
	double sum,ans,tmp;
	while(scanf("%d%d",&n,&w)!=EOF)
	{
		if(n == 0 && w == 0) break;
		maxd = mored = 0;
		for(i = 0;i < maxn;i ++) mat[i] = 0;
		for(i = 0;i < n;i ++)
		{
			scanf("%d",&num[i]);
			mat[num[i]/w] = 1;
			if(mat[num[i]/w] > mored) mored = mat[num[i]/w];
			if(num[i]/w > maxd) maxd = num[i]/w;
		}
		ans = 0;
		for(i = 0;i <= maxd;i ++)
		{
			ans += (mat[i]*1.0)/mored*((maxd-i)*1.0/maxd);
		}
		ans += 0.01;
		printf("%.6f\n",ans);
	}
	return 0;
}
/*
const int maxn = 1048576;

int bat[22] = {0,1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,
32768,65536,131072,262144,524288,1048576};
int dp[maxn],n;
int main()
{
	int i,j,k,tmp,tmp2,t,m,ans;
	scanf("%d",&n);
	ans = 0;
	for(i = 1;i <= n;i ++)
	{
		scanf("%d",&tmp);
		ans += tmp;
		for(j = 1;j < bat[n+1];j ++)
			if(j&bat[i]) dp[j] = dp[j-bat[i]] + tmp;
	}
	scanf("%d",&m);
	for(i = 1;i <= m;i ++)
	{
		scanf("%d",&tmp);
		t = 0;
		scanf("%d",&k);
		for(j = 0;j < k;j ++)
		{
			scanf("%d",&tmp2);
			t += bat[tmp2];
		}
		for(j = 0;j < bat[n+1];j ++)
			dp[j|t] = min(dp[j|t],dp[j]+tmp);
		//for(j = t;j < maxn;j ++)
		//	if((j&t)==t) dp[j] = min(dp[j],dp[j-t] + tmp);
	}
	scanf("%d",&m);
	for(i = 1,t = 0;i <= m;i ++)
	{
		scanf("%d",&tmp);
		t += bat[tmp];
	}
	if(m == 0) printf("0\n");
	else
	{
		for(j = t;j < bat[n+1];j ++)
			if((j&t)==t && dp[j] < ans) ans = dp[j];
		printf("%d\n",ans);
	}
	return 0;
}
/*1004
const int maxn = 2100;

int wa[maxn],wb[maxn],wv[maxn],wn[maxn];
bool Comp(int *r,int a,int b,int l)
{
	return r[a] == r[b] && r[a+l] == r[b+l];
}
//n 是队列的长度+ 1
//每次用时，要清空r的第n元素（队列从开始）
//sa[1]…sa[n] 排名第一…..的后缀从那里开始

void Da(int *r,int *sa,int n,int m) 
{
	int i,j,p,*x,*y,*t;
	r[n-1] = 0;
	x = wa; y = wb;
	for(i = 0;i <= m;i ++) wn[i] = 0;
	for(i = 0;i < n;i ++) wn[x[i]=r[i]] = 1;
	for(i = 1;i <= m;i ++) wn[i] += wn[i-1];
	for(i = n-1;i >= 0;i --) sa[--wn[x[i]]] = i;

	for(j = 1,p = 1;p < n;j <<= 1,m = p)
	{
		for(i = n-j,p = 0;i < n;i ++) y[p++] = i;
		for(i = 0;i < n;i ++) if(sa[i] >= j) y[p++] = sa[i] - j;

		for(i = 0;i < n;i ++) wv[i] = x[y[i]];
		for(i = 0;i <= m;i ++) wn[i] = 0;
		for(i = 0;i < n;i ++) wn[wv[i]] = 1;
		for(i = 1;i <= m;i ++) wn[i] += wn[i-1];
		for(i = n-1;i >= 0;i --) sa[--wn[wv[i]]] = y[i];

		t = x; x = y; y = t;
		for(x[sa[0]] = 0,i = 1,p = 1;i < n;i ++)
			x[sa[i]] = Comp(y,sa[i-1],sa[i],j) ? p-1:p++;
	}
}

//height[i] 排好序的后缀i与i-1的最长公共前缀
//ranka[i] suffix(i) 的排名
int height[maxn],ranka[maxn];

void CallHeight(int *r,int *sa,int n)
{
	int i,j,k = 0;
	for(i = 1;i <= n;i ++) ranka[sa[i]] = i;

	for(i = 0;i < n;height[ranka[i++]] = k)
		for(k?k--:0,j = sa[ranka[i]-1];r[i+k] == r[j+k];k ++);
}

//height[] 确认rmq
int bt[15][maxn];
int bat[] = {1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536};

void InitRMQ(int n)
{
	int i,j,k;
	for(k = 0;bat[k] <= n;k ++) ;
	k --;
	for(i = 1;i <= n;i ++)
		bt[0][i] = i;
	for(i = 1;i <= k;i ++)
	{
		for(j = 1;j+bat[i] <= n+1;j ++)
		{
			if(height[bt[i-1][j]] > height[bt[i-1][j+bat[i-1]]])
				bt[i][j] = bt[i-1][j+bat[i-1]];
			else
				bt[i][j] = bt[i-1][j];
		}
	}
}

int check(int x,int y)  //数组c[x] -- > c[y] 之间最小
{
	int sum = 0,len,k;
	x = ranka[x]; y = ranka[y];
	if(x > y) swap(x,y);
	x ++;
	len = y - x + 1;
	for(k = 0;bat[k] <= len;k ++);
	k --;
	sum = min(height[bt[k][x]],height[bt[k][y-bat[k]+1]]);
	return sum;
}

int a[maxn],sa[maxn],len,n;
char c[maxn];
int main()
{
	int i,j,x,y,tmp;
	int ans,st;
	gets(c);
	for(len = 0;c[len] != '\0';len ++)
		a[len] = c[len];
	n = len+len+1;
	a[len] = 1;
	for(i = 1;i <= len;i ++)
		a[len+i] = c[len-i];

	Da(a,sa,n+1,250);
	CallHeight(a,sa,n);
	InitRMQ(n);
	
	ans = 0;
	for(i = 0;i < len;i ++)
	{
		x = i;y = n-i-1; //奇数
		tmp = check(x,y);
		if(tmp*2-1 > ans)
		{
			ans = tmp*2-1;
			st = x-tmp+1;
		}
		y = n-i-2;  //偶数
		tmp = check(x,y);
		if(tmp*2-2 > ans)
		{
			ans = tmp*2-2;
			st = x-tmp+2;
		}
	}
	//printf("%d\n",ans);
	for(i = st;i < st+ans;i ++)
		printf("%c",c[i]);
	printf("\n");
	return 0;
}
/*
const int maxn = 11005;

struct Node{
	int v,next;
};
Node mat[maxn*2];
int eda[maxn];
int n,len;

int dp[2][2][maxn];

void addEda(int u,int v)
{
	mat[len].v = v; mat[len].next = eda[u];
	eda[u] = len ++ ;
	swap(u,v);
	mat[len].v = v; mat[len].next = eda[u];
	eda[u] = len ++ ;
}

//dp[0] 父亲不建
void dfs(int u,int fa)
{
	dp[0][0][u] = dp[1][0][u] = 0; 
	dp[1][1][u] = dp[0][1][u] = 1;

	int i,j,v,tmp;
	tmp = maxn;
	for(i = eda[u];i != -1;i = mat[i].next)
	{
		if(mat[i].v == fa) continue;
		v = mat[i].v;
		dfs(v,u);
		dp[1][1][u] += min(dp[1][0][v],dp[1][1][v]);  //父亲节点覆盖
		dp[1][0][u] += min(dp[0][0][v],dp[0][1][v]);

		dp[0][1][u] += min(dp[1][0][v],dp[1][1][v]);
		dp[0][0][u] += min(dp[0][0][v],dp[0][1][v]);//子节点至少一个得建
		if(dp[0][1][v] - dp[0][0][v] < tmp) tmp = dp[0][1][v] - dp[0][0][v];
	}
	if(tmp != maxn && tmp > 0) dp[0][0][u] += tmp;
	if(dp[0][0][u] == 0) dp[0][0][u] = 1;
}
int main()
{
	int i,j,x,y;
	len = 0;
	while(scanf("%d",&n)!=EOF)
	{
		for(i = 1;i <= n;i ++) eda[i] = -1;
		for(i = 1;i < n;i ++)
		{
			scanf("%d%d",&x,&y);
			addEda(x,y);
		}
		dfs(1,-1);
		printf("%d\n",min(dp[0][0][1],dp[0][1][1]));
	}
	return 0;
}
/* a
typedef long long LL;
int main()
{
	int n,i,j;
	LL t,tmp,x,y;
	LL l,r,mid,best;
	scanf("%d",&n);
	for(i = 0;i < n;i ++)
	{
		if(i != 0) printf(" ");
		scanf("%lld",&t);
		if(t == 1 || t == 2)
		{
			printf("1");
			continue;
		}
		tmp = t-1;
		l = best = 1;r = tmp;
		while(l <= r)
		{
			mid = (l+r)/2;
			if(mid*(mid-1)/2 <= tmp)
			{
				best = mid;
				l = mid + 1;
			}else r = mid - 1;
		}
		if(best*(best-1)/2 == tmp) printf("1");
		else printf("0");
	}
	printf("\n");
	return 0;
}

/*
const int maxn = 2005;

int wa[maxn],wb[maxn],wv[maxn],wn[maxn];
bool Comp(int *r,int a,int b,int l)
{
	return r[a] == r[b] && r[a+l] == r[b+l];
}
//n 是队列的长度+ 1
//每次用时，要清空r的第n元素（队列从开始）
//sa[1]…sa[n] 排名第一…..的后缀从那里开始

void Da(int *r,int *sa,int n,int m) 
{
	int i,j,p,*x,*y,*t;
	r[n-1] = 0;
	x = wa; y = wb;
	for(i = 0;i <= m;i ++) wn[i] = 0;
	for(i = 0;i < n;i ++) wn[x[i]=r[i]] = 1;
	for(i = 1;i <= m;i ++) wn[i] += wn[i-1];
	for(i = n-1;i >= 0;i --) sa[--wn[x[i]]] = i;

	for(j = 1,p = 1;p < n;j <<= 1,m = p)
	{
		for(i = n-j,p = 0;i < n;i ++) y[p++] = i;
		for(i = 0;i < n;i ++) if(sa[i] >= j) y[p++] = sa[i] - j;

		for(i = 0;i < n;i ++) wv[i] = x[y[i]];
		for(i = 0;i <= m;i ++) wn[i] = 0;
		for(i = 0;i < n;i ++) wn[wv[i]] = 1;
		for(i = 1;i <= m;i ++) wn[i] += wn[i-1];
		for(i = n-1;i >= 0;i --) sa[--wn[wv[i]]] = y[i];

		t = x; x = y; y = t;
		for(x[sa[0]] = 0,i = 1,p = 1;i < n;i ++)
			x[sa[i]] = Comp(y,sa[i-1],sa[i],j) ? p-1:p++;
	}
}

//height[i] 排好序的后缀i与i-1的最长公共前缀
//ranka[i] suffix(i) 的排名
int height[maxn],ranka[maxn];

void CallHeight(int *r,int *sa,int n)
{
	int i,j,k = 0;
	for(i = 1;i <= n;i ++) ranka[sa[i]] = i;

	for(i = 0;i < n;height[ranka[i++]] = k)
		for(k?k--:0,j = sa[ranka[i]-1];r[i+k] == r[j+k];k ++);
}

//height[] 确认rmq
int bt[15][maxn];
int bat[] = {1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536};

void InitRMQ(int n)
{
	int i,j,k;
	for(k = 0;bat[k] <= n;k ++) ;
	k --;
	for(i = 1;i <= n;i ++)
		bt[0][i] = i;
	for(i = 1;i <= k;i ++)
	{
		for(j = 1;j+bat[i] <= n+1;j ++)
		{
			if(height[bt[i-1][j]] > height[bt[i-1][j+bat[i-1]]])
				bt[i][j] = bt[i-1][j+bat[i-1]];
			else
				bt[i][j] = bt[i-1][j];
		}
	}
}

int check(int x,int y)  //数组c[x] -- > c[y] 之间最小
{
	int sum = 0,len,k;
	x = ranka[x]; y = ranka[y];
	if(x > y) swap(x,y);
	x ++;
	len = y - x + 1;
	for(k = 0;bat[k] <= len;k ++);
	k --;
	sum = min(height[bt[k][x]],height[bt[k][y-bat[k]+1]]);
	return sum;
}

int a[maxn],sa[maxn];
char c[maxn];
int hash[30];
int mat[30];
int main()
{
	int tmp,sum,stmp,mtmp;
	int t,n,len,i,j,k,sn,x,y;
	scanf("%d",&t);
	while(t --)
	{
		scanf("%s",c);
		for(len = sn = 0; c[len] != '\0';len ++)
		{
			a[len] = c[len];
			if(hash[c[len]-'a'] != 1)
			{
				hash[c[len]-'a'] = 1;
				mat[sn++] = c[len];
			}
		}
		a[len] = 1;
		for(i = 1;i <= len;i ++)
			a[len+i] = c[len-i];
		n = len+len+1;
		sum = 0;
		Da(a,sa,n+1,200);
		CallHeight(a,sa,n);
		InitRMQ(n);
		for(i = 0;i < len;i ++)
		{
			x = i; y = n-i-1;  //x为中心的情况
			tmp = check(x,y);
			sum += tmp;

			y = n-i-2;  //偶数情况
			tmp = check(x,y);
			if(tmp > 0) sum += tmp - 1;
		}
		for(i = 0;i < len;i ++)
		{
			mtmp = a[i];
			for(j = 0;j < sn;j ++)
			{
				if(mat[j] == mtmp) continue;
				a[i] = mat[j]; a[n-1-i] = mat[j];
				stmp = 0;
				Da(a,sa,n+1,200);
				CallHeight(a,sa,n);
				InitRMQ(n);
				for(k = 0;k < len;k ++)
				{
					x = k; y = n-k-1;  //x为中心的情况
					tmp = check(x,y);
					stmp += tmp;

					y = n-k-2;
					tmp = check(x,y);
					if(tmp > 0) stmp += tmp - 1;
				}
				if(stmp > sum) sum = stmp;
			}
			a[i] = mtmp;a[n-1-i] = mtmp;
		}
		for(i = 0;i < sn;i ++) hash[i] = 0;
		printf("%d\n",sum);
	}
	return 0;
}
/*
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;

#define MP make_pair
#define A first
#define B second

#define PB push_back
#define FR(i, a, b) for(int i=(a); i<(b); i++)
#define FOR(i, n) FR(i, 0, n)
#define RF(i, a, b) for(int i=(b)-1; i>=(a); i--)
#define ROF(i, n) RF(i, 0, n)
#define EACH(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it)

typedef long long ll;

int r, c;
ll grid[50][50], answer[50][50];;

void moo(ll key) {
	memset(grid, 0, sizeof(grid));
	FR(i, 1, c+1) 
		grid[1][i] = (key >> (i - 1)) % 2LL;
	FR(i, 1, r+1)
		FR(j, 1, c+1)
		grid[i+1][j] = grid[i][j] ^ grid[i][j-1] ^ grid[i][j+1] ^ grid[i-1][j];
	FR(j, 1, c+1)
		if(grid[r+1][j] != 0) return;
	FR(i, 1, r+1) FR(j, 1, c+1)
		answer[i][j] = grid[i][j];
}

ll mask[50][50];
ll lis[50];
int t;

int dot(ll a, ll b) {
	ll x = a & b;
	int res = 0;
	FOR(i, 60) res += ((x >> i) % 2LL);
	return res % 2;
}

void showmask(ll x) {
	FOR(i, c) printf("%lld", (x>>i)%2LL);
	printf("\n");
}

int leadingbit(ll x) {
	FOR(i, c) if((x>>i)%2LL == 1LL) return i;
	return -1;
}

ll findkey() {
	t = 0;
	memset(mask, 0, sizeof(mask));
	FR(i, 1, c+1) 
		mask[1][i] = (1LL<<(i-1));
	FR(i, 1, r+1)
		FR(j, 1, c+1)
		mask[i+1][j] = mask[i][j] ^ mask[i][j-1] ^ mask[i][j+1] ^ mask[i-1][j];
	t = 0;
	FR(j, 1, c+1)
		lis[t++] = mask[r+1][j];
	//FOR(i, t) {printf("%d   ", dot(lis[i], ((1LL<<40) - 1))); showmask(lis[i]);}
	int t1 = 0;
	FOR(i, c) {
		FR(j, t1, t) if((lis[j]>>i)%2LL == 1LL) {
			swap(lis[t1], lis[j]);
			break;
		}
		if((lis[t1] >> i)%2LL == 1LL) {
			t1++;
			FR(j, t1, t) if((lis[j]>>i)%2LL == 1LL)
				lis[j] = lis[j] ^ lis[t1-1];
		}
	}
	ll key = 0;
	ROF(i, c) {
		int i1 = 0;
		while(i1 < t && (leadingbit(lis[i1]) != i)) ++i1;
		//printf("%d:", i1);
		if(i1 < t) {
			if(dot(key, lis[i1])) key += (1LL<<i);
		}
		else key += (1LL<<i);
		//showmask(key);
	}
	//FOR(i, t) showmask(lis[i]);
	//showmask(key);
	return key;
}

int main() {
	//freopen("harm.in", "r", stdin);
	//freopen("harm.out", "w", stdout);
	
	int ct;
	scanf("%d", &ct);
	while(ct--) {
		memset(answer, 0, sizeof(answer));
		scanf("%d%d", &r, &c);
		moo(findkey());
		FR(i, 1, r+1) { 
			FR(j, 1, c+1) {
				//if(answer[i][j] ^ answer[i-1][j] ^ answer[i+1][j] ^ answer[i][j-1] ^ answer[i][j+1] != 0) {printf("FUBAR %d %d\n\n", i,j); assert(0);}
				printf("%d", answer[i][j]);
				if(j == c) printf("\n");
				else printf(" ");
			}
		}
	}
}


#include <iostream>
#include <string.h>
#include <math.h>
using namespace std ;

const int MAX = 100;
int mod = 10000;
int baselen =4;
typedef int type;
struct bint{
    type dig[MAX],len;
    bint(){len = 0;dig[0] = 0;}
};
//大数加大数。
void add(const bint &a,const bint &b,bint &c) 
{
 	 type i,carry;
 	 for(i = carry = 0;i <= a.len||i <= b.len||carry;i ++)
 	 {
	  	   if(i <= a.len) carry += a.dig[i];
	  	   if(i <= b.len) carry += b.dig[i];
	  	   c.dig[i] = carry%mod;
	  	   carry /= mod;
   	 }
   	 c.len = i-1;
}
//小数加大数。
void add(const bint& a,type  b,bint &c)
{
 	 type i;
 	 for(i = 0;i <= a.len||b;i ++)
 	 {
	  	   if(i <= a.len) b+= a.dig[i];
	  	   c.dig[i] = b%mod;
	  	   b /= mod;
   	 }
   	 c.len = i-1;
} 
//大数乘小数
void mul(const bint & a,const type &b,bint &c)
{
 	 type i,carry;
 	 for(i = carry = 0;i <= a.len||carry;i ++)
 	 {
	  	   if(i <= a.len) carry += b*a.dig[i];
	  	   c.dig[i] = carry%mod;
	  	   carry /= mod;
   	 }
   	 i --;
   	 while(i && (!c.dig[i])) i --;
   	 c.len = i;
} 
//大数乘大数
void mul(const bint &a,const bint &b,bint &c)
{
 	 type i,j,carry;
 	 for(i = a.len+b.len+1;i >= 0;i --) c.dig[i] = 0;
 	 for(i = 0;i <= a.len;i ++)
	 {
	    carry = 0;
		for(j = 0;j <= b.len||carry;j ++)
		{
			carry += c.dig[i+j];
			if(j <= b.len) carry += a.dig[i]*b.dig[j];
			c.dig[i+j] = carry%mod;
			carry /= mod;
		}
	 }
	 i = a.len+b.len+1;
	 while(i&&c.dig[i] == 0) i--;
	 c.len = i;
}
//大数除以小数  d是余数
void div(const bint &a,const type &b,bint &c,type & d)
{
	type i;
	for(i = a.len,d = 0;i >= 0;i --)
	{
		d = d*mod + a.dig[i];
		c.dig[i] = d/b;
		d = d%b;
	}
	i = a.len;
	while(i && c.dig[i] == 0) i --;
	c.len = i;
}


void print(int val)
{
	if(val <= 9) printf("%d",val);
	else printf("%c",val - 10 + 'A');
}

void outprint(int val,int y)
{
	if(val  == 0) return ;
	outprint(val/y,y);
	print(val%y);
}
int outp[100];
void chuli(bint & val,type y)
{
	int i,tmp = 0,j,ol;
	outprint(val.dig[val.len],y);
	for(i = val.len-1;i >= 0;i --)
	{
		tmp = tmp*mod + val.dig[i];
		ol = 0;
		while(tmp > 0)
		{
			outp[ol++] = tmp%y;
			tmp /= y;
		}
		for(j = ol;j < baselen-1;j ++)
			printf("0");
		for(j = ol-1;j >= 0;j --)
			print(outp[j]);
	}
}

int main()
{
	int t,x,y;
	int i,j,len,tmp;
	bint bx,tx,sum;
	char z[20];
	scanf("%d",&t);
	while(t --)
	{
		sum.dig[0] = 0; sum.len = 0;
		bx.dig[0] = 1; bx.len = 0;
		scanf("%d%d%s",&x,&y,z);
		
		mod = 1;
		baselen = 1;

		while(mod < 10000)
		{
			mod *= y;
			baselen ++;
		}
		len = strlen(z);
		if(z[0] == '0' && len == 1)
		{
			printf("0\n");
			continue;
		}
		for(i = len-1;i >= 0;i --)
		{
			if(z[i] >= '0' && z[i] <= '9') 
				tmp = z[i] - '0';
			else
				tmp = z[i] - 'A' + 10;
			
			mul(bx,tmp,tx);
			
			add(tx,sum,sum);
			mul(bx,x,tx);
			tmp = 0;
			add(tx,tmp,bx);
		}
		chuli(sum,y);
		printf("\n");
	}
	return 0;
}


/*
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
const int maxn = 10005;

int n,m;
int a[maxn],b[maxn],c[maxn];

int hash[maxn];
struct Node{
	int v,next;
};
Node mat[maxn];
int len;
void Add(int u,int s)
{
	mat[len].v = s;
	mat[len].next = hash[u];
	hash[u] = len ++;
}

int find(int u,int i,int j)
{
	int s = hash[u];
	while(s != -1)
	{
		if(mat[s].v != i && mat[s].v != j)
			return mat[s].v;
		s = mat[s].next;
	}
}
int main()
{
	bool cfind = false;
	len = 0;
	int s[4],tmp;
	int i,j;
	scanf("%d%d",&n,&m);
	for(i = 0;i <= m;i ++)
	{
		b[i] = c[i] = 0;
		hash[i] = -1;
	}
	for(i = 0;i < n;i ++)
	{
		scanf("%d",&a[i]);
		a[i] %= m;
		b[a[i]] = 1;
	}
	for(i = n-1;i >= 0;i --)
		Add(a[i],i+1);

	s[0] = s[1] = s[2] = maxn;
	for(i = 0;i < n;i ++)
	{
		for(j = i+1;j < n;j ++)
		{
			tmp = (a[i] + a[j])%m;
			tmp = (m - tmp)%m;
			c[tmp] = 1;
			c[a[i]] = 1;
			c[a[j]] = 1;
			if(c[tmp] <= b[tmp])
			{
				s[2] = find(tmp,i+1,j+1);
				s[0] = i+1;
				s[1] = j+1;
				break;
			}
		}
		if(s[0] != maxn) 
		{
			cfind = true;
			break;
		}
	}
	sort(s,s+3);
	if(cfind)
		printf("%d %d\n %d\n",s[0],s[1],s[2]);
	else
		printf("-1\n");
	return 0;
}

/*
#include "stdio.h"
#include "string.h"
#define maxn 20201

int wa[maxn],wb[maxn],wv[maxn],wn[maxn];
int cmp(int *r,int a,int b,int l)
{return r[a]==r[b]&&r[a+l]==r[b+l];}
void da(int *r,int *sa,int n,int m)
{
     int i,j,p,*x=wa,*y=wb,*t;
     for(i=0;i<m;i++) wn[i]=0;
     for(i=0;i<n;i++) wn[x[i]=r[i]]++;
     for(i=1;i<m;i++) wn[i]+=wn[i-1];
     for(i=n-1;i>=0;i--) sa[--wn[x[i]]]=i;
     for(j=1,p=1;p<n;j*=2,m=p)
     {
       for(p=0,i=n-j;i<n;i++) y[p++]=i;
       for(i=0;i<n;i++) if(sa[i]>=j) y[p++]=sa[i]-j;
       for(i=0;i<n;i++) wv[i]=x[y[i]];
       for(i=0;i<m;i++) wn[i]=0;
       for(i=0;i<n;i++) wn[wv[i]]++;
       for(i=1;i<m;i++) wn[i]+=wn[i-1];
       for(i=n-1;i>=0;i--) sa[--wn[wv[i]]]=y[i];
       for(t=x,x=y,y=t,p=1,x[sa[0]]=0,i=1;i<n;i++)
       x[sa[i]]=cmp(y,sa[i-1],sa[i],j)?p-1:p++;
     }
     return;
}

char c[maxn];
int r[maxn],n,sa[maxn];
int main()
{
	scanf("%s",c);
	int i,j,len;
	len = strlen(c);
	for(i = 0;i < len;i ++)
		r[i] = c[i];
	da(r,sa,len+1,200);
	return 0;
}
/*
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

//skind 红 1 或者黑 0
const int Maxn = 15;

int c[Maxn][Maxn];
bool gameover;

struct King{
	int x,y;
};

King kg[2]; //黑0，红 1

bool kingFaceToFace()
{
	int i;
	if(kg[0].y == kg[1].y)
	{
		for(i = kg[0].x+1;i < kg[1].x;i ++)
			if(c[i][kg[0].y] != 0) return false;
		return true;
	}
	return false;
}

bool safe(int x,int y)
{
	if(x >= 1 && x <= 10 && y >= 1 && y <= 9) return true;
	return false;
}

bool checkKing(int skind,int x,int y)  //仅判断位置是否合法,没有判断跳过去吃 将
{
	if(skind == 0){
		if(x >= 1 && x <= 3 && y >= 4 && y <= 6)
			return true;
	}else{
		if(x >= 8 && x <= 10 && y >= 4 && y <= 6)
			return true;
	}
	return false;
}

bool checkMandarins(int skind,int x,int y)   //士
{
	if(skind == 0){
		if((x == 1 || x == 3) && (y == 4 || y == 6)) return true;
		if(x == 2 && y == 5) return true;
		
	}else{
		if((x == 8 || x == 10) && (y == 4 || y == 6)) return true;
		if(x == 9 && y == 5) return true;

	}
	return false;
}

bool checkElephants(int skind,int x,int y)  //象
{
	if(skind == 0){
		if((x == 1 || x == 5) && (y == 3 || y == 7)) return true;
		if(x == 3 && (y == 1 || y == 5 || y == 9)) return true;
		
	}else{
		if((x == 6 || x == 10) && (y == 3 || y == 7)) return true;
		if(x == 8 && (y == 1 || y == 5 || y == 9)) return true;
		
	}
	return false;
}

bool checkKnights(int fx,int fy,int x,int y)  //马，挡马脚  8方向
{
	int dx,dy;
	dx = x-fx; dy = y-fy;
	if((abs(dx) == 2 && abs(dy) == 1) || (abs(dx) == 1 && abs(dy) == 2)){

		dx /= 2; dy /= 2;
		if(c[fx+dx][fy+dy] == 0) return true; //用c，没有给绊马脚
	}
	return false;
}

bool checkRooks(int fx,int fy,int x,int y)  //车，没有检测终点，（颜色相同不可以吃）
{
	int s,e;
	if(fx == x){
		s = min(fy,y)+1; e = max(fy,y);
		while(s < e)
		{
			if(c[x][s] != 0) return false;
			s ++;
		}
		return true;
	}else if(fy == y){
		s = min(fx,x)+1; e = max(fx,x);
		while(s < e)
		{
			if(c[s][y] != 0) return false;
			s ++;
		}
		return true;
	}
	return false;
}

bool checkCannons(bool Eat,int fx,int fy,int x,int y)  //炮，是走 false 还是吃  true
{
	int s,e,cs;
	if(fx == x){
		cs = 0;
		s = min(fy,y)+1; e = max(fy,y);
		while(s < e)
		{
			if(c[x][s] != 0)  cs ++;
			s ++;
		}
		if(cs > 1) return false;
		if(Eat && cs == 1) return true;  //吃，有个在中间
		if((!Eat) && cs == 0) return true; //走，没有东西在中间
		
	}else if(fy == y){
		cs = 0;
		s = min(fx,x)+1; e = max(fx,x);
		while(s < e)
		{
			if(c[s][y] != 0)  cs ++;
			s ++;
		}
		if(cs > 1) return false;
		if(Eat && cs == 1) return true;  //吃，有个在中间
		if((!Eat) && cs == 0) return true; //走，没有东西在中间
		
	}
	return false;
}

bool checkPawns(int skind,int fx,int fy,int x,int y)
{
	if(abs(x-fx)+abs(y-fy) != 1) return false;
	if(skind == 0)
	{
		//没有过河前
		if(fx <= 5 && x-fx == 1) return true;
		if(fx > 5 && x >= fx) return true;
	}else
	{
		if(fx >= 6 && x-fx == -1) return true;
		if(fx < 6 && x <= fx) return true;
	}
	return false;
}

int getkind(int x,int y)
{
	if(c[x][y] >= 8) return 0;  //黑
	else return 1;   //红
}

void checkGameover(int x,int y)
{
	if(c[x][y] == 1 || c[x][y] == 8) gameover = true;
}

bool check(int skind,int fx,int fy,int x,int y)
{
	bool eat;
	if(fx == x && fy == y) return false;
	int tmp;
	if(gameover) return false;
	if(safe(x,y))
	{
		if(c[fx][fy] == 0) return false;

		tmp = getkind(fx,fy);
		if(tmp != skind) return false; //走的棋子不是自己的

		if(c[x][y] == 0) eat = false;
		else
		{
			tmp = getkind(x,y);
			if(tmp == skind)   return false; // 棋子走的位置有自己的棋子占着
			eat = true;
		}
		if(c[fx][fy] == 1 || c[fx][fy] == 8)  //将
		{
			if(abs(fx-x) + abs(fy-y) != 1) return false;
			if(fy == y && (c[x][y] == 1 || c[x][y] == 8)) //将军
			{
				checkGameover(x,y);
				return true;
			}
			if(checkKing(skind,x,y)) //方框里面走
			{
				kg[skind].x = x; //更新将军
				kg[skind].y = y;
				c[x][y] = c[fx][fy];
				c[fx][fy] = 0;
				if((!gameover) && kingFaceToFace()) return false;
				return true;
			}
		}else if(c[fx][fy] == 2 || c[fx][fy] == 9) //士
		{
			if(abs(x-fx) == 1 && abs(y-fy)==1)
			{
				if(checkMandarins(skind,x,y))
				{
					c[x][y] = c[fx][fy];
					c[fx][fy] = 0;
					if((!gameover) && kingFaceToFace()) return false;
					return true;
				}
			}
		}else if(c[fx][fy] == 3 || c[fx][fy] == 10) //相
		{
			int dx,dy;
			dx = x-fx; dy = y-fy;
			if(abs(dx) == 2 && abs(dy) == 2)
			{
				dx /= 2;  dy /= 2;
				if(c[fx+dx][fy+dy] == 0) //没有给挡道
				{
					if(checkElephants(skind,x,y))
					{
						c[x][y] = c[fx][fy];
						c[fx][fy] = 0;
						if((!gameover) && kingFaceToFace()) return false;
						return true;
					}
				}
			}			
		}else if(c[fx][fy] == 4 || c[fx][fy] == 11) //马
		{
			if(checkKnights(fx,fy,x,y))
			{
				checkGameover(x,y);
				c[x][y] = c[fx][fy];
				c[fx][fy] = 0;
				if((!gameover) && kingFaceToFace()) return false;
				return true;
			}
		}else if(c[fx][fy] == 5 || c[fx][fy] == 12) //车
		{
			if(checkRooks(fx,fy,x,y))
			{
				checkGameover(x,y);
				c[x][y] = c[fx][fy];
				c[fx][fy] = 0;
				if((!gameover) && kingFaceToFace()) return false;
				return true;
			}
		}else if(c[fx][fy] == 6 || c[fx][fy] == 13) //炮
		{
			if(checkCannons(eat,fx,fy,x,y))
			{
				checkGameover(x,y);
				c[x][y] = c[fx][fy];
				c[fx][fy] = 0;
				if((!gameover) && kingFaceToFace()) return false;
				return true;
			}
		}else if(c[fx][fy] == 7 || c[fx][fy] == 14) //卒
		{
			if(checkPawns(skind,fx,fy,x,y))
			{
				checkGameover(x,y);
				c[x][y] = c[fx][fy];
				c[fx][fy] = 0;
				if((!gameover) && kingFaceToFace()) return false;
				return true;
			}
		}
	}
	return false;
}

int main()
{
	bool legal;
	int fx,fy,x,y;

	int n,k;  //k == 0 红先
	int t,ncase,step,i,j;
	ncase = 0;
	scanf("%d",&t);
	while(t --)
	{
		gameover = false;
		legal = true;
		step = 0;

		for(i = 1;i <= 10;i ++)
			for(j = 1;j <= 9;j ++)
			{
				scanf("%d",&c[i][j]);
				if(c[i][j] == 1) kg[1].x = i,kg[1].y = j;
				else if(c[i][j] == 8) kg[0].x = i,kg[0].y = j;
			}
		scanf("%d%d",&n,&k);
		k = 1^k;

		for(i = 1;i <= n;i ++)
		{
			scanf("%d%d%d%d",&fx,&fy,&x,&y);
			if(step != 0) continue;
			if(!check(k,fx,fy,x,y))
			{
				step = i;
				legal = false;
			}
			k = 1^k;
		}

		ncase ++;
		printf("Case %d: ",ncase);
		if(legal) printf("Legal move\n");
		else
		{
			printf("Illegal move on step %d\n",step);
		}
	}
	return 0;
}
/*
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define Max 8000000

struct Node{
	int s,a;
	Node():s(0),a(0){};
};

Node Tree[Max];
int n,m;

void Add(int rootx,int Lx,int Ly,int Rx,int Ry,int x1,int y1,int x2,int y2,int a)
{
	if(Lx == x1 && Ly == y1 && Rx == x2 && Ry == y2)
	{
		Tree[rootx].a += a;
		return ;
	}else
	{
		if(Tree[rootx].a != 0)
		{
			Tree[rootx].s += Tree[rootx].a*(Ry-Ly+1)*(Rx-Lx+1);
			Tree[rootx*4+1].a += Tree[rootx].a;
			Tree[rootx*4+2].a += Tree[rootx].a;
			Tree[rootx*4+3].a += Tree[rootx].a;
			Tree[rootx*4+4].a += Tree[rootx].a;
			Tree[rootx].a = 0;
		}
		Tree[rootx].s += (y2-y1+1)*(x2-x1+1)*a;
		int midx,midy;
		midx = (Lx+Rx)>>1;
		midy = (Ly+Ry)>>1;
		if(x1 <= midx && y1 <= midy)
			Add(rootx*4+1,Lx,Ly,midx,midy,x1,y1,min(midx,x2),min(midy,y2),a);
		if(x2 > midx && y1 <= midy)
			Add(rootx*4+2,midx+1,Ly,Rx,midy,max(x1,midx+1),y1,x2,min(midy,y2),a);
		if(x1 <= midx && y2 > midy)
			Add(rootx*4+3,Lx,midy+1,midx,Ry,x1,max(y1,midy+1),min(x2,midx),y2,a);
		if(x2 > midx && y2 > midy)
			Add(rootx*4+4,midx+1,midy+1,Rx,Ry,max(x1,midx+1),max(y1,midy+1),x2,y2,a);
	}
}

int Queue(int rootx,int Lx,int Ly,int Rx,int Ry,int x1,int y1,int x2,int y2)
{
	int sum = 0;
	if(Lx == x1 && Ly == y1 && Rx == x2 && Ry == y2)
	{
		sum = Tree[rootx].s + Tree[rootx].a*(Ry-Ly+1)*(Rx-Lx+1);
	}else
	{
		if(Tree[rootx].a != 0)
		{
			Tree[rootx].s += Tree[rootx].a*(Ry-Ly+1)*(Rx-Lx+1);
			Tree[rootx*4+1].a += Tree[rootx].a;
			Tree[rootx*4+2].a += Tree[rootx].a;
			Tree[rootx*4+3].a += Tree[rootx].a;
			Tree[rootx*4+4].a += Tree[rootx].a;
			Tree[rootx].a = 0;
		}
		int midx,midy;
		midx = (Lx+Rx)>>1;
		midy = (Ly+Ry)>>1;
		if(x1 <= midx && y1 <= midy)
			sum += Queue(rootx*4+1,Lx,Ly,midx,midy,x1,y1,min(midx,x2),min(midy,y2));
		if(x2 > midx && y1 <= midy)
			sum += Queue(rootx*4+2,midx+1,Ly,Rx,midy,max(x1,midx+1),y1,x2,min(midy,y2));
		if(x1 <= midx && y2 > midy)
			sum += Queue(rootx*4+3,Lx,midy+1,midx,Ry,x1,max(y1,midy+1),min(x2,midx),y2);
		if(x2 > midx && y2 > midy)
			sum += Queue(rootx*4+4,midx+1,midy+1,Rx,Ry,max(x1,midx+1),max(y1,midy+1),x2,y2);
	}
	return sum;
}
char getc()
{
	char c;
	while(c = getchar())
		if(c == 'X' || c == 'L' || c == 'k'|| c == EOF) break;
	return c;
}
int scan()
{
	char c;
	int num,sign;
	num = sign = 0;
	while(c = getchar())
		if(c == '-' || (c >= '0' && c <= '9')) break;
	if(c == '-') sign = 1;
	else num = c - '0';
	while(c = getchar())
		if(c >= '0' && c <= '9') num = num*10 + c - '0';
		else break;
	if(sign) return -num;
	else return num;
}

int main()
{
	char c;
	int x1,y1,x2,y2,a;
	c = getc();
	n = scan(); m = scan();
	//scanf("%s%d%d",c,&n,&m);
	while(1)
	{
		c = getc();
		if(c == EOF) break;
		if(c == 'L')
		{
			x1 = scan(); y1 = scan(); x2 = scan(); y2 = scan(); a = scan();
			//scanf("%d%d%d%d%d",&x1,&y1,&x2,&y2,&a);
			Add(0,1,1,n,m,x1,y1,x2,y2,a);
		}else if(c == 'k'){
			x1 = scan(); y1 = scan(); x2 = scan(); y2 = scan(); 
			//scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			a = Queue(0,1,1,n,m,x1,y1,x2,y2);
			printf("%d\n",a);
		}
	}
	return 0;
}
*/
/*
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define Max(x,y) (x)>(y)?(x):(y)
struct Q
{
    double x, y;
}q[100001], sl[10], sr[10];

int cntl, cntr, lm, rm;
double ans;

int cmp(const void*p1, const void*p2)
{
    struct Q*a1=(struct Q*)p1;
    struct Q*a2=(struct Q*)p2;
    if (a1->x<a2->x)return -1;
    else if (a1->x==a2->x)return 0;
    else return 1;
}

double CalDis(double x1, double y1, double x2, double y2)
{
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

void MinDis(int l, int r)
{
    if (l==r) return;
    double dis;
    if (l+1==r)
    {
        dis=CalDis(q[l].x,q[l].y,q[r].x,q[r].y);
        if (ans>dis) ans=dis;
        return;
    }
    int mid=(l+r)>>1, i, j;
    MinDis(l,mid);
    MinDis(mid+1,r);

    lm=mid+1-5;
    if (lm<l) lm=l;
    rm=mid+5;
    if (rm>r) rm=r;

    cntl=cntr=0;
    for (i=mid;i>=lm;i--)
    {
        if (q[mid+1].x-q[i].x>=ans)break;
        sl[++cntl]=q[i];
    }
    for (i=mid+1;i<=rm;i++)
    {
        if (q[i].x-q[mid].x>=ans)break;
        sr[++cntr]=q[i];
    }

    for (i=1;i<=cntl;i++)
        for (j=1;j<=cntr;j++)
        {
            dis=CalDis(sl[i].x,sl[i].y,sr[j].x,sr[j].y);
            if (dis<ans) ans=dis;
        }
}

int main ()
{
    int n, i,t;
	scanf("%d",&t);
    while (t--)
    {
		scanf("%d",&n);
        for (i=1;i<=n;i++)
            scanf("%lf %lf", &q[i].x,&q[i].y);
        qsort(q+1,n,sizeof(struct Q),cmp);
        ans=CalDis(q[1].x,q[1].y,q[2].x,q[2].y);
        MinDis(1,n);
        printf("%.2lf\n",ans);
    }
    return 0;
}*/