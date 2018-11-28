#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <sstream>

#include <cmath>

typedef unsigned long long ULL;
typedef long long LL;
typedef unsigned long UL;
typedef unsigned int UI;
typedef unsigned char UC;

using namespace std;

bool select(int idx, int *d, int *c, int *c_)
{
	if(idx == 0) return false;

	c_[idx] = c[idx];
	--d[c[idx]];
	if(select(idx - 1, d, c, c_)) return true;
	++d[c[idx]];
	for(int i = 0; i<=9; ++i) {
		if(i>c[idx] && d[i]) {
			c_[idx] = i;
			int d_[10];
			for(int j=0;j<10;++j) d_[j]=d[j];
			--d[i];
			bool flag2 = true;
			for(int j=idx-1;j>=0;--j) {
				bool flag = false;
				for(int k=0;k<=9;++k) {
					if(d[k]) {
						--d[k];
						c_[j] = k;
						flag = true;
						break;
					}
				}
				if(!flag) {
					flag2 = false;
					break;
				}
			}
			if(flag2) return true;
			for(int j=0;j<10;++j) d[j]=d_[j];
		}
	}
	return false;
}

void select2(int idx, int*d, int*c, int*c_)
{
//	for(int i=0;i<=9;++i) cerr << i << ':' << d[i] << endl;
	for(int i=1;i<=9;++i) {
		if(d[i]) {
			--d[i];
			c_[idx]=i;
			break;
		}
	}
	--idx;
	while(idx>=0) {
		for(int i=0;i<=9;++i) {
			if(d[i]) {
				--d[i];
				c_[idx]=i;
				break;
			}
		}
		--idx;
	}
}

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		ULL result = 0;
		ULL val;
		cin >> val;
		int d[10],c[25],c_[25];
		for(int i=0;i<10;++i) d[i] = 0;
		int idx = 0;
		while(val > 0) {
			c[idx++] = val % 10;
			++d[val % 10];
			val /= 10;
		}
		--idx;
		if(!select(idx, d, c, c_)) {
			++idx;
			++d[0];
			select2(idx, d, c, c_);
		}
		for(int i=idx;i>=0;--i) {
//cerr << i << ':' << c_[i] << endl;
			result=result*10+c_[i];
		}

		cout << "Case #" << nn+1 << ": " << result << endl;
	}
	
	return 0;
}
