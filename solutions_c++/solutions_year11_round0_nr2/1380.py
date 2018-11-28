#include<cstdio>
#include<vector>

using namespace std;

/*
	Q = 1; W = 2; E = 3; R = 4
	A = 5; S = 6; D = 7; F = 8
*/
int baseEl(char c) {
	switch(c) {
		case 'Q': return 1; break;
		case 'W': return 2; break;
		case 'E': return 3; break;
		case 'R': return 4; break;
		case 'A': return 5; break;
		case 'S': return 6; break;
		case 'D': return 7; break;
		case 'F': return 8; break;
		default: return -1;
	}
}

char combine[9][9];	// (i, j) contains the non-base element resultant from the combination of i and j
bool opposed[9][9];	// (i, j) tells us if i and j are opposed elements

int main() {
	int T = 0;
	scanf("%d ", &T);

	for (int caseNum = 1; caseNum <= T; caseNum++) {
		for (int i = 1; i <= 8; i++) {
			for (int j = 1; j <= 8; j++) {
				combine[i][j] = '0';
				opposed[i][j] = false;
			}
		}

		int c = 0;
		scanf("%d ", &c);
		for(int i = 0; i < c; i++) {
			char s[4];
			scanf("%s", s);

			combine[ baseEl(s[0]) ][ baseEl(s[1]) ] = s[2];
			combine[ baseEl(s[1]) ][ baseEl(s[0]) ] = s[2];
		}

		int d = 0;
		scanf("%d ", &d);
		for(int i = 0; i < d; i++) {
			char s[3];
			scanf("%s", s);

			opposed[ baseEl(s[0]) ][ baseEl(s[1]) ] = true;
			opposed[ baseEl(s[1]) ][ baseEl(s[0]) ] = true;
		}

		int n = 0;
		scanf("%d ", &n);

		vector<char> elements;

		for (int i = 0; i < n; i++) {
			char c = '\0';
			scanf("%c", &c);

			if (elements.size() > 0) {
				// Test if the last two elements combine
				int e = baseEl(elements[ elements.size() - 1 ]);

				if (e != -1) {
					if (combine[baseEl(c)][e] != '0') {
						elements.erase( elements.end()-1 );
						elements.push_back( combine[ baseEl(c) ][e] );
					}
					else {
					// Test if there is some opposed element in the list
						for (int j = 0; j < elements.size(); j++) {
							int k = baseEl(elements[j]);
							if (k != -1) {
								if (opposed[ baseEl(c) ][k]) {
									elements.clear();
									break;
								}
							}
						}

						if(elements.size() > 0) elements.push_back(c);
					}
				}
				else {
				// Test if there is some opposed element in the list
					for (int j = 0; j < elements.size(); j++) {
						int k = baseEl(elements[j]);
						if (k != -1) {
							if (opposed[ baseEl(c) ][k]) {
								elements.clear();
								break;
							}
						}
					}

					if(elements.size() > 0) elements.push_back(c);
				}
			}
			else
				elements.push_back(c);
		}

		printf("Case #%d: [", caseNum);

		if (elements.size() > 0) {
			printf("%c", elements[0]);

			for (int i = 1; i < elements.size(); i++)
				printf(", %c", elements[i]);
		}
		printf("]\n");
	}

	return 0;
}
