#include<iostream>
#include<fstream>
#include<cmath>
#include<sstream>
#include<limits>
using namespace std;

float average(float a[],int size)
{
	float sum =0.0;
	for(int i=0;i<size;i++)
		sum+=a[i];
	return (sum);
}
void main ()
{
	ifstream input("A-small-attempt3.in",ios::in);
	if(!input)
	{
		cout<< "Error Opening File"<<endl;
		exit(1);
	}
	else
	{
		ofstream output("A-small-attempt3.out",ios::out);

		int cases;
		input >> cases;

		int solvedCases=0;
		while(solvedCases < cases)
		{
			int A,B;
			input >> A>>B;

			float *Pa = new float[A];
			for(int i=0;i<A;i++)
				input >> Pa[i];

			float *ePa = new float[A];
			for(int i=0;i<A;i++)
				ePa[i]= 1-Pa[i];

			float *P = new float[(int)pow(2.0,A)];
			for(int i=0;i<(int)pow(2.0,A);i++)
				P[i]=1;

			
			float *a = new float[(int)pow(2.0,A)];	
			float *b = new float[(int)pow(2.0,A)];
			float *c = new float[(int)pow(2.0,A)];
			float *d = new float[(int)pow(2.0,A)];


			for(int i=0;i<(int)pow(2.0,A);i++)
			{
				int k=i;
				int ak=0;
				int bk=0;
				int ck=0;
				for( int j=0;j<A;j++)
				{
					if((k%2) == 0)
					{
						P[i]*=Pa[A-j-1];
						if(A-1 == 0 || A-2 == 0)
							ck=1;
					}
					else
					{
						P[i]*=ePa[A-j-1];
						ak=1;
						if(j != 0)
							bk=1;
						if((j != 0) || (j != 1))
							ck=1;
					}
					k=k/2;
				}
				if(ak==1)
					a[i]=2*B + 2 -A;
				else
					a[i]= B-A+1;

				if(bk==1)
					b[i] = 2*B+4-A;
				else
					b[i] = B-A+3;

				if(ck==0)
					c[i] = 2*B+6-A;
				else
					c[i] = B-A+5;

				d[i] = B+2;
			}


			float *result = new float[(int)pow(2.0,A)];
			float *result1 = new float[(int)pow(2.0,A)];
			float *result2 = new float[(int)pow(2.0,A)];
			float *result3 = new float[(int)pow(2.0,A)];
			
			for(int j=0;j<(int)pow(2.0,A);j++)
			{
				result[j] = P[j]*a[j];
				result1[j] = P[j]*b[j];
				result2[j] = P[j]*c[j];
				result3[j] = P[j]*d[j];
			}

		
			float min = average(result,(int)pow(2.0,A));
			float min1 = average(result1,(int)pow(2.0,A));
			if(min >min1)
				min = min1;
			min1 = average(result2,(int)pow(2.0,A));
			if(min >min1)
				min = min1;
			min1 = average(result3,(int)pow(2.0,A));
			if(min >min1)
				min = min1;

			output.setf(ios::fixed,ios::floatfield);
			output.precision(6);
			output<<"Case #" <<solvedCases+1<<": "<<min<<endl;
			/*
			std::stringstream ss;
			ss.precision(std::numeric_limits<long float>::digits10);//override the default
			ss << min;
     
			
			output << "Case #" <<solvedCases+1<<": "<<min;
			bool dot=false;
			int nZeros=0;

			string str = ss.str();
			cout << str <<endl;
			for (int i=0;i<str.length();i++)
			{
				if(i==6)
					break;
				if(str[i] == '.')
					dot = true;
				if(dot)
					nZeros++;
			}
			if(!dot)
				output <<'.';
			for(int i =0 ;i<6-nZeros;i++)
				output<<'0';
			output<<endl;*/
			solvedCases++;
		}		
		output.close();
	}
	input.close();
}
