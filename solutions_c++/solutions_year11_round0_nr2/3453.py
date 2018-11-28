/*
 * google02a.cpp
 *
 *  Created on: 07.05.2011
 *      Author: jet-lee
 */

#include <stdlib.h>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <vector>

int T;

using namespace std;


int main(int argc, char* argv[])
{


	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);

	infile >> T;
	printf("Case %i \n",T);


	for(int t=0; t<T; t++)
	{
		int C;
		int D;
		int N;

		// read combinded characters
		infile >> C;
		char combine[C][3];

		for(int c=0;c<C;c++)
		{
			infile >> &combine[c][0];
			//printf("Combin: %s \n",combine[c]);
		}

		// read opposed characters
		infile >> D;
		char opposed[D][2];

		for(int d=0;d<D;d++)
		{
			infile >> &opposed[d][0];
			//printf("Opposed: %s \n",opposed[d]);
		}

		// read string
		infile >> N;
		char characters[N];

		infile >> &characters[0];
		//printf("Characters: %s \n",characters);


		/*********************************************/

		vector<char> output;
		output.push_back(characters[0]);

		for(int n=1;n<N;n++)
		{
			bool com = false;
			bool opp = false;

			if(!output.empty())
			{

				for(int c=0;c<C;c++)
				{
					char tmp1[2];
					char tmp2[2];
					tmp1[0] = output[output.size()-1];
					tmp1[1] = characters[n];
					tmp2[0] = characters[n];
					tmp2[1] = output[output.size()-1];

					if(strncmp(tmp1,combine[c],2)==0 || strncmp(tmp2,combine[c],2)==0)
					{
						output.pop_back();
						output.push_back(combine[c][2]);

						com = true;
						break;
					}
				}
			}

			if(!com && !output.empty())
			{
				for(int d=0;d<D;d++)
				{
					int count = 0;
					while(count < output.size())
					{
						char tmp1[2];
						char tmp2[2];
						tmp1[0] = characters[n];
						tmp1[1] = output[count];
						tmp2[0] = output[count];
						tmp2[1] = characters[n];

						if(strncmp(tmp1,opposed[d],2)==0 || strncmp(tmp2,opposed[d],2)==0)
						{
//							int rev_count = output.size();
//							while(rev_count>count)
//							{
//								output.pop_back();
//								rev_count--;
//							}
							output.clear();

							opp = true;
							break;
						}

						count++;
					}
				}
			}

			if(!com && !opp)
			{
				output.push_back(characters[n]);
			}
		}
		/*********************************************/

		printf("Case %i Output = ",t+1);
		for(int i=0;i<output.size();i++)
		{
			printf("%c",output[i]);
		}
		printf("\n");

		outfile << "Case #" << t+1 <<": [";
		for(int v=0;v<output.size();v++)
		{
			outfile << output[v];
			if(v!=output.size()-1)
			{ outfile << ", ";}
		}
		outfile << "] \n";
	}
}
