#include <iostream>

#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>

#define FALSE 0
#define TRUE 1

typedef struct job {
	char robot;
	int button;
	int position;
} job;

using namespace std;

int main (int argc, char * const argv[]) {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int N;
	cin >> N;
	//N: number of test cases
	for (int cur_case=1; cur_case<=N; cur_case++) {
		int k;
		int result = 0;
		queue<job*> O;
		queue<job*> B;
		bool O_finished = FALSE;
		bool B_finished = FALSE;
		cin >> k;
		for (int i=0; i<k; i++) {
			char robot;
			int button;
			cin >> robot >> button;
			job *buf = (job*) malloc(sizeof(job));
			buf->robot = robot;
			buf->button = button;
			buf->position = i+1;
			if (robot == 'O') O.push(buf);
			else B.push(buf);
		}
		if (O.empty()) O_finished = TRUE;
		if (B.empty()) B_finished = TRUE;
		int job_num = 1;
		int o_pos = 1;
		int b_pos = 1;
		
		while ((!O_finished) || (!B_finished)) {
			job* orange;
			job* blue;
			bool just_pushed = FALSE;
			result++;
			if (!O.empty()) {
				orange = O.front();
				if (o_pos < orange->button) o_pos++;
				else if (o_pos > orange->button) o_pos--;
				else {
					if (orange->position == job_num ) {
						job_num++;
						O.pop();
						just_pushed = TRUE;
						free(orange);
					}
				}
			} else O_finished = TRUE;
			
			if (!B.empty()) {
				blue = B.front();
				if (b_pos < blue->button) b_pos++;
				else if (b_pos > blue->button) b_pos--;
				else {
					if (blue->position == job_num && !just_pushed) {
						job_num++;
						B.pop();
						free(blue);
					}
				}
			} else B_finished = TRUE;
		}
		printf("Case #%d: %d\n", cur_case, result-1);
	}
	return 0;
}
