#include <fstream>
#include <iostream>
using namespace std;

int main(){
	ifstream fin("C:\\Users\\ting\\Documents\\Visual Studio 2008\\Projects\\Google2012\\Debug\\file.in");
	ofstream fout("C:\\Users\\ting\\Documents\\Visual Studio 2008\\Projects\\Google2012\\Debug\\file.out");

	int cases;
	int counter = 1;

	fin >> cases;
	
	while(counter <= cases){
		int dancers;
		int surprises;
		int par;
		int score;

		int answer = 0;

		fin >> dancers;
		fin >> surprises;
		fin >> par;

		for(int i = 0; i < dancers; i++)
		{
			fin >> score;
			if(par > 1)
			{
				if(score >= 3 * par - 2)
					answer++;
				else if((score >= 3 * par - 4) && (score < 3 * par - 2))
				{
					if(surprises > 0)
					{
						surprises--;
						answer++;
					}
				}
			}
			else
			{
				if((par == 1) && (score > 0))
					answer++;
				if(par == 0)
					answer++;
			}
		}

		fout << "Case #" << counter << ": " << answer << endl;
		counter++;
	}

	return 0;
}