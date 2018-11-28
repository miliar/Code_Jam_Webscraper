#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int findNext(vector<int> &vec, int v) {
	int result=-1;
	for (int i=0;i<vec.size();i++)
		if (vec[i]>v) {
			result = vec[i];
			break;
		}
	return result;
}

int main() {
	int T;
	cin >> T;
	for (int z=0;z<T;z++) {

		int N;
		cin >> N;

		vector<int> goalButton;
		vector<char> goalRobot;
		vector<int> oButton,bButton;

		for (int i=0;i<N;i++) {
			int button;
			char robot;
			cin >> robot >> button;
			goalButton.push_back(button);
			goalRobot.push_back(robot);
			if (robot=='O')
				oButton.push_back(i);
			else
				bButton.push_back(i);
		}

		// pointers
		int t=0;
		int oPos = 1;
		int bPos = 1;

		// step by each goal
		for (int i=0;i<N;i++) {		
			int targetButton = goalButton[i];
			int dif1;
			if (goalRobot[i] == 'O')
				dif1 = (targetButton - oPos);
			else
				dif1 = (targetButton - bPos);

			int targetButtonNext;
			if (goalRobot[i] == 'O') {
				int tmp = findNext(bButton,i);
				if (tmp==-1)
					targetButtonNext = -1;
				else
					targetButtonNext = goalButton[tmp];
			} else {
				int tmp = findNext(oButton,i);
				if (tmp==-1)
					targetButtonNext = -1;
				else
					targetButtonNext = goalButton[tmp];
			}

			// 
			if (targetButtonNext==-1) {
				t += abs(dif1)+1;
				if (goalRobot[i] == 'O')
					oPos = targetButton;
				else
					bPos = targetButton;
			} else {
				int dif2;
				if (goalRobot[i] == 'O')
					dif2 = (targetButtonNext - bPos);
				else
					dif2 = (targetButtonNext - oPos);
				

				t += abs(dif1)+1;
				if (goalRobot[i] == 'O') {
					oPos = targetButton;
					if (abs(dif2)<=abs(dif1)+1)
						bPos = targetButtonNext;
					else
						bPos += dif2/abs(dif2)*(abs(dif1)+1); 
				} else {
					bPos = targetButton;
					if (abs(dif2)<=abs(dif1)+1)
						oPos = targetButtonNext;
					else
						oPos += dif2/abs(dif2)*(abs(dif1)+1); 
				}

			}

		}

		cout << "Case #" << z+1 << ": " << t << endl;



	}

}