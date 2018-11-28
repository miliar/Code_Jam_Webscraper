#include <stdio.h>

class S {
	public:
		int mindex[100];
		int mpos[100];
		int mmany;
		int pos;
		int mfocus;

		S() {
			pos = 1;
			mmany = 0;
			mfocus = 0;
		}

		void putMission(int index, int pos) {
			mindex[mmany] = index;
			mpos[mmany] = pos;
			mmany++;
		}

		bool done() {
			return mfocus == mmany;
		}

		bool op(int nowMpos) {
			if (!done()) {
				if (pos < mpos[mfocus])
					pos++;
				else if (pos > mpos[mfocus])
					pos--;
				else if (mindex[mfocus] == nowMpos) {
					mfocus++;
					return true;
				}
			}
			return false;
		}
};

int main() {
	int ecase, ecount;
	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		S o, b;
		int en;
		char id[100];
		int pos[100];
		scanf("%d", &en);
		for (int i = 0; i < en; i++) {
			scanf(" %c%d", &id[i], &pos[i]);
			if (id[i] == 'O')
				o.putMission(i, pos[i]);
			else
				b.putMission(i, pos[i]);
		}

		int nowMissFocus = 0;
		int time = 0;
		while (!o.done() || !b.done()) {
			bool ore = o.op(nowMissFocus);
			bool bre = b.op(nowMissFocus);
			if (ore || bre)
				nowMissFocus++;
			//printf("%d -- %d -- %d,%d\n", time, nowMissFocus, o.pos, b.pos);
			time++;
		}
		printf("Case #%d: %d\n", ecount, time);
	}

	return 0;
}
