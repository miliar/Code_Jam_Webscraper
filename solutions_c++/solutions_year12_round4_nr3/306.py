#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MP make_pair
#define PB push_back

using namespace std;

const int MAXN = 2110;

int idx[MAXN];
int N;
double h[MAXN];
bool in[MAXN];
int q[MAXN];

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int T;	cin >> T;
	
	for(int cas = 1; cas <= T; ++cas)
	{
		cin >> N;
		for(int i = 1; i < N; ++ i)
		{
//			idx[i] = i + 1;
			cin >> idx[i];	
		}
		
		printf("Case #%d:", cas);
		
		
		h[N] = 1000.0;
		h[N-1] = 999.0;
		for(int i = 0; i <= N; ++ i)
		{
			in[i] = 0;
			q[i] = -1;	
		}
		in[N] = in[N-1] = 1;
		int qn = 0;
		q[qn ++] = N;
		q[qn ++] = N - 1;
		bool error = 0;
		
		for(int i = N-2; i > 0 && !error; -- i)	
		{
			if(!in[idx[i]])
			{
				error = 1;
				break;	
			}	
			
			bool flag = 0;
			while(q[qn - 1] != idx[i])	
			{
				flag = 1;
				in[q[--qn]] = 0;
			}
//			cout << "qn  " <<qn << " " << q[qn] << endl;	
			
			if(flag == 0)
			{
				double d = (h[q[qn-2]] - h[q[qn-1]]) / (q[qn-2] - q[qn-1]);
				h[i] = h[q[qn-1]] - (q[qn-1] - i) * d - 0.1;	
			}
			else if(qn == 1)
			{
				double d = (h[q[qn-1]] - h[q[qn]]) / (q[qn-1] - q[qn]);
				h[i] = h[q[qn]] - (q[qn] - i) * d + 0.1;	
			}
			else
			{
				double d = (h[q[qn-2]] - h[q[qn-1]]) / (q[qn-2] - q[qn-1]);
				double high = h[q[qn-1]] - (q[qn-1] - i) * d;
				
				d = (h[q[qn-1]] - h[q[qn]]) / (q[qn-1] - q[qn]);
				double low = h[q[qn]] - (q[qn] - i) * d;
				
				h[i] = (low + high) / 2; 	
			}
			
//			puts("debug");
//			cout << i << " " << h[i] << endl;
//			for(int j = qn; j >= 0; j --)	cout << q[j] << " ";cout << endl;
			
			q[qn ++] = i;
			in[i] = 1;
		}
		
		if(error)
		{
			puts(" Impossible");
			continue;	
		}
		
		double m = 1e9;
		for(int i = 1; i <= N; ++ i)
		{
			m = min(m, 2e8 / h[i]);	
		}
//		cout << m << " " << m*h[1] << endl;
		for(int i = 1; i <= N; ++ i)
		{
			printf(" %d", (int)(m * h[i] + 0.0001));	
		}
		puts("");

	}
	
	
	return 0;	
}
