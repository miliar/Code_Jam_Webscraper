// CodeJam2011.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>


int FindNextButton(char hallway, char hallwayList[1000], int current, int num)
{
	if((current+1) > num)
	{
		return -1;
	}
	for(int i = current+1; i <= num; i++)
	{
		if(hallwayList[i] == hallway)
		{
			return i;
		}
	}
	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int count;
	int num;
	FILE* fin = fopen("c:\\input.txt","r");
	FILE* fout = fopen("c:\\output1.txt","w+");
	fscanf(fin, "%d", &count);
	bool print = false;

	for(int i = 0 ; i < count; i++)
	{
		char hallway = ' ';
		int button = 0;

		char s_pace;
		
		fscanf(fin, "%d", &num);

		if(print)
		{
			fprintf(fout, "****************** Case %d \n", i+1);
		}
		char hallwayList[1000];
		int buttonList[1000];
		int pushList[1000];

		for(int j = 0; j < num; j++)
		{
			fscanf(fin," %c %d", &hallwayList[j+1], &buttonList[j+1]);
			if(print)
			{
				fprintf(fout, "%c%d ", hallwayList[j+1], buttonList[j+1]);
			}
			pushList[j+1] =	 0;
		}

		if(print)
		{
			fprintf(fout, "\n");
		}
		int current = 1;
		int curOrange = 1;
		int curBlue = 1;

		int second;

		for(second = 1; second <= 65535; second++)
		{
			if(print)
			{
				fprintf(fout, "second %d \n", second);
			}

			if(hallwayList[current] == 'O') //ORANGE
			{
				//Manage Orange
				if(buttonList[current] > curOrange)
				{
					curOrange++;
					if(print)
					{
						fprintf(fout, "Orange: Move orange to button %d\n", curOrange);
					}
				}else if(buttonList[current] == curOrange)
				{
					if(print)
					{
						fprintf(fout, "Orange: Push button %d\n", curOrange);
					}
					pushList[current] = 1;
				}else
				{
					curOrange--;
					if(print)
					{
						fprintf(fout, "Orange: Move orange to button %d\n", curOrange);
					}
				}
				//Manage Blue
				int nextBlue = FindNextButton('B', hallwayList, current, num);
				if(nextBlue == -1)
				{
					if(print)
					{
						fprintf(fout, "Blue: Do nothing at button %d \n", curBlue);	
					}
				}else if(curBlue < buttonList[nextBlue])
				{
					curBlue++;
					if(print)
					{
						fprintf(fout, "Blue: Move blue to button %d \n", curBlue);
					}
				}else if(curBlue > buttonList[nextBlue])
				{
					curBlue--;
					if(print)
					{
						fprintf(fout, "Blue: Move blue to button %d \n", curBlue);
					}
				}else
				{
					if(print)
					{
						fprintf(fout, "Blue: Do nothing at button %d \n", curBlue);
					}
				}
				} else// BLUE
				{
					//Manage Blue
					if(buttonList[current] > curBlue)
					{
						curBlue++;
						if(print)
						{
							fprintf(fout, "Blue: Move orange to button %d\n", curBlue);
						}
					}else if(buttonList[current] == curBlue)
					{
						if(print)
						{
							fprintf(fout, "Blue: Push button %d\n", curBlue);
						}
						pushList[current] = 1;
					}else
					{
						curBlue--;
						if(print)
						{
							fprintf(fout, "Blue: Move orange to button %d\n", curBlue);
						}
					}

					//Manage Orange
					int nextOrange = FindNextButton('O', hallwayList, current, num);
					if(nextOrange == -1)
					{
						if(print)
						{
							fprintf(fout, "Orange: Do nothing at button %d \n", curOrange);
						}
					}else if(curOrange < buttonList[nextOrange])
					{
						curOrange++;
						if(print)
						{
							fprintf(fout, "Orange: Move orange to button %d \n", curOrange);
						}
					}else if(curOrange > buttonList[nextOrange])
					{
						curOrange--;
						if(print)
						{
							fprintf(fout, "Orange: Move orange to button %d \n", curOrange);
						}
					}else
					{
						if(print)
						{
							fprintf(fout, "Orange: Do nothing at button %d \n", curOrange);
						}
					}
				}

				if(pushList[current] == 1)
				{
					if(current == num)
					{
						fprintf(fout, "Case #%d: %d\n", i+1, second);
						break;
					}else
					{
						current++;
					}
				}
		}
	}

	fclose(fin);
	fclose(fout);
	return 0;
}

