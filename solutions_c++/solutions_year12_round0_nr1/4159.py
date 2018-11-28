/*
 * Speaking.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: Jason Wu
 */

#include "Speaking.h"

void QR2012::Speaking::solve() {
	char example[4][101];
	char ans[4][101];
	char map[123];

	strcpy(example[0], "ejp mysljylc kd kxveddknmc re jsicpdrysi");
	strcpy(example[1], "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	strcpy(example[2], "de kr kd eoya kw aej tysr re ujdr lkgc jv");
	strcpy(example[3], "y qee");

	strcpy(ans[0], "our language is impossible to understand");
	strcpy(ans[1], "there are twenty six factorial possibilities");
	strcpy(ans[2], "so it is okay if you want to just give up");
	strcpy(ans[3], "a zoo");

	memset(map, 0, sizeof map);
	REP(i, 4) REP(j, 101) {
		int c = example[i][j];
		if (c == '\0') break;
		if (c == ' ') continue;
		if (map[c] == 0)
			map[c] = ans[i][j];
	}

	//z to q and space to space
	map['z'] = 'q';
	map[' '] = ' ';

//	for (int i = 97; i < 123; i++) {
//		printf("%c to %c\n", (char)i, map[i]);
//	}

	int T;
	char G[101];
	char A[101];

	scanf("%d\n", &T);

	for (int c = 1; c <= T; c++) {
		scanf("%[^\n]\n", G);
		memset(A, '\0', sizeof A);
		int j = -1;
		while (G[++j] != '\0')
			A[j] = map[G[j]];

		printf("Case #%d: %s\n", c, A);
	}
}
