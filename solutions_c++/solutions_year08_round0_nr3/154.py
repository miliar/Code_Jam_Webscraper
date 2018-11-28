// GCJ_TennisRacquet.cpp : Defines the entry point for the console application.
//

#include <string.h>
#include <math.h>

const float PI = 3.14159265358979323846f;

struct TPoint
{
	double x, y;
};

double PointDistance(TPoint aPointA, TPoint aPointB)
{
	return sqrt((aPointB.x-aPointA.x)*(aPointB.x-aPointA.x) + (aPointB.y-aPointA.y)*(aPointB.y-aPointA.y));
}

int PointInCircle(TPoint aPoint, double aR)
{
	return aPoint.x*aPoint.x + aPoint.y*aPoint.y <= aR * aR;
}

int RectInCircle(TPoint aUL, TPoint aUR, TPoint aLL, TPoint aLR, double aR)
{
	return PointInCircle(aUL, aR) && PointInCircle(aUR, aR) && PointInCircle(aLL, aR) && PointInCircle(aLR, aR);
}

int _tmain(int argc, _TCHAR* argv[])
{
	// Get N value
	int g_N;
	scanf("%d", &g_N);

	double resultArr[100];

	for (int c = 0; c < g_N; c++)
	{
		resultArr[c] = 0;

		// Get Tunraround Time value
		double g_f;
		scanf("%lf", &g_f);
		double g_R;
		scanf("%lf", &g_R);
		double g_t;
		scanf("%lf", &g_t);
		double g_r;
		scanf("%lf", &g_r);
		double g_g;
		scanf("%lf", &g_g);

		int innerRectCount = ceil(g_R/(g_g + 2*g_r));

		//printf("Inner Rect Count = %d\n", innerRectCount, g_g);

		// Quick Reject Bad Rect
		if (g_g < 2*g_f)
		{
			resultArr[c] = 1;
			continue;
		}

		double holeArea = 0;

		TPoint tUpperLeft, tUpperRight, tLowerLeft, tLowerRight;
		for (int x = -innerRectCount; x < innerRectCount; x++)
			for (int y = -innerRectCount; y < innerRectCount; y++)
			{
				// Find Boundary
				tUpperLeft.x = g_r+(g_g+2*g_r)*x;
				tUpperLeft.y = g_r+g_g+(g_g+2*g_r)*y;

				tLowerRight.x = g_r+g_g+(g_g+2*g_r)*x;
				tLowerRight.y = g_r+(g_g+2*g_r)*y;

				tUpperRight.x = tLowerRight.x;
				tUpperRight.y = tUpperLeft.y;

				tLowerLeft.x = tUpperLeft.x;
				tLowerLeft.y = tLowerRight.y;

				// Contract Rect
				tUpperLeft.x += g_f;
				tUpperLeft.y -= g_f;

				tLowerRight.x -= g_f;
				tLowerRight.y += g_f;

				tUpperRight.x -= g_f;
				tUpperRight.y -= g_f;

				tLowerLeft.x += g_f;
				tLowerLeft.y += g_f;

				if (RectInCircle(tUpperLeft, tUpperRight, tLowerLeft, tLowerRight, g_R-g_t-g_f))
				{
					holeArea += (g_g-2*g_f)*(g_g-2*g_f);
				}
				else
				{
					TPoint tPoint;
					if (tUpperLeft.x <= 0 && tUpperLeft.y >= 0)
					{
						// Flip Horizontal
						tUpperLeft.x = -tUpperLeft.x;
						tUpperRight.x = -tUpperRight.x;
						tLowerLeft.x = -tLowerLeft.x;
						tLowerRight.x = -tLowerRight.x;
						tPoint = tUpperLeft;
						tUpperLeft = tUpperRight;
						tUpperRight = tPoint;
						tPoint = tLowerLeft;
						tLowerLeft = tLowerRight;
						tLowerRight = tPoint;
					}
					else if (tUpperLeft.x <= 0 && tUpperLeft.y <= 0)
					{
						// Flip Horizontal and Flip Vertical
						tUpperLeft.x = -tUpperLeft.x;
						tUpperRight.x = -tUpperRight.x;
						tLowerLeft.x = -tLowerLeft.x;
						tLowerRight.x = -tLowerRight.x;
						tUpperLeft.y = -tUpperLeft.y;
						tUpperRight.y = -tUpperRight.y;
						tLowerLeft.y = -tLowerLeft.y;
						tLowerRight.y = -tLowerRight.y;

						tPoint = tUpperLeft;
						tUpperLeft = tUpperRight;
						tUpperRight = tPoint;
						tPoint = tLowerLeft;
						tLowerLeft = tLowerRight;
						tLowerRight = tPoint;

						tPoint = tUpperLeft;
						tUpperLeft = tLowerLeft;
						tLowerLeft = tPoint;
						tPoint = tUpperRight;
						tUpperRight = tLowerRight;
						tLowerRight = tPoint;
					}
					else if (tUpperLeft.x >= 0 && tUpperLeft.y <= 0)
					{
						// Flip Vertical
						tUpperLeft.y = -tUpperLeft.y;
						tUpperRight.y = -tUpperRight.y;
						tLowerLeft.y = -tLowerLeft.y;
						tLowerRight.y = -tLowerRight.y;
						tPoint = tUpperLeft;
						tUpperLeft = tLowerLeft;
						tLowerLeft = tPoint;
						tPoint = tUpperRight;
						tUpperRight = tLowerRight;
						tLowerRight = tPoint;
					}

					double newR = g_R-g_t-g_f;

					// Check like it's in quarter 1
					int tIsUpperLeftInCircle = PointInCircle(tUpperLeft, newR);
					int tIsLowerLeftInCircle = PointInCircle(tLowerLeft, newR);
					int tIsUpperRightInCircle = PointInCircle(tUpperRight, newR);
					int tIsLowerRightInCircle = PointInCircle(tLowerRight, newR);

					if (tIsLowerLeftInCircle && !tIsUpperLeftInCircle && !tIsUpperRightInCircle && !tIsLowerRightInCircle)
					{
						// Only 1 Point in Circle (Lower Left)
						// Find Intersect Point A B
						TPoint tPointA, tPointB;
						tPointA.x = sqrt(newR*newR - tLowerLeft.y*tLowerLeft.y);
						tPointA.y = tLowerLeft.y;
						tPointB.x = tLowerLeft.x;
						tPointB.y = sqrt(newR*newR - tLowerLeft.x*tLowerLeft.x);
						holeArea += abs((tPointA.y - tPointB.y)*(tPointA.x - tPointB.x) / 2);
						double tC = 2 * asin( PointDistance(tPointA, tPointB) / newR / 2);
						holeArea += newR * newR * (tC - sin(tC)) / 2;
					}
					else if (tIsLowerLeftInCircle && tIsUpperLeftInCircle && !tIsUpperRightInCircle && !tIsLowerRightInCircle)
					{
						// Left Points are in Circle
						// Find Intersect Point A B
						TPoint tPointA, tPointB;
						tPointA.x = sqrt(newR*newR - tUpperLeft.y*tUpperLeft.y);
						tPointA.y = tUpperLeft.y;
						tPointB.x = sqrt(newR*newR - tLowerLeft.y*tLowerLeft.y);
						tPointB.y = tLowerLeft.y;
						holeArea += abs((g_g - 2 * g_f) * (tPointA.x - tUpperLeft.x + tPointB.x - tLowerLeft.x) / 2);
						double tC = 2 * asin( PointDistance(tPointA, tPointB) / newR / 2);
						holeArea += newR * newR * (tC - sin(tC)) / 2;
					}
					else if (tIsLowerLeftInCircle && !tIsUpperLeftInCircle && !tIsUpperRightInCircle && tIsLowerRightInCircle)
					{
						// Lower Points are in Circle
						// Find Intersect Point A B
						TPoint tPointA, tPointB;
						tPointA.x = tLowerLeft.x;
						tPointA.y = sqrt(newR*newR - tLowerLeft.x*tLowerLeft.x);
						tPointB.x = tLowerRight.x;
						tPointB.y = sqrt(newR*newR - tLowerRight.x*tLowerRight.x);
						holeArea += abs((g_g - 2 * g_f) * (tPointA.y - tLowerLeft.y + tPointB.y - tLowerRight.y) / 2);
						double tC = 2 * asin( PointDistance(tPointA, tPointB) / newR / 2);
						holeArea += newR * newR * (tC - sin(tC)) / 2;
					}
					else if (tIsLowerLeftInCircle && tIsUpperLeftInCircle && !tIsUpperRightInCircle && tIsLowerRightInCircle)
					{
						// 3 Points are in Circle
						// Find Intersect Point A B
						TPoint tPointA, tPointB;
						tPointA.x = sqrt(newR*newR - tUpperLeft.y*tUpperLeft.y);
						tPointA.y = tUpperLeft.y;
						tPointB.x = tLowerRight.x;
						tPointB.y = sqrt(newR*newR - tLowerRight.x*tLowerRight.x);
						holeArea += abs((g_g - 2 * g_f) * (tPointA.x - tUpperLeft.x));
						holeArea += abs( (g_g - 2 * g_f + tPointB.y - tLowerRight.y) * (tPointB.x - tPointA.x) / 2);
						double tC = 2 * asin( PointDistance(tPointA, tPointB) / newR / 2);
						holeArea += newR * newR * (tC - sin(tC)) / 2;
					}

				}
			}

		resultArr[c] = (PI * g_R * g_R - holeArea) / (PI * g_R * g_R);
	}

	// Print out the result
	for (int c = 0; c < g_N; c++)
		printf("Case #%d: %f\r\n", c+1, resultArr[c]);

	return 0;
}

