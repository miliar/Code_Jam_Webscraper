#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;

//int IsInsideVector(vector<long long> v, long long x);

void main()
{
	FILE* fpIn = fopen("C:\\A.txt", "r");
	if(fpIn == NULL)
		printf("Unable to read file from C:\\A-large-attempt0.in");

	FILE *fpOut = fopen("C:\\output.txt", "w");
	if(fpOut == NULL)
		printf("Unable to create a output file at C:\\output.txt");


	int total_tests = 1;
	int case_num = 1;

//	int index1, index2, index3;
	int points;
	long result = 0;
	vector<long long> vX;
	vector<long long> vY;
	fscanf(fpIn, "%d", &total_tests);
	long n, A, B, C, D, x0, y0, M;
	long long X,Y;
	while(case_num<=total_tests)
	{
		fscanf(fpIn, "%ld%ld%ld%ld%ld%ld%ld%ld", &n, &A, &B, &C, &D, &x0, &y0, &M);

		X = x0;
		Y = y0;
		vX.push_back(X);
		vY.push_back(Y);
		for(int i = 1; i<= n-1; i++)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			vX.push_back(X);
			vY.push_back(Y);
		}

		int points = vX.size();
		for(long long index1 = 0; index1< points-2; index1++)
		{
			for(long long index2 = index1+1; index2< points-1; index2++)
			{
				for(long long index3 = index2+1; index3<points; index3++)
				{
					long long centerX = (vX[index1] + vX[index2] + vX[index3]);
					if(centerX % 3 == 0)
						centerX = centerX/3;
					else
						continue;

					long long centerY = (vY[index1] + vY[index2] + vY[index3]);
					if(centerY % 3== 0)
						centerY = centerY/3;
					else
						continue;
					
				//	if((IsInsideVector(vX, centerX)==1) && (IsInsideVector(vY,centerY)==1))
						result++;
				}
			}
		}

		fprintf(fpOut, "Case #%d: %ld\n", case_num, result);
		cout<<result<<endl;
		vX.clear();
		vY.clear();
		result = 0;
		case_num++;
	}	
}

// int IsInsideVector(vector<long long> v, long long x)
// {
// 	vector<long long>::iterator i;
// 	for(i = v.begin(); i != v.end(); i++)
// 	{
// 		if(*i == x)
// 			return 1;
// 	}
// 	return 0;
// }