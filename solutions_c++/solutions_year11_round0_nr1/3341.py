/*
 * Olaf "Ritave" Tomalka
 * GCJ 2011
 */
#include <iostream>
#include <vector>
#include <cmath>

void DoTest()
{
	int n;
	std::cin >> n;
	std::vector<std::pair<char, int> > Order;
	std::vector<int> Orange,Blue;
	Order.reserve(100); Orange.reserve(100); Blue.reserve(100);
	for (int i=0;i<n;i++)
	{
		char Bot;
		int Numb;
		std::cin >> Bot >> Numb;
		if (Bot=='O')
			Orange.push_back(Numb);
		else
			Blue.push_back(Numb);
		
		Order.push_back(std::make_pair<char, int>(Bot,Numb));
	}

	int OrangeButt=0,BlueButt=0;
	int TotalTime=0,BlueAt=1,OrangeAt=1,BlueTime=0,OrangeTime=0;
	for (int i=0;i<n;i++)
	{
		if (OrangeButt<Orange.size())
		{
			OrangeTime+=std::abs(OrangeAt-Orange[OrangeButt]);
			OrangeAt=Orange[OrangeButt];
		}
		if (BlueButt<Blue.size())
		{
			BlueTime+=std::abs(BlueAt-Blue[BlueButt]);
			BlueAt=Blue[BlueButt];
		}
		if (Order[i].first=='O')
		{
			OrangeTime++;
			// Wait for it
			if (BlueTime<OrangeTime)
				BlueTime=OrangeTime;
			TotalTime=OrangeTime;
			OrangeButt++;
		} else
		{
			BlueTime++;
			if (OrangeTime<BlueTime)
				OrangeTime=BlueTime;
			TotalTime=BlueTime;
			BlueButt++;
		}
	}

	std::cout << TotalTime << std::endl;
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	int t;
	std::cin >> t;
	for (int i=0;i<t;i++)
	{
		std::cout << "Case #" << i+1 << ": ";
		DoTest();
	}
}
