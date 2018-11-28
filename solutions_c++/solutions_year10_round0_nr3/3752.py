#include<iostream.h>
#include<conio.h>


int calculateMoney(int [], int, int);
int rearrangeArray(int[], int, int);


int main()
{
    int T, R, k, N, i, j, size_of_group[10], no_of_trips;
    long int money_earned,answer[1000];
    cin >> T;
    for(i = 0; i < T; i++)
    {
		cin >> R >> k >> N;    // Max no. of trips
		for(j = 0; j < N; j++)
		{
			cin >> size_of_group[j];
		}

		money_earned = 0;
		for(no_of_trips = 1; no_of_trips <= R; no_of_trips++)
		{
			money_earned += calculateMoney(size_of_group, k, N);
		}

		answer[i] = money_earned;

	}
	for(i = 0; i < T; i++)
	cout << "Case #" << (i+1) << ": " << answer[i] << endl;
	return 0;
}



/* To calculate the money */
int calculateMoney(int size_of_group[], int k, int N)
{
	int i, people_in = 0, no_of_shifts ;
	for(i = 0; i < N; i++)
	{
		if((people_in + size_of_group[i]) <= k)
		people_in += size_of_group[i];
		else
		{
			no_of_shifts = i;
			rearrangeArray(size_of_group, N, no_of_shifts);
			break;
		}
	}
	return people_in;
}



/* To rearrange the queue */
int rearrangeArray(int size_of_group[], int N, int no_of_shifts)
{
 int i, temp;

 while(no_of_shifts>0)
 {
  temp = size_of_group[0];
  for(i = 0; i < N-1; i++)
  {
	size_of_group[i] = size_of_group[i+1];
  }
  size_of_group[i] = temp;
  no_of_shifts--;
 }
}
