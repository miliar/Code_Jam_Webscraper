#include <stdio.h>
#include <list>

#define SWITCH(cur) (cur) = ((cur)==&aTrains)?&bTrains:&aTrains

using namespace std;

struct Clock
{
	int hour, min;
	struct Clock operator+(const int add) const
	{
		struct Clock newClk(*this);
		newClk.min += add;
		if (newClk.min>59)
		{
			newClk.hour++;
			newClk.min -= 60;
		}
		return(newClk);
	}
	bool operator<(const struct Clock in) const
	{
		if (hour<in.hour)
			return(true);
		else if (hour==in.hour && min<in.min)
			return(true);
		else
			return(false);
	}
	bool operator>=(const struct Clock in) const {return(!(*this < in));}
};

struct Time
{
	struct Clock depart, arrive;
};

bool compArrive(const struct Time t1, const struct Time t2)
{
	return(t1.arrive.operator<(t2.arrive));
}

bool compDepart(const struct Time t1, const struct Time t2)
{
	return(t1.depart<t2.depart);
}

int main(const int argc, const char *const argv[])
{
	FILE *input;
	int cases, i, j, turnaround, na, nb, outa, outb;
	struct Time temp;
	list<struct Time> aTrains, bTrains, *current;
	list<struct Time>::iterator k;
	struct Time min;
	if (argc < 2)
	{
		fprintf(stderr, "enter file name as first argument\n");
		return(1);
	}
	if (!(input = fopen(argv[1], "r")))
	{
		fprintf(stderr, "enter file name as first argument\n");
		return(2);
	}
	fscanf(input, "%d\n", &cases);
	for (i=0; i<cases; i++)
	{
		fscanf(input, "%d\n", &turnaround);
		fscanf(input, "%d %d\n", &na, &nb);
		for (j=0; j<na; j++)
		{
			fscanf(input, "%d:%d %d:%d\n", &temp.depart.hour, &temp.depart.min, &temp.arrive.hour, &temp.arrive.min);
			aTrains.push_back(temp);
		}
		for (j=0; j<nb; j++)
		{
			fscanf(input, "%d:%d %d:%d\n", &temp.depart.hour, &temp.depart.min, &temp.arrive.hour, &temp.arrive.min);
			bTrains.push_back(temp);
		}
		outa = 0;
		outb = 0;

		while (!aTrains.empty() && !bTrains.empty())
		{
			aTrains.sort(compArrive);
			bTrains.sort(compArrive);
			int a = aTrains.size();
			a = bTrains.size();
			struct Time asdf = *(aTrains.begin());
			asdf = *(bTrains.begin());
			if ((aTrains.begin()->arrive)<(bTrains.begin()->arrive))
			{
				outa++;
				min = *(aTrains.begin());
				aTrains.pop_front();
				bTrains.sort(compDepart);
				bTrains.sort(compDepart);
				current = &bTrains;
			}
			else
			{
				outb++;
				min = *(bTrains.begin());
				bTrains.pop_front();
				aTrains.sort(compDepart);
				bTrains.sort(compDepart);
				current = &aTrains;
			}
			while (1)
			{
				for (k=current->begin(); k!=current->end(); k++)
				{
					if (k->depart>=(min.arrive + turnaround))
					{	
						min = *k;
						current->erase(k);
						break;
					}
				}
				if (k==current->end())
					break;
				SWITCH(current);
			}
		}
		outa += aTrains.size();
		outb += bTrains.size();
		
		printf("Case #%d: %d %d\n", i+1, outa, outb);
		aTrains.clear();
		bTrains.clear();
	}
}
