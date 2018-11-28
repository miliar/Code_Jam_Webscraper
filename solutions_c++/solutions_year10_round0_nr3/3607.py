/*#include<iostream>
#include<cmath>
using namespace std;
#define bint long long

//基于素数筛选法，计算欧拉函数phi[1] to phi[MAX],复杂度约为n，很快
//传入三个数组:
//phi[]用于存放欧拉函数
//prime[]用来存放小于i的所有素数，这里其实是一个模拟堆栈
//isprime[]用来标志该数是不是素数，初始值为0
/**/////////////////////BEGEIN_TEMPLATE_BY_ABILITYTAO_ACM/////////////////////////
/*
#define MAX 2000000

bint prime[MAX+1]={0};
bool isprime[MAX+1]={0};
int get_phi()//这是一个基于素数筛选的线性算法，很快
{
	bint i,j;
	bint len=0;
	for(i=2;i<=MAX;i++)
	{

		if(isprime[i]==false) //false代表是质数
			prime[++len]=i;
		for(j=1;j<=len&&prime[j]*i<=MAX;j++)
		{
			isprime[prime[j]*i]=true;//true代表是合数
			if(i%prime[j]==0)
				break;
		}

	}
	return len;
}


bint muti_mod(bint a,bint b,bint n){
	bint exp = a%n, res = 0;
	while(b)
	{
		if(b&1)
		{
			res += exp;
			if(res>=n) res -= n;
		}
		exp <<= 1;
		if(exp>n) exp -= n;

		b>>=1;
	}
	return res;
}

// ret = (a^b)%n 
bint mod_exp(bint a,bint p,bint m){ 
	bint exp=a%m, res=1; //   
	while(p>1)
	{
		if(p&1)// 
			res=muti_mod(res,exp,m);
		exp = muti_mod(exp,exp,m);
		p>>=1;
	}
	return muti_mod(res,exp,m);
}


bint getx(bint n,bint x)//计算n!中质因子x的出现次数
{
	if(n==0)
		return 0;
	return n/x+getx(n/x,x);
}

bint a[MAX+1];

int main()
{
	int t;
	int len=get_phi();
	bint n,m;
	scanf("%d",&t);
	while(t--)
	{
		memset(a,0,sizeof(a));
		scanf("%lld%lld",&n,&m);//现在要算C(n+m,n)
		int i;
		for(i=1;i<=len;i++)
		{
			if(prime[i]>n+m)
				break;
			a[i]=getx(n+m,prime[i]);
		}
		for(i=1;i<=len;i++)
		{
			if(prime[i]>n)
				break;
			
			a[i]-=getx(n,prime[i]);
		}
		for(i=1;i<=len;i++)
		{
			if(prime[i]>m)
				break;
			a[i]-=getx(m,prime[i]);
		}
		int tt=n+1;
		for(i=1;i<=len;i++)
		{
			if(tt==1)
				break;
			while(tt%prime[i]==0)
			{
				a[i]--;
				tt/=prime[i];
			}

		}
		tt=(n-m+1);
		for(i=1;i<=len;i++)
		{
			if(tt==1)
				break;
			while(tt%prime[i]==0)
			{
				a[i]++;
				tt/=prime[i];
			}

		}

		bint res=1;
		for(i=1;i<=len;i++)
		{
			
			if(a[i]==0)
				continue;
			bint t=mod_exp(prime[i],a[i],20100501);
			res*=t;
				res%=20100501;
		}
		printf("%I64d\n",res);
	}
	return 0;



}

*/
/*
#include <map>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
const int maxn=1010;
map<string,int> mmap;
struct node
{

	string name;
	int a,b,c;
	bool operator <(node other)
	{

		if(a!=other.a)
			return a>other.a;
		else if(b!=other.b)
			return b>other.b;
		else if(c!=other.c)
			return c>other.c;
		return name<other.name;
	}
}arr[maxn];

void init(int n)
{

	int i;
	for(i=1;i<=n;i++)
		arr[i].a=arr[i].b=arr[i].c=0;
}

int main()
{
	int t;
	int n,m;
	int i,j;
	int casenum=0;
	scanf("%d",&t);
	while(t--)
	{
		
		casenum++;


		
		scanf("%d",&n);
		init(n);
		for(i=1;i<=n;i++)
		{
			string t;
			cin>>t;
			mmap[t]=i;
			arr[i].name=t;
		}
		scanf("%d",&m);
		for(i=1;i<=m;i++)
		{
			string t;
			cin>>t;

			cin>>t;
			int tt=mmap[t];
			arr[tt].a++;

			cin>>t;
			tt=mmap[t];
			arr[tt].b++;

			cin>>t;
			tt=mmap[t];
			arr[tt].c++;
			
		}

		sort(arr+1,arr+1+n);
	//	reverse(arr+1,arr+1+n);
		for(i=1;i<=n;i++)
		{
			cout<<arr[i].name<<' '<<arr[i].a<<' '<<arr[i].b<<' '<<arr[i].c<<endl;
		}
		cout<<endl;
	}
	return 0;
}

*/

/*
#include <stdlib.h>
#include<iostream>
#define eps 1e-8
#define zero(x) (((x)>0?(x):-(x))<eps)
struct point{double x,y;};

//计算cross product (P1-P0)x(P2-P0)
double xmult(point p1,point p2,point p0){
	return (p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y);
}
//graham算法顺时针构造包含所有共线点的凸包,O(nlogn)
point p1,p2;
int graham_cp(const void* a,const void* b){
	double ret=xmult(*((point*)a),*((point*)b),p1);
	return zero(ret)?(xmult(*((point*)a),*((point*)b),p2)>0?1:-1):(ret>0?1:-1);
}
void _graham(int n,point* p,int& s,point* ch){
	int i,k=0;
	for (p1=p2=p[0],i=1;i<n;p2.x+=p[i].x,p2.y+=p[i].y,i++)
		if (p1.y-p[i].y>eps||(zero(p1.y-p[i].y)&&p1.x>p[i].x))
			p1=p[k=i];
	p2.x/=n,p2.y/=n;
	p[k]=p[0],p[0]=p1;
	qsort(p+1,n-1,sizeof(point),graham_cp);
	for (ch[0]=p[0],ch[1]=p[1],ch[2]=p[2],s=i=3;i<n;ch[s++]=p[i++])
		for (;s>2&&xmult(ch[s-2],p[i],ch[s-1])<-eps;s--);
}

//构造凸包接口函数,传入原始点集大小n,点集p(p原有顺序被打乱!)
//返回凸包大小,凸包的点在convex中
//参数maxsize为1包含共线点,为0不包含共线点,缺省为1
//参数clockwise为1顺时针构造,为0逆时针构造,缺省为1
//在输入仅有若干共线点时算法不稳定,可能有此类情况请另行处理!
//不能去掉点集中重合的点
int graham(int n,point* p,point* convex,int maxsize=1,int dir=0){
	point* temp=new point[n];
	int s,i;
	_graham(n,p,s,temp);
	for (convex[0]=temp[0],n=1,i=(dir?1:(s-1));dir?(i<s):i;i+=(dir?1:-1))
		if (maxsize||!zero(xmult(temp[i-1],temp[i],temp[(i+1)%s])))
			convex[n++]=temp[i];
	delete []temp;
	return n;
}

point p[2020];
point res[2020];
int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<2*n;i++)
			scanf("%lf%lf",&p[i].x,&p[i].y);
		if(n==1)
		{
			printf("%.3lf %.3lf\n",(p[0].x+p[1].x)/2,(p[0].y+p[1].y)/2);
			continue;
		}
		else
		{

			graham(2*n,p,res);
		}
		printf("%.3lf %.3lf\n",(p[0].x+p[n].x)/2,(p[0].y+p[n].y)/2);

	}
	return 0;


}
*/

/*

#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;

struct node
{
	int dir;
	int pre;
	int step;
	char x[10];
}l[400000];


char x[15];
char ansx[15]="123456780";
int perm[] = {1,1,2,6,24,120,720,5040,40320};//n！ 
int d[] = {-1,-3, 1, 3};//四个方向的下标变换,左上右下。
bool move[][4] = {0,0,1,1, 1,0,1,1, 1,0,0,1, 0,1,1,1, 1,1,1,1, 1,1,0,1, 0,1,1,0, 1,1,1,0, 1,1,0,0}; 
//各个位置的可行变换
int v[362881];//数组判重
int hash()//用逆序数和变进制进行hash 
{ 
	int h = 0; 
	for(int i = 1;i<9;i++)
	{ 
		int count = 0; 
		for(int j=0;j<i;j++) 
			if(x[j] > x[i])count ++; 
		h += count * perm[i]; 
	} 
	return h; 
} 




int pos;
void search(char x[])
{
	for(int i=0;i<9;i++)
		if(x[i]=='0')
		{
			pos=i;
			break;
		}

}
char ans[4000000]={0};
void GetDir(int h)
{
	memset(ans,0,sizeof(ans));
	int i;
	int n=l[h].step;
	ans[n+1]=0;
	for(i=n;i>=1;i--)
	{
		
		if(l[h].dir==0)
			ans[i]='l';
		else if(l[h].dir==1)
			ans[i]='u';
		else if(l[h].dir==2)
			ans[i]='r';
		else if(l[h].dir==3)
			ans[i]='d';
		h=l[h].pre;
	}
}



int main()
{
	

	int head,tail;

	char t[5];
	while(scanf("%s",t)!=EOF)
	{

	
		x[0]=t[0];
		for(int i=0;i<9;i++)
		{
			scanf("%s",t);
			x[i]=t[0];
			if(x[i]=='x')
				x[i]='0';
		}
		memset(v,0,sizeof(int)*362881);
		head=tail=1;
	
		//
		int code=hash();
		v[code]=1;
		l[head].step=0;
		l[head].pre=-1;
		strcpy(l[head].x,x);
		//initial

		while(head<=tail)
		{
			if(strcmp(l[head].x,ansx)==0)
				break;//此时head为所求解
			search(l[head].x);
			for(int i=0;i<4;i++)
			{
				if(move[pos][i]==0)
					continue;
				strcpy(x,l[head].x);
				int np=pos+d[i];
				swap(x[pos],x[np]);
				int code=hash();
				if(!v[code])
				{
					
					tail++;
					v[code]=1;
					l[tail].step=l[head].step+1;
					l[tail].pre=head;
					l[tail].dir=i;
					strcpy(l[tail].x,x);
				}

			}
			head++;
		}
		if(head>tail)
			printf("unsolvable\n");
		else
		{
			GetDir(head);
			printf("%s\n",ans+1);
		}
	}


	return 0;
}
*/

/*
#include<iostream>
#include<cstring>
using namespace std;
int dp[10][100]=
{
	{1,2,4,8,16,20,39,62,116,152,286,396,748,1024,1893,2512,4485,5638,9529,10878,16993,17110,23952,20224,24047,15578,14560,6274,3910,760,221,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{1,3,5,10,14,28,42,80,108,202,278,524,726,1348,1804,3283,4193,7322,8596,13930,14713,21721,19827,25132,18197,18978,9929,7359,2081,878,126,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{1,4,8,8,16,32,60,72,136,200,376,512,964,1296,2368,3084,5482,6736,11132,12208,18612,18444,24968,19632,22289,13600,11842,4340,2398,472,148,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
};


char s[5][5];

void input()
{

	int i,j;
	for(i=0;i<3;i++)
		for(j=0;j<3;j++)
		{
			cin>>s[i][j];
		}
}

int search()
{

	int p=0;
	int i,j;
	for(i=0;i<3;i++)
		for(j=0;j<3;j++)
		{

			if(s[i][j]=='0')
				return p;
			p++;
		}
}


int main()
{

	int t;
	scanf("%d",&t);
	while(t--)
	{
		input();
		int pos=search();
		int q;
		scanf("%d",&q);
		for(int i=1;i<=q;i++)
		{
			int t;
			scanf("%d",&t);
			if((pos==0||pos==2||pos==6||pos==8)&&t<=50)
				printf("%d\n",dp[0][t]);
			else if(pos==4&&t<=50)
				printf("%d\n",dp[2][t]);
			else if(t<=50)
				printf("%d\n",dp[1][t]);
			else
				printf("0\n");
		}


	}
	return 0;
}
*/
/*

#include<iostream>
#include<algorithm>
using namespace std;
#define INF 999999999
int n,m;
int a[1010];
int dp[1010];
int sum[1010];

bool check(int mid)
{
	int i,j;
	memset(dp,0,sizeof(dp));
	for(i=1;i<=n;i++)
	{
		dp[i]=INF;
		for(j=0;j<i;j++)
		{
			if(sum[i]-sum[j]<=mid)
					dp[i]=min(dp[i],dp[j]+1);
		}
	}
	if(dp[n]<=m)
		return true;
	else
		return false;
}

int main()
{
	int t;

	int i,j;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			sum[i]=sum[i-1]+a[i];
		}
		int l=-100000;
		int r=100000;
		int ans=-1;
		while(l<=r)
		{
			int mid=(l+r)>>1;
			if(check(mid))
			{
				r=mid-1;
				ans=mid;
			}
			else
			{

				l=mid+1;
			}
		}
		printf("%d\n",ans);
	
	}
	return 0;


}

*/
/*

#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;
const int maxn=1000;

int n,t;
struct point
{
	int x,y;
}p[maxn];

//注意该模板的结点n表示为0~n-1
//注意该模板的复杂度为n*O(bfs)，大概是平方级别
//除了clear()外，其他数组不需要清空，应该已经做了保护
//通过ZOJ 3316 Game数据测试，可用性较高
//2010年5月6日18:54:16
struct Graph {
	int n, match[maxn];//match用来保存调用max_match()后各个点的匹配信息
	bool adj[maxn][maxn];//用来保存边的信息，
	void clear() {
		memset(adj, 0, sizeof(adj));
		n = 0;//注意调用clear函数后，邻接矩阵会置成0，所以注意调用这个函数的时间啊
	}
	void insert(const int &u, const int &v) {
	//	get_max(n, max(u, v) + 1);
		adj[u][v] = adj[v][u] = 1;
	}
	int max_match() {
		memset(match, -1, sizeof(match));
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			if (match[i] == -1) {
				ans += bfs(i);
			}
		}
		return ans;
	}
	int Q[maxn], pre[maxn], base[maxn];
	bool hash[maxn];
	bool in_blossom[maxn];
	int bfs(int p) {
		memset(pre, -1, sizeof(pre));
		memset(hash, 0, sizeof(hash));
		for (int i = 0; i < n; ++i) {
			base[i] = i;
		}
		Q[0] = p;
		hash[p] = 1;
		for (int s = 0, t = 1; s < t; ++s) {
			int u = Q[s];
			for (int v = 0; v < n; ++v) {
				if (adj[u][v] && base[u] != base[v] && v != match[u]) {
					if (v == p || (match[v] != -1 && pre[match[v]] != -1)) {
						int b = contract(u, v);
						for (int i = 0; i < n; ++i) {
							if (in_blossom[base[i]]) {
								base[i] = b;
								if (hash[i] == 0) {
									hash[i] = 1;
									Q[t++] = i;
								}
							}
						}
					} else if (pre[v] == -1) {
						pre[v] = u;
						if (match[v] == -1) {
							argument(v);
							return 1;
						} else {
							Q[t++] = match[v];
							hash[match[v]] = 1;
						}
					}
				}
			}
		}
		return 0;
	}
	void argument(int u) {
		while (u != -1) {
			int v = pre[u];
			int k = match[v];
			match[u] = v;
			match[v] = u;
			u = k;
		}
	}
	void change_blossom(int b, int u) {
		while (base[u] != b) {
			int v = match[u];
			in_blossom[base[v]] = in_blossom[base[u]] = true;
			u = pre[v];
			if (base[u] != b) {
				pre[u] = v;
			}
		}
	}
	int contract(int u, int v) {
		memset(in_blossom, 0, sizeof(in_blossom));
		int b = find_base(base[u], base[v]);
		change_blossom(b, u);
		change_blossom(b, v);
		if (base[u] != b) {
			pre[u] = v;
		}
		if (base[v] != b) {
			pre[v] = u;
		}
		return b;
	}
	int find_base(int u, int v) {
		bool in_path[maxn] = {};
		while (true) {
			in_path[u] = true;
			if (match[u] == -1) {
				break;
			}
			u = base[pre[match[u]]];
		}
		while (!in_path[v]) {
			v = base[pre[match[v]]];
		}
		return v;
	}
};
//////////////////TEMPLATE_COLLECTED_BY_ABILITYTAO/////////////////////////////

Graph g;
int get(point a,point b)
{
	return abs(a.x-b.x)+abs(a.y-b.y);
}

void init()
{
	int i,j;
	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
		{
			if(get(p[i],p[j])<=t)
				g.insert(i,j);
		}


}
int main()
{
	while(scanf("%d",&n)!=EOF)
	{
		
		g.clear();
		g.n=n;//注意clear之后n被置成了0，要重新赋值
		
		int i;
		for(i=0;i<n;i++)
			scanf("%d%d",&p[i].x,&p[i].y);
		scanf("%d",&t);
		init();
		int ans=g.max_match();
		if((n-ans*2)!=0)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}
*/
/*

#include<iostream>
#include<cmath>
using namespace std;
typedef struct vir{
	double re,im;
	vir(){}
	vir(double a,double b){re=a;im=b;}
	vir operator +(const vir &b){ return vir(re+b.re,im+b.im);}
	vir operator -(const vir &b){ return vir(re-b.re,im-b.im);}
	vir operator *(const vir &b){ return vir(re*b.re-im*b.im,re*b.im+b.re*im);}
}vir;
vir x1[200005],x2[200005];
const double Pi = acos(-1.0);
void change(vir *x,int len,int loglen)
{
	int i,j,k,t;
	for(i=0;i<len;i++)
	{
		t = i;
		for(j=k=0;j<loglen;j++,t>>=1)
			k = (k<<1)|(t&1);
		if(k<i)
		{
			vir wt =  x[k];
			x[k] = x[i];
			x[i] = wt;
		}
	}
}
void fft(vir *x,int len,int loglen)
{
	int i,j,t,s,e;
	change(x,len,loglen);
	t = 1;
	for(i=0;i<loglen;i++,t<<=1)
	{
		s = 0;
		e = s + t;
		while(s<len)
		{
			vir a,b,wo(cos(Pi/t),sin(Pi/t)),wn(1,0);
			for(j=s;j<s+t;j++)
			{
				a = x[j];
				b = x[j+t]*wn;
				x[j] = a + b;
				x[j+t] = a - b;
				wn =wn*wo;
			}
			s = e+t;
			e = s+t;
		}
	}
}

void dit_fft(vir *x,int len,int loglen)
{
	int i,j,s,e,t=1<<loglen;
	for(i=0;i<loglen;i++)
	{
		t>>=1;
		s=0;
		e=s+t;
		while(s<len)
		{
			vir a,b,wn(1,0),wo(cos(Pi/t),-sin(Pi/t));
			for(j=s;j<s+t;j++)
			{
				a = x[j]+x[j+t];
				b = (x[j]-x[j+t])*wn;
				x[j] = a;
				x[j+t] = b;
				wn = wn*wo;
			}
			s = e+t;
			e = s+t;
		}
	}
	change(x,len,loglen);
	for(i=0;i<len;i++)
		x[i].re/=len;
}


int main()
{
	char a[100005],b[100005];
	int i,len1,len2,t,over,len,loglen;

	while(scanf("%s%s",a,b)!=EOF)
	{
		len1 = strlen(a)<<1;
		len2 = strlen(b)<<1;
		len = 1;
		loglen = 0;
		while(len<len1)
		{
			len<<=1;
			loglen++;
		}
		while(len<len2)
		{
			len<<=1;
			loglen++;
		}
		for(i=0;a[i]!='\0';i++)
		{
			x1[i].re = a[i]-'0';
			x1[i].im = 0;
		}
		for(;i<len;i++)
			x1[i].re = x1[i].im = 0;
		for(i=0;b[i]!='\0';i++)
		{
			x2[i].re = b[i]-'0';
			x2[i].im = 0;
		}
		for(;i<len;i++)
			x2[i].re = x2[i].im = 0;
		fft(x1,len,loglen);
		fft(x2,len,loglen);
		for(i=0;i<len;i++)
			x1[i] = x1[i]*x2[i];
		dit_fft(x1,len,loglen);
		for(i=(len1+len2)/2-2,over=loglen=0;i>=0;i--)
		{
			t = x1[i].re + over + 0.5;
			a[loglen++] = t%10;
			over =  t/10;
		}
		while(over)
		{
			a[loglen++] = over%10;
			over /= 10;
		}
		for(loglen--;loglen>=0&&!a[loglen];loglen--);
		if(loglen<0)
			putchar('0');
		else
			for(;loglen>=0;loglen--)
				putchar(a[loglen]+'0');
		putchar('\n');
	}
	return 0;
}

*/
/*
//福大的题目，有无数个建筑标号从1,2,3....inf
//其中有一些被摧毁了，问剩下的第k个建筑是几号
//线段树+离散化
//注意加了一个0号点，和无穷大的点
#include<iostream>
using namespace std;
//给定n个摧毁目标，在剩下的数字中第k个哪个数字，转化成线段树 
const int maxn=50005;
int a[maxn],b[maxn];
typedef struct node
{
	int l,r,val;
}node;
node tree[4*maxn]; 
void build(int k,int l,int r)
{
	tree[k].l=l;tree[k].r=r;
	if(l==r){tree[k].val=a[l+1]-a[l]-1;return ;}
	int mid=(l+r)>>1;
	build(k*2,l,mid);build(k*2+1,mid+1,r);
	tree[k].val=tree[k*2].val+tree[k*2+1].val;
}
int query(int k,int x)
{
	if(tree[k].l==tree[k].r){return a[tree[k].l]+x;}
	if(tree[k*2].val>=x)return query(k*2,x);
	else return query(k*2+1,x-tree[k*2].val);
} 
int main()
{
	int i,j,k,n,m,len;
	while(scanf("%d",&n)!=EOF)
	{
		for(i=0;i<n;i++)scanf("%d",&a[i]);
		a[n]=0;a[n+1]=1000000000;n+=2;
		sort(a,a+n);
		len=1;
		for(i=1;i<n;i++)if(a[i]!=a[i-1])a[len++]=a[i];//判重，收缩点
		build(1,0,len-2);//-2是因为len++和端点数从0开始
		scanf("%d",&m);
		for(i=0;i<m;i++)scanf("%d",&b[i]);
		for(i=0;i<m;i++)printf("%d\n",query(1,b[i]));
		printf("\n");
	}
	return 0;
} 
*/


#include <iostream>
using namespace std;

typedef long long ll;
int groups[1005];
int next[1005],sum[1005];

int main(){
	int tt,t,r,k,n,i,j;
	FILE *fin =fopen("C-small-attempt2.in","r");
	FILE *fout = fopen("QC.out","w");
	fscanf(fin,"%d",&t);
	tt = 0;
	while(t--){
		tt++;
		int tsum = 0;
		fscanf(fin,"%d %d %d",&r,&k,&n);
		for(i = 0; i < n; i++)
		{
			fscanf(fin,"%d",groups+i);
			tsum+=groups[i];
		}
		int index = 0;
		ll ans = 0;

		if(tsum <= k){
			ans = tsum * r;
		}
		else{
			for(i = 0; i < n; i++){
				tsum = 0;
				index = i;
				while(tsum+groups[index] <= k){
					tsum+=groups[index];
					index++;
					if(index == n)index = 0;
				}
				next[i] = index;
				sum[i] = tsum;
			}

			index = 0;
			for(i = 0; i < r; i++){
				ans+=ll(sum[index]);
				index = next[index];
			}
		}
		//printf("%d\n",tt);
		fprintf(fout,"Case #%d: %I64d\n",tt,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}