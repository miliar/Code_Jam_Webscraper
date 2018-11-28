// Daniel Grunwald

#include <iostream>
#include <string>
#include <map>

using namespace std;
#define TEST
#ifdef TEST
#define dout(X) cerr << X << endl
#else
#define dout(X) 
#endif

const int MAXINT = 0x7fffffff;
typedef long long int int64;

bool sieve[1000001];
const int MAXP = 2000002;
int parent[MAXP]; // 0..1000000 = prime factors, 1000001..2000000
int rank[MAXP];
int count;

int getRepresentative(int index)
{
	if (parent[index] == index)
		return index;
	else {
		int r = getRepresentative(parent[index]);
		parent[index] = r;
		return r;
	}
}
void combine(int index1, int index2)
{
	index1 = getRepresentative(index1);
	index2 = getRepresentative(index2);
	if (index1 != index2) {
		if (rank[index1] < rank[index2]) {
			parent[index1] = index2;
		} else if (rank[index1] > rank[index2]) {
			parent[index2] = index1;
		} else {
			parent[index1] = index2;
			rank[index2]++;
		}
	}
}

int main()
{
	memset(sieve, 1, sizeof(sieve));
	sieve[0] = false;
	sieve[1] = false;
	for (int i = 2; i < 1000; i++) {
		if (sieve[i]) {
			for (int j = i+i; j < 1000001; j+=i)
				sieve[j] = false;
		}
	}

	int N;
	cin >> N;
	for (int test = 1; test <= N; test++) {
		memset(rank, 0, sizeof(rank));
		for (int j = 0; j < MAXP; j++)
			parent[j] = j;
		int64 A, B, P;
		cin >> A >> B >> P;
		int index = 1000001;
		for (int64 i = A; i <= B; i++) {
			if (P < MAXINT) {
				for (int j = P; j < 1000001; j++) {
					if (sieve[j]) {
						if ((i % j) == 0) {
							combine(index, j);
						}
					} 
				}
			}
			index++;
		}
		index = 1000001;
		int result = 0;
		for (int64 i = A; i <= B; i++) {
			int rep = getRepresentative(index);
			if (rank[rep] != -1) {
				result++;
				rank[rep] = -1;
			}
			index++;
		}
		cout << "Case #" << test << ": " << result << endl;
	}
	return 0;
}