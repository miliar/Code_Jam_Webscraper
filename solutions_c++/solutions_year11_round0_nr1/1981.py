#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {

    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
	int buttons;
	cin >> buttons;
	int orangePos = 1, bluePos = 1;
	int bTime = 0 , oTime = 0;
	vector<char> bots(buttons,'A');
	vector<int> toPush(buttons,0);

	for (int i = 0; i < buttons; ++i) {
	    cin >> bots[i];
	    cin >> toPush[i];
	}

	for (size_t i = 0; i < bots.size(); ++i) {

	    if (bots[i] == 'O') {
		if (bTime > oTime) {
		    int dist = max(0,max(orangePos - toPush[i], toPush[i] - orangePos)-(bTime - oTime)) + 1;
		    oTime = bTime + dist;
		    orangePos = toPush[i];
		} else {
		    int dist = max(orangePos - toPush[i], toPush[i] - orangePos) + 1;
		    oTime += dist;
		    orangePos = toPush[i];
		}
	    } else {
		if (oTime > bTime) {
		    int dist = max(0,max(bluePos - toPush[i], toPush[i] - bluePos)-(oTime - bTime)) + 1;
		    bTime = oTime + dist;
		    bluePos = toPush[i];
		} else {
		    int dist = max(bluePos - toPush[i], toPush[i] - bluePos) + 1;
		    bluePos = toPush[i];
		    bTime += dist;
		}
	    }
	}


	int res = max(oTime, bTime);
	
	cout << "Case #" << testcase << ": " << res << endl;

    }


}
