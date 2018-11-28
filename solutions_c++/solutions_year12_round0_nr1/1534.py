#include <stdio.h>
#include <iostream>

using namespace std;

/*
a y		b h		c e		d s		e o		f c		g v		h x		i d
j u		k i		l g		m l		n b		o k		p r		q z		r t
s n		t w		u j		v p		w f		x m		y a		z q
*/

char convertTable[26];
void initTable() {
	convertTable[0] = 'y';
	convertTable[1] = 'h';
	convertTable[2] = 'e';
	convertTable[3] = 's';
	convertTable[4] = 'o';
	convertTable[5] = 'c';
	convertTable[6] = 'v';
	convertTable[7] = 'x';
	convertTable[8] = 'd';
	convertTable[9] = 'u';
	convertTable[10] = 'i';
	convertTable[11] = 'g';
	convertTable[12] = 'l';
	convertTable[13] = 'b';
	convertTable[14] = 'k';
	convertTable[15] = 'r';
	convertTable[16] = 'z';
	convertTable[17] = 't';
	convertTable[18] = 'n';
	convertTable[19] = 'w';
	convertTable[20] = 'j';
	convertTable[21] = 'p';
	convertTable[22] = 'f';
	convertTable[23] = 'm';
	convertTable[24] = 'a';
	convertTable[25] = 'q';
}

void run(char * buffer) {
	int i=0;
	while(buffer[i] != '\0') {
		if((int) buffer[i] > 32)
			buffer[i] = (char) (convertTable[(int) buffer[i]-'a']);
		i++;
	}
}

int main() {
	int n;
	char buffer[128];
	
	initTable();
	
	scanf("%d\n", &n);
	for(int i=0; i<n; i++) {
		cin.getline (buffer, 128);
		run(buffer);
		cout << "Case #" << i+1 << ": " << buffer << endl;
	}
	return 0;
}