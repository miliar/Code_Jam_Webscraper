#include <fstream>
#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
  ifstream inp("A-large.in", ifstream::in);
  ofstream outp("outputlarge.txt", ofstream::out);
  int N, T, button, *buttonseq;
  char robot, *robotseq;
  int *o_array, *b_array;
  int o_index, b_index;
	int total_time, o_time, b_time;
  int o_posn, b_posn;

  inp>>T;

  for(int i = 1; i <= T; i++)
  {
    inp>>N;
    o_index = 0;
    b_index = 0;
    robotseq = new char[N];
    buttonseq = new int[N];
    o_array = new int[N];
    b_array = new int[N];

    /* Get test case values */    
    for(int j=0; j<N; j++)
    {
      inp>>robot;
			robotseq[j] = robot;
			inp>>button;
			buttonseq[j] = button;

      if (robot == 'O' || robot == 'o')
      {
        //Orange
				o_array[o_index] = j;
				o_index++;
      }
			else if (robot == 'B' || robot == 'b')
			{
				//Blue
				b_array[b_index] = j;
				b_index++;
			}
			else
			{
				// Error
				cout<<"Error"<<endl;
			}
    }
		o_array[o_index] = -1;
		b_array[b_index] = -1;

    /* Find solution */
		total_time = 0;
		o_time = 0;
		b_time = 0;
		o_index = 0;
		b_index = 0;

		o_posn = 1;
		b_posn = 1;

		for(int j = 0; j < N; j++)
		{
			if (robotseq[j] == 'O' || robotseq[j] == 'o')
			{
				o_time += buttonseq[j]>o_posn?buttonseq[j]-o_posn:o_posn-buttonseq[j];
				o_posn = buttonseq[j];

				if (o_time < b_time)
				{
					o_time = b_time;
				}

				o_time++;
			}
			else if (robotseq[j] == 'B' || robotseq[j] == 'b')
			{
				b_time += buttonseq[j]>b_posn?buttonseq[j]-b_posn:b_posn-buttonseq[j];
				b_posn = buttonseq[j];

				if (b_time < o_time)
				{
					b_time = o_time;
				}
				b_time++;
			}
			else
			{
				cout<<"Error"<<endl;
			}
		}

		total_time = o_time>b_time?o_time:b_time;
		outp<<"Case #"<<i<<": "<<total_time<<endl;
    /* Clean up */
    delete robotseq;
    delete buttonseq;
    delete o_array;
    delete b_array;
  }
	return 0;
}

