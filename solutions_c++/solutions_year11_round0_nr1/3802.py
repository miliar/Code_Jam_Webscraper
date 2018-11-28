#include<iostream>
#include<vector>
using namespace std;
int main(){
	int T = 0;
	scanf("%d", &T); getchar();
	for (int tt = 0; tt < T; tt++){
		int N = 0;
		scanf("%d", &N); getchar();
		vector<int> steps, robots;
		for (int i = 0; i < N; ++i){
			char ch;
			int s;
			scanf("%c %d", &ch, &s); 
			getchar();
			if (ch == 'O'){
				steps.push_back(s);
				robots.push_back(-1);//-1 for orange robots
			}else{
				steps.push_back(s);
				robots.push_back(1);//1 for blue robots			
			}
		}
		int flag = 0;//flag 
		int posJ = 1; 
		int posB = 1;
		int wait = 0;
		int time = 0;

		if (robots[0] == -1){
			wait = steps[0] - posJ + 1;
			flag = -1;
			posJ = steps[0];
			time += wait;
		}else{
			wait = steps[0] - posB + 1;
			flag = 1;
			posB = steps[0];		
			time += wait;
		}
		int tmp = 0;
		for (int i = 1; i < N; ++i){
			if (flag == -1 && robots[i] == -1){
				tmp = (steps[i] - posJ > 0 ? steps[i] - posJ : -1 * (steps[i] - posJ));
				wait += tmp + 1;
				time += tmp + 1;
				posJ = steps[i];
			} else if(flag == 1 && robots[i] == 1){
				tmp = (steps[i] - posB > 0 ? steps[i] - posB : -1 * (steps[i] - posB));
				wait += tmp + 1;
				time += tmp + 1;
				posB = steps[i];			
			} else if(flag == -1 && robots[i] == 1){
				tmp = (steps[i] - posB > 0 ? steps[i] - posB : -1 * (steps[i] - posB));
				wait = ((tmp - wait > 0) ? (tmp - wait) : 0)  + 1;
				time += wait;
				posB = steps[i];
				flag = 1;
			} else if (flag == 1 && robots[i] == -1){
				tmp = (steps[i] - posJ > 0 ? steps[i] - posJ : -1 * (steps[i] - posJ));
				wait = ((tmp - wait > 0) ? (tmp - wait) : 0)  + 1;
				time += wait;
				posJ = steps[i];
				flag = -1;
			}
		}
		printf("Case #%d: %d\n", tt + 1, time);
	}
	//getchar();getchar();
	return 0;
};