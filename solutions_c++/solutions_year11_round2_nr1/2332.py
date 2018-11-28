#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt", ios::out | ios::trunc);
	out << setprecision(15);
	int sizeOfTests = 0;
//read
	if (in == 0 || out == 0)
	{
		cout << "Epic fail!";
		return 0;
	}
	in >> sizeOfTests;





	for (int k = 0; k < sizeOfTests; k++)
	{
		int l = 0;
		in >> l;
		bool flag = true;
		int **A = new int*[l];
		double *RPI = new double[l];
		double *WP = new double[l];
		double *OWP = new double[l];
		double *OOWP = new double[l];
		
		double *xWP = new double[l];
		for (int i = 0; i < l; i++)
		{
			A[i] = new int[l];
		}

		for (int i = 0; i < l; i++)
		{
			char temp;
			in.get(temp); // kill "/n"
			for(int j = 0; j < l; j++)
			{
				char c;
				in.get(c);
				switch(c)
				{
				case '1': A[i][j] = 1; break;
				case '0': A[i][j] = -1; break;
				default: A[i][j] = 0; break;
				}
			}
		}

		for (int i = 0; i < l; i++)
		{
			int nwins = 0, n = 0;
			for(int j = 0; j < l; j++)
			{
				if (A[i][j] == -1)
				{
					n++;
				}
				
				if (A[i][j] == 1)
				{
					nwins++;
					n++;					
				}
				
			}
			
			WP[i] = nwins/(double)n;
		}

		// start test
		for (int s = 0; s < l; s++)
		{
			OWP[s] = 0.0;
			
			int opponents = 0;
			for (int i = 0; i < l; i++)
			{
				if (!(s == i || A[s][i] == 0))
				{
					int nwins = 0, n = 0;
					for(int j = 0; j < l; j++)
					{
						if (j!=s)
						{
							if (A[i][j] == -1)
							{
								n++;
							}

							if (A[i][j] == 1)
							{
								nwins++;
								n++;					
							}
						}

					}

					xWP[i] = nwins/(double)n;
					opponents++;
				}
				else
				{
					xWP[i] = 0.0;
				}
				
				OWP[s]+=xWP[i];
			}
			OWP[s]/=(double)(opponents);
			
		}
		// end test

		
		for (int i = 0; i < l; i++)
		{
			double temp = 0.0;
			int n = 0;
			for(int j = 0; j < l; j++)
			{
				if (A[i][j] == -1 || A[i][j] == 1)
				{
					temp+=OWP[j];
					n++;
				}
			}

			OOWP[i] = temp/(double)n;
			//cout << OOWP[i] << endl;
		}

		for (int i = 0; i < l; i++)
		{
			RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		}




		out << "Case #" << k+1 << ": " << endl;
		
		for( int i = 0; i < l; i++)
		{
			out << RPI[i] << endl;
		}

		for (int i = 0; i < l; i++)
		{
			delete [] A[i];
		}

		delete [] A;
		A = 0;

		delete [] RPI;
		RPI = 0;
		delete [] WP;
		WP = 0;
		delete [] OWP;
		OWP = 0;
		delete [] OOWP;
		OOWP = 0;
		delete [] xWP;
		xWP = 0;
	}


	return 0;
}