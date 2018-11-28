#include<iostream>
#include<fstream>
#include<sstream>
#include<string>

using namespace std;

int main()
{
	ifstream in("C-small-attempt0.in");
	ofstream out("Output.out");
	stringstream Num;
	string Number;
	char Temp;
	int T, A[50], B[50], N, Value, PreValue[7];
	in >> T;
	for(int i = 0; i < T; i++)
	{
		in >> A[i];
		in >> B[i];
	}

	for(int i = 0; i < T; i++)
	{
		N = 0;
		if(B[i] < 11 || A[i] == B[i])
		{
			N = 0;
		}
		else
		{
			for(int j = B[i]; j > A[i]; j--)
			{
				Num.str("");
				Num << j;
				Number = Num.str();
				for(int l = 1; l < Number.length(); l++)
				{
					for(int k = 1; k < Number.length(); k++)
					{
						Temp = Number[k];
						Number[k] = Number[k-1];
						Number[k-1] = Temp;
					}
					Value = atoi(Number.c_str());
					PreValue[l-1] = Value;
					for(int m = 0; m < l-1; m++)
					{
						if(PreValue[m] == Value && Value < j && Value >= A[i])
						{
							N--;
							break;
						}
					}
					if(Value < j && Value >= A[i])
						N++;
				}
			}
		}
		
		out << "Case #" << (i+1) << ": ";
		out << N << endl;
	}

	out.close();
	in.close();
	return 0;
}