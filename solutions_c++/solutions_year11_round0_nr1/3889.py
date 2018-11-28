#include <cstdio>
#include <queue>
using namespace std;

int _abs(const int x) {if(x<0) return -x; return x;}

int main(void)
{
	int cases;
	int steps;
	int time;

	queue<int> blue;
	queue<int> orange;
	queue<char> sequence;

	int position_of_blue;
	int position_of_orange;

	char buf[2048];

	FILE *fp = fopen("A-large.in", "r");
	FILE *fp2 = fopen("A-large.out", "w");

	fgets(buf, 2047, fp);
	sscanf(buf, "%d", &cases);
	for(int i=1; i<=cases; ++i) {
		char *buffer = buf;
		fgets(buffer, 2047, fp);
		sscanf(buffer, "%d", &steps);

		while(steps--) {
			char robot;
			int button;

			while(*buffer != ' ') buffer++;
			sscanf(buffer, "%*c%c %d", &robot, &button);
			buffer += 3;

			if(robot == 'O') {
				orange.push(button);
				sequence.push('O');
			}
			else {
				blue.push(button);
				sequence.push('B');
			}
		}

		time = 0;
		position_of_orange = position_of_blue = 1;

		while(!sequence.empty()){
			if(sequence.front() == 'O') {
				if(orange.front() == position_of_orange) {
					orange.pop();
					if(!blue.empty() && blue.front() != position_of_blue) {
						blue.front() > position_of_blue? position_of_blue++ : position_of_blue--;
					}
					time++;
				}
				else {
					int distance = _abs(orange.front() - position_of_orange);
					position_of_orange = orange.front();
					orange.pop();
					if(!blue.empty() && blue.front() != position_of_blue) {
						if(blue.front() < position_of_blue) {
							position_of_blue -= distance+1;
							if(blue.front() >= position_of_blue)
								position_of_blue = blue.front();
						}
						else {
							position_of_blue += distance+1;
							if(blue.front() <= position_of_blue)
								position_of_blue = blue.front();
						}
					}
					time += distance+1;
				}
			}
			else {
				if(blue.front() == position_of_blue) {
					blue.pop();
					if(!orange.empty() && orange.front() != position_of_orange) {
						orange.front() > position_of_orange? position_of_orange++ : position_of_orange--;
					}
					time++;
				}
				else {
					int distance = _abs(blue.front() - position_of_blue);
					position_of_blue = blue.front();
					blue.pop();
					if(!orange.empty() && orange.front() != position_of_orange) {
						if(orange.front() < position_of_orange) {
							position_of_orange -= distance+1;
							if(orange.front() >= position_of_orange)
								position_of_orange = orange.front();
						}
						else {
							position_of_orange += distance+1;
							if(orange.front() <= position_of_orange)
								position_of_orange = orange.front();
						}
					}
					time += distance+1;
				}
			}
			sequence.pop();
		}

		printf("Case #%d: %d\n", i, time);
		fprintf(fp2, "Case #%d: %d\n", i, time);
	}

	fclose(fp);
	fclose(fp2);
	return 0;
}