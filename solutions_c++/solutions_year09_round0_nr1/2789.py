#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main()
{
	FILE * file_in = fopen("A-large.in", "r");
	FILE * file_out = fopen("output.txt", "w");

	int L, D, N;
	fscanf(file_in, "%d %d %d\n", &L, &D, &N);
	char exists_words[5000][16];
	for(int count = 0; count < D; count++)
	{
		fscanf(file_in, "%s\n", exists_words[count]);
	}

	char test_word[15*28];

	bool correct[5000];
	bool temp_correct[5000];
		
	char *token = NULL;
	bool left = false;

	for(int count = 0; count < N; count++)
	{
		for(int i = 0; i < D; i++)
			correct[i] = true;
		for(int i = 0; i < D; i++)
			temp_correct[i] = false;  //use foe ( )

		int match_num = 0;
		fscanf(file_in, "%s\n", test_word); 
		
		int comparing = 0;
		for(int token = 0; token < strlen(test_word); token++)
		{
			if(test_word[token]== '(')
				left = true;
			else if(test_word[token] == ')')
			{
				left = false;
				for(int i = 0; i < D; i++)
				{
					if(temp_correct[i] == false)
						correct[i] = false;
				}
				for(int i = 0; i < D; i++)
					temp_correct[i] = false;  //use foe ( )
				comparing++;
			}
			else
			{
				if(left)
				{
					for(int i = 0; i < D; i++)
					{
						if(test_word[token] == exists_words[i][comparing])
							temp_correct[i] = true; //match or
					}
				}
				else
				{
					for(int i = 0; i < D; i++)
					{
						if(test_word[token] != exists_words[i][comparing])
							correct[i] = false; //not match
					}
					comparing++;
				}
			}
		}
		for(int i = 0; i < D; i++)
		{
			if(correct[i])
				match_num++;
		}
		fprintf(file_out, "Case #%d: %d\n", count+1, match_num);
	}

	fclose(file_in);
	fclose(file_out);
}