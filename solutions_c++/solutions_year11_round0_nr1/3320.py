#include <iostream>
#include "stdio.h"
#define dprintf if(false) printf

using namespace std;

int main() {
	freopen("bottrust.in", "r", stdin);
	freopen("bottrust.out", "w", stdout);
	int nr_cases;
	//cin >> nr_cases;
	//printf("nr_cases: %d\n", nr_cases);
	scanf("%d", &nr_cases);

	for(int i = 0; i<nr_cases; i++) {
		int n;
		//cin >> n;//
		scanf("%d", &n);

		int list[n];
		bool color[n]; //false = orange, true = blue


		int next_blue = -1;
		int next_orange = -1;
		int pos_blue = 1;
		int pos_orange = 1;

		for(int j=0; j<n; j++) {
			//printf("getting data\n");
			int plats;
			char ch;
			//cin >> ch;
			//cin >> plats;
			scanf(" %c %d", &ch, &plats);
			list[j] = plats;
			//printf("plats: %d, color: %c\n", plats, ch);
			if(ch == 'O') {
				color[j] = false;
				if(next_orange == -1)
					next_orange = plats;
			} else {
				color[j] = true;
				if(next_blue == -1)
					next_blue = plats;
			}
		}
		scanf("%c", 0);

		int time = 0;
		int next_task = 0;
		for(int j=0; j<n; j++) {
			dprintf("i for\n");
			//printf("Task %d   next blue: %d, curr blue: %d    next orange: %d, curr orange: %d\n", j, next_blue, pos_blue, next_orange, pos_orange);
			while((  (color[j] == false) && (pos_orange != next_orange)  ) || (  (color[j] == true) && (pos_blue != next_blue)  )) {
				dprintf("Orange: %d  Blue: %d\nNext or: %d   Next bl: %d\n", pos_orange, pos_blue, next_orange, next_blue);
				//printf("i while\n");
				int d = next_orange - pos_orange;
				if(d > 0) {
					pos_orange++;
					dprintf("Orange moves forwards.\n");
				} else if(d < 0) {
					pos_orange--;
					dprintf("Orange moves backwards.\n");
				}

				d = next_blue - pos_blue;
				if(d > 0) {
					pos_blue++;
					dprintf("Blue moves forwards.\n");
				} else if(d < 0) {
					pos_blue--;
					dprintf("Blue moves backwards.\n");
				}
				time++;
				dprintf("Ny tid: %d\n", time);
			}

			dprintf("Orange: %d  Blue: %d\nNext or: %d   Next bl: %d\n", pos_orange, pos_blue, next_orange, next_blue);

			if(color[j] == false) {
				dprintf("Orange presses button.\n");
				for(int k = j+1; k<n; k++) {
					if(color[k] == false) {
						next_orange = list[k];
						break;
					}
				}

				int d = next_blue - pos_blue;
				if(d > 0) {
					pos_blue++;
					dprintf("Blue moves forwards.\n");
				} else if(d < 0) {
					pos_blue--;
					dprintf("Orange moves backwards.\n");
				}
				time++;
				dprintf("Ny tid: %d\n", time);
			} else {
				dprintf("Blue presses button.\n");
				for(int k = j+1; k<n; k++) {
					if(color[k] == true) {
						next_blue = list[k];
						break;
					}
				}

				int d = next_orange - pos_orange;
				if(d > 0) {
					pos_orange++;
					dprintf("Orange moves forwards.\n");
				} else if(d < 0) {
					pos_orange--;
					dprintf("Blue moves backwards.\n");
				}
				time++;
				dprintf("Ny tid: %d\n", time);
			}
		}

		printf("Case #%d: %d\n", (i+1), time);

	}
}
