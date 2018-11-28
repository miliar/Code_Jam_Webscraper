#include <stdio.h>
#include <stdlib.h>
#define OUTFILE "trains.out"
#define MAXTRIPS 100
#define MAXLEN 50

class time {
	int hour, min;
public:
	time() { hour = min = 0; }
	time(int h, int m) {
		hour = h;
		min = m;
	}
	time operator=(time t) {
		this->min = t.min;
		this->hour = t.hour;
		return *this;
	}
	time operator+(int m) {
		time newtime(this->hour, this->min + m);
		if (newtime.min >= 60) {
			newtime.min -= 60;
			newtime.hour ++;
		}
		return newtime;
	}
	bool operator>=(time t) {
		if ((t.hour < this->hour) || ((t.hour == this->hour) && (t.min <= this->min))) return true; 
		else return false;
	}
	int get_hour() { return hour; }
	int get_min() { return min; }
	void set_hour(int h) { hour = h; }
	void set_min(int m) { min = m; }
	void set_time(int h, int m) { set_hour(h); set_min(m); }
};

class trip {
	time depart, arrive;
	char start;
public:
	trip() { start = 0; }
	trip(int h1, int m1, int h2, int m2, char ch) { depart.set_time(h1, m1); arrive.set_time(h2, m2); start = ch;}
	trip(time d, time a, char ch) { depart = d; arrive = a; start = ch; }
	time get_depart() { return depart; }
	time get_arrive() { return arrive; }
	char get_start() { return start; }
	void set_depart(time d) { 
		depart = d; 
//		printf("Departing at %02d:%02d\n", depart.get_hour(), depart.get_min()); 
	}
	void set_arrive(time a) { 
		arrive = a; 
//		printf("Arriving at %02d:%02d\n", arrive.get_hour(), arrive.get_min()); 
	}
	void set_start(char ch) { 
		start = ch; 
//		printf("Starting at station %c\n", start); 
	}
};

int main(void) {
	FILE *fin = NULL, *fout = fopen(OUTFILE, "wt");
	trip trips[MAXTRIPS * 2], temp;
	int turn, cases, index, atrips, btrips, j, i, dh, dm, ah, am, tottrips;
	time depart, arrive;
	char filename[MAXLEN + 1], part[3], check;

	printf("Enter input file name: ");
	scanf("%s", filename);
	fin = fopen(filename, "rt");
	fscanf(fin, "%i\n", &cases);
	for (index = 0; index < cases; index ++) {
		fscanf(fin, "%i\n%i %i\n", &turn, &atrips, &btrips);
		printf("Case #%i: Turn: %i, A-Trips: %i, B-Trips: %i\n", index + 1, turn, atrips, btrips);
//		fscanf(fin, "%i:%i %i:%i\n", &dh, &dm, &ah, &am);
		for (tottrips = 0; tottrips < atrips + btrips; tottrips ++) {
//			fscanf(fin, "%02i:%02i %02i:%02i\n", &dh, &dm, &ah, &am);
			fscanf(fin, "%[^:]:", part);
			dh = atoi(part);
			fscanf(fin, "%[^ ] ", part);
			dm = atoi(part);
			fscanf(fin, "%[^:]:", part);
			ah = atoi(part);
			fscanf(fin, "%[^\n]\n", part);
			am = atoi(part);
			printf("Trip #%i: Departs %02i:%02i from %c and arrives %02i:%02i\n", tottrips + 1, dh, dm, tottrips < atrips ? 'A' : 'B', ah, am);
			depart.set_time(dh, dm);
			arrive.set_time(ah, am);
			trips[tottrips].set_depart(depart);
			trips[tottrips].set_arrive(arrive);
			trips[tottrips].set_start(tottrips<atrips?'A':'B');
			for (i = tottrips - 1; i >= 0; i --) {
				if (!(trips[i + 1].get_depart() >= trips[i].get_depart())) {
					temp.set_depart(trips[i + 1].get_depart());
					temp.set_arrive(trips[i + 1].get_arrive());
					temp.set_start(trips[i + 1].get_start());
					trips[i + 1].set_depart(trips[i].get_depart());
					trips[i + 1].set_arrive(trips[i].get_arrive());
					trips[i + 1].set_start(trips[i].get_start());
					trips[i].set_depart(temp.get_depart());
					trips[i].set_arrive(temp.get_arrive());
					trips[i].set_start(temp.get_start());
				} else break;
			}
		}
		check = 'X';
		for (atrips = btrips = 0; check != 'C'; ) {
			check = 'C';
			depart.set_time(0, 0);
			for (i = 0; i < tottrips; i ++) {
				if (trips[i].get_start() == 'C' || trips[i].get_start() == check || !(trips[i].get_depart() >= depart)) continue;
				if (check == 'C' && trips[i].get_start() == 'A') atrips ++;
				if (check == 'C' && trips[i].get_start() == 'B') btrips ++;
				check = trips[i].get_start();
				trips[i].set_start('C');
				arrive = trips[i].get_arrive() + turn;
				depart.set_time(arrive.get_hour(), arrive.get_min());
			}
		}
		fprintf(fout, "Case #%i: %i %i\n", index + 1, atrips, btrips);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
