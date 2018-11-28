//      main.cpp
//      
//      Copyright 2012 Alessio Barducci <alessio@alessio-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.

#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main(int argc, char** argv)
{
	ifstream in("B-small-attempt0.in");
	ofstream out("output.txt");
	
	int T;
	in >> T;
	
	for (int i = 0; i < T; i++)
	{
		int N;
		in >> N;
		int S;
		in >> S;
		int p;
		in >> p;
		vector<int> total;
		for (int j = 0; j < N; j++)
		{
			int tmp;
			in >> tmp;
			total.push_back(tmp);
		}
		/*for (int j = 0; j < N; j++)
			cout << total.at(j) << " ";
		cout << endl;*/
		
		int* surp = new int[S]();
		for (int j = 0; j < S; j++)
		{
			surp[j] = j;
		}
		
		bool cont = true;
		int best = -1;
		
		if (S == 0)
		{
			int tmpTotal = 0;
			for (int j = 0; j < N; j++)
			{
				if (total.at(j) == 0)
				{
					int point = 0;
					if (point >= p)
						tmpTotal++;
				}
				else
				{
					int point = ceil((float)((float)total.at(j)) / 3.);
					if (point >= p)
						tmpTotal++;
				}
			}
			best = tmpTotal;
		}
		else
		{
			while (cont && S > 0)
			{
				int tmpTotal = 0;
				for (int j = 0; j < N; j++)
				{
					if (total.at(j) == 0)
					{
						int point = 0;
						if (point >= p)
							tmpTotal++;
					}
					else
					{
						bool found = false;
						for (int k = 0; k < S; k++)
							if (surp[k] == j)
							{
								int point = ceil((float)((float)total.at(j) + 2.) / 3.);
								//cout << point << endl;
								if (point >= p)
									tmpTotal++;
								found = true;
								k = S;
							}
						if (!found)
						{
							int point = ceil((float)((float)total.at(j)) / 3.);
							//cout << point << endl;
							if (point >= p)
								tmpTotal++;
						}
					}
				}
				if (tmpTotal > best)
					best = tmpTotal;
					
				surp[S - 1]++;
				if (surp[S - 1] == N)
				{
					bool tmpCont = false;
					for (int j = S - 2; j >= 0; j--)
					{
						if (surp[j] < N - S)
						{
							surp[j]++;
							int ref = surp[j];
							for (int k = j+1; k < S; k++)
								surp[k] = ref + (j - k);
							tmpCont = true;
						}
					}
					if (tmpCont == false)
					{
						cont = false;
					}
				}
			}
		}
		out << "Case #" << i+1 << ": ";
		out << best << endl;
		
		delete[] surp;
	}
	out.close();
	
	
	return 0;
}
