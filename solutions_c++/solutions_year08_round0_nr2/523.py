#include <iostream>
#include <string>
#include <math.h>
#include <string.h>
#include <sstream>

typedef struct _horaire
{
	int d;
	int a;
	bool take;
} horaire;

int main()
{
	int n=0;
	std::cin >> n;
	for (int c=0;c<n;c++)
	{
		int T,NA,NB;
		std::cin >> T;
		std::cin >> NA >> NB;
			/*std::cout << T << "\n";
			std::cout << NA << "\n";
			std::cout << NB << "\n";*/
		horaire A[NA];
		std::string str;
		int h, m;
		for (int i=0;i<NA;i++)
		{
			std::cin >> str;
			str[2]=' ';
			std::istringstream(str) >> h >> m;
			A[i].d=h*60 + m;
			std::cin >> str;
			str[2]=' ';
			std::istringstream(str) >> h >> m;
			A[i].a=h*60 + m;
			A[i].take = false;
			//std::cout << A[i].d << " " << A[i].a << "\n";
		}
		horaire B[NB];
		for (int i=0;i<NB;i++)
		{
			std::cin >> str;
			str[2]=' ';
			std::istringstream(str) >> h >> m;
			B[i].d=h*60 + m;
			std::cin >> str;
			str[2]=' ';
			std::istringstream(str) >> h >> m;
			B[i].a=h*60 + m;
			B[i].take = false;
			//std::cout << B[i].d << " " << B[i].a << "\n";
		}
		
		int outA=0;
		for (int i=0;i<NA;i++)
		{
			int s=-1;
			for (int j=0;j<NB;j++)
			{
				//std::cout << B[j].a + T << " " << A[i].d << "\n";
				if ( (B[j].a + T) <= A[i].d && B[j].take == false)
					if (s!=-1)
					{
						if ( (B[j].a + T) > (B[s].a + T))
							s=j;
					}
					else
						s=j;
			}
			if (s==-1)
				outA++;
			else
				B[s].take = true;
		}
		
		int outB=0;
		for (int i=0;i<NB;i++)
		{
			int s=-1;
			for (int j=0;j<NA;j++)
			{
				//std::cout << A[j].a + T << " " << B[i].d << "\n";
				if ( (A[j].a + T) <= B[i].d && A[j].take == false)
					if (s!=-1)
					{
						if ( (A[j].a + T) > (A[s].a + T))
							s=j;
					}
					else
						s=j;
			}
			if (s==-1)
				outB++;
			else
				A[s].take = true;
		}
		std::cout << "Case #" << c+1 << ": " << outA << " " << outB << "\n";
	}
	return 0;
}

