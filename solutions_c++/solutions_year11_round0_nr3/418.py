#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

long c[1001];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("data.out","w",stdout);
	int t, n, i, j, cas=1;
	long sum, min, s;

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		sum = 0; s = 0;
		for(i=0; i<n; i++)
		{
			scanf("%ld",&c[i]);
			sum += c[i];
			s ^= c[i];
			if(!i) min = c[i];
			else if(min > c[i])
				min = c[i];
		}

		printf("Case #%d: ",cas++);
		if(s) printf("NO\n");
		else printf("%ld\n",sum-min);
	}
	return 0;
}





//1001
//#include <iostream>
//#include <stdio.h>
//#include <string.h>
//#include <math.h>
//using namespace std;
//
//int main()
//{
//	int t, i, j;
//	double l, a, v, ans, time;
//
//	scanf("%d",&t);
//	while(t--)
//	{
//		scanf("%lf%lf%lf",&l,&a,&v);
//		double t1 = sqrt(l/a);
//		double t2 = v/a;
//
//		if(t1 <= t2) ans = 2*t1;
//		else
//		{
//			double s = a*t2*t2;
//			time = (l-s)/v;
//			ans = 2*t2 + time;
//		}
//
//		printf("%.16lf\n",ans);
//	}
//	return 0;
//}


//1002
//#include <iostream>
//#include <stdio.h>
//#include <string.h>
//using namespace std;
//
//int main()
//{
//	int t, i, n, a0;
//	double a, d, ans, b;
//
//	scanf("%d",&t);
//	while(t--)
//	{
//		scanf("%d%d",&a0,&n);
//		b = a0;
//		ans = 0.0; i = 1;
//		bool flag = true;
//		while (n--)
//		{
//			scanf("%lf",&a);
//			if(!flag) continue;
//			if(a < b) { flag = false; continue; }
//			b = a;
//			d = (a - a0)/(double)i;
//			i++;
//			if(ans < d) ans = d;
//		}
//		if(!flag) printf("-1\n");
//		else printf("%.16lf\n",ans);
//	}
//	return 0;
//}



//#include <iostream>
//#include <algorithm>
//#include <stdio.h>
//#include <string.h>
//using namespace std;
//
//struct node
//{
//	int num;
//	int time;
//	int k;
//}st[52];
//
//struct leave
//{
//	int time;
//	int k;
//}dep[52];
//
//int table[52];
//bool f[52], p[52];
//
//int cmp1(leave a, leave b)
//{
//	return a.time < b.time;
//}
//
//int main()
//{
//	int t, i, j, k, n1, n2, n3, n4, m, ans;
//
//	scanf("%d",&t);
//	while(t--)
//	{
//		scanf("%d",&n1);
//		for(i=0; i<n1; i++)
//		{
//			scanf("%d",&table[i]);
//			f[i] = false;
//		}
//		sort(table, table+n1);
//
//		scanf("%d",&n2);
//		for(i=0; i<n2; i++)
//			scanf("%d",&st[i].num);
//
//		scanf("%d",&n3);
//		for(i=0; i<n3; i++)
//		{
//			scanf("%d",&st[i].time);
//			p[i] = true;
//		}
//
//		scanf("%d",&n4);
//		for(i=0; i<n4; i++)
//		{
//			scanf("%d",&dep[i].time);
//			dep[i].k = i;
//		}
//		sort(dep, dep+n4, cmp1);
//
//		ans = 0;
//		m = n1; j = 0;
//		for(i=0; i<n2; i++)
//		{
//			while(p[dep[j].k] == false || st[i].time >= dep[j].time)
//			{
//				if(p[dep[j].k] == false)
//					j++;
//				if(st[i].time >= dep[j].time)
//				{
//					m ++;
//					f[st[j].k] = false;
//					j ++;
//				}
//			}
//			/*while(p[dep[j].k] == false)
//				j++;*/
//
//			//if(st[i].time < dep[j].time)
//			{
//				if(m == 0) { p[i] = false; ans += st[i].num; continue; }
//				for(k=0; k<n1; k++)
//					if(st[i].num <= table[k] && !f[k])
//					{
//						st[i].k = k;
//						m --;
//						f[k] = true;
//						break;
//					}
//				if(k >= n1) { ans += st[i].num; p[i] = false; }
//			}
//		}
//
//		printf("%d\n",ans);
//	}
//	return 0;
//}



//1006
//#include <iostream>
//#include <algorithm>
//#include <stdio.h>
//#include <string.h>
//using namespace std;
//
//struct post 
//{
//	long price;
//	bool flag;
//}p[10000];
//
//int cmp(post a, post b)
//{
//	return a.price < b.price;
//}
//
//int main()
//{
//	int t, i, j, n, m, k;
//	long sum, s;
//
//	scanf("%d",&t);
//	while(t--)
//	{
//		memset(p, 0, sizeof(p));
//		scanf("%d",&n);
//		for(i=0; i<n; i++)
//			scanf("%ld",&p[i].price);
//
//		scanf("%d",&m);
//		sum = 0;
//		for(i=0; i<m; i++)
//		{
//			scanf("%d",&k);
//			p[k].flag = 1;
//			sum += p[k].price;
//		}
//
//		if(m == n || m == 0) { printf("%d\n",m); continue; }
//
//		sort(p, p+n, cmp);
//
//		s = 0;
//		int num = 0;
//		for(i=0; i<n; i++)
//			if(s + p[i].price <= sum)
//			{
//				num ++;
//				s += p[i].price;
//			}
//			else break;
//
//		printf("%d\n",num);
//	}
//	return 0;
//}



//A
//#include <iostream>
//#include <stdio.h>
//#include <string.h>
//using namespace std;
//
//int main()
//{
//	int t, sz;
//	long i, j, n, k, end, st, ca, ans, s;
//
//	scanf("%d",&t);
//	while(t--)
//	{
//		//printf("\n");
//		scanf("%ld%ld",&n,&k);
//
//		scanf("%d",&sz);
//
//		ans = 0; st = 0; end = k - 1;
//		while (sz--)
//		{
//			scanf("%ld",&ca);
//			if(ca>=st && ca<=end) continue;
//			else
//			{
//				if(ca >= end)
//				{
//					s = ca - end;
//					if(s >= k) ans += k;
//					else ans += s;
//					
//					end = ca;
//					st = end - k + 1;
//				}
//				else
//				{
//					s = st - ca;
//					if(s >= k) ans += k;
//					else ans += s;
//
//					st = ca;
//					end = st + k - 1;
//				}
//			}
//		}
//		printf("%ld\n",ans);
//	}
//	return 0;
//}



//D
//#include <iostream>
//#include <stdio.h>
//#include <string.h>
//using namespace std;
//
//int num[10001];
//
//void getScore()
//{
//	memset(num, 0, sizeof(num));
//	for(int i=0; i<=100; i++)
//	{
//		for(int j=i; j<=100; j++)
//		{
//			int k = i*i + j*j;
//			if(k > 10000) break;
//			else
//			{
//				num[k] ++;
//			}
//		}
//	}
//}
//
//int main()
//{
//	int t, up, low, i, ans, k;
//
//	getScore();
//	scanf("%d",&t);
//	while(t--)
//	{
//		scanf("%d%d",&up,&low);
//		ans = 0; k = 0;
//		for(i=up; i<=low; i++)
//		{
//			if(ans < num[i]) 
//			{
//				ans = num[i];
//				k = i;
//			}
//			else if(ans == num[i])
//				k = i;
//		}
//		printf("%d\n",k);
//	}
//	return 0;
//}



//E
//#include <iostream>
//#include <stdio.h>
//#include <string.h>
//#include <string>
//using namespace std;
//#define inf 0xfffffff
//
//int t, n, a[51][30], len[51], ans, size;
////char s[52], word[51][52];
//string s, word[51];
//string temp;
//
//void dfs(int st, int sum)
//{
//	if(st == size)
//	{
//		if(ans > sum) ans = sum;
//		return;
//	}
//
//	int i, j, k;
//	for(i=st; i<size; i++)
//	{
//		int d;
//		for(j=0; j<n; j++)
//		{
//			if(size - i < len[j]) continue;
//			temp = s.substr(i, len[j]);
//			if(temp != word[j])
//			{
//				d = 0;
//				for(k=0; k<len[j]; k++)
//				{
//					if(a[j][temp[k]-'0'])
//					{
//						if(temp[k] != word[j][k])
//							d ++;
//					}
//					else
//					{
//						break;
//					}
//				}
//			}
//
//			if(k >= len[j]) dfs(i+len[j], sum+d);
//		}
//
//		if(j >= n) { break; }
//	}
//}
//
//int main()
//{
//	int t, i, j, k;
//
//	scanf("%d",&t);
//	getchar();
//	while (t--)
//	{
//		memset(a, 0, sizeof(a));
//		//gets(s);
//		cin >> s;
//		scanf("%d",&n);
//		for (i=0; i<n; i++)
//		{
//			//scanf("%s",word[i]);
//			//len[i] = strlen(word[i]);
//			cin >> word[i];
//			len[i] = word[i].size();
//			for(j=0; j<len[i]; j++)
//				a[i][word[i][j]-'0'] = 1;
//		}
//
//		size = s.size();
//		ans = 0;
//		bool flag = true;
//		for(i=0; i<size; i++)
//		{
//			int d, Min = -1, m;
//			for(j=0; j<n; j++)
//			{
//				if(size - i < len[j]) continue;
//				temp = s.substr(i, len[j]);
//				d = 0;
//				for(k=0; k<len[j]; k++)
//				{
//					if(a[j][temp[k]-'0'])
//					{
//						if(temp[k] != word[j][k])
//							d ++;
//					}
//					else
//					{
//						break;
//					}
//				}
//
//				if(k >= len[j])
//					if(Min == -1 || Min > d) { Min = d; m = len[j]; }
//				//if(k >= len[j]) { ans += d; i += len[j]-1; break; }
//			}
//
//			if(Min == -1) { flag = false; break; }
//			else { ans += Min; i += m - 1; }
//		}
//
//		if(flag) printf("%d\n",ans);
//		else printf("-1\n");
//
//		/*size = s.size();
//		ans = inf;
//		dfs(0, 0);
//
//		if(ans == inf) printf("-1\n");
//		else printf("%d\n",ans);*/
//	}
//	return 0;
//}



//G
//#include <iostream>
//#include <stdio.h>
//#include <string.h>
//using namespace std;
//
//int main()
//{
//	int t, n;
//	long long i, cs, a[51], ans, num;
//
//	scanf("%d",&t);
//	while (t--)
//	{
//		scanf("%d",&n);
//		for(i=0; i<n; i++)
//			scanf("%lld",&a[i]);
//		scanf("%lld",&cs);
//
//		ans = 0;
//		for(i=0; i<n; i++)
//		{
//			if(a[i] == 0) continue;
//			if(a[i] <= cs) ans += cs;
//			else
//			{
//				num = a[i]/cs;
//				ans += num * cs;
//				if(a[i]%cs != 0)
//					ans += cs;
//			}
//			
//		}
//		printf("%lld\n",ans);
//	}
//	return 0;
//}





//#include <iostream>
//#include <malloc.h>
//using namespace std;
//
//int next[400002], len, ans[400002];
//char s[400002];
//
//void Next()
//{
//	int i=1, j=0;
//	next[1] = 0;
//
//	while(i <= len)
//	{
//		if(j==0 || s[i-1] == s[j-1])
//		{
//			i++; j++;
//			next[i] = j;
//		}
//		else j = next[j];
//	}
//}
//
//int main()
//{
//	int i, k;
//
//	while(scanf("%s",s) != EOF)
//	{
//		len = strlen(s);
//		Next();
//		ans[0] = len;
//		i = len; k = 1;
//		while(i != 1)
//		{
//			if(next[i] != 1)
//				ans[k++] = next[i];
//			i = next[i];
//		}
//
//		for(i=k-1; i>0; i--)
//			printf("%d ",ans[i]);
//		printf("%d\n",ans[0]);
//	}
//	return 0;
//}



//1001 Daydream
//#include <iostream>
//#include <string>
//using namespace std;
//
//char ch;
//
//int main()
//{
//	long n, i, max, start, end, a, b;
//	long f[300];
//
//	while(scanf("%ld",&n) != EOF)
//	{
//		getchar();
//		memset(f, -1, sizeof(f));
//		max = 0; a = b = 0;
//		for(i=0; i<n; i++)
//		{
//			scanf("%c",&ch);
//			if(f[ch] == -1) f[ch] = i;
//			else
//			{
//				b = i - 1;
//				if(max < i-a)
//				{
//					max = i - a; 
//					start = a; end = i - 1;
//				}
//				a = f[ch] + 1;
//				f[ch] = i;
//			}
//		}
//
//		b = i - 1;
//		if(max < b-a+1)
//		{
//			max = b-a+1; start = a; end = b;
//		}
//
//		printf("%ld %ld %ld\n",max, start, end);
//	}
//	return 0;
//}



//hdu 2675
//#include <iostream>
//using namespace std;
//
//#define e 2.7182818284
//
//int main()
//{
//	double y;
//
//	while(scanf("%lf",&y) != EOF)
//	{
//		printf("%.5lf\n",e*y);
//	}
//	return 0;
//}



//poj 2777
//#include <iostream>
//using namespace std;
//
//int main()
//{
//	int l, t, m, a, b, c;
//	char ch;
//
//	while(scanf("%d%d%d",&l,&t,&m) != EOF)
//	{
//		while(m--)
//		{
//			getchar();
//			scanf("%c",&ch);
//			if(ch == 'P')
//			{
//				scanf("%d%d",&a,&b);
//			}
//			else
//			{
//			}
//		}
//	}
//	return 0;
//}




//#include <iostream>
//#include <string>
//#include <algorithm>
//using namespace std;
//
//const int N = 41000;
//const int D = 10;
//const int M = 200;
//const int offset = 100;
//
//int n, s[N], cnt[N], mem[4][N], h[N];
//int *rank, *nrank, *sa, *nsa;
//
//void radix_sort()
//{
//	int i, j, k;
//	rank = mem[0];
//	nrank = mem[1];
//	sa = mem[2];
//	nsa = mem[3];
//
//	for(i=0; i<n; i++)
//		cnt[s[i]] ++;
//	for(i=1; i<M; i++)
//		cnt[i] += cnt[i-1];
//	for(i=n-1; i>=0; i--)
//		sa[--cnt[s[i]]] = i;
//
//	for(rank[0]=0,i=1; i<n; i++)
//	{
//		rank[sa[i]] = rank[sa[i-1]];
//		if(s[sa[i]] != s[sa[i-1]]) rank[sa[i]] ++;
//	}
//
//	for(k=1; k<n && rank[sa[n-1]]<n-1; k*=2)
//	{
//		for(i=0; i<n; i++)
//			cnt[rank[sa[i]]] = i + 1;
//		for(i=n-1; i>=0; i--)
//			if(sa[i]-k >= 0)
//				nsa[--cnt[rank[sa[i]-k]]] = sa[i] - k;
//
//		for(i=n-k; i<n; i++)
//			nsa[--cnt[rank[i]]] = i;
//
//		for(nrank[nsa[0]],i=1; i<n; i++)
//		{
//			nrank[nsa[i]] = nrank[nsa[i-1]];
//			if(rank[nsa[i]] != rank[nsa[i-1]] || rank[nsa[i]+k] != rank[nsa[i-1]+k])
//				nrank[nsa[i]] ++;
//		}
//
//		swap(rank, nrank);
//		swap(sa, nsa);
//	}
//}
//
//void get_lcp_rmq()
//{
//	int i, j, k;
//	for(i=0,k=0; i<n; i++)
//	{
//		if(rank[i] == n-1) 
//			h[rank[i]] = k = 0;
//		else
//		{
//			if(k > 0) k--;
//			j = sa[rank[i]+1];
//			while(s[i+k] == s[j+k])
//				k ++;
//			h[rank[i]] = k;
//		}
//	}
//}
//
//bool search_ans(int len)
//{
//	int i, l=N, r=0, ma, mi;
//
//	for(i=0; i<n-2; i++)
//	{
//		if(h[i] < len)
//		{
//			l = N; r = 0;
//		}
//		else
//		{
//			mi = sa[i]; ma = sa[i+1];
//			if(mi > ma) swap(mi, ma);
//			l = min(mi, l);
//			r = max(ma, r);
//			if(r-l >= len) return true;
//		}
//	}
//	return false;
//}
//
//int main()
//{
//	int i, j, k;
//
//	while(scanf("%d",&n)!=EOF && n)
//	{
//		memset(cnt, 0, sizeof(cnt));
//		memset(mem, 0, sizeof(mem));
//
//		for(i=0; i<n; i++)
//			scanf("%d",&s[i]);
//
//		for(i=0; i<n-1; i++)
//			s[i] = s[i+1] - s[i] + offset;
//		s[n-1] = 0;
//
//		radix_sort();
//		get_lcp_rmq();
//
//		int low = 0, up = n, mid;
//		//bool get = 0;
//		while(low < up)
//		{
//			mid = (low + up + 1) / 2;
//			if(search_ans(mid)) low = mid;
//			else up = mid - 1;
//		}
//
//		if(low < 4) printf("0\n");
//		else printf("%d\n",low+1);
//	}
//	return 0;
//}





//A
//#include <iostream>
//#include <stdio.h>
//#include <string.h>
//using namespace std;
//
//const int M = 1000;
//
//int dir[8][3] = {{-1,-1,-1}, {-1,-1,1}, {-1,1,-1}, {-1,1,1}, {1,-1,-1}, {1,-1,1}, {1,1,-1}, {1,1,1}};
//int ans, x1, y1, z1, x, y, z;
//int path[7][3], t[7][3];
////bool a[2001][2001][2001];
//
//void dfs(int x0, int y0, int z0, int step)
//{
//	if(step > 6) return;
//
//	//if(a[x0+M][y0+M][z0+M] == true) return;
//
//	t[step][0] = x0;
//	t[step][1] = y0;
//	t[step][2] = z0;
//
//	if(x0==x1 && y0==y1 && z0==z1)
//	{
//		if(ans > step)
//		{
//			ans = step;
//			for(int i=0; i<=step; i++)
//			{
//				path[i][0] = t[i][0];
//				path[i][1] = t[i][1];
//				path[i][2] = t[i][2];
//			}
//		}
//		return;
//	}
//
//	if(step == 6) return;
//	//a[x0+M][y0+M][z0+M] = true;
//
//	int i, xx, yy, zz;
//	for(i=0; i<8; i++)
//	{
//		xx = x0 + x*dir[i][0];
//		yy = y0 + y*dir[i][1];
//		zz = z0 + z*dir[i][2];
//		dfs(xx, yy, zz, step+1);
//
//		xx = x0 + x*dir[i][0];
//		yy = y0 + z*dir[i][1];
//		zz = z0 + y*dir[i][2];
//		dfs(xx, yy, zz, step+1);
//
//		xx = x0 + y*dir[i][0];
//		yy = y0 + x*dir[i][1];
//		zz = z0 + z*dir[i][2];
//		dfs(xx, yy, zz, step+1);
//
//		xx = x0 + y*dir[i][0];
//		yy = y0 + z*dir[i][1];
//		zz = z0 + x*dir[i][2];
//		dfs(xx, yy, zz, step+1);
//
//		xx = x0 + z*dir[i][0];
//		yy = y0 + x*dir[i][1];
//		zz = z0 + y*dir[i][2];
//		dfs(xx, yy, zz, step+1);
//
//		xx = x0 + z*dir[i][0];
//		yy = y0 + y*dir[i][1];
//		zz = z0 + x*dir[i][2];
//		dfs(xx, yy, zz, step+1);
//	}
//}
//
//int main()
//{
//	int x0, y0, z0, i;
//
//	while(scanf("%d%d%d%d%d%d",&x0,&y0,&z0,&x1,&y1,&z1) != EOF)
//	{
//		scanf("%d%d%d",&x,&y,&z);
//		
//		//memset(a, 0, sizeof(a));
//		ans = 10;
//		dfs(x0, y0, z0, 0);
//
//		printf("To get from (%d,%d,%d) to (%d,%d,%d) takes ",x0,y0,z0,x1,y1,z1);
//		if(ans > 6)
//			printf("more than 6 3D knight moves (%d,%d,%d).\n",x,y,z);
//		else
//		{
//			printf("%d 3D knight moves (%d,%d,%d): ",ans,x,y,z);
//			for(i=0; i<=ans; i++)
//			{
//				if(i) printf(" => ");
//				printf("(%d,%d,%d)", path[i][0], path[i][1], path[i][2]);
//			}
//			printf("\n");
//		}
//	}
//	return 0;
//}




//#include <iostream>
//#include <algorithm>
//#include <queue>
//using namespace std;
//
//struct Node
//{
//	int num;
//	struct Node left, right;
//	bool operator < (const Node &A) const {
//		return num > A.num;
//	}
//};
//
//int length;
//
//void compute(Node tree, int deep)
//{
//	if(tree.left == NULL && tree.right == NULL)
//	{
//		length += deep * tree.num;
//		return;
//	}
//
//	compute(tree.left, deep+1);
//	compute(tree.right, deep+1);
//}
//
//int main()
//{
//	int n, i, a;
//	Node tree;
//
//	while(scanf("%d",&n) != EOF)
//	{
//		priority_queue<Node> PQ;
//
//		for(i=0; i<n; i++)
//		{
//			scanf("%d",&a);
//			tree.num = a;
//			tree.left = tree.right = NULL;
//			PQ.push(tree);
//		}
//
//		while(PQ.size() > 1)
//		{
//			Node temp1 = PQ.top();
//			PQ.pop();
//			Node temp2 = PQ.top();
//			PQ.pop();
//
//			Node node;
//			node.num = temp1.num + temp2.num;
//			node.left = temp1;
//			node.right = temp2;
//
//			PQ.push(node);
//		}
//
//		tree = PQ.push();
//		length = 0;
//		compute(tree, 0);
//		printf("%d\n",length);
//	}
//	return 0;
//}


//#include <iostream>
//#include <queue>
//#include <stdio.h>
//#include <string.h>
//using namespace std;
//#define Inf 0xfffff
//
//struct Node
//{
//    int x, y, step;
//}start, end;
//
//char map[21][21];
//int n, m, step, dir[4][2]={0,1, 0,-1, 1,0, -1,0};
//int visit[21][21];
//
//void bfs()
//{
//    step = Inf;
//
//    queue<Node> Q;
//
//    Q.push(start);
//	
//	visit[start.x][start.y] = 1;
//    while(!Q.empty())
//    {
//        Node temp = Q.front();
//        Q.pop();
//        for(int i=0; i<4; i++)
//        {
//            Node cur;
//            cur.x = temp.x + dir[i][0];
//            cur.y = temp.y + dir[i][1];
//
//            if(cur.x<0 || cur.x>=n || cur.y<0 || cur.y>=m) continue;
//
//            if(map[cur.x][cur.y] == '*')
//                continue;
//            else if(map[cur.x][cur.y] == 'T')
//            {
//                if(step > temp.step + 1)
//                    step = temp.step + 1;
//                continue;
//            }
//            else if(map[cur.x][cur.y] == '.')
//                cur.step = temp.step + 1;
//            else if(map[cur.x][cur.y] == '|')
//            {
//                cur.x += dir[i][0];
//                cur.y += dir[i][1];
//
//                if(temp.step%2 != 0)
//                {
//                    if(dir[i][0] == 0)
//                        cur.step = temp.step + 1;
//                    else
//                        cur.step = temp.step + 2;
//                }
//                else
//                {
//                    if(dir[i][0] == 0)
//                        cur.step = temp.step + 2;
//                    else
//                        cur.step = temp.step + 1;
//                }
//            }
//            else if(map[cur.x][cur.y] == '-')
//            {
//                cur.x += dir[i][0];
//                cur.y += dir[i][1];
//
//                if(temp.step%2 == 0)
//                {
//                    if(dir[i][0] == 0)
//                        cur.step = temp.step + 1;
//                    else
//                        cur.step = temp.step + 2;
//                }
//                else
//                {
//                    if(dir[i][0] == 0)
//                        cur.step = temp.step + 2;
//                    else
//                        cur.step = temp.step + 1;
//                }
//            }
//
//            if(map[cur.x][cur.y] == '*') continue;
//            else if(map[cur.x][cur.y] == 'T')
//            {
//                if(step > temp.step + 1)
//                    step = temp.step + 1;
//                continue;
//            }
//
//            visit[cur.x][cur.y] = 1;
//            Q.push(cur);
//        }
//    }
//}
//
//int main()
//{
//    while(scanf("%d%d",&n,&m) != EOF)
//    {
//        for(int i=0; i<n; i++)
//        {
//            getchar();
//            for(int j=0; j<m; j++)
//            {
//                scanf("%c",&map[i][j]);
//                if(map[i][j] == 'S')
//                {
//                    start.x = i;
//                    start.y = j;
//                    start.step = 0;
//                }
//                else if(map[i][j] == 'T')
//                {
//                    end.x = i;
//                    end.y = j;
//                }
//            }
//        }
//
//		memset(visit, 0, sizeof(visit));
//
//        bfs();
//
//        printf("%d\n",step);
//    }
//    return 0;
//}