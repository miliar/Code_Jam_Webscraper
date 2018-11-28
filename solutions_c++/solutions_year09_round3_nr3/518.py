#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

typedef int released[101];
typedef bool empty[101];

long long solve(int P, int Q, released &rel, empty e, 
		long long sum=0,int depth = 0) {
			long long minsum = 0;
		if (depth == Q)
			return sum;
		for(int i = 1; i <= Q; i++)
			if (!e[rel[i]]) {
				e[rel[i]] = true;
				long long tmp = 0;
				for(int u = rel[i]+1; u <= P; u++)
					if (e[u])
						break;
					else
						tmp++;
				for(int u = rel[i]-1; u > 0; u--)
					if (e[u])
						break;
					else
						tmp++;
				if (minsum == 0)	
					minsum = solve(P, Q, rel, e, sum+tmp, depth+1);
				else
					minsum = min(minsum, 
					solve(P, Q, rel, e, sum+tmp, depth+1));
				e[rel[i]] = false;
			}
		return minsum;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	for(int i = 1; i <= T; i++) {
		int P, Q;
		fin >> P >> Q;
		released rel;
		for(int i2 = 1; i2 <= Q; i2++) {
			fin >> rel[i2];
		}
		empty eee;
		for(int i2 = 0; i2 <= P; i2++)
			eee[i2] = false;
		fout << "Case #" << i << ": " << solve(P, Q, rel, eee) << endl;	
	}
	fin.close();
	fout.close();
	return 0;
}
