#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin("c:\\input.txt");
    ofstream fout("c:\\output.txt");
	int cases;
	fin>>cases;
	int numn = 1;
	while(cases--)
	{
		int p, q;
		fin>>p>>q;
		vector <int>pris;
		pris.resize(q);
		for(int i = 0; i < q; i++)
		{
			fin>>pris[i];
		}
		sort(pris.begin(),pris.end());
		vector <int>orig;
		orig = pris;
		int min = 0;

		///////////////////////
		do{
			vector <int> rooms;
			rooms.resize(p+2);
			for(int j = 0; j < p+2; j++)
			{
				rooms[j] = 0;
			}
			int now = 0;
			vector <int> thisp;
			thisp = pris;
			rooms[0] = 1;
			rooms[p+1] = 1;
			for(int i = 0; i < q; i++)
			{
				int today = thisp.back();
				thisp.pop_back();
				rooms[today] = 1;
				int j = today-1;
				while(rooms[j] == 0)
				{
					j--;
					now++;
				}
				j = today+1;
				while(rooms[j] == 0)
				{
					j++;
					now++;
				}
			}
			min = now;
			next_permutation(pris.begin(),pris.end());
		}while(false);

		while(pris != orig)
		{
			vector <int> rooms;
			rooms.resize(p+2);
			for(int j = 0; j < p+2; j++)
			{
				rooms[j] = 0;
			}
			int now = 0;
			vector <int> thisp;
			thisp = pris;
			rooms[0] = 1;
			rooms[p+1] = 1;
			for(int i = 0; i < q; i++)
			{
				int today = thisp.back();
				thisp.pop_back();
				rooms[today] = 1;
				int j = today-1;
				while(rooms[j] == 0)
				{
					j--;
					now++;
				}
				j = today+1;
				while(rooms[j] == 0)
				{
					j++;
					now++;
				}
			}
			if(min > now)
				min = now;
			next_permutation(pris.begin(),pris.end());
		}

///////////////////////////////////
		fout<<"Case #"<<numn++<<": "<<min<<endl;

		

	}
	fin.close();
    fout.close();
    return 0;
}