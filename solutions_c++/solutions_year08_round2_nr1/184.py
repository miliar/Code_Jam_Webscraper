/*
Crop Triangles
View problem statement. Download inputs once your code is ready.
(you will have limited time to submit your answer)
Small input
5 points	
Download A-small.inMore options   ¨‹
SubmitYou may try multiple times. (Penalty for incorrect submissions.)Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp
Large input
10 points	
Download A-large.inMore options   ¨‹
SubmitYou have 8 minutes to solve 1 input file. (Judged after contest.)Your submission was received. You can still resubmit for minutes.
Only your last submission counts.
temp

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
0 <= A, B, C, D, x0, y0, M<= 109.

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
*/

#include <fstream>

using namespace std;

ifstream ifs("A-large.in");
ofstream ofs("A-large.out");

long long cc[3][3];

void gen(int n, int a, int b, int c, int d, int x0, int y0, int m)
{
	long long x = x0, y = y0;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			cc[i][j] = 0;
		}
	}
	for (int i = 0; i < n; i++) {
		++cc[x % 3][y % 3];
		x = (a * x + b) % m;
		y = (c * y + d) % m;
	}
}

int main(void)
{
	int re;
	int n, a, b, c, d, x0, y0, m;
	long long ans;

	ifs >> re;
	for (int ri = 1; ri <= re; ri++) {
		ifs >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		gen(n, a, b, c, d, x0, y0, m);
		ans = 0;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				ans += cc[i][j] * (cc[i][j] - 1) * (cc[i][j] - 2) / 6;
			}
		}
		for (int i = 0; i < 3; i++) {
			ans += cc[i][0] * cc[i][1] * cc[i][2];
			ans += cc[0][i] * cc[1][i] * cc[2][i];
		}
		ans += cc[0][0] * cc[1][1] * cc[2][2];
		ans += cc[0][0] * cc[1][2] * cc[2][1];
		ans += cc[0][1] * cc[1][0] * cc[2][2];
		ans += cc[0][1] * cc[1][2] * cc[2][0];
		ans += cc[0][2] * cc[1][0] * cc[2][1];
		ans += cc[0][2] * cc[1][1] * cc[2][0];
		ofs << "Case #" << ri << ": " << ans << endl;
	}

	return 0;
}

