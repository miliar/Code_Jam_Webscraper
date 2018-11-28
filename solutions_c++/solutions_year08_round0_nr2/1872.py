#include <iostream>
#include <fstream>

using namespace std;

const int MN = 22;

ifstream inf("B-small-attempt3.in");
ofstream outf("B-small-attempt3.txt");

int N = 0;
int T = 0;
int NA = 0;
int aTimeTable[MN][2] = {0};
int NB = 0;
int bTimeTable[MN][2] = {0};

int as = 0;
int AT[MN] = {0};
int bs = 0;
int BT[MN] = {0};


int bubbleSort(int array[][2], int number)
{
	int i,j,t,s;
	for(j=1; j<=number; j++)
		for(i=0; i<(number-j); i++)
		{
			if(array[i][0] > array[i+1][0])
			{
				t=array[i][0];
				array[i][0]=array[i+1][0];
				array[i+1][0]=t;

				s=array[i][1];
				array[i][1]=array[i+1][1];
				array[i+1][1]=s;
			}//if
		}//for
		return 0;
}//bubbleSort

int insertTrain(int * arr, int time)
{
	int i;
	int number = arr[0];
	for ( i = number; i >= 1; i-- )
	{
		if ( time > arr[i])
		{
			arr[i+1] = time;
			arr[0]++;
			return 0;
		}//if

		arr[i+1] = arr[i];
	}//for
	arr[1] = time;
	arr[0]++;
	return 0;
}//insertTrain

int deletTrain(int *arr, int index)
{
	int i = 0;
	for (i = index; i < arr[0]; i++)
	{
		arr[i] = arr[i+1];
	}
	arr[0]--;
	return 0;
}

int train(int tt[2], int * arr1, int * arr2)
{
	int i;
	if (arr1[0] > 0)
	{
		for ( i = 1; i <= arr1[0]; i++ )
		{
			if ( tt[0] >= arr1[i] )
			{
				deletTrain(arr1,i);
				insertTrain(arr2,tt[1]+T);
				return 0;
			}//if
		}//for
	}//if

	insertTrain(arr2, tt[1] + T);

	if ( arr1 == AT)
		as++;
	else
		bs++;

	return 0;
}


int main()
{

	int i, j, k;

	inf>>N;
	for ( k = 0; k < N; k++)
	{
		inf>>T;
		inf>>NA;
		inf>>NB;
		for ( i = 0; i < NA; i++)
		{
			char t;
			inf>>t;
			aTimeTable[i][0] = aTimeTable[i][0] * 10 + (t - '0');
			inf>>t;
			aTimeTable[i][0] = aTimeTable[i][0] * 10 + (t - '0');
			inf>>t;
			inf>>t;
			aTimeTable[i][0] = aTimeTable[i][0] * 10 + (t - '0');
			inf>>t;
			aTimeTable[i][0] = aTimeTable[i][0] * 10 + (t - '0');


			inf>>t;
			aTimeTable[i][1] = aTimeTable[i][1] * 10 + (t - '0');
			inf>>t;
			aTimeTable[i][1] = aTimeTable[i][1] * 10 + (t - '0');
			inf>>t;
			inf>>t;
			aTimeTable[i][1] = aTimeTable[i][1] * 10 + (t - '0');
			inf>>t;
			aTimeTable[i][1] = aTimeTable[i][1] * 10 + (t - '0');
			
		}//for

		for ( i = 0; i < NB; i++)
		{
			char t;
			inf>>t;
			bTimeTable[i][0] = bTimeTable[i][0] * 10 + (t - '0');
			inf>>t;
			bTimeTable[i][0] = bTimeTable[i][0] * 10 + (t - '0');
			inf>>t;
			inf>>t;
			bTimeTable[i][0] = bTimeTable[i][0] * 10 + (t - '0');
			inf>>t;
			bTimeTable[i][0] = bTimeTable[i][0] * 10 + (t - '0');
			
			
			inf>>t;
			bTimeTable[i][1] = bTimeTable[i][1] * 10 + (t - '0');
			inf>>t;
			bTimeTable[i][1] = bTimeTable[i][1] * 10 + (t - '0');
			inf>>t;
			inf>>t;
			bTimeTable[i][1] = bTimeTable[i][1] * 10 + (t - '0');
			inf>>t;
			bTimeTable[i][1] = bTimeTable[i][1] * 10 + (t - '0');
		}//for

		bubbleSort(aTimeTable,NA);
		bubbleSort(bTimeTable,NB);
		
		aTimeTable[NA][0] = 2500;
		bTimeTable[NB][0] = 2500;
		i = 0; j = 0;
		while ( i < NA ||j < NB )
		{
			if ( aTimeTable[i][0] < bTimeTable[j][0] )
			{
				train(aTimeTable[i],AT,BT);
				i++;
				
			}//if
			else
			{
				train(bTimeTable[j],BT,AT);
				j++;

			}//else
		}//while
		
		outf<<"Case #"<<k+1<<": "<<as<<" "<<bs<<"\n";
		T = 0;
		NA = 0; NB = 0;
		memset(aTimeTable,0,sizeof(int)*MN*2);
		memset(bTimeTable,0,sizeof(int)*MN*2);
		memset(AT,0,sizeof(int)*MN);
		memset(BT,0,sizeof(int)*MN);
		as = 0; bs = 0;
	}
	return 0;
}