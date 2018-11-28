#include <fstream.h>
#include <list>

using namespace std;

int main()
{
	int T, N, button;
	char robot;
	list<int> butOrange;
	list<int> butBlue;
	list<bool> isOrange;
	
	int time, nextO, nextB;
	int posO, posB, tmp;

	fstream fin("robots.txt",ios::in);
	FILE *fout = fopen("robots_out.txt","w");

	fin >> T;
	for (int t=0; t<T; t++)
	{
		fin >> N;
		for (int n = 0; n < N; n++)
		{
			fin >> robot;
			fin >> button;
			
			if (robot == 'O')
			{
			        butOrange.push_back(button);
			        isOrange.push_back(true);
			        continue;
			}
		        butBlue.push_back(button);
		        isOrange.push_back(false);
		}

		time = 0;
		posO = posB = 1;
		nextO = abs(posO - butOrange.front());
		nextB = abs(posB - butBlue.front());
		for (int n = 0; n < N; n++)
		{
			if (isOrange.front())
			{//organge
			        time += nextO + 1;
			        nextB -= nextO + 1;
				if (nextB < 0)
				        nextB = 0;
				posO = butOrange.front();
				butOrange.pop_front();
				nextO = abs(posO - butOrange.front());
			}
			else
			{//blue
			        time += nextB + 1;
			        nextO -= nextB + 1;
				if (nextO < 0)
				        nextO = 0;
				posB = butBlue.front();
				butBlue.pop_front();
				nextB = abs(posB - butBlue.front());
			}
                        isOrange.pop_front();
		}
		fprintf(fout, "Case #%d: %d\n", t + 1, time);
	}

	fin.close();
	fclose(fout);

	return 0;
}
