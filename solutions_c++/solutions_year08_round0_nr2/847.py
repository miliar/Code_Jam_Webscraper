#include <iostream>

using namespace std;

void bubblesort(int num, int array[], int endarray[])
{
	for(int i=0; i<num; ++i)
		for(int j=i+1; j<num; ++j)
			if(array[j] < array[i])
			{
				int temp = array[j];
				array[j] = array[i];
				array[i] = temp;
				temp = endarray[j];
				endarray[j] = endarray[i];
				endarray[i] = temp;
			}
}

void remove(int size, int pos, int array[])
{
	for(int i=pos+1; i<size; ++i)
		array[i-1] = array[i];
}

int main()
{
	int N, T, NA, NB, itemp;
	char ctemp;
	int ATrips[100], BTrips[100], aavail, bavail, Aend[100], Bend[100];
	int lefta, leftb;
	cin >> N;
	for(int casenum = 0; casenum < N; ++ casenum)
	{
		cin >> T >> NA >> NB;
		for(int reads = 0; reads < NA; ++reads)
		{
			cin >> itemp >> ctemp;
			ATrips[reads] = 60 * itemp;
			cin >> itemp;
			ATrips[reads] += itemp;

			cin >> itemp >> ctemp;
			Aend[reads] = 60 * itemp;
			cin >> itemp;
			Aend[reads] += itemp;
			Aend[reads] += T;
		}
		for(int reads = 0; reads < NB; ++reads)
		{
			cin >> itemp >> ctemp;
			BTrips[reads] = 60 * itemp;
			cin >> itemp;
			BTrips[reads] += itemp;

			cin >> itemp >> ctemp;
			Bend[reads] = 60 * itemp;
			cin >> itemp;
			Bend[reads] += itemp;
			Bend[reads] += T;
		}
		bubblesort(NA, ATrips, Aend);
		bubblesort(NB, BTrips, Bend);

		cout << "Case #" << casenum+1 << ": ";
		lefta = NA; leftb = NB;
		for(int i = 0; i < NA; ++ i)
			for(int j=0; j<leftb; ++j)
				if(Aend[i] <= BTrips[j])
				{
					remove(leftb--, j, BTrips);
					break;
				}
		for(int i = 0; i < NB; ++ i)
			for(int j=0; j<lefta; ++j)
				if(Bend[i] <= ATrips[j])
				{
					remove(lefta--, j, ATrips);
					break;
				}
		cout << lefta << " " << leftb << endl;
	}

	return 0;
}
