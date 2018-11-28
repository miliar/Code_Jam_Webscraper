//#include<stdio.h>
//#include<math.h>
//#define N 120
//struct node
//{
//	int rank;
//	int pos;
//};
//node a[N];
//int lena = 0;
//node b[N];
//int lenb = 0;
//int main()
//{
//	freopen("a.in", "r", stdin);
//	freopen("output.txt", "w", stdout);
//	int t;
//	int n;
//	scanf("%d", &t);
//	int cas = 1;
//	while (t--)
//	{
//		char s[2];
//		int pos;
//		lena = 0;
//		lenb = 0;
//		scanf("%d", &n);
//		for (int i = 0; i < n; ++i)
//		{
//			scanf("%s%d", s, &pos);
//			if (s[0] == 'O')
//			{
//				a[lena].rank = i;
//				a[lena++].pos = pos;
//			}
//			else
//			{
//				b[lenb].rank = i;
//				b[lenb++].pos = pos;
//			}
//
//		}
//		int o_pos = 1, b_pos = 1;
//		int o_cost, b_cost;
//		int i = 0, j = 0;
//		int num = 0 ;
//		while (i < lena && j < lenb)
//		{
//			o_cost = abs(a[i].pos - o_pos);
//			b_cost = abs(b[j].pos - b_pos);
//
//			if (a[i].rank < b[j].rank)
//			{
//				num += o_cost + 1;
//				o_pos = a[i].pos;
//				++i;
//				
//				if (b_cost <= o_cost)
//				{
//					b_pos = b[j].pos;
//				}
//				else 
//				{
//					if (b[j].pos >= b_pos)
//						b_pos += o_cost + 1;
//					else b_pos -= o_cost + 1;
//				}
//
//			}
//			else
//			{
//				num += b_cost + 1;
//				b_pos = b[j].pos;
//				++j; 
//				if (o_cost <= b_cost)
//				{
//					o_pos = a[i].pos;
//				}
//				else 
//				{
//					if (a[i].pos > o_pos)
//						o_pos += b_cost + 1;
//					else o_pos -= b_cost + 1;
//
//				}
//
//			}
//		}
//		if (i < lena)
//		{
//			for (; i < lena; ++i)
//			{
//				num += abs(a[i].pos - o_pos) + 1;
//				o_pos = a[i].pos;
//			}
//		}
//		else if (j < lenb)
//		{
//			for (; j < lenb; ++j)
//			{
//				num += abs(b[j].pos - b_pos) + 1;
//				b_pos = b[j].pos;
//			}
//		}
//		printf("Case #%d: %d\n", cas++, num);	
//
//
//	}
//	return 0;
//}

/*

#include <stdio.h>
#define N 1020

int main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	int cas = 1;
	scanf("%d", &t);
	while (t--)
	{
		int n;
		scanf("%d", &n);
		int Min = 10000000;
		int yihuo = 0;
		int a; 
		long long sum = 0; 
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &a);
			sum += a;
			if (Min > a)
				Min = a;
			if (i == 0)
				yihuo = a;
			else yihuo ^= a;

		}
		printf ("Case #%d: ", cas++);
		if (yihuo)
		{
			printf("NO\n");
		}
		else printf("%d\n", sum - Min);


	}
	return 0;
}

*/
//
//#include <stdio.h>
//#include <stdlib.h>
//
//#define N 1020
//int a[N];
//int b[N];
//int main()
//{
//	freopen("a.in", "r", stdin);
//	freopen("output.txt", "w", stdout);
//	int t;
//	int cas = 1;
//	scanf("%d", &t);
//	while (t--)
//	{
//		int n; 
//		scanf("%d", &n);
//		for (int i = 0; i < n; ++i)
//		{
//			scanf("%d", a+i);
//			b[i] = a[i];
//		}
//
//		int num  = 0;
//		int k; 
//		int temp;
//		for (int i = 0; i < n - 1; ++i)
//		{
//			k = i;
//			for (int j = i + 1; j < n; ++j)
//			{
//				if (a[k] > a[j])
//					k = j;
//			}
//			if (k != i)
//			{
//				++num;
//				temp = a[i];
//				a[i] = a[k];
//				a[k] = temp;
//			}
//		}
//		num = 0;
//		for (int i = 0; i < n; ++i)
//		{
//			if (b[i] != a[i])
//				num++;
//		}
//		printf("Case #%d: %.6lf\n", cas++, num * 1.0);
//
//	}
//	return 0;
//}

#include <stdio.h>

int main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int cas = 1;
	while (t--)
	{
		long long n;
		int pd, pg;
		bool pass = true;
		scanf("%lld%d%d", &n, &pd, &pg);

		//if (pd < pg)
			//pass = false;
		//else
		{
			int i;
			if ((pd && !pg)||(!pd && pg)||(pd < 100 && pg == 100))
				pass = false;
			else if (pd != 0)
			{
				int min = n < 100?n:100;
				for (i = 1; i <= min; ++i)
				{
					int x = i * pd;
					if (x % 100 == 0)
						break;
				}
				if (i <= min)
					pass = true;
				else pass = false;
			}
		}
		
		printf("Case #%d: ", cas++);
		//printf("%d %d %d ", n, pd, pg);
		if (pass) printf("Possible\n");
		else printf("Broken\n");




	}
	return 0;
}