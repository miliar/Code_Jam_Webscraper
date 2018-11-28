#include <iostream>
#include <iomanip>
#include <vector>
#include <math.h>

using namespace std;

typedef vector<int> VI;

int C, N;
VI centerX, centerY, R;

double getmax(double a, double b)
{
  if (a > b)
    return a;
  else
    return b;
}

double getmin(double a, double b, double c)
{
  if (a < b && a < c)
    return a;
  else if (b < c)
    return b;
  else
    return c;
}

double dist(double x1, double y1, double x2, double y2)
{
  return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
}

double solve()
{
  cin >> N;
  R.resize(N);
  centerX.resize(N);
  centerY.resize(N);
  for (int i = 0; i < N; i++)
    cin >> centerX[i] >> centerY[i] >> R[i];

  if (N == 1)
    return R[0];
  else 
    if (N == 2)
      return getmax(R[0], R[1]);
    else
      return 
	getmin(getmax(R[0], (dist(centerX[1],centerY[1],centerX[2],centerY[2])+R[1]+R[2])/2),
	       getmax(R[1], (dist(centerX[2],centerY[2],centerX[0],centerY[0])+R[2]+R[0])/2),
	       getmax(R[2], (dist(centerX[0],centerY[0],centerX[1],centerY[1])+R[0]+R[1])/2));
}

int main()
{
  cin >> C;
  for (int i = 0; i < C; i++)
    cout << "Case #" << i+1 << ": " << setprecision(9) << solve() << endl;

  return 0;
}
