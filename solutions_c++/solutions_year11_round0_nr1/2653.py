// GJam.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <list>
#include <assert.h>
using namespace std;

	struct button_t
	{
		int value;
		int order;
	};

int main(int argc, char* argv[])
{
	assert(argc > 1);
	FILE * output =  0; 
	if (argc > 2)
	{
		output = freopen(argv[2], "w", stdout);
	}
	FILE * input = fopen(argv[1], "r");


	int count;
	fscanf(input, "%d", &count);

	list<button_t>  blue,  orange;
		
	for (int i = 0; i < count; ++i)
	{
		blue.clear();
		orange.clear();
		char tc[4];
		int pos;
		int length;
		fscanf(input,"\n%d", &length);
		for (int j=0;j<length;++j)
		{
			fscanf(input," %s %d", tc, &pos);
			button_t b = {pos, j};
			if (tc[0] == 'O')
				orange.push_back(b);
			else
				blue.push_back(b);			
			cerr << tc << " " << pos << "  ";
		}
		cerr << endl;
		fscanf(input,"\n");
		int time = 0,
		b_pos = 1, o_pos = 1;
			//cerr << "b_pos : " << b_pos << ", o_pos : " << o_pos << ", time : " << time << endl;
		while(!blue.empty() || !orange.empty())
		{
			//cerr << "b_pos : " << b_pos << ", o_pos : " << o_pos << ", time : " << time << endl;
			if (blue.empty())
			{
				time += abs(o_pos - orange.front().value) + 1;
				o_pos = orange.front().value;
				orange.pop_front();
			}
			else if (orange.empty())
			{
				time += abs(b_pos - blue.front().value) + 1;
				b_pos = blue.front().value;
				blue.pop_front();
			}
			else
			{
				button_t o_but = orange.front();
				button_t b_but = blue.front();
				int o_diff = abs(o_pos - o_but.value);
				int b_diff = abs(b_pos - b_but.value);

				if (o_but.order < b_but.order)
				{
					o_pos = o_but.value;
					if (o_diff < b_diff)
					{
						if (b_pos < b_but.value)
							b_pos += (o_diff+1);
						else
							b_pos -= (o_diff+1);	
					}
					else
					{
						b_pos = b_but.value;
					}
					orange.pop_front();
					time += o_diff + 1;
				}
				else
				{
					b_pos = b_but.value;
					if (b_diff < o_diff)
					{
						if (o_pos < o_but.value)
							o_pos += (b_diff+1);
						else
							o_pos -= (b_diff+1);	
					}
					else
					{
						o_pos = o_but.value;
					}
					blue.pop_front();
					time += b_diff + 1;
				}
			}
		} // end while
		cout << "Case #" << (i+1) << ": " << time << endl;


	}
	

	if (output)
		fclose(output);
	if (input)
		fclose(input);
	return 0;
}

