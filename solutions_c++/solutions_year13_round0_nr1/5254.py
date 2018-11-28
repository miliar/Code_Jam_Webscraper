#include <stdio.h>
#include <fstream>

typedef unsigned char Board[4];

void checkBoard(int n, std::fstream &in, FILE *out) {
	Board b = {0, 0, 0, 0};
	bool done = true;
	for(int j = 0; j < 4; j++) {
		char line[100];
		in >> line;

		for(int k = 0; k < 4; k++) {
			switch(line[k]) {
			case 'X':
				b[j] += (1 << (2 * k));
				break;
			case 'O':
				b[j] += (2 << (2 * k));
				break;
			case 'T':
				b[j] += (3 << (2 * k));
				break;
			case '.':
				done = false;
				break;
			default:
				fprintf(stderr, "SERIOUS ERROR\n");
			}
		}
	}
		
	// Horizontal Check
	unsigned char hc = 0xFF; 
	unsigned char dcl = 0x00;
	unsigned char dcr = 0x00;
	for(int j = 0; j < 4; j++) {
		hc = hc & b[j];
		dcl += b[j] & (0x03 << (j * 2));
		dcr += b[j] & (0xc0 >> (j * 2));
		if((b[j] & 0x55) == 0x55) {
			// DONE X won
			fprintf(out, "Case #%d: X won\n", n);
			return;
		} else if((b[j] & 0xAA) == 0xAA) {
			// DONE O won
			fprintf(out, "Case #%d: O won\n", n);
			return;
		}
	}
	if(hc != 0) {
		if((hc & 0x55)) {
			fprintf(out, "Case #%d: X won\n", n);
		} 
		if((hc & 0xAA)) {
			fprintf(out, "Case #%d: O won\n", n);
		}
		return;
	}
	if((dcl & 0x55) == 0x55) {
			fprintf(out, "Case #%d: X won\n", n);
		return;
	} else if((dcl & 0xAA) == 0xAA) {
		fprintf(out, "Case #%d: O won\n", n);
		return;
	}
	if((dcr & 0x55) == 0x55) {
		fprintf(out, "Case #%d: X won\n", n);
		return;
	} else if((dcr & 0xAA) == 0xAA) {
		fprintf(out, "Case #%d: O won\n", n);
		return;
	}

	if(done) {
		fprintf(out, "Case #%d: Draw\n", n);
		return;
	}
	fprintf(out, "Case #%d: Game has not completed\n", n);
}

int main(int argc, char **argv) {
	std::fstream in("input.txt");
	FILE *out = fopen("output.txt", "w");

	int boards;
	in >> boards;

	for(int i = 0; i < boards; i++) {
		checkBoard(i + 1, in, out);
	}

	in.close();
	fclose(out);
}