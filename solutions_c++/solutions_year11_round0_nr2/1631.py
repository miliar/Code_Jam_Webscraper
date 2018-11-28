#include<iostream>
using namespace std;
void run();
int hash(char);

char combine[9][9];
bool clear[9][9];

int main () {
    freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int credits;
	cin >> credits;
	for (int i = 0; i < credits; ++ i) {
		cout <<"Case #"<<i+1<<": ";
		run();
	}
	return 0;
}

int hash(char c) {
	switch(c) {
		case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
		default: return 8;
	}
	return -1;
}

void run() {
	for (int i = 0; i < 9; ++ i) {
	for (int j = 0; j < 9; ++ j){
		clear[i][j] = false;
		combine[i][j] = ' ';
	}
	}
	int com, clr, N;
	cin >> com;
	char a, b, c;
	for (int i = 0; i < com; ++ i) {
		cin >>a >>b >>c;
		combine[hash(a)][hash(b)] = combine[hash(b)][hash(a)] = c;
	}
	cin >> clr;
	for (int i = 0; i < clr; ++ i) {
		cin >> a >> b;
		clear[hash(a)][hash(b)] = clear[hash(b)][hash(a)] = true;
	}
	/*cout << "##################"<< endl;
	for (int i = 0; i < 8; ++ i) {
	for (int j = 0; j < 8; ++ j){
		cout << clear[i][j] << ' ';
	}
	cout << endl;
	}
	cout <<endl;
	for (int i = 0; i < 8; ++ i) {
	for (int j = 0; j < 8; ++ j){
		cout << combine[i][j] << ' ';
	}
	cout << endl;
	}
	cout << "##################"<< endl;*/
	
	cin >> N;
	int top = 0;
	char str[200];
	for (int i = 0; i < N; ++ i) {
		cin >> str[top];
		++ top;
		if (top == 1)
			continue;
		char comb = combine[hash(str[top-1])][hash(str[top-2])];
		if (comb != ' ') {
				//cout << "combine "<<str[top-2] <<' '<<str[top-1] << comb << endl;
			-- top;
			str[top -1] = comb;
			continue;
		}
		for (int j = top - 2; j >=0; --j) {
			if (clear[hash(str[top-1])][hash(str[j])]) {
				//cout << "clear since "<<str[j] <<' '<<str[top-1] <<endl;
				top = 0;
				break;
			}
		}
	}
	if (top == 0) {
		cout <<"[]" << endl;
		return;
	}
	cout << '[';
	for (int i = 0; i < top-1; ++ i) 
		cout <<str[i]<<", ";
	cout << str[top-1] << ']' << endl;	
}
