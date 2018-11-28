#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define REPP(i,m,n) for (int i = m; i < m+n; i++)
#define REPR(i,a,b) for (int i = a; i <= b; i++)

#define foreach(it,type) for (typeof(type.begin()) it = type.begin(); it != type.end(); it++)

#define MAX(n,m) (((n) > (m)) ? (n) : (m))
#define MIN(n,m) (((n) < (m)) ? (n) : (m))

typedef vector<int> vi;

bool cmp(int n1, int n2) {return n1 > n2; }

map<int, int> cargo;

int main(int argc, char* argv[]) {
  ifstream fin (argv[1]);

  int T;
  fin >> T;

	REP(test,T) {
		cargo.clear();

		int L,N,C;
		long long t;
		fin >> L >> t >> N >> C;

		vi nums(C);
		REP(c,C) { fin >> nums[c]; }

		int rep = N / C;
		int rem = N % C;
		//cout << "rep: " << rep << " rem: " << rem << endl;

		long long sum = 0;
		long long totalsum = 0;
		REP(c,C) { 
			sum += nums[c];
			if (c < rem) { 
			  totalsum += 2 * nums[c];
				cargo[nums[c]]++;
			}
		}
		sum *= 2;
		//cout << "sum: " << sum << endl;

		totalsum += sum * rep;
		//cout << "totalsum: " << totalsum << endl;

		rep -= t / sum;
		REP(c,C) {
			cargo[nums[c]] += rep;
		}

		long long target = t % sum;
		target /= 2;

		long long nsum = 0;
		REP(c,C) { 
			nsum += nums[c];
			cargo[nums[c]]--;
			if (nsum < target) {}
			else if (nsum == target) { break; }
			else { cargo[nsum - target]++; break; }
		}
 
 		bool(*pt)(int,int) = cmp;
		set<int,bool(*)(int,int)> keys(pt);
		foreach(it,cargo) {
			keys.insert(it->first);
			//cout << "cargo: (" << it->first << ", " << it->second <<")"<<endl;
		}
 
		foreach(it,keys) {
			int count = cargo[*it];
			if (count <= 0) continue;
			if (L > count) {
				totalsum -= *it * count;
				L -= count;
				//cout << "took " << count << " of " << *it << endl;
			} else {
				totalsum -= *it * L;
				//cout << "took " << L << " of " << *it << endl;
				break;
			}
		}
		
		cout << "Case #" << test+1 << ": " << totalsum << endl;
	}

  return 0;
}
