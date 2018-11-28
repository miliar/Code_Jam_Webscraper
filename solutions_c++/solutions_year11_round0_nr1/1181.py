#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

enum Robot { Orange, Blue};
struct Button {
	int pos;
	Robot robot;
};

int cal_time(vector<Button>& btnList) {
	int seconds = 0;

	//Robot start, snd;
	int OLastTime = 0, BLastTime = 0;
	int OLastPos = 1, BLastPos = 1; 
	size_t i =0, length = btnList.size();

	int dis;
	int timeLeft;
	while( i < length) {
		if(btnList[i].robot == Orange) {
			dis = abs(btnList[i].pos - OLastPos);
			timeLeft = seconds - OLastTime;
			if(dis - timeLeft > 0) {
				seconds += dis - timeLeft;
			}
			seconds++;
			OLastTime = seconds;
			OLastPos = btnList[i].pos;
		} else  {
			dis = abs(btnList[i].pos - BLastPos);
			timeLeft = seconds - BLastTime;
			if(dis - timeLeft > 0) {
				seconds += dis - timeLeft;
			}
			seconds++;
			BLastTime = seconds;
			BLastPos =  btnList[i].pos;
		}
		i++;
	}

	return seconds;
}

int main(int argc, char* argv[])
{
	FILE* ifile = fopen("A-small-attempt0.in", "r");
	if(ifile == NULL) {
		printf("open file error!");
		return -1;
	}
	FILE* out = fopen("out", "w");

	int recordNo;
	fscanf(ifile, "%d", &recordNo);
	printf("Record: %d\n", recordNo);

	int i = 1;
	int btnCnt; Button btn;
	vector<Button> btnList;
	while(i <= recordNo) {
		btnList.clear();
		fscanf(ifile, "%d", &btnCnt);
		cout<<btnCnt<<endl;
		int j = 1; char ch; int pos;
		while(j <= btnCnt) {
			fscanf(ifile, " %c", &ch);
			fscanf(ifile, "%d", &pos);
			btn.pos = pos;
			if(ch == 'O')
				btn.robot = Orange;
			else
				btn.robot = Blue;
			btnList.push_back(btn);
			j++;
		}

		int seconds = cal_time(btnList);
		fprintf(out, "Case #%d: %d\n", i, seconds);
		i++;
	}

	fclose(ifile);
	fclose(out);

	return 0;
}

