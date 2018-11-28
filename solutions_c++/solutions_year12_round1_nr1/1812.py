#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double min(double *y, int a)
{
	double m = y[0];
	for (int i=1; i<a+2; i++)
	{
		if (y[i] < m)
		{
			m = y[i];
		}
	}

	return m;
}

int inc(bool *m, int a)
{
	// return the leftmost true position
	int i = 0;
	bool p = m[0];
	while (p && i < a)
	{
		m[i] = false;
		i++;
		p = m[i];
	}
	if (i >= a)
	{
		// end of the test
		return a;
	}
	m[i] = true;
	return i;
}

int main()
{
	ifstream fi("input.txt");
	ofstream fo("output.txt");
	
	int t;
	fi>>t;
	for (int i=0; i<t; i++)
	{
		int a, b;
		double *c = new double[a];
		double ac = 1.0f;
		fi>>a>>b;
		for (int j=0; j<a; j++)
		{
			fi>>c[j];
			ac *= c[j];
		}
		
		double *exp = new double[a+2];
		// strategy 3
		exp[a+1] = b + 2;
		
		// strategy 1
		exp[a] = ac * (b-a+1.0) + (1.0-ac) * (b-a+1.0+b+1.0);
		
		// strategy 2
		// iterate over binary rep of the mistake
		// mistake at ith place
		bool *m = new bool[a];
		for (int j=0; j<a; j++)
		{
			m[j] = false;
			exp[j] = 0.0;
		}
		
		int lm = a;
		do {
			double prob = 1.0;
			for (int k=0; k<a; k++)
			{
				prob *= (m[k])? (1.0 - c[k]) : c[k];
			}
			
			for (int k=0; k<a; k++)
			{
				if (a-1-k > lm)
				{
					// backspace too few places
					exp[k] += prob * (2.0*(k+1)+b-a+1.0+b+1.0);
					// cout<<"( "<<prob<<", "<<(2*(k+1)+b-a+1+b+1)<<" )"<<endl;
				}
				else
				{
					// backspace enough
					exp[k] += prob * (2.0*(k+1.0)+b-a+1.0);
					// cout<<"( "<<prob<<", "<<(2*(k+1)+b-a+1)<<" )"<<endl;
				}
				// cout<<"exp["<<k<<"]="<<exp[k];
			}
			
			lm = inc(m, a);
			
			for (int k=0; k<a; k++)
			{
				cout<<m[k]<<", ";
			}
			cout<<endl;
			
			// cout<<"lm = "<<lm;
		} while (a != lm);
		
		// for (int j=0; j<a+2; j++)
		// {
			// cout<<exp[j]<<", ";
		// }
		// cout<<endl;
		
		fo<<"Case #"<<i+1<<fixed<<": "<<setprecision(6)<<min(exp, a)<<endl;
	}
	
	return 0;
}
