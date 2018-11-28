#include <fstream>
#include <iostream>
#include <list>
#include <string>

#define MAX_N 10
#define MAX_C 1
#define MAX_D 1

using namespace std;

int main()
{
	int T = 0;
	int N = 0;
	int C = 0;
	int D = 0;

	ifstream in("in.in");
	char* elementList = new char[MAX_N];
	char* elementListFinal = new char[MAX_N];

	in >> T;

	for(int k = 0; k < T; k++)
	{
		in >> C;
		
		string* combiners = new string[C];
		
		for(int i = 0; i < MAX_N; i++)
		{
			elementList[i] = '0';
			elementListFinal[i] = '0';
		}

		char element = 0;
		string s = "";

		in.ignore(1, ' ');

		for(int i = 0; i < C; i++)
		{
			getline(in, s, ' ');
			combiners[i] = s;
		}


		in >> D;
		if(D != 0) 
		{
			in.ignore(1, ' ');
		}

		string* opposers = new string[D];

		for(int i = 0; i < D; i++)
		{
			getline(in, s, ' ');
			opposers[i] = s;
		}

		in >> N;

		for(int i = 0; i < N; i++)
		{
			in >> elementList[i];
			if(i == N - 1)
			{
				elementList[i+1] = '\0';
			}
		}

		char last = '0';
		int index = 0;
		char c1 = '0';
		char c2 = '0';
		char c3 = '0';
		char o1 = '0';
		char o2 = '0';
		bool firstOp = false;
		bool secondOp = false;
		if(C > 0)
		{
			c1 = combiners[0].at(0);
			c2 = combiners[0].at(1);
			c3 = combiners[0].at(2);
		}
		if(D > 0)
		{
			o1 = opposers[0].at(0);
			o2 = opposers[0].at(1);
		}
		for(int i = 0; i < N; i++)
		{
			char e = elementList[i];
			bool proceed = false;

			/*if(e == o1)
			{
				firstOp = true;
			}else if(e == o2)
			{
				secondOp = true;
			}*/

			if((e == c1 && last == c2) || (e == c2 && last == c1))
			{
				//kombinera elementen
				elementListFinal[index - 1] = c3;
				last = elementListFinal[index - 1];
				proceed = true;
			}else if(e == o2)
			{
				
				//rensa listan
				for(int n = 0; n < index; n++)
				{
					if(elementListFinal[n] == o1)
					{
						proceed = true;
					}
				}
				if(proceed)
				{
					for(int j = 0; j < index; j++)
					{
						elementListFinal[j] = '0';
					}

					index = 0;
					last = '0';
				}
			}else if(e == o1)
			{
				for(int n = 0; n < index; n++)
				{
					if(elementListFinal[n] == o2)
					{
						proceed = true;
					}
				}
				if(proceed)
				{
					for(int j = 0; j < index; j++)
					{
						elementListFinal[j] = '0';
					}

					index = 0;
					last = '0';
				}
			}
			if(!proceed)
			{
				elementListFinal[index++] = e;
				last = e;
			}
		}

		elementListFinal[index] = '\0';

		cout << "Case #" << k+1 << ": [";
		if(elementListFinal[0] == '\0')
		{
			cout << "]" << endl;
		}

		for(int i = 0; elementListFinal[i] != '\0'; i++)
		{
			if(elementListFinal[i + 1] != '\0')
			{
				cout << elementListFinal[i] << ", ";
			}else
			{
				cout << elementListFinal[i] << "]" << endl;
			}
		}

		delete[] combiners;
		delete[] opposers;
	}
	return 0;
}