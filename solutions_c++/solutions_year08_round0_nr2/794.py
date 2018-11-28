// t02.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream.h"
#include "string.h"
#include "math.h"

int main(int argc, char* argv[])
{
	int		num_cases = 0;

	FILE	*fp = fopen("B-large.in.txt","rt");
	FILE	*fp2 =fopen("OutputL.txt","wt");

	if (!fp)
	{
		cout<<"Error opening file input1.txt"<<endl;
		return 0;
	}
	fscanf(fp, "%d", &num_cases);

	for(int icase=0;icase<num_cases;icase++)
	{
		int		turnaround_time, na, nb;
		int		i, j;

		int		*tab_h1, *tab_m1, *tba_h1, *tba_m1;
		int		*tab_h2, *tab_m2, *tba_h2, *tba_m2;
		int		*tab_1, *tab_2, *tba_1, *tba_2;
		int		*tab_f, *tba_f;
		bool	*tab_leaved, *tba_leaved;


		fscanf(fp, "%d", &turnaround_time);
		fscanf(fp, "%d", &na);
		fscanf(fp, "%d", &nb);

		tab_h1 = (int*) new int[na];
		tab_m1 = (int*) new int[na];
		tab_h2 = (int*) new int[na];
		tab_m2 = (int*) new int[na];
		tba_h1 = (int*) new int[nb];
		tba_m1 = (int*) new int[nb];
		tba_h2 = (int*) new int[nb];
		tba_m2 = (int*) new int[nb];

		tab_1 = (int*) new int[na];
		tab_2 = (int*) new int[na];
		tba_1 = (int*) new int[nb];
		tba_2 = (int*) new int[nb];

		tab_f = (int*) new int[na];
		tba_f = (int*) new int[nb];

		tab_leaved = (bool*) new bool[na];
		tba_leaved = (bool*) new bool[nb];

		cout<<"Case #"<<icase+1<<": ";
		fprintf(fp2, "Case #%d: ", icase+1);

		for (i=0; i<na; i++)
		{
			fscanf(fp, "%d", &tab_h1[i]);
			fscanf(fp, ":%d", &tab_m1[i]);
			fscanf(fp, "%d", &tab_h2[i]);
			fscanf(fp, ":%d", &tab_m2[i]);

			tab_1[i] = 60*tab_h1[i] + tab_m1[i];
			tab_2[i] = 60*tab_h2[i] + tab_m2[i];

			tab_leaved[i] = false;
			tab_f[i] = -1;
		}

		for (i=0; i<nb; i++)
		{
			fscanf(fp, "%d", &tba_h1[i]);
			fscanf(fp, ":%d", &tba_m1[i]);
			fscanf(fp, "%d", &tba_h2[i]);
			fscanf(fp, ":%d", &tba_m2[i]);

			tba_1[i] = 60*tba_h1[i] + tba_m1[i];
			tba_2[i] = 60*tba_h2[i] + tba_m2[i];

			tba_leaved[i] = false;
			tba_f[i] = -1;
		}

		int	begin_time_ab = 24*60;
		int	begin_time_ba = 24*60;
		int	begin_train_ab = -1;
		int	begin_train_ba = -1;
		int	ready_time;

		for (i=0; i<na; i++)
		{
			if (tab_1[i]<begin_time_ab)
			{
				begin_time_ab = tab_1[i];
				begin_train_ab = i;
			}
		}
		for (i=0; i<nb; i++)
		{
			if (tba_1[i]<begin_time_ba)
			{
				begin_time_ba = tba_1[i];
				begin_train_ba = i;
			}
		}

		int	current_time;
		enum {ab, ba} way_to_go;

		if (begin_time_ab<begin_time_ba)
		{
			current_time = begin_time_ab;
			way_to_go = ab;
		}
		else
		{
			current_time = begin_time_ba;
			way_to_go = ba;
		}

		bool	flag_still_to_go = true;

		while (flag_still_to_go)
		{
			if (way_to_go == ab)
			{
				ready_time = tab_2[begin_train_ab] + turnaround_time;
				tab_leaved[begin_train_ab] = true;
				int	nearest_one = -1;
				for (j=0; j<nb; j++)
				{
					if (tba_1[j]>=ready_time && tba_f[j]<0)
					{
						if (nearest_one == -1)
						{
							nearest_one = j;
						}
						else
						{
							if (tba_1[j] < tba_1[nearest_one]) nearest_one = j;
						}
					}
				}
				tba_f[nearest_one] = begin_train_ab;
			}
			else
			{
				ready_time = tba_2[begin_train_ba] + turnaround_time;
				tba_leaved[begin_train_ba] = true;
				int	nearest_one = -1;
				for (j=0; j<na; j++)
				{
					if (tab_1[j]>=ready_time && tab_f[j]<0)
					{
						if (nearest_one == -1)
						{
							nearest_one = j;
						}
						else
						{
							if (tab_1[j] < tab_1[nearest_one]) nearest_one = j;
						}
					}
				}
				tab_f[nearest_one] = begin_train_ba;
			}



			bool	flag_same_time = false;

			begin_time_ab = 24*60;
			begin_time_ba = 24*60;
			begin_train_ab = -1;
			begin_train_ba = -1;

			flag_still_to_go = false;

			for (i=0; i<na; i++)
			{
				if (tab_leaved[i]==false)
				{
					flag_still_to_go = true;
					if (tab_1[i]<=current_time)
					{
						flag_same_time = true;
						begin_train_ab = i;
						way_to_go = ab;
						break;
					}
					else
					{
						if (tab_1[i]<=begin_time_ab)
						{
							begin_time_ab = tab_1[i];
							begin_train_ab = i;
						}
					}
				}
			}
			for (i=0; i<nb; i++)
			{
				if (tba_leaved[i]==false)
				{
					flag_still_to_go = true;
					if (tba_1[i]<=current_time)
					{
						flag_same_time = true;
						begin_train_ba = i;
						way_to_go = ba;
						break;
					}
					else
					{
						if (tba_1[i]<=begin_time_ba)
						{
							begin_time_ba = tba_1[i];
							begin_train_ba = i;
						}
					}
				}
			}

			if (flag_same_time == true)
			{
			}
			else
			{
				if (begin_time_ab<begin_time_ba)
				{
					current_time = begin_time_ab;
					way_to_go = ab;
				}
				else
				{
					current_time = begin_time_ba;
					way_to_go = ba;
				}
			}
		}

		int	needed_ab, needed_ba;
		needed_ab = 0;
		needed_ba = 0;

		for(i=0; i<na; i++)
		{
			if (tab_f[i]<0) needed_ab++;
		}
		for(i=0; i<nb; i++)
		{
			if (tba_f[i]<0) needed_ba++;
		}

		cout<<needed_ab<<" "<<needed_ba<<endl;
		fprintf(fp2, "%d %d\n", needed_ab, needed_ba);

		delete[]	tab_h1, tab_m1, tab_h2, tab_m2, tba_h1, tba_m1, tba_h2, tba_m2,
					tab_1, tab_2, tba_1, tba_2, tab_f, tba_f, tab_leaved, tba_leaved;
	}
	return 0;
}


