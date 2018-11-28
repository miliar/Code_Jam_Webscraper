#include <stdio.h>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;

typedef long long int64;

#define Eo(x) { cerr << (#x) << " = " << (x) << endl; }


inline int fh(int x) { return x | (x+1); }
inline int fs(int x) { return (x & (x+1))-1; }
const int fsize = 1<<11;
int64 fenv[fsize];
void update(int id, int value)
{
	for(; id<fsize; id = fh(id))
		fenv[id] += value;
}
int64 get(int id)
{
	int64 ans = 0;
	for(; id>=0; id = fs(id))
		ans += fenv[id];
	return ans;
}

int64 mget(int startPos, int n, int count)
{
	if(startPos+count < n)
		return get(startPos + count) - get(startPos-1);
	return get(n-1) - get(startPos-1) + get((startPos+count)-n);
}

int main()
{
	int t; scanf("%d", &t);
	for(int i=0; i<t; i++)
	{
//		Eo(i);
		int r, k, n;
		scanf("%d %d %d", &r, &k, &n);
		memset(fenv, 0, sizeof(fenv));
		for(int j=0; j<n; j++)
		{
			int tmp; scanf("%d", &tmp);
			update(j, tmp);
		}
//		for(int j=0; j<n; j++) Eo(get(j));
		
		int64 ans = 0;
		int startPos = 0;
		int64 kk = k;
		for(int j=0; j<r; j++)
		{
			int left = 0;
			int right = n-1;
			int mid;
			int64 value;
			while(right-left>1)
			{
				mid = (right+left)/2;
				value = mget(startPos, n, mid);
//				Eo(value);
//				Eo(mid); Eo(value);
				if(value == kk) left = right = mid;
				else if(value < kk) left=mid;
				else right = mid;
			}
//			Eo(left);
			if(left<n-1 && mget(startPos, n, left+1) <= kk) left++;
//			Eo(left);
			ans += mget(startPos, n, left);
			startPos += left+1;
			startPos %= n;
//			Eo(ans); Eo(startPos);
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}

