/*
 * Olaf "Ritave" Tomalka
 * 2010 Google Code Jam
 */
#include <iostream>

const int MAKS=1000;

int array[MAKS];

int main()
{
	int t,n,k,r,cashGot;
	std::cin >> t;
	for (int i=0;i<t;i++)
	{
		std::cin >> r >> k >> n;
		for (int j=0;j<n;j++)
		{
			std::cin >> array[j];
		}
		
		cashGot=0;
		int placeInQueue=0;
		int placeStarting=0;
		int placesLeft;
		bool been;
		for (int j=0;j<r;j++)
		{
			been=false;
			placesLeft=k;
			placeStarting=placeInQueue;
			while ((placeInQueue!=placeStarting || !been) && placesLeft>=array[placeInQueue])
			{
				cashGot+=array[placeInQueue];
				placesLeft-=array[placeInQueue];
				placeInQueue=(placeInQueue+1)%n;
				been=true;
			}
		}
		std::cout << "Case #" << i+1 << ": " << cashGot << '\n';
	}
}
