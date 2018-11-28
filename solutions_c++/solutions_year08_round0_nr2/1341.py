#include <iostream>
using namespace std;

int n;
int t;
int nA;
int nB;
int timeA[101][3];
int timeB[101][3];
int result[100][2];

void Sort(int [100][3], int, int);
int AddMin(int);

void main()
{
	int hr;
	int min;
	char ch;

	cout<<"Enter number of inputs :";
	cin>>n;
	cout<<"Enter entire input set, all at once"<<endl;

	for(int i=0; i<n; i++)
	{
		cin>>t;
		cin>>nA>>nB;
		int j;

		for(j=0; j<nA; j++)
		{
			cin>>hr>>ch>>min;
			timeA[j][0]=hr*100+min;

			cin>>hr>>ch>>min;
			timeA[j][1]=hr*100+AddMin(min);

			timeA[j][2]=0;
		}
		timeA[j][0]=9999;
		timeA[j][1]=9999;

		for(j=0; j<nB; j++)
		{
			cin>>hr>>ch>>min;
			timeB[j][0]=hr*100+min;

			cin>>hr>>ch>>min;
			timeB[j][1]=hr*100+AddMin(min);

			timeB[j][2]=0;
		}
		timeB[j][0]=9999;
		timeB[j][1]=9999;

		result[i][0]=0;
		result[i][1]=0;

		Sort(timeA, nA, 0);
		Sort(timeB, nB, 1);

		for(int j=0; j<nB; j++)
		{
			for(int k=0; k<nA; k++)
			{
				if(timeB[j][1]<=timeA[k][0] && timeA[k][2]==0)
				{
					timeA[k][2]=1;
					break;
				}
			}
		}

		Sort(timeA, nA, 1);
		Sort(timeB, nB, 0);

		for(int j=0; j<nA; j++)
		{
			for(int k=0; k<nB; k++)
			{
				if(timeA[j][1]<=timeB[k][0] && timeB[k][2]==0)
				{
					timeB[k][2]=1;
					break;
				}
			}
		}

		//calculate result

		for(int j=0; j<nA; j++)
		{
			if(timeA[j][2]==0)
				result[i][0]++;
		}
		for(int j=0; j<nB; j++)
		{
			if(timeB[j][2]==0)
				result[i][1]++;
		}
	}

	for(int i=0; i<n; i++)
	{
		cout<<endl<<"Case #"<<i+1<<": "<<result[i][0]<<" "<<result[i][1];
	}
}

void Sort(int time[101][3], int count, int x)
{
	int swap[3];
	for(int i=0; i<count-1; i++)
	{
		for(int j=0; j<count-1; j++)
		{
			if(time[j][x]>time[j+1][x])
			{
				swap[0]=time[j][0];
				swap[1]=time[j][1];
				swap[2]=time[j][2];

				time[j][0]=time[j+1][0];
				time[j][1]=time[j+1][1];
				time[j][2]=time[j+1][2];

				time[j+1][0]=swap[0];
				time[j+1][1]=swap[1];
				time[j+1][2]=swap[2];
			}
		}
	}
}

int AddMin(int x)
{
	int output;

	if(x+t>=60)
		output=100+(x+t-60);
	else
		output=x+t;

	return output;
}