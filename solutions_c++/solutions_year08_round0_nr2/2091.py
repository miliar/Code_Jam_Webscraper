#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdlib.h>

struct timetable
{
	int hh,mm;
};

timetable operator+(timetable x, int y);
timetable operator-(timetable x, timetable y);
int operator<=(timetable x, timetable y);

void main()
{
	clrscr();

	int test_case, turn, NA, NB, no_of_train_A, no_of_train_B,count;
	int flag, list_done_A[100], list_done_B[100], list_var, deduct = 0;
	timetable NA_dept[100], NA_ariv[100], NB_dept[100], NB_ariv[100];
	timetable diff;
	char ch[5];

	ofstream ofile("output.txt");
	ifstream file("time.in");
	file.getline(ch,5,'\n');
	test_case = atoi(ch);
	for(int i=0; i<test_case; i++)
	{
		file.getline(ch,5,'\n');
		turn = atoi(ch);
		file.getline(ch,5,' ');
		NA = atoi(ch);
		file.getline(ch,5,'\n');
		NB = atoi(ch);
		no_of_train_A = NA;
		no_of_train_B = NB;
		for(char j=0; j<NA; j++)
		{
			file.getline(ch,5,':');
			NA_dept[j].hh = atoi(ch);
			file.getline(ch,5,' ');
			NA_dept[j].mm = atoi(ch);
			file.getline(ch,5,':');
			NB_ariv[j].hh = atoi(ch);
			file.getline(ch,5,'\n');
			NB_ariv[j].mm = atoi(ch);
		}
		for(char k=0; k<NB; k++)
		{
			file.getline(ch,5,':');
			NB_dept[k].hh = atoi(ch);
			file.getline(ch,5,' ');
			NB_dept[k].mm = atoi(ch);
			file.getline(ch,5,':');
			NA_ariv[k].hh = atoi(ch);
			file.getline(ch,5,'\n');
			NA_ariv[k].mm = atoi(ch);
		}
		count = 0;
		for(j=0; j<NB; j++)
		{
			diff.hh = 23;
			diff.mm = 59;
			deduct = 0;
			int l;
			for(k=0; k<NA; k++)
			{
				flag = 1;
				for(l=0; l<count; l++)
					if(list_done_A[l] == k)
						flag = 0;
				if(flag)
				{
					if( (NA_ariv[j] + turn) <= NA_dept[k] )
					{
						deduct = 1;
						if( (NA_dept[k] - (NA_ariv[j] + turn)) <= diff )
						{
							diff = NA_dept[k] - (NA_ariv[j] + turn);
							cout<<diff.hh<<":"<<diff.mm<<" ";
							list_var = k;
						}
					}
				}
			}
			if(deduct)
			{
				no_of_train_A--;
				list_done_A[count++] = list_var;
			}
		}

		count = 0;
		for(j=0; j<NA; j++)
		{
			diff.hh = 23;
			diff.mm = 59;
			deduct = 0;
			int l;
			for(k=0; k<NB; k++)
			{
				flag = 1;
				for(l=0; l<count; l++)
					if(list_done_B[l] == k)
						flag = 0;
				if(flag)
				{
					if( (NB_ariv[j] + turn) <= NB_dept[k] )
					{
						deduct = 1;
						if( (NB_dept[k] - (NB_ariv[j] + turn)) <= diff )
						{
							diff = NB_dept[k] - (NB_ariv[j] + turn);
							cout<<diff.hh<<":"<<diff.mm<<" ";
							list_var = k;
						}
					}
				}
			}
			if(deduct)
			{
				no_of_train_B--;
				list_done_B[count++] = list_var;
			}
		}

		ofile<<"Case #"<<i+1<<": "<<no_of_train_A<<" "<<no_of_train_B<<"\n";

	}

	getch();
}

timetable operator+(timetable x, int y)
{
	x.mm += y;
	if(x.mm >= 60)
	{
		x.mm = x.mm - 60;
		x.hh++;
	}
	return x;
}

int operator<=(timetable x, timetable y)
{
	if(x.hh < y.hh)
		return 1;
	else if(x.hh > y.hh)
		return 0;
	else if(x.mm < y.mm)
		return 1;
	else if(x.mm > y.mm)
		return 0;
	else
		return 1;
}

timetable operator-(timetable x, timetable y)
{
	timetable temp;
	if(x.hh > y.hh && x.mm > y.mm)
	{
		temp.hh = x.hh - y.hh;
		temp.mm = x.mm - y.mm;
	}
	else if(x.hh > y.hh && x.mm < y.mm)
	{
		temp.hh = x.hh - y.hh - 1;
		temp.mm = (60 - y.mm) + x.mm;
	}
	else if(x.hh == y.hh && x.mm > y.mm)
	{
		temp.hh = 0;
		temp.mm = x.mm - y.mm;
	}
	else if(x.hh == y.hh && x.mm == y.mm)
	{
		temp.hh = 0;
		temp.mm = 0;
	}
	else
	{	temp.hh = 23;
		temp.mm = 59;
	}

	return temp;
}