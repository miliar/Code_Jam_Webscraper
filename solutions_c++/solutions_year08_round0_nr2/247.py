#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

typedef struct {
	int hh, mm;
	int comein;
} TRAIN;

bool operator < (const TRAIN a, const TRAIN b)
{
	if (a.hh == b.hh) {
		if (a.mm == b.mm)
			return (a.comein > b.comein);
		else
			return (a.mm < b.mm);
	}
	else 
		return (a.hh < b.hh);
}

TRAIN DepTrain(string t)
{
	TRAIN tmp;
	tmp.hh = (t[0]-'0')*10 + t[1]-'0';
	tmp.mm = (t[3]-'0')*10 + t[4]-'0';
	tmp.comein = 0;
	return tmp;
}

TRAIN ArvTrain(string t, int dt)
{
	TRAIN tmp;
	tmp.hh = (t[0]-'0')*10 + t[1]-'0';
	tmp.mm = (t[3]-'0')*10 + t[4]-'0' + dt;
	tmp.hh += tmp.mm/60;
	tmp.mm %= 60;
	tmp.comein = 1;
	return tmp;
}

int main()
{
	int N, T, NA, NB, i, k;
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	cin >> N;
	for (k = 1; k <= N; k ++)
	{
		cin >> T >> NA >> NB;
		vector <TRAIN> TA, TB;
		string str;
		for (i = 0; i < NA; i ++) {
			cin >> str;
			TA.push_back(DepTrain(str));
			cin >> str;
			TB.push_back(ArvTrain(str, T));
		}
		for (i = 0; i < NB; i ++) {
			cin >> str;
			TB.push_back(DepTrain(str));
			cin >> str;
			TA.push_back(ArvTrain(str, T));
		}

		sort(TA.begin(), TA.end());
		sort(TB.begin(), TB.end());

		int MA, MB, SA, SB;
		MA = MB = SA = SB = 0;
		for (i = 0; i < TA.size(); i ++) {
			if (TA[i].comein == 1)
				MA ++;
			else {
				if (MA == 0)
					SA ++;
				else
					MA --;
			}
		}
		for (i = 0; i < TB.size(); i ++) {
			if (TB[i].comein == 1)
				MB ++;
			else {
				if (MB == 0)
					SB ++;
				else
					MB --;
			}
		}

		cout << "Case #" << k << ": " << SA << " " << SB << endl;
	}
	return 0;
}