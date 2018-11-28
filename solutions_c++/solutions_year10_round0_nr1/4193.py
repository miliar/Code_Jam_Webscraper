// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

template<typename Type>
class Vector : public vector<Type>
{
public:
	Vector(size_type _Count, const Type& _Val) : vector<Type>(_Count, _Val){}
	int& operator[](int index)
	{
		if(index < 0)
		{
			r = 1;
			return r;
		}
		return vector<Type>::operator[](index);
	}
	int Power(int index)
	{
		if(index < 0)
			return 1;
		int res = 1;
		for(int i = 0; i <= index; i++)
		{
			res &= vector<Type>::operator[](i);
		}
		return res;
	}
	int Res()
	{
		int res = 1;
		for(Vector::iterator iter = this->begin(); iter != this->end(); ++iter)
		{
			res *= *iter;
		}
		return res;
	}
	int r;
};

int _tmain(int argc, _TCHAR* argv[])
{

	int T, N, K;

	ifstream from("input.txt");
	ofstream to("output.txt");

	string input;
	getline(from, input);
	T = atoi(input.c_str());

	for(int c = 0; c < T; c++)
	{

		input.clear();

		getline(from, input);
		istringstream ist(input);
		ostringstream ost;

		ist >> N >> K;

	//int N = 4, K = 20;

		Vector<int> snaps(N, 0), snaps2(N, 0);
		for(int i = 0; i < K; i++)
		{
			for(int j = 0; j < snaps.size(); j++)
			{
				if(i % 2 == 0)
				{
					//int a = snaps[j];
					//int b = snaps[j]^1;
					//int c = snaps.Power(j - 1);
					snaps2[j] = snaps.Power(j - 1) == 0 ? snaps[j]: snaps[j]^1;
				}
				else
				{
					//int a = snaps2[j];
					//int b = snaps2[j]^1;
					//int c = snaps2.Power(j - 1);
					snaps[j] = snaps2.Power(j - 1) == 0 ? snaps2[j]: snaps2[j]^1;
				}
			}
			//if(i % 2)
			//	printf("%d\t\t: %d\t%d\t%d\t%d\t\n", i, snaps[0], snaps[1], snaps[2], snaps[3]);
			//else
			//	printf("%d\t\t: %d\t%d\t%d\t%d\t\n", i, snaps2[0], snaps2[1], snaps2[2], snaps2[3]);

		}

		int res;

		if(K % 2 == 0)
		{
			res = snaps.Res();
		}
		else
			res = snaps2.Res();

		ost<<"Case #"<< c+1 <<": "<< (res == 1? "ON": "OFF")<<'\n';
		to << ost.str();

	}

	from.close();
	to.close();

	return 0;
}

