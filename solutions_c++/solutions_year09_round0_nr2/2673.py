#include<iostream>

#define SMALL_DEFAULT_VALUE -10001

int main()
{
	int cases_ = 0;
	int H = 0;
	int W = 0;

	std::cin >> cases_;

	for(int iii=0; iii<cases_; iii++)
	{
		std::cin >> H;
		std::cin >> W;

		int **back_trace_arr = (int **)malloc(H * W * sizeof(int *));
		for(int i=0; i<H*W; i++)
		{
			back_trace_arr[i] = (int *)malloc(2 * sizeof(int));
			back_trace_arr[i][0] = -1;
			back_trace_arr[i][1] = -1;
		}

		

		int **array = (int **)malloc(H * sizeof(int *));
		for(int a=0; a<H; a++)
			array[a] = (int *)malloc(W * sizeof(int));

		char **ans_array = (char **)malloc(H * sizeof(char *));
		for(int a=0; a<H; a++)
			ans_array[a] = (char *)malloc(W * sizeof(char));

		for(int a=0; a<H; a++)
			for(int b=0; b<W; b++)
			{
				array[a][b] = 10001;
				ans_array[a][b] = '*';
			}

		for(int i=0; i<H; i++)
			for(int j=0; j<W; j++)
				std::cin >> array[i][j];

		char small_alpha = 'a';
		char temp_alpha = '\0';
		int index = 0;
		int smaller = SMALL_DEFAULT_VALUE;
		int i = 0;
		int j = 0;

		for(int ii=0; ii<H; ii++)
			for(int jj=0; jj<W; jj++)
			{
				index = 0;
				i = ii;
				j = jj;
				back_trace_arr[index][0] = i;
				back_trace_arr[index][1] = j;

				index ++;

				while(true)
				{

					//if(ans_array[i][j] != '*')
					//{
						smaller = SMALL_DEFAULT_VALUE;
						if(i+1 < H && array[i][j] > array[i+1][j])
						{
							smaller = array[i+1][j];
							back_trace_arr[index][0] = i+1;
							back_trace_arr[index][1] = j;
						}
						if(j+1 < W && array[i][j] > array[i][j+1])
						{
							if(smaller == SMALL_DEFAULT_VALUE)
								smaller = array[i][j+1];
							if(array[i][j+1] <= smaller)
							{
								smaller = array[i][j+1];
								back_trace_arr[index][0] = i;
								back_trace_arr[index][1] = j+1;
							}
						}
						if(j-1 >= 0 && array[i][j] > array[i][j-1])
						{
							if(smaller == SMALL_DEFAULT_VALUE)
								smaller = array[i][j-1];
							if(array[i][j-1] <= smaller)
							{
								smaller = array[i][j-1];
								back_trace_arr[index][0] = i;
								back_trace_arr[index][1] = j-1;
							}
						}

						if(i-1 >=0 && array[i][j] > array[i-1][j])
						{
							if(smaller == SMALL_DEFAULT_VALUE)
								smaller = array[i-1][j];
							if(array[i-1][j] <= smaller)
							{
								smaller = array[i-1][j];
								back_trace_arr[index][0] = i-1;
								back_trace_arr[index][1] = j;
							}
						}

						if(smaller == SMALL_DEFAULT_VALUE)
						{
							if(ans_array[i][j] == '*')
							{
								temp_alpha = small_alpha;
								small_alpha ++;
							}
							else
							{
								temp_alpha = ans_array[i][j];
							}
	
							ans_array[i][j] = temp_alpha;

							index --;


							while(index >= 0)
							{

								ans_array[back_trace_arr[index][0]][back_trace_arr[index][1]] = temp_alpha;
								back_trace_arr[index][0] = -1;
								back_trace_arr[index][1] = -1;
								index --;
							}

							break;
						}
						else
						{
							i = back_trace_arr[index][0];
							j = back_trace_arr[index][1];
						}

					index ++;
				}
			}

	std::cout << "Case #" << iii+1<<":"<< std::endl;
		for(int i=0; i<H; i++)
		{
			for(int j=0; j<W; j++)
				std::cout << ans_array[i][j] << " " << std::flush;
			std::cout << std::endl;
		}
			
	}

	return 0;
}

