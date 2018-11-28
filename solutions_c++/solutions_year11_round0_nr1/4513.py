#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


int atoiX(char * &s)
{
	int num = 0;

	// skip leading spaces
	while ((*s == ' ') || (*s == '\t'))
		++s;

	while (isdigit(*s)) {
		num = num*10 + *s - '0';
		++s;
	}

	// skip trailing spaces
	while ((*s == ' ') || (*s == '\t'))
		++s;

	return num;
}

int doTestCase(FILE *fs)
{
	int robot  = 0;     // 0 => Orange, 1 => blue
	int button = 0;     // which buttons needs to be pressed
	int lastPushed = 0; // when was the last button pushed

	int robotPosition[2];
	int robotTime[2];

	char buf[8192];
	if (fgets(buf, sizeof(buf), fs) == NULL) {
		// could be also end of file
	}
	
	// get number of buttons
	char* s = buf;
	int numButtons = atoiX(s);

	robotPosition[0] = 1;
	robotPosition[1] = 1;

	robotTime[0] = 0;
	robotTime[1] = 0;

	while (numButtons--) {
		robot = (*s++ == 'O') ? 0 : 1;

		// now see which button needs to be pressed
		int button = atoiX(s);
		
		int time = abs(button - robotPosition[robot]) +  // how many moves need to be made
					1;								  // then 1 second to press the button

		time += robotTime[robot];
		if (time <= lastPushed) {
			// next push must be after the last push
			time = lastPushed+1;
		}

		lastPushed           = time;
		robotTime[robot]     = time;
		robotPosition[robot] = button;
	}

	return lastPushed;
}
	

int readFile(const char* file)
{
	// open file
	FILE* fs = fopen(file, "r");
	if (fs == NULL) {
		return 1;
	}

	// read number of test cases
	char buf[16];
	if (fgets(buf, sizeof(buf), fs) == NULL) {
		fclose(fs);
		return 1;
	}

	int numTestCases = atoi(buf);

	// now process all the cases
	for (int i = 1; i <= numTestCases; ++i) {
		int time = doTestCase(fs);
		printf("Case #%d: %d\n", i, time);
	}

	fclose(fs);
	return 0;
}

int main(int argc, char *argv[])
{
	int i = 1;
	for (int i=1; i < argc; i++) {
		readFile(argv[i]);
	}

	return 0;
}
