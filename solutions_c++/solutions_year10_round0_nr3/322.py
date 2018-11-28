#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

typedef unsigned long long  uint;

uint a[3000];
uint score[3000];
uint next[3000];

uint foo()
{
	uint n ,k ,r;
    cin >> r >> k >> n;
	for (int i = 0;i<n;i++) cin >>a[i];
	for (int i = n;i<n*2;i++) a[i] = a[i-n];
	for (int i = 0;i<n;i++)
	{
		uint sum = 0;
		next[i] = i + n;
		for (int j = 0;j<n;j++)
		{
			sum += a[i+j];
			if (sum > k){
			  next[i] = i+j;
			  break;
			}
			score[i] = sum;
		}
		next[i] %= n;
	}
	int mark[2000];
	for (int i = 0;i<n;i++) mark[i] = -1;
	int cycle_len = 0;
	int st = 0;

	int leader[2000]; //save headers
	uint score_cycle = 0;

	uint total = 0;
	for (int ptr = 0; ; ptr++)
	{
		if (-1 != mark[st])
		{
			int cyc_st = mark[st];
			int cyc_ed = ptr;
			cycle_len = cyc_ed - cyc_st;

			for (int i = cyc_st; i < cyc_ed; i++) score_cycle += score[ leader[i] ];
			for (int i = 0;i < r && i < cyc_st; i++) total += score[ leader[i] ];
			r -= cyc_st;
			if (r > 0)
			{
				total += r / cycle_len * score_cycle;
				r %= cycle_len; 
				for (int i = cyc_st; i < cyc_st + r; i++)
					total += score[ leader[i] ];
			}
		    return total;
		}
		else
		{
			mark[st] = ptr;
			leader[ptr] = st;
			st = next[st];
		}
	}

	return -1;
}

int main()
{
	 int c; 
	 cin >> c;
	 for (int i = 0;i < c; i++)
	 {
		 cout << "Case #"<< i+1 << ": " << foo() << endl;
	
	 }
}