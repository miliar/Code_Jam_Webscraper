#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>

using namespace std;

bool isok(int note,int threshold,int& surprise)
{
	int res = note % 3;
	int ent = note / 3;

	if(note == 0)
	{
		if(threshold == 0) return true;
		else return false;
	}

	if(threshold <= ent) return true;

	else if (res == 1 && threshold <= ent+1)  return true;
	else if (res == 2 && threshold <= ent+1)  return true;


	if((res == 0) && surprise && (threshold <= ent+1))
	{
		--surprise;
		return true;
	}
	if((res == 2) && surprise && (threshold <= ent +2) )
	{
		--surprise;		
		return true;
	}
	

	return false;
}

int main()
{
	std::ifstream file("B-large.in", std::ifstream::in);
	std::ofstream file2("out.txt", std::ofstream::out);

	int nb;
	file >> nb;

	for(int i = 0; i < nb; ++i)
	{
		int googlers,surprise,threshold;
		int res = 0;

		file >> googlers;
		file >> surprise;
		file >> threshold;

		for(int j = 0; j < googlers; ++j)
		{
			int tmp;

			file >> tmp;
			res += isok(tmp,threshold,surprise);
		}
		file2 << "Case #" << i+1 << ": " << res << endl;
	}
}