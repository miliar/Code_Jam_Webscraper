#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable: 4018)
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

struct point
{
	double X, Y;
};

int NNNN, TT;
int N, M, NN, MM;
int Count;
double Width, TotArea, Area;
point Lowers[101];
point Uppers[101];
double List[101];

int main()
{
	cin >> NNNN;
	for (TT = 1; TT <= NNNN; TT++)
	{
		cin >> Width >> N >> M >> Count;
		for (int I = 0; I < N; I++)
			cin >> Lowers[I].X >> Lowers[I].Y;
		for (int I = 0; I < M; I++)
			cin >> Uppers[I].X >> Uppers[I].Y;
		TotArea = 0;
		for (int I = 0; I < N - 1; I++)
			TotArea -= (Lowers[I + 1].X - Lowers[I].X) * (Lowers[I].Y + Lowers[I + 1].Y) / 2;
		for (int I = 0; I < M - 1; I++)
			TotArea += (Uppers[I + 1].X - Uppers[I].X) * (Uppers[I].Y + Uppers[I + 1].Y) / 2;
		Area = TotArea / Count;
		NN = MM = 0;
		for (int I = 0; I < Count - 1; I++)
		{
			double Remain = Area ;
			while (Remain > 0)
			{
				double H = Uppers[MM].Y - Lowers[NN].Y;
				double UpDelta = (Uppers[MM + 1].Y - Uppers[MM].Y) / (Uppers[MM + 1].X - Uppers[MM].X);
				double LowDelta = (Lowers[NN + 1].Y - Lowers[NN].Y) / (Lowers[NN + 1].X - Lowers[NN].X);
				double Delta = UpDelta - LowDelta;
				double W = min(Uppers[MM + 1].X, Lowers[NN + 1].X) - Lowers[NN].X;
				double Temp = W * H + Delta * W * W / 2;
				if (Temp < Remain)
				{
					Remain -= Temp;
				}
				else
				{
					double A = Delta / 2;
					double B = H;
					double C = -Remain;
					if (fabs(A) > 1e-10)
						W = (-B + sqrt(B * B - 4 * A * C)) / (2 * A);
					else
						W = -C / B;
					Temp = W * H + Delta * W * W / 2;
					Remain = 0;
					List[I] = Lowers[NN].X + W;
				}
				Lowers[NN].X += W;
				Lowers[NN].Y += LowDelta * W;
				Uppers[MM].X += W;
				Uppers[MM].Y += UpDelta * W;
				if (Lowers[NN].X + 1e-12 >= Lowers[NN + 1].X) NN++;
				if (Uppers[MM].X + 1e-12 >= Uppers[MM + 1].X) MM++;
			}
		}
		printf("Case #%d:\n", TT);
		for (int I = 0; I < Count - 1; I++)
			printf("%.12f\n", List[I]);
	}
	return 0;
}
