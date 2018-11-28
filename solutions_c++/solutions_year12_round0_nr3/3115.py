#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	int *A;
	int *B;
	int *result;

	ifstream fin ("C-small-attempt2.IN");
	fin >> T;

	A = new int [T];
	B = new int [T];
	result = new int [T];

	for (int i=0; i<T; i++)
	{
		fin >> A[i] >> B[i];
		result[i] = 0;
	}

	for (int i=0; i<T; i++)
	{
		if (A[i]<100)
		{
			for (int j=0; j<(B[i]-A[i]+1); j++)
			{
				if (((((A[i]+j)%10)*10 + ((A[i]+j)-(A[i]+j)%10)/10) >= A[i]) &&
					((((A[i]+j)%10)*10 + ((A[i]+j)-(A[i]+j)%10)/10) <= B[i]))
				{
					if ((A[i]+j)%10 != ((A[i]+j)-(A[i]+j)%10)/10)
					{
						result[i]++;
					}
				}
			}

			if (result[i]%2==1)
			{
					result[i] /=2;
					result[i] +=1;
			}
			else
				result[i] /=2;
		}


		//100-999
		else if (A[i]<1000)
		{
			for (int j=0; j<(B[i]-A[i]+1); j++)
			{
				if (((((A[i]+j)%10)*100 + ((A[i]+j)-(A[i]+j)%10)/10) >= A[i]) &&
					((((A[i]+j)%10)*100 + ((A[i]+j)-(A[i]+j)%10)/10) <= B[i]))
				{
					if (!((A[i]+j)%10 == ((A[i]+j-(A[i]+j)%10-((A[i]+j)-(A[i]+j)%100))/10) && ((A[i]+j)%10 == (A[i]+j-(A[i]+j)%100)/100)))
						result[i]++;
				}
			}

			for (int j=0; j<(B[i]-A[i]+1); j++)
			{
				if (((((A[i]+j)%100)*10 + ((A[i]+j)-(A[i]+j)%100)/100) >= A[i]) &&
					((((A[i]+j)%100)*10 + ((A[i]+j)-(A[i]+j)%100)/100) <= B[i]))
				{
					if (!((A[i]+j)%10 == ((A[i]+j-(A[i]+j)%10-((A[i]+j)-(A[i]+j)%100))/10) && ((A[i]+j)%10 == (A[i]+j-(A[i]+j)%100)/100)))
						result[i]++;
				}
			}

			if (result[i]%2==1)
			{
					result[i] /=2;
					result[i] +=1;
			}
			else
				result[i] /=2;
		}


		//1000-9999
		else if (A[i]<10000)
		{
			for (int j=0; j<(B[i]-A[i]+1); j++)
			{
				if (((((A[i]+j)%10)*1000 + ((A[i]+j)-(A[i]+j)%10)/10) >= A[i]) &&
					((((A[i]+j)%10)*1000 + ((A[i]+j)-(A[i]+j)%10)/10) <= B[i]))
				{
					if (!(((A[i]+j)%10 == (((A[i]+j)-(A[i]+j)%1000)/1000)) &&
						((A[i]+j)%10 == (((A[i]+j)-(A[i]+j)%100)-((A[i]+j)-(A[i]+j)%1000))/100) &&
						((A[i]+j)%10 == (((A[i]+j)-(A[i]+j-(A[i]+j)%100)-(A[i]+j)%10))/10)))
					{
						if (!(((A[i]+j)%100) == ((A[i]+j)-((A[i]+j)%100))/100))
						{
							cout << A[i]+j << endl;
							result[i]++;
						}
					}
				}
			}

			for (int j=0; j<(B[i]-A[i]+1); j++)
			{
				if (((((A[i]+j)%100)*100 + ((A[i]+j)-(A[i]+j)%100)/100) >= A[i]) &&
					((((A[i]+j)%100)*100 + ((A[i]+j)-(A[i]+j)%100)/100) <= B[i]))
				{
					if (!(((A[i]+j)%10 == (((A[i]+j)-(A[i]+j)%1000)/1000)) &&
						((A[i]+j)%10 == (((A[i]+j)-(A[i]+j)%100)-((A[i]+j)-(A[i]+j)%1000))/100) &&
						((A[i]+j)%10 == (((A[i]+j)-(A[i]+j-(A[i]+j)%100)-(A[i]+j)%10))/10)))
					{
						if (!(((A[i]+j)%100) == ((A[i]+j)-((A[i]+j)%100))/100))
						{
							cout << A[i]+j << endl;
							result[i]++;
						}
					}
				}
			}

			for (int j=0; j<(B[i]-A[i]+1); j++)
			{
				if (((((A[i]+j)%1000)*10 + ((A[i]+j)-(A[i]+j)%1000)/1000) >= A[i]) &&
					((((A[i]+j)%1000)*10 + ((A[i]+j)-(A[i]+j)%1000)/1000) <= B[i]))
				{
					if (!(((A[i]+j)%10 == (((A[i]+j)-(A[i]+j)%1000)/1000)) &&
						((A[i]+j)%10 == (((A[i]+j)-(A[i]+j)%100)-((A[i]+j)-(A[i]+j)%1000))/100) &&
						((A[i]+j)%10 == (((A[i]+j)-(A[i]+j-(A[i]+j)%100)-(A[i]+j)%10))/10)))
					{
						if (!(((A[i]+j)%100) == ((A[i]+j)-((A[i]+j)%100))/100))
						{
							cout << A[i]+j << endl;
							result[i]++;
						}
					}
				}
			}

			if (result[i]%2==1)
			{
					result[i] /=2;
					result[i] +=1;
			}
			else
				result[i] /=2;
		}
		
	}

	ofstream fout ("C.txt");

	for (int i=0; i<T; i++)
	{
		fout << "Case #";
		fout << i+1;
		fout << ": ";

		fout << result[i];
		fout << endl;
	}

	delete [] A;
	delete [] B;
	delete [] result;

	return 0;
}