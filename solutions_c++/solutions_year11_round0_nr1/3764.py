/*
 * google01.cpp
 *
 *  Created on: 07.05.2011
 *      Author: jet-lee
 */

//#include <math.h>
#include <stdlib.h>
#include <fstream>
#include <stdio.h>
#include <string.h>

int T;

using namespace std;

int main(int argc, char* argv[])
{


	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);


	infile >> T;

	printf("Cases insgesamt = %i \n",T);


	for(int t=0;t<T;t++)
	{

		int my_time = 0;

		int N;
		infile >> N;


		int o_pos = 1;
		int b_pos = 1;

		int o_length = 0;
		int b_length = 0;
		int o_pointer = 0;
		int b_pointer = 0;

		int pointer = 0;
		char sequence[N];
		int o_array[100];
		int b_array[100];

		// Save current sequence
		for(int n=0;n<N;n++)
		{
			char robot;
			infile >> robot;

			if(robot=='O')
			{
				sequence[n] = 'O';
				infile >> o_array[o_length];
				o_length++;

			}
			else if(robot=='B')
			{
				sequence[n] = 'B';
				infile >> b_array[b_length];
				b_length++;
			}
		}

//		printf("Sequenz:");
//		for(int n=0;n<N;n++)
//		{
//			 printf(" %c |",sequence[n]);
//		}
//		printf("\n O-Array : ");
//
//
//		for(int i=0;i<o_length;i++)
//		{
//			printf(" %i |",o_array[i]);
//		}
//
//		printf("\n B-Array : ");
//
//		for(int i=0;i<b_length;i++)
//		{
//			printf(" %i |",b_array[i]);
//		}
//
//		printf("\n");

		bool push = false;
		while((o_pointer<o_length) | (b_pointer<b_length))
		{

			if(o_pointer < o_length)
			{
				//printf("O: Case %i o_pointer = %i o_pos = %i\n",t,o_pointer,o_pos);

				if(abs(o_array[o_pointer]-o_pos)==0)
				{
					if(sequence[pointer]=='O' & !push)
					{
						o_pointer++;
						pointer++;
						push = true;
					}
				}
				else
				{
					if(o_pos<o_array[o_pointer])
					{
						o_pos++;
					}
					else if (o_pos>o_array[o_pointer])
					{
						o_pos--;
					}

				}
			}


			if(b_pointer < b_length)
			{

				//printf("O: Case %i b_pointer = %i b_pos = %i\n",t,b_pointer,b_pos);

				if(abs(b_array[b_pointer]-b_pos)==0 & !push)
				{
					if(sequence[pointer]=='B')
					{
						b_pointer++;
						pointer++;
						push=true;
					}
				}
				else
				{
					if(b_pos<b_array[b_pointer])
					{
						b_pos++;
					}
					else if (b_pos>b_array[b_pointer])
					{
						b_pos--;
					}

				}
			}

			push = false;
			my_time++;

		}

		printf("Case #%i: %i \n",t+1,my_time);
		outfile << "Case #" << t+1 <<": " << my_time <<"\n";

	}


}
