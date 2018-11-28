//poj 2537
//简单dp,求幂太大时可以转化为多次除。
/*
#include <iostream>
using namespace std;

double dp[110][10];
int main()
{
	int k, n;
	while (scanf("%d%d", &k, &n) != EOF)
	{
		for (int i = 0; i <= k; i++)
			dp[1][i] = 1;
		for (int i = 2; i <= n; i++)
		{
			dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
			for (int j = 1; j < k; j++)
			{
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1];
			}
			if (k != 0)
				dp[i][k] = dp[i - 1][k - 1] + dp[i - 1][k];
		}
		double ans = 0;
		for (int i = 0; i <= k; i++)
			ans += dp[n][i];
		for (int i = 1; i <= n; i++)
			ans /= (k + 1.0);
		printf("%.5lf\n", ans * 100);
	}
	return 0;
}
*/
//poj 2264
//
/*
#include <cstdio>
#include <iostream>

using namespace std;

char str1[110], str2[110], lcs[110];
int dp[110][110],l;

void getlcs(int pos1, int pos2)
{
	if (pos1 < 0 || pos2 < 0)
		return;
	if (str1[pos1] == str2[pos2])
	{
		getlcs(pos1 - 1, pos2 - 1);
		lcs[l++] = str1[pos1];
	}
	else
	{
		if (dp[pos1][pos2] == dp[pos1 - 1][pos2])
		{
			getlcs(pos1 - 1, pos2);
		}
		else
		{
			getlcs(pos1, pos2 - 1);
		}
	}
}
int main()
{
	while (scanf("%s%s", str1, str2) != EOF)
	{
		int i, j;
		memset(dp, 0, sizeof(dp));
		int len1 = strlen(str1), len2 = strlen(str2);
		for (i = 0; i < len1; i++)
		{
			if (str2[0] == str1[i])
			{
				dp[i][0] = 1;
				break;
			}
		}
		for (i; i < len1; i++)
			dp[i][0] = 1;
		for (i = 0; i < len2; i++)
		{
			if (str1[0] == str2[i])
			{
				dp[0][i] = 1;
				break;
			}
		}
		for (i; i < len2; i++)
			dp[0][i] = 1;
		for (i = 1; i < len1; i++)
		{
			for (j = 1; j < len2; j++)
			{
				if (str1[i] == str2[j])
					dp[i][j] = dp[i - 1][j - 1] + 1;
				else
				{
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
				}
			}
		}
		l = 0;
		getlcs(len1 - 1, len2 - 1);
		lcs[l] = '\0';
		int ptr = 0,ptr1 = 0, ptr2 = 0;
		while (ptr1 < len1 || ptr2 < len2)
		{
			while (str1[ptr1] && str1[ptr1] != lcs[ptr])
			{
				printf("%c", str1[ptr1]);
				ptr1++;
			}
			while (str2[ptr2] && str2[ptr2] != lcs[ptr])
			{
				printf("%c", str2[ptr2]);
				ptr2++;
			}
			printf("%c", lcs[ptr]);
			ptr++, ptr1++, ptr2++;
		}
		printf("\n");
	}
	return 0;
}
*/
//poj 11764
/*
#include <iostream>
using namespace std;

inline int getmod(int a, int b)
{
	return ((a % b) + b) % b;
}

bool dp[10010][110];
int num[10010];
int main()
{
	int n, k;
	while (scanf("%d%d", &n, &k) != EOF)
	{
		memset(dp, false, sizeof(dp));
		for (int i = 0; i < n; i++)
			scanf("%d", &num[i]);
		dp[0][getmod(num[0], k)] = true;
		for (int i = 0; i < n - 1; i++)
		{
			for (int j = 0; j < k; j++)
			{
				if (dp[i][j] != false)
				{
					dp[i + 1][getmod(j + num[i + 1], k)] = true;
					dp[i + 1][getmod(j - num[i + 1], k)] = true;
				}
			}
		}
		if (dp[n - 1][0] == true)
			printf("Divisible\n");
		else
			printf("Not divisible\n");
	}
	return 0;
}
*/
/*
#include <iostream>
using namespace std;

int v[1000];
int main()
{
	int cash;
	int n, num, mon, ptr;
	while (scanf("%d", &cash) != EOF)
	{
		ptr = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d%d", &num, &mon);
			int sum = 0, j;
			for (j = 0; ; j++)
			{
				if (sum + (1 << j) <= num)
				{
					sum += (1 << j);
					v[ptr++] = (1 << j) * mon;
				}
				else
					break;
			}
			if (sum == num)
				continue;
			else
			{
				v[ptr++] = (num - sum) * mon;
			}
		}
		bool dp[100010] = {false};
		dp[0] = true;
		for (int i = 0; i < ptr; i++)
		{
			if (dp[cash] == true)
				break;
			for (int j = cash;j >= 0; j--)
			{
				if (dp[j] && j + v[i] <= cash)
					dp[j + v[i]] = true;
			}
		}
		for (int i = cash; i >= 0; i--)
		{
			if (dp[i])
			{
				printf("%d\n", i);
				break;
			}
		}
	}
	return 0;
}
*/
//poj 2978
//dp[i][j][k]表示到第i个数时，使用了的颜色状态为j，并且最后一位的颜色为k的方法。
//当c[i]的颜色已经在j中出现过时，若k == c[i], 则dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + 1);
//若k != c[i],则dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k]);
//当c[i]的颜色还没在j中出现过时，则可以更新dp[i][j | (1 << c[i])][c[i]] = max(dp[i - 1][j][k]) + 1的值，同时，dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k]);
/*
#include <iostream>
using namespace std;

int c[110];
int dp[110][1 << 5][5];
int main()
{
	int m, n, end;
	while (scanf("%d%d", &n, &m) && m && n)
	{
		memset(dp, 0, sizeof(dp));
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &c[i]);
			c[i]--;
		}
		end = (1 << m) - 1;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 0; j <= end; j++)
			{
				if (j & (1 << c[i]))
				{
					for (int k = 0; k < m; k++)
					{
						if (k == c[i])
							dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + 1);
						else
						{
							dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k]);
						}
					}
				}
				else
				{
					for (int k = 0; k < m; k++)
					{
						dp[i][j | (1 << c[i])][c[i]] = max(dp[i][j | (1 << c[i])][c[i]], dp[i - 1][j][k] + 1);
						dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k]);
					}
				}
			}
		}
		int MAX = -1;
		for (int i = 0; i <= end; i++)
		{
			for (int j = 0; j < m; j++)
				MAX = max(MAX, dp[n][i][j]);
		}
		printf("%d\n", n - MAX);
	}	
	return 0;
}
*/
//quicksort
/*
#include <ctime>
#include <cstdlib>
#include <iostream>
using namespace std;

void quicksort(int a[], int l, int r)
{
	if (l == r)
		return;
	if (r == l + 1)
	{
		if (a[l] > a[r])
			swap(a[l], a[r]);
		return;
	}
	int mid = (l + r) / 2;
	if (a[mid] > a[r])
		swap(a[mid], a[r]);
	if (a[l] < a[mid])
		swap(a[mid], a[l]);
	if (a[l] > a[r])
		swap(a[l], a[r]);
	int lptr = l + 1, rptr = r, temp = a[l];
	while (lptr < rptr)
	{
		while (a[lptr] <= temp && lptr < rptr)
			lptr++;
		while (a[rptr] >= temp && lptr < rptr)
			rptr--;
		if (lptr != rptr)
			swap(a[lptr], a[rptr]);
	}
	swap(a[l], a[lptr - 1]);
	quicksort(a, l, lptr - 2);
	quicksort(a, lptr, r);
}

int in[20000010];
int main()
{
	srand(time(0));
	int n = 1000;
	for (int i = 0; i < n; i++)
	{
		in[i] = 10000000;
	}
	time_t s, t;
	s = clock();
	quicksort(in, 0, n - 1);
	t = clock();
	cout << t - s << endl;
	for (int i = 0; i < n - 1; i++)
	{
		if (in[i] > in[i + 1])
		{
			cout << "WA" << endl;
			break;
		}
	}
	
	system("pause");
	return 0;
}
*/
/*
#include<stdio.h>
#include<time.h>
#include<conio.h>
#include<stdlib.h>


#include <iostream>
#include <ctime>
using namespace std;

int a[10000010];
int partition(int low, int high){
    int mid=(low+high)/2;
    int midvalue=0;//中间值
    int m;//记录中间位置的数的下标
    if((a[mid]<=a[high]&&a[mid]>=a[low])||(a[mid]>a[high]&&a[mid]<a[low])){
        midvalue=a[mid];
        m=mid;
    }
       else {
           if((a[low]>=a[mid]&&a[low]<=a[high])||(a[low]<a[mid]&&a[low]>a[high])){

               midvalue=a[low];
               m=low;
           }
                  else {midvalue=a[high];m=high;}
       }
    int swap=0;
    while(low<high){
        while(low<high&&a[high]>=midvalue&&m!=high) high--;
        while(low<high&&a[low]<midvalue&&m!=low) low++;
        swap=a[high];
        a[high]=a[low];
        a[low]=swap;
        if(m==high) high--;
        if(m==low) low++;
    }
    a[low]=midvalue;
    return low;
}

void Qsort(int begin,int end){
    int mid;
    if(begin<end){
        mid=partition(begin,end);
        Qsort(begin,mid-1);
        Qsort(mid+1,end);
    }
}

int main()
{
	int n;
	while (cin >> n)
	{
		for (int i = 0; i < n; i++)
			cin >> a[i];
		time_t end,start;
		float t;
		start=clock();
		Qsort(0,n - 1);
		end=clock();
		for (int i = 0; i < n; i++)
			cout << a[i] << " ";
		cout << endl;
		t=(end-start);
		printf("\nThe time it cost:%.3f sec\n",t/1000);
	//system("pause");
	}
	return 0;
}
*/
//poj 1944
//枚举断点，然后通过设置计数指针，得出测度。。
/*
#include <iostream>
using namespace std;

int a[10010][2];
int flag[2020];

int main()
{
	int n, p, ans;
	while (scanf("%d%d", &n, &p)!= EOF)
	{
		ans = 1010;
		for (int i = 0; i < p; i++)
		{
			scanf("%d%d", &a[i][0], &a[i][1]);
			if (a[i][0] > a[i][1])
				swap(a[i][0], a[i][1]);
		}
		for (int i = 1; i <= n; i++)
		{
			for (int j = 0; j <= n; j++)
				flag[j] = flag[j + n] = 0;
			for (int j = 0; j < p; j++)
			{
				if (a[j][0] <= i)
					a[j][0] += n;
				if (a[j][1] <= i)
					a[j][1] += n;
				if (a[j][0] > a[j][1])
					swap(a[j][0], a[j][1]);
				flag[a[j][0]]++, flag[a[j][1]]--;
			}
			int count = 0, pre = i + 1, sum = 0;
			for (int j = i + 1; j <= i + 1 + n; j++)
			{
				if (flag[j] > 0)
				{
					if (count != 0)
					{
						sum += j - pre;
					}
					pre = j;
					count++;
					continue;
				}
				if (flag[j] < 0)
				{
					sum += j - pre;
					pre = j;
					count--;
					continue;
				}
			}
			if (sum < ans)
				ans = sum;
		}
		printf("%d\n", ans);
	}
	//system("pause");
	return 0;
}
*/
//poj 1091
//WA
/*
#include <cstdio>
#include <iostream>
using namespace std;

const int MAXN = 200000;
__int64 pd[MAXN];

__int64 get(int step, __int64 curpro, __int64 m, __int64 n)
{
	__int64 ans = 0, temp, cur;
	for (int i = step; i <= pd[0]; i++)
	{
		temp = m / (curpro * pd[i]);
		cur = 1;
		for (int j = 1; j <= n; j++)
			cur *= temp;
		ans += cur;
		ans -= get(step + 1, curpro * pd[i], m, n);
	}
	return ans;
}
int main()
{
	__int64 n, m, temp;
	freopen("1091.in", "r", stdin);
	freopen("myans.out", "w", stdout);
	while (scanf("%I64d %I64d", &n, &m) != EOF)
	{
	pd[0] = 0, temp = m;
	__int64 i;
	for (i = 2; i * i <= temp; i++)
	{
		if (temp % i == 0)
		{
			pd[++pd[0]] = i;
			while (temp % i == 0)
				temp /= i;
		}
	}
	if (temp != 1)
		pd[++pd[0]] = temp;
	__int64 tot = 1;
	for (i = 1; i <= n; i++)
		tot *= m;
	printf("%I64d\n", tot - get(1, 1, m, n));
	}
	return 0;
}
*/
//poj 2992
/*
#include <iostream>
using namespace std;

bool notprime[510];
int pt[500];
long long pn[500];
int main()
{
	notprime[1] = true;
	for (int i = 2; i <= 500; i++)
	{
		if (notprime[i] == false)
		{
			pt[++pt[0]] = i;
			for (int j = i + i; j <= 500; j += i)
			{
				notprime[j] = true;
			}
		}
	}
	int n, k;
	while (scanf("%d%d", &n, &k) != EOF)
	{
		memset(pn, 0, sizeof(pn));
		for (int i = 1; i <= pt[0]; i++)
		{
			for (int j = pt[i]; j <= n; j *= pt[i])
			{
				pn[i] += n / j;
			}
			for (int j = pt[i]; j <= k; j *= pt[i])
			{
				pn[i] -= k / j;
			}
			for (int j = pt[i]; j <= (n - k); j *= pt[i])
			{
				pn[i] -= (n - k) / j;
			}
		}
		long long ans = 1;
		for (int i = 1; i <= pt[0]; i++)
			ans *= (pn[i] + 1);
		printf("%I64d\n", ans);
	}
}
*/
//poj 2376
//排序+贪心。。类似于区间最小覆盖。但又不同。每一次都要寻找到最优的值。
/*
#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 30000;
struct seg
{
	int b, e;
}a[MAXN];

bool comp(seg t1, seg t2)
{
	if (t1.b == t2.b)
		return t1.e > t2.e;
	return t1.b < t2.b;
}

int main()
{
	int n, t, i;
	//freopen("2376.in", "r", stdin);
	//freopen("myans.out", "w", stdout);
	while (scanf("%d%d", &n, &t) != EOF)
	{
	for (i = 0; i < n; i++)
		scanf("%d%d", &a[i].b, &a[i].e);
	sort(a, a + n, comp);
	int ans = 0, best = -1, end = 0;
	for (i = 0; i < n; )
	{
		if (a[i].b > end + 1 && best == -1)
		{
			printf("-1\n");
			break;
		}
		if (a[i].b > end + 1 && best != -1)
		{
			ans++;
			if (a[best].e == t)
			{
				printf("%d\n", ans);
				break;
			}
			end = a[best].e;
			best = -1;
			continue;
		}
		if (a[i].e <= end)
		{
			i++;
			continue;
		}
		if (a[i].b <= end + 1 && (best == -1 || a[i].e > a[best].e))
		{
			best = i;
		}
		i++;
	}
	if (i == n)
	{
		if (a[best].e == t)
		{
			ans++;
			printf("%d\n", ans);
		}
		else
			printf("-1\n");
	}
	}
	//system("pause");
	return 0;
}
*/
/*
#include <iostream>
using namespace std;

int main()
{
	freopen("2376.in", "w", stdout);
	for (int i = 0; i < 20; i++)
	{
		int temp1 = rand() % 10 + 1;
		int temp2 = rand() % 20 + 1;
		cout << temp1 << " " << temp2 << endl;
		for (int i = 0; i < temp1; i++)
		{
			int cur1 = rand() % 20 + 1;
			int cur2 = rand() % 20 + 1;
			while (cur1 > cur2)
			{
				cur2 = rand() % 20 + 1;
			}
			cout << cur1 << " " << cur2 << endl;
		}
	}
	return 0;
}
*/
/*
#include <iostream>
#include <algorithm>
using namespace std;
struct Duan
{
	int start;
	int end;
};
struct Duan s[25005];
int comp (struct Duan a,struct Duan b)
{
	return (a.start<b.start)||(a.start==b.start && a.end>b.end);
}

int main ()
{
	int n,t,count,i,j,frist,second,tag,tag1;
	freopen("2376.in", "r", stdin);
	freopen("otherans.out", "w", stdout);
	while (scanf ("%d%d",&n,&t) != EOF)
	{
	for (i=0;i<n;i++)
		scanf ("%d%d",&s[i].start,&s[i].end);
	sort(s,s+n,comp);
	if (s[0].start==1)
	{
		if (s[0].end==t)
		{
			printf ("1\n");
		}
		else
		{
			count=1;
	    	frist=second=s[0].end;
	     	j=0;
	    	tag=0;
	        while (1)
			{
		    	tag1=0;			
		    	for (i=1+j;i<n;i++)
				{
			    	if (s[i].start-1<=frist && second<s[i].end)
					{
				         second=s[i].end;
				    	 j=i;
					     tag1=1;
					}
				}
		    	if (tag1==0)
	    			break;
	    		count++;			
		    	if (second==t)
				{
	     			tag=1;
		      		printf ("%d\n",count);
		    		break;
				}
		    	frist=second;
			
			}
    		if (tag==0)
		    	printf ("-1\n");
		}
	}
	else 
		printf ("-1\n");
	}
	return 0;
}
*/
/*
#include <iostream>
using namespace std;

int main()
{
	int n, q;

	return 0;
}
*/
//hdu 3401
/*
#include <iostream>
using namespace std;

#define MAXN 2010
#define inf 100000000

int ap[MAXN],bp[MAXN],as[MAXN],bs[MAXN], dp[MAXN][MAXN], q[MAXN][2];

int main()
{
	int t, T, MaxP, W;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d%d%d", &T, &MaxP, &W);
		for (int i = 1; i <= T; i++)
		{
			scanf("%d%d%d%d", &ap[i], &bp[i], &as[i], &bs[i]);
		}
		for (int i = 1; i <= T; i++)
			for (int j = 0; j <= MaxP; j++)
				dp[i][j] = -inf;
		for (int i = 1; i <= W + 1; i++)
		{
			for (int j = 0; j <= as[i]; j++)
				dp[i][j] = -(j * ap[i]);
		}
		for (int i = 2; i <= T; i++)
		{
			for (int j = 0; j <= MaxP; j++)
			{
				dp[i][j] = max(dp[i][j], dp[i - 1][j]);
			}
			if (i - W - 1 < 1)
				continue;
			int head = 0, tail = -1, cur;
			for (int j = 0; j <= MaxP; j++)
			{
				cur = dp[i - W - 1][j] + j * (ap[i]);
				while (head <= tail && q[tail][1] < cur)
					tail--;
				q[++tail][1] = cur, q[tail][0] = j;
				while (head <= tail && q[head][0] + as[i] < j)
					head++;
				dp[i][j] = max(dp[i][j], q[head][1] - j * ap[i]);
			}
			head = 0, tail = -1;
			for (int j = MaxP; j >= 0; j--)
			{
				cur = dp[i - W - 1][j] + j * (bp[i]);
				while (head <= tail && q[tail][1] < cur)
					tail--;
				q[++tail][1] = cur, q[tail][0] = j;
				while (head <= tail && q[head][0] - bs[i] > j)
					head++;
				dp[i][j] = max(dp[i][j], q[head][1] - j * bp[i]);
			}
		}
		int ans = -1;
		for (int i = 0; i <= MaxP; i++)
			ans = max(ans, dp[T][i]);
		printf("%d\n", ans);
	}
	return 0;
}
*/










//poj 1118
/*
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;

struct p
{
	int x,y;
}pt[1010];
double k[1010];
int main()
{
	int n;
	int ans, c, count;
	while (scanf("%d", &n) && n)
	{
		ans = 0;
		for (int i = 0; i < n; i++)
			scanf("%d%d", &pt[i].x, &pt[i].y);
		for (int i = 0; i < n; i++)
		{
			c = 0, count = 0;
			for (int j = 0; j < n; j++)
			{
				if (i == j)
					continue;
				if (pt[j].x == pt[i].x)
					c++;
				else
				{
					k[count++] = double(pt[j].y - pt[i].y) / double(pt[j].x - pt[i].x);
				}
			}
			if (c + 1 > ans)
				ans = c + 1;
			sort(k, k + count);
			c = 1;
			for (int j = 1; j < count; j++)
			{
				if (k[j] == k[j - 1])
					c++;
				else
				{
					if (c + 1 > ans)
						ans = c + 1;
					c = 1;
				}
			}
			if (c + 1 > ans)
				ans = c + 1;
		}
		printf("%d\n", ans);
	}
	return 0;
}
*/
/*
#include <cstdlib>
#include <iostream>
using namespace std;

void quicksort(int a[], int l, int r)
{
	if (l == r)
		return;
	if (r == l + 1)
	{
		if (a[l] > a[r])
			swap(a[l], a[r]);
		return;
	}
	int mid = (l + r) / 2;
	if (a[mid] > a[r])
		swap(a[mid], a[r]);
	if (a[l] < a[mid])
		swap(a[mid], a[l]);
	if (a[l] > a[r])
		swap(a[l], a[r]);
	int lptr = l + 1, rptr = r, temp = a[l];
	while (lptr < rptr)
	{
		while (a[lptr] <= temp && lptr < rptr)
			lptr++;
		while (a[rptr] >= temp && lptr < rptr)
			rptr--;
		if (lptr != rptr)
			swap(a[lptr], a[rptr]);
	}
	swap(a[l], a[lptr - 1]);
	quicksort(a, l, lptr - 2);
	quicksort(a, lptr, r);
}

int in[10010];
int main()
{
	int t, n, k;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; i++)
			scanf("%d", &in[i]);
		quicksort(in, 0, n - 1);
		printf("%d\n", in[k - 1]);
	}
	system("pause");
	return 0;
}
*/
#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 110;
char str[MAXN][MAXN];
double wp[MAXN], owp[MAXN], oowp[MAXN];
int win[MAXN], tot[MAXN];
int main()
{
	int t, n;
	freopen("Aa.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
			scanf("%s", str[j]);
		int wg = 0, t = 0;
		for (int j = 0; j < n; j++)
		{
			wg = 0, t = 0;
			for (int k = 0; k < n; k++)
			{
				if (str[j][k] == '1')
					wg++;
				if (str[j][k] != '.')
					t++;
			}
			win[j] = wg, tot[j] = t;
			wp[j] = double(wg) / double(t);			
		}
		int c = 0;
		double sum = 0;
		for (int j = 0; j < n; j++)
		{
			c = 0, sum = 0;
			for (int k = 0; k < n; k++)
			{
				if (j == k || str[k][j] == '.')
					continue;
				else
				{
					c++;
					if (str[k][j] == '1')
						sum += double(win[k] - 1) / double(tot[k] - 1);
					else
						sum += double(win[k]) / double(tot[k] - 1);

				}
			}
			owp[j] = sum / double(c);
		}
		for (int j = 0; j < n; j++)
		{
			c = 0, sum = 0;
			for (int k = 0; k < n; k++)
			{
				if (j == k || str[k][j] == '.')
					continue;
				c++;
				sum += owp[k];
			}
			oowp[j] = sum / double(c);
		}
		printf("Case #%d:\n", i);
		for (int j = 0; j < n; j++)
			printf("%.8lf\n", 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j]);
	}
	return 0;
}