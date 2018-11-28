#include <iostream>

int nCase;
int nMaxCases;

int nSwitches;
int nSnaps;

bool bLightOn;

void Initialize()
{
	nCase = 0;
	nMaxCases = -1;
}

bool ReadInput()
{
	bool ret = false;
	if (nCase != nMaxCases)
	{
		nCase++;
		if (nMaxCases < 0)
			std::cin >> nMaxCases;

		std::cin >> nSwitches;
		std::cin >> nSnaps;

		ret = true;
	}
	return ret;
}

void Solve()
{
	bLightOn = false;
	if (nSnaps > 0)
	{
		long modulus = (1 << nSwitches);
		bLightOn = ((nSnaps % modulus) + 1 == modulus);
	}
}

void WriteOutput()
{
	// Write case number
	std::cout << "Case #" << nCase << ": " << (bLightOn ? "ON" : "OFF") << std::endl;
}

int main()
{
	Initialize();
	while (ReadInput())
	{
		Solve();
		WriteOutput();
	}
	return 0;
}