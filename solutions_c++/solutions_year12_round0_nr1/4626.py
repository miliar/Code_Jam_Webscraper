#include <stdlib.h>
#include <stdio.h>


char map[256];


void map_update_char(char eng, char google) {
	if (eng == google && map[eng] == eng)
		return;
	if (eng && google) {
		if (map[eng] == eng) {	// ok
			map[eng] = google;
			return;
		};
		if (map[eng] == google)
			return;
	};
	printf("ERROR, cannot update %c with %c\n", eng, google);
};


void map_update(char* eng, char* google) {
	for (; *eng && *google; eng++, google++)
		map_update_char(*eng, *google);
};


bool map_check() {
	printf("checking the map:\n");
	printf("\t");
	for (int i = 'a'; i <= 'z'; i++)
		printf("%c", i);
	printf("\n");
	printf("\t");
	for (int i = 'a'; i <= 'z'; i++)
		printf("%c", map[i]);
	printf("\n");
	
	for (int i = 'a'; i <= 'z'; i++) {
		int j = map[i];
		while (j != i && j != map[j])
			j = map[j];
		if (j != i) {
//			return false;
			printf("NOK: %c and %c\n", i, j);
			
		};
	};
	return true;
};


char translate_to_eng(char google){
	for (int i = 0; i <= 255; i++)
		if (map[i] == google) 
			return i;
	printf("ERROR! : could not translate\n");
};



void init() {
	for (int i = 0; i < sizeof(map); i++)
		map[i] = i;
	map_update("aoz", "yeq");
	map_update(	"our language is impossible to understand",
				"ejp mysljylc kd kxveddknmc re jsicpdrysi");
	map_update(	"there are twenty six factorial possibilities",
				"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	map_update(	"so it is okay if you want to just give up",
				"de kr kd eoya kw aej tysr re ujdr lkgc jv");
	map_update("q", "z");

//	if (!map_check()) printf("ERROR: map is not complete!\n");
};


int solve(int ctry){
	init();
	printf("Case #%d: ", ctry);
	char c;
	while (1) {
		scanf("%c", &c);
		printf("%c", translate_to_eng(c));
		if (c == '\n') break;
	};
};


int main(){

	if (freopen("test.in", "rt", stdin)){
//		freopen("A-large-practice.out", "wt", stdout);
		int tries = 0;
		char c;
		scanf("%d%c", &tries, &c);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-small-attempt0.in", "rt", stdin)){
		freopen("A-small-attempt0.out", "wt", stdout);
		int tries = 0;
		char c;
		scanf("%d%c", &tries, &c);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-large-practice.in", "rt", stdin)){
		freopen("A-large-practice.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};