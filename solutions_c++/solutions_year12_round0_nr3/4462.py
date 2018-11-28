#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
int a[10];
void Reverse(int* arr, int b, int e) {
	for(; b < e; b++, e--) {
		int temp = arr[e];
		arr[e] = arr[b];
		arr[b] = temp;
	}
} 
void right_shift(int* arr, int N, int k)
{
	k %= N;
	Reverse(arr, 0, N - k - 1);
	Reverse(arr, N - k, N - 1);
	Reverse(arr, 0, N - 1);
}

/*void RightShift(int* arr, int N, int K)
{
    K %= N;
    while(K--)
    {
        int t = arr[N - 1];
        for(int i = N - 1; i > 0; i --)
            arr[i] = arr[i - 1];
        arr[0] = t;
    }
}*/
int seperate(int* arr,int n)
{
	int i = 0;
	while(n)
	{
		arr[i++] = n % 10;
		n /= 10;
	}
	Reverse(arr,0,i-1);
	return i;
}
int total(int* arr,int N)
{
	int res = 0;
	int p = 10;
	for(int i = 0;i < N;i++)
	{
		res = res * p + arr[i];
	}
	return res;
}
int solve(int A,int B)
{
	int res = 0;
	int cnt = 0;
	int sum = 0;
	for(int i = A;i <= B;i++)
	{
		set<int> s;
		cnt = seperate(a,i);
		for(int k = 0;k < cnt;k++)
		{
			right_shift(a,cnt,1);
			if(a[0] == 0)continue;
			sum = total(a,cnt);
			if( sum > i && sum >= A && sum <= B)
			{
				s.insert(sum);
			}
		}
		res += s.size();
	}
	return res;
}
int main()
{
	int T,A,B,n = 0;
	FILE* fp = freopen("C-small-attempt2.in","r",stdin);
	FILE* fout = fopen("out.txt","w");
	fscanf(fp,"%d",&T);
	while( n < T)
	{
		n++;
		fscanf(fp,"%d%d",&A,&B);	
		int res = solve(A,B);
		fprintf(fout,"Case #%d: %d\n",n,res);
	}
	return 0;
}