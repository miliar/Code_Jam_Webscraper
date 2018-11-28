#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

int temparr[10][20];



int main()
{

	ifstream fin;
	ofstream fout;

	int count[20];

	string ip;

	string tempstr;


	fin.open ("in.txt", ifstream::in);

	fout.open("output.txt");

	int N;

	fin >> N;

	getline(fin, ip);

	for(int i = 0; i < N; i++)
	{
		ip.resize(0);

		getline(fin, ip);

		tempstr.resize(0);

		tempstr = ip;

		char temp;
		int minvalpos = ip.size()-1;
		int swappos = ip.size()-1;

		for(int k = 0; k < 10; k++)
		{
			count[k] = 0;
		}

		for(int j = ip.size()-1; j > 0; j--)
		{
			if(ip[j-1] < ip[j])
			{
				break;
			}
		}

		if(j == 0)
		{
			int size = ip.size();

			tempstr.resize(size+1);

			tempstr[0] = '0';

			for(int y = 0; y < ip.size(); y++)
			{
				tempstr[y+1] = ip[y];
			}

			tempstr[y+1] = '\0';

			ip = tempstr;

		}
		

		for(j = ip.size()-1; j > 0; j--)
		{
			if(ip[j-1] < ip[j])
			{
				if(j < ip.size()-1)
				{
					temparr[tempstr[j]-'0'][count[tempstr[j]-'0']] = j;
					count[tempstr[j]-'0']++;
					for(int l = 0; l < 10; l++)
					{
						if(count[l] > 0)
						{
							if(tempstr[temparr[l][count[l]-1]] > tempstr[j-1])
							{
								ip[j-1] = tempstr[temparr[l][count[l]-1]];
								count[l]--;
								break;
							}
						}
					}
					temparr[tempstr[j-1]-'0'][count[tempstr[j-1]-'0']] = j-1;
					count[tempstr[j-1]-'0']++;

				}
				else
				{
					ip[j-1] = ip[j];
					ip[j] = tempstr[j-1];
				}
				swappos = j-1;
				break;
			}
			else
			{
				temparr[tempstr[j]-'0'][count[tempstr[j]-'0']] = j;
				count[tempstr[j]-'0']++;
			}
		}

		int m;
		m = swappos+1;

	



		if(m <= ip.size()-1)
		{

				for(int l = 0; l < 10; l++)
				{
					if(count[l] > 0)
					{
						for(int n = 0; n < count[l]; n++)
						{
							ip[m] = tempstr[temparr[l][n]];
							m++;
						}
					}
				}
		}
		else
		{
			
		}



		fout << "Case #" << i+1 << ": " << ip << "\n";
		
		
	}

	return 0;
	

}