#include <cstdio>

using namespace std;

int N, T, NA, NB;

struct Time
{
	int HH;
	int MM;
};

struct TimeTable
{
	Time S;
	Time E;
};

TimeTable A_Time[100];
TimeTable B_Time[100];

bool	  A_Use[100];
bool	  B_Use[100];

void InputData()
{
	scanf("%d", &T);
	scanf("%d %d", &NA, &NB);

	for(int i = 0; i < NA; i++ )
	{
		scanf("%d:%d %d:%d", &A_Time[i].S.HH, &A_Time[i].S.MM, 
							 &A_Time[i].E.HH, &A_Time[i].E.MM);
	}

	for(int i = 0; i < NB; i++ )
	{
		scanf("%d:%d %d:%d", &B_Time[i].S.HH, &B_Time[i].S.MM, 
							 &B_Time[i].E.HH, &B_Time[i].E.MM);
	}
}

void Swap(TimeTable& l, TimeTable& r)
{
	TimeTable t;
	t = l;
	l = r;
	r = t;
}

void Sort(int count, TimeTable* in)
{
	for(int i = 0; i < count; i++ )
	{
		for(int j = 0; j < count-1; j++ )
		{
			if( in[j].S.HH > in[j+1].S.HH )
			{
				Swap(in[j], in[j+1]);
			}
			else if( in[j].S.HH == in[j+1].S.HH )
			{
				if( in[j].S.MM > in[j+1].S.MM )
				{
					Swap(in[j], in[j+1]);
				}
			}
		}
	}

}

void Sort()
{
	Sort(NA, A_Time);
	Sort(NB, B_Time);
}

void InitUseVector()
{
	for(int i = 0; i < 100; i++ )
	{
		A_Use[i] = false;
		B_Use[i] = false;
	}
}

void FindNextTrain(int nDep, int nArr, TimeTable* pDep, TimeTable* pArr, bool* UseVector)
{
	TimeTable Temp;
	for(int i = 0; i < nDep; i++)
	{
		Temp.S.HH = pDep[i].S.HH;
		Temp.S.MM = pDep[i].S.MM;

		Temp.E.MM = pDep[i].E.MM + T;
		if( Temp.E.MM >= 60 )
		{
			Temp.E.HH = 1;
			Temp.E.MM -= 60;
		}
		else
		{
			Temp.E.HH = 0;
		}

		Temp.E.HH += pDep[i].E.HH;

		for(int j = 0; j < nArr; j++ )
		{
			if( UseVector[j] ) continue;
			if( pArr[j].S.HH == Temp.E.HH 
				&& pArr[j].S.MM >= Temp.E.MM )
			{
				UseVector[j] = true;
				break;
			}
			if( pArr[j].S.HH > Temp.E.HH )
			{
				UseVector[j] = true;
				break;
			}
		}
	}
}

void SelectTrain()
{
	InitUseVector();
	FindNextTrain(NA, NB, A_Time, B_Time, B_Use);
	FindNextTrain(NB, NA, B_Time, A_Time, A_Use);
}

int GetResult(int count, bool* vec)
{
	int result = 0;
	for(int i = 0; i < count; i++ )
	{
		if( !vec[i] ) result++;
	}

	return result;
}

int GetResultA()
{
	return GetResult(NA, A_Use);
}

int GetResultB()
{
	return GetResult(NB, B_Use);
}

int main()
{
	scanf("%d", &N);

	int count = 1;

	while( N --> 0 )
	{
		InputData();
		Sort();
		SelectTrain();

		printf("Case #%d: %d %d\n", count, GetResultA(), GetResultB());
		count++;
	}

	return 0;
}
