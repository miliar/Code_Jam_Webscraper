#include <iostream>
#include <iomanip> 
#include <string> 
#include <algorithm> 
#include <vector> 
#include <set> 
#include <map> 
#include <math.h> 
#include <cstdlib>
#include <queue>
using namespace std;

struct steps {
	int button, number; 	
};

steps make_step(int b, int n) {
	steps a;
	a.button = b;
	a.number = n;
	return a;
}

int dabs(int a) {
	if (a < 0) {
		return -a;
	}
	return a;
}

int main(void) {
	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.in","r",stdin);
	freopen("/Users/admin/Desktop/[Contests]/informatics/Cpl/be/a.out","w",stdout);
	int t, n, answer = 0;
	char c;
	int k;
	steps p, orange_need, blue_need;
	queue<steps> orange, blue;

	scanf("%d", &t);
	for(int i = 0; i < t; i++) {

		scanf("%d", &n);
		for(int j = 0; j < n; j++) {
			cin >> c >> k;
			p = make_step(k, j);
			if (c == 'O') {
				orange.push(p);
			} else {
				blue.push(p);
			}
		}
		int orange_now = 1, blue_now = 1;
		
		if (orange.size() > 0) {
			orange_need = orange.front();
			orange.pop();
		} else {
			orange_need.number = 200;	
		}
		if (blue.size() > 0) {
			blue_need = blue.front();
			blue.pop();
		} else {
			blue_need.number = 200;	
		}
		
		while (blue_need.number != 200 || orange_need.number != 200) {
			if (orange_need.number < blue_need.number) {
				answer = answer + dabs(orange_need.button - orange_now) + 1;
				//cout << "Orange :" << answer << endl;
				if (dabs(orange_need.button - orange_now) + 1 >= dabs(blue_need.button - blue_now)) {
					blue_now = blue_need.button;
				} else {
					if (blue_now < blue_need.button) {
						blue_now += dabs(orange_need.button - orange_now) + 1;
					} else {
						blue_now -= dabs(orange_need.button - orange_now) + 1;
					}
				}
				orange_now = orange_need.button;
				if (orange.size() > 0) {
					orange_need = orange.front();
					orange.pop();
				} else {
					orange_need.number = 200;	
				}
			}
			if (orange_need.number > blue_need.number) {
				answer += dabs(blue_need.button - blue_now) + 1;
				//cout << "Blue :" << answer << endl;
				
				if (dabs(blue_need.button - blue_now) + 1 >= dabs(orange_need.button - orange_now)) {
					orange_now = orange_need.button;
				} else {
					if (orange_now < orange_need.button) {
						orange_now += dabs(blue_need.button - blue_now) + 1;
					} else {
						orange_now -= dabs(blue_need.button - blue_now) + 1; 
					}		
				}
				blue_now = blue_need.button;
				if (blue.size() > 0) {
					blue_need = blue.front();
					blue.pop();
				} else {
					blue_need.number = 200;	
				}
			}
		}
		cout <<  "Case #" << i + 1 << ": "<< answer << endl;
		answer = 0;
	}

	return 0;
}