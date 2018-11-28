// B.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

std::ifstream in ("B.in");
std::ofstream out ("B.out");

int N;
int A, B, P;


int mas[1001];
int primes[169] = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997};

void input()
{
	in >> A >> B >> P;
}

int solve()
{
	int result = 0;
	for (int i=A; i<=B; i++)
	{
		mas[i] = i;
	}
	int i=0;
	while (primes[i]<P)
	{
		i++;
	}
	int start = i;
	while (i<169 && primes[i] <= B )
	{
		int s = -1;
		int j = A;
		while (j<=B && (j%primes[i])!=0)
			j++;
		if (j<=B)
			s = j;
		else
			break;
		for (int m = j; m<=B; m++)
		{
			if ((m%primes[i]) == 0)
			{
				//mas[m] = s;
				int y = mas[m];
				for (int x=A; x<=B; x++)
				{
					if (mas[x] == y)
					{
						mas[x] = s;
					}
				}
			}
		}
		i++;
	}
	/*for (i=A; i<=B; i++)
	{
		out << mas[i] << " ";
		
	}
	out << "\n";*/
	std::set<int> S;	
	for ( i=A; i<=B; i++)
	{
		S.insert(mas[i]);
	}
	return S.size();
}

int main()
{
	in >> N;
	for (int k=0; k<N; k++)
	{
		input();
		
		out << "Case #" << k+1 << ": "  << solve() << "\n";
	}

	return 0;
}