#include <stdio.h>

struct TIMETABLE
{
	int start;
	int end;
	int isok;
};

void inputtimetable(FILE *fp, TIMETABLE *tt, int num)
{
	int cj;
	int hour, min;
	for(cj = 0; cj < num; cj++)
	{
		fscanf(fp, "%d:%d", &hour, &min);
		tt[cj].start = hour * 60 + min;
		fscanf(fp, "%d:%d", &hour, &min);
		tt[cj].end = hour * 60 + min;
		tt[cj].isok = 0;
	}
	return ;
}

void sorttimetable(TIMETABLE *tt, int num)
{
	int ci, cj;
	TIMETABLE temp;
	for(ci = 0; ci < num - 1; ci++)
	{
		for(cj = 0; cj < num - 1 - ci; cj++)
		{
			if(tt[cj].start > tt[cj + 1].start)
			{
				temp = tt[cj];
				tt[cj] = tt[cj + 1];
				tt[cj + 1] = temp;
			}
		}
	}
}

int trytrain(TIMETABLE *ta, TIMETABLE *tb, int na, int nb, int t)
{
	int count = 0;
	int starttime = 0;
	int endwhile = 0;
	int startta = 0, starttb = 0;
	int state = 0;
	while(!endwhile)
	{
		switch(state)
		{
		case 0:
			while(startta < na)
			{
				if(ta[startta].isok != 1 && starttime <= ta[startta].start)
					break;
				startta++;
			}
			if(startta < na)
			{
				starttime = ta[startta].end + t;
				count++;
				startta++;
				state = 1;
			}
			else
				endwhile = 1;
			break;
		case 1:
			while(starttb < nb)
			{
				if(tb[starttb].isok != 1 && starttime <= tb[starttb].start)
					break;
				starttb++;
			}
			if(starttb < nb)
			{
				starttime = tb[starttb].end + t;
				count++;
				starttb++;
				state = 0;
			}
			else
				endwhile = 1;
		}
	}
	return count;
}

int settrain(TIMETABLE *ta, TIMETABLE *tb, int na, int nb, int t)
{
	int count = 0;
	int starttime = 0;
	int endwhile = 0;
	int startta = 0, starttb = 0;
	int state = 0;
	while(!endwhile)
	{
		switch(state)
		{
		case 0:
			while(startta < na)
			{
				if(ta[startta].isok != 1 && starttime <= ta[startta].start)
					break;
				startta++;
			}
			if(startta < na)
			{
				starttime = ta[startta].end + t;
				ta[startta].isok = 1;
				count++;
				startta++;
				state = 1;
			}
			else
				endwhile = 1;
			break;
		case 1:
			while(starttb < nb)
			{
				if(tb[starttb].isok != 1 && starttime <= tb[starttb].start)
					break;
				starttb++;
			}
			if(starttb < nb)
			{
				starttime = tb[starttb].end + t;
				tb[starttb].isok = 1;
				count++;
				starttb++;
				state = 0;
			}
			else
				endwhile = 1;
		}
	}
	return count;
}

int isEnd(TIMETABLE *ta, TIMETABLE *tb, int na, int nb)
{
	int ci;
	int ret = 1;
	for(ci = 0; ci < na; ci++)
	{
		if(ta[ci].isok == 0)
		{
			ret = 0;
			break;
		}
	}
	for(ci = 0; ci < nb && ret == 1; ci++)
	{
		if(tb[ci].isok == 0)
		{
			ret = 0;
			break;
		}
	}
	return ret;
}

int main()
{
	int n;
	int ci, cj;
	FILE *fpin, *fpout;
	int t;
	int na, nb;
	int tryab, tryba;
	int numa = 0, numb = 0;
	int endwhile;

	TIMETABLE tta[100], ttb[100];
	fpin = fopen("B-small-attempt0.in", "r");
	fpout = fopen("B-small-attempt0.out", "w");

	fscanf(fpin, "%d", &n);
	for(ci = 0; ci < n; ci++)
	{
		numa = 0;
		numb = 0;
		fscanf(fpin, "%d", &t);
		fscanf(fpin, "%d%d", &na, &nb);
		inputtimetable(fpin, tta, na);
		inputtimetable(fpin, ttb, nb);
		sorttimetable(tta, na);
		sorttimetable(ttb, nb);
		do
		{
			tryab = trytrain(tta, ttb, na, nb, t);
			tryba = trytrain(ttb, tta, nb, na, t);
			if(tryab >= tryba)
			{
				settrain(tta, ttb, na, nb, t);
				numa++;
			}
			else
			{
				settrain(ttb, tta, nb, na, t);
				numb++;
			}
			endwhile = isEnd(tta, ttb, na, nb);
		} while(!endwhile);
		fprintf(fpout, "Case #%d: %d %d\n", ci + 1, numa, numb);
	}
	
	fclose(fpin);
	fclose(fpout);
	return 0;
}