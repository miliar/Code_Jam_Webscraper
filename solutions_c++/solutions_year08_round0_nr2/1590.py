#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

#define MAXN 100


using namespace std;

int get_line_number()
{
	int n;

	string s_temp;
	getline(cin, s_temp);
	istringstream s_temp2(s_temp);
	s_temp2 >> n;

	return n;
}


int get_int_from_time(string h)
{
	int i;

	istringstream mins(h.substr(3,5));
	int temp;
	mins >> temp;


	i = temp;

	istringstream hours(h.substr(0,2));
	hours >> temp;

	i += 60*temp;

	return i;
}


int process(int T, int N1, int *departures, int N2, int *arrivals)
{
	int result = N1;

	set<int> taken_trains;
	map<int, int> assoc_trains;

	for (int t = 0; t < N1; t++)
	{
		int timeaux = -1;
		int candidate = -1;

		for (int i = 0; i < N2; i++)
		{
			if (taken_trains.find(i) == taken_trains.end())
			{
				if ((arrivals[i] + T <= departures[t]) && (arrivals[i] + T > timeaux))
				{
					timeaux = arrivals[i] + T;
					candidate = i;
				}
			}
		}


		if (candidate != -1)
		{
			taken_trains.insert(candidate);
			result--;
		}
		
	}

	return result;
}


int main()
{
	int N;
	N = get_line_number();
	for (int n=1; n<=N; n++)
	{
		int T = get_line_number();

		string stemp;

		getline(cin, stemp, ' ');
		istringstream sstemp(stemp);
		int NA;
		sstemp >> NA;

		getline(cin, stemp);
		istringstream sstemp2(stemp);
		int NB;
		sstemp2 >> NB;

		int departure_A[MAXN];
		int arrival_B[MAXN];

		for (int i = 0; i < NA; i++)
		{
			getline(cin, stemp, ' ');
			departure_A[i] = get_int_from_time(stemp);

			getline(cin, stemp);
			arrival_B[i] = get_int_from_time(stemp);
		}

		int departure_B[MAXN];
		int arrival_A[MAXN];

		for (int i = 0; i < NB; i++)
		{
			getline(cin, stemp, ' ');
			departure_B[i] = get_int_from_time(stemp);

			getline(cin, stemp);
			arrival_A[i] = get_int_from_time(stemp);
		}

		int NtrainsA = process(T, NA, departure_A, NB, arrival_A);
		int NtrainsB = process(T, NB, departure_B, NA, arrival_B);

		cout << "Case #" << n << ": " << NtrainsA << " " << NtrainsB << endl;
	}
}

