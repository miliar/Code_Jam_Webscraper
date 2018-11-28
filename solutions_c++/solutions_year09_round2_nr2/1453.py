#include <iostream>
#include <fstream>

using namespace std;
int Nfra[20];
int Ncou;
int N;

void breakN(int N)
{
	Ncou = 0;
	while (N >= 10)
	{
		Nfra[Ncou++] = N % 10;
		N = N / 10;
	}
	
	Nfra[Ncou] = N;
	
	int temp;
	
	for (int i = 0; i <= Ncou /2; i++)
	{
		temp = Nfra[i];
		Nfra[i] = Nfra[Ncou - i];
		Nfra[Ncou - i] = temp;
	}
	return ;	
}

void getNext(int j)
{
	int temp;
	
	for (int m = j; m <= Ncou; m++)
	{
		for (int n = Ncou; n > m; n--)
		{
			if (Nfra[n] < Nfra[n - 1])
			{
				temp = Nfra[n];
				Nfra[n] = Nfra[n - 1];
				Nfra[n - 1] = temp;
			}	
		}
		
	}	
}

int main()
{
	ifstream in("B-small-attempt1.in");
	ofstream out("B-small-attempt1.out");
	
	int C;
	in >> C;
	
	for (int i = 1; i <= C; i++)
	{
		in >> N;
		
		breakN(N);
		
		
		int j, s;
		for (j = Ncou - 1; j >= 0; j--)
		{
			if (Nfra[j] < Nfra[j + 1])
			{
				break;	
			}		
		}
		
		if (j < 0)
		{
			for (int s = Ncou + 1; s >= 1; s--)
			{
				Nfra[s] = Nfra[s - 1];
			}
			
			Nfra[0] = 0;
			j = 0;
			Ncou++;
		}
		
		for (s = Ncou; s >= 1; s--)
		{
			if (Nfra[s] > Nfra[j])
			{
				break;	
			}
		}
		
		int temp = Nfra[s];
			Nfra[s] = Nfra[j];
			Nfra[j] = temp;
		
			getNext(j + 1);
			
		out << "Case #" << i << ": ";
		for (int p = 0; p <= Ncou; p++)
		{
			out << Nfra[p];
		}
		out << endl;
		
	}
		
	in.close();
	out.close();
	return 0;	
}
