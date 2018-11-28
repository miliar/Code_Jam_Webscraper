#include <stdlib.h>
#include "iostream"
#include <conio.h>
#include <stdio.h>

using namespace std;

#define MAX_LIMIT 4

FILE *fp2;
int *button_type;

int get_num(FILE *fp)
{
	char Num[MAX_LIMIT],c;
	int i = 0;
	c = getc(fp);

	while( c != ' ' &&  c != '\n' && c != EOF)
	{
		Num[i] = c;
		i++;
		c = getc(fp);      
	}   

	i = atoi(Num);
	return i;    
}

void handle_case(FILE *fp,int case_no)
{
	char c;
	int no_of_buttons = get_num(fp);

	int *button_pos_b = (int *)malloc(sizeof(int)*no_of_buttons);
	int *button_pos_o = (int *)malloc(sizeof(int)*no_of_buttons);
	int *button_type = (int *)malloc(sizeof(int)*no_of_buttons);

	int ib = 0;int io = 0;
	for(int i1 = 0;i1 < no_of_buttons; i1++)
	{
		c = fgetc(fp);
		if(c == 'B')
		{
			fgetc(fp);
			button_pos_b[ib++] = get_num(fp);
			button_type[i1] = 0;
		}
		else if(c == 'O')
		{
			fgetc(fp);
			button_pos_o[io++] = get_num(fp);
			button_type[i1] = 1;
		}	
	}

	int time = 0;
	int co = 1;int cb = 1;
	int jb = 0;int jo = 0;
	int to = 0;int tb = 0;
	int time_to_complete = 0;

	for(int i2 = 0;i2 < no_of_buttons;i2++)
	{
		if(button_type[i2] == 0)
		{
			time_to_complete = button_pos_b[jb]-cb;
			if(time_to_complete < 0)
				time_to_complete = -time_to_complete;

			cb = button_pos_b[jb++];
			time_to_complete-=tb;
			if(time_to_complete > 0)
				time_to_complete+=1;
			else
				time_to_complete = 1;
			time+=time_to_complete;
			to += time_to_complete;
			tb = 0;
		}
		else
		{
			time_to_complete = button_pos_o[jo]-co;
			if(time_to_complete < 0)
				time_to_complete = -time_to_complete;

			co = button_pos_o[jo++];
			time_to_complete-=to;
			if(time_to_complete > 0)
				time_to_complete+=1;
			else
				time_to_complete = 1;
			time+=time_to_complete;
			tb += time_to_complete;
			to = 0;
		}
	}

	free(button_pos_b);
	free(button_pos_o);
	free(button_type);

	fprintf(fp2,"Case #%d: %d\n",case_no,time);

}

int main() 
{
	FILE *fp1;
	int no_of_cases = 0;

	fp1 = fopen("E:/A-large.in", "r");
	fp2 = fopen("E:/A-large.out","w");

	no_of_cases = get_num(fp1);

	for(int i = 1;i <= no_of_cases;i++)
		handle_case(fp1,i);

	fclose(fp1) ;
	fclose(fp2) ;
	cout << "Answers found";
	getch();
	return 0;
}