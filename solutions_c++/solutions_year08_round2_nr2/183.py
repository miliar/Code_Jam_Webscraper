/*
Number Sets
View problem statement. Download inputs once your code is ready.
(you will have limited time to submit your answer)
Small input
5 points	
More options   ¨‹
SubmitYou have solved this input set.Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp
Large input
10 points	
Redownload A-large.inMore options   ¨‹
SubmitYour submission was received. You can still resubmit for 5:23 minutes.
Only your last submission counts.
Time Remaining: 5:23  
You may resubmit this multiple times within the remaining
time-frame. Only your last submission will count.
your output file:
source file(s):  	
remove
Add another file

Problem

Some pranksters have watched too much Discovery Channel and now they want to build a crop triangle during the night. They want to build it inside a large crop that looks like an evenly spaced grid from above. There are some trees planted on the field. Each tree is situated on an intersection of two grid lines (a grid point). The pranksters want the vertices of their crop triangle to be located at these trees. Also, for their crop triangle to be more interesting they want the center of that triangle to be located at some grid point as well. We remind you that if a triangle has the vertices (x1, y1), (x2, y2) and (x3, y3), then the center for this triangle will have the coordinates ((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3).

You will be given a set of points with integer coordinates giving the location of all the trees on the grid. You are asked to compute how many triangles you can form with distinct vertexes in this set of points so that their center is a grid point as well (i.e. the center has integer coordinates).

If a triangle has area 0 we will still consider it a valid triangle.

Input

The first line of input gives the number of cases, N. N test cases follow. Each test case consists of one line containing the integers n, A, B, C, D, x0, y0 and M separated by exactly one space. n will be the number of trees in the input set. Using the numbers n, A, B, C, D, x0, y0 and M the following pseudocode will print the coordinates of the trees in the input set. mod indicates the remainder operation.

The parameters will be chosen such that the input set of trees will not have duplicates.

X = x0, Y = y0
print X, Y
for i = 1 to n-1
  X = (A * X + B) mod M
  Y = (C * Y + D) mod M
  print X, Y

Output

For each test case, output one line containing "Case #X: " where X is the test case number (starting from 1). This should be followed by an integer indicating the number of triangles which can be located at 3 distinct trees and has a center that is a grid point.

Limits

1 <= N <= 10,
0 <= A, B, C, D, x0, y0<= 109,
1 <= M <= 109.

Small dataset

3 <= n <= 100.

Large dataset

3 <= n <= 100000.

Sample

Input
  	
Output
 
2
4 10 7 1 2 0 1 20
6 2 0 2 1 1 2 11

	Case #1: 1
Case #2: 2

In the first test case, the 4 trees in the generated input set are (0, 1), (7, 3), (17, 5), (17, 7).
View problem statement. Download inputs once your code is ready.
(you will have limited time to submit your answer)
Small input
10 points	
Download B-small.inMore options   ¨‹
SubmitYou may try multiple times. (Penalty for incorrect submissions.)Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp
Large input
25 points	
Download B-large.inMore options   ¨‹
SubmitYou have 8 minutes to solve 1 input file. (Judged after contest.)Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp

Problem

You start with a sequence of consecutive integers. You want to group them into sets.

You are given the interval, and an integer P. Initially, each number in the interval is in its own set.

Then you consider each pair of integers in the interval. If the two integers share a prime factor which is at least P, then you merge the two sets to which the two integers belong.

How many different sets there will be at the end of this process?

Input

One line containing an integer C, the number of test cases in the input file.

For each test case, there will be one line containing three single-space-separated integers A, B, and P. A and B are the first and last integers in the interval, and P is the number as described above.

Output

For each test case, output one line containing the string "Case #X: Y" where X is the number of the test case, starting from 1, and Y is the number of sets.

Limits

Small dataset

1 <= C <= 10

1 <= A <= B <= 1000

2 <= P <= B

Large dataset

1 <= C <= 100

1 <= A <= B <= 1012

B <= A + 1000000

2 <= P <= B

Sample

Input
  	
Output
 
2
10 20 5
10 20 3

Case #1: 9
Case #2: 7
*/

#include <fstream>
#include <algorithm>

using namespace std;

ifstream ifs("B-small-attempt0.in");
ofstream ofs("B-small-attempt0.out");

#include <cstring>

const int MAXN = 1 << 20;

class DSet {
public:
	int p[MAXN],t;
	
	void init() {
		for (int i = 0; i < MAXN; i++) {
			p[i] = i;
		}
	}

	int root(int x)
	{
		if (p[x] == x) {
			return x;
		}
		else {
			return p[x] = root(p[x]);
		}
	}

	void setFriend(int i, int j) {
		i = root(i);
		j = root(j);
		p[i] = j;
	}

	int cnt(int n)
	{
		int ret = 0;

		for (int i = 0; i < n; i++) {
			if (p[i] == i) {
				ret++;
			}
		}

		return ret;
	}
};

#include <cmath>

unsigned int plist[500000], pcount;
unsigned int isPrime[(MAXN >> 5) + 1];

#define setbitzero(a) (isPrime[(a) >> 5] &= (~(1 << ((a) & 31))))
#define setbitone(a) (isPrime[(a) >> 5] |= (1 << ((a) & 31)))
#define ISPRIME(a) (isPrime[(a) >> 5] & (1 << ((a) & 31)))

void initPrime() {
	int i, j, m;
	int t = (MAXN >> 5) + 1;
	for (i = 0; i < t; ++i) {
		isPrime[i] = 2863311530;
	}
	plist[0] = 2;
	setbitone(2);
	setbitzero(1);
	m = (int) sqrt((double) MAXN);
	pcount = 1;
	for (i = 3; i <= m; i += 2) {
		if (ISPRIME(i)) {
			plist[pcount++] = i;
			for (j = i << 1; j <= MAXN; j += i) {
				setbitzero(j);
			}
		}
	}
	if (!(i & 1)) {
		++i;
	}
	for (; i <= MAXN; i += 2) {
		if (ISPRIME(i)) {
			plist[pcount++] = i;
		}
	}
}

DSet ds;

int main(void)
{
	int re;
	long long a, b, p;

	initPrime();
	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		ifs >> a >> b >> p;
		ds.init();
		for (int i = lower_bound(plist, plist + pcount, p) - plist; a + plist[i] <= b; i++) {
			long long tmp = (a + plist[i] - 1) / plist[i] * plist[i];
			for (long long j = tmp + plist[i]; j <= b; j += plist[i]) {
				ds.setFriend(tmp - a, j - a);
			}
		}
		ofs << "Case #" << ri << ": " << ds.cnt(b - a + 1) << endl;
	}

	return 0;
}