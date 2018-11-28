#include <iostream>
using namespace std;

typedef struct Score {
	int point;
	struct Score* next;
} score;

typedef struct TestCase {
	int googlers;
	int surprising;
	int p;
	score* dance;
} testcase;

void freeList(score* list) {
	score* seeker = list;
	while (seeker != 0) {
		score* aux = seeker->next;
		free(seeker);
		seeker = aux;
	}
}

score* readPoints(int size) {
	score* list = (score*) malloc(sizeof(score));
	list->next = 0;
	score* seeker = list;

	cin >> seeker->point;

	int i = 0;

	while (++i < size) {
		score* s = (score*) malloc(sizeof(score));
		s->next = 0;
		seeker->next = s;
		seeker = s;
		cin >> seeker->point;
	}

	return list;
}

int verifyTrue(int min, int surprise, int point) {
    int base = point / 3;

    switch (point % 3) {
        case 0:
        {
            if (base >= min)
                return 1;
            else if (surprise > 0 && base > 0 && base + 1 >= min) {
                return 2;
            }
            break;
        }
        case 1:
        {
            if (base >= min || base + 1 >= min)
                return 1;
            else if (surprise > 0 && base + 1 >= min) {
                return 2;
            }
            break;
        }
        case 2:
        {
            if (base >= min || base + 1 >= min)
                return 1;
            else if (surprise > 0 && base + 2 >= min) {
                return 2;
            }
            break;
        }
    }

    return 0;
}

int analysePoints(testcase t) {
	int min = t.p;
	int surprise = t.surprising;
	int number = 0;

	score* seeker = t.dance;
	while (seeker != 0) {
	    switch(verifyTrue(min, surprise, seeker->point)) {
	        case 1: number++; break;
	        case 2: number++; surprise--; break;
	    }
		seeker = seeker->next;
	}

	return number;
}

int dance(testcase t) {
	cin >> t.googlers;
	cin >> t.surprising;
	cin >> t.p;

	t.dance = readPoints(t.googlers);
	int result = analysePoints(t);

	freeList(t.dance);

	return result;
}

int main () {
	int testCases;
	testcase google;

	cin >> testCases;

	for (int i=0; i < testCases - 1; i++) {
		int result = dance(google);
		cout << "Case #" << i+1 << ": " << result << endl;
	}

	cout << "Case #" << testCases << ": " << dance(google);

	return 0;
}
