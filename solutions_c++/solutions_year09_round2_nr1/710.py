//pku
#include "iostream"
#include "sstream"
#include "iomanip"
#include "algorithm"
#include "string"
#include "functional"
#include "list"
#include "vector"
#include "stack"
#include "deque"
#include "set"
#include "map"
#include "utility"
#include "numeric"
#include "cmath"
using namespace std;

#define min(a, b) ((a)<(b)?(a):(b))
#define min3(a, b, c) ((a)<(b)?((a)<(c)?(a):(c)):((b)<(c)?(b):(c)))
#define max(a, b) ((a)>(b)?(a):(b))
#define max3(a, b, c) ((a)>(b)?((a)>(c)?(a):(c)):((b)>(c)?(b):(c)))

#define INF 0x7fffffff
#define Pi acos(-1.0)
#define  Eps 1e-6

#ifdef _GNUC_
#define int64 long long
#define Printf64(n) printf("%lld\n", n)
#else /* MSVC, say */
#define int64 __int64
#define Printf64(n) printf("%I64d\n", n)
#endif 

#define MAX 100

struct MyNode
{
	double p;
	string f;
	MyNode *lchild, *rchild, *pare;

	MyNode()
	{
		pare=lchild=rchild=0;
	}
}root;

string ff[100];
int cntFF;

int main()
{
	int i, j, k, n, m,  test, cnt=0;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 

	char buff[512];
	char ch;
	string str, name;
	double pp;

	scanf("%d", &test);
	int outC=0;
	while(test--)
	{
		//stack<char> s;
		root.lchild=root.rchild=0;
		MyNode *cp = &root, *q=0;

		int l;
		scanf("%d\n", &l);
		
		while(l--)
		{
			gets(buff);
			istringstream strin(buff);
			while(strin>>ch)
			{
				if(ch=='(')
				{
					q= new MyNode();
					if(cp->lchild==0)
						cp->lchild=q;
					else
						cp->rchild=q;
					q->pare=cp;
					cp=q;					
				}
				else if(ch==')')
				{
					cp=cp->pare;
				}
				else if(isdigit(ch))
				{
					strin.putback(ch);
					strin>>cp->p;
				}
				else
				{
					strin.putback(ch);
					strin>>cp->f;
				}
			}
		}

		printf("Case #%d:\n", ++outC);
		scanf("%d\n", &n);
		while(n--)
		{
			gets(buff);
			istringstream strin(buff);
			string fe;
			double res=1.0;

			strin>>name>>m;
			for(i=0; i<m; ++i)
				strin>>ff[i];
			cp=root.lchild;
			while(cp)
			{
				res*=cp->p;
				for(i=0; i<m; ++i)
					if(ff[i]==cp->f)
						break;
				if(i<m)
					cp=cp->lchild;
				else
					cp=cp->rchild;
			}
			printf("%.8lf\n", res);
		}
	}

	return 0;
}

