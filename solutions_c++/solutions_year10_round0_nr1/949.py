#include <iostream>
#include <fstream>

int min_switch[30];
void init()
{
	min_switch[0] = 1;
	for(int i =0; i < 29;++i)
	{
		min_switch[i+1] = 2* min_switch[i] + 1;
	}
}
int main(int argc, char* argv[])
{
	std::ifstream inf(argv[1]);
	int cases ;
	inf >> cases;
	init();
	for(int i =0; i < cases;++i)
	{
		int idx;
		int switchs;
		inf >> idx >>  switchs ;
		if(((switchs + 1) % (min_switch[idx -1] + 1))==0)
		{
			std::cout << "Case #" << i+1 << ": ON\n";
		}
		else
		{
			std::cout << "Case #" << i+1 << ": OFF\n";
		}
	}
	return 0;
}
