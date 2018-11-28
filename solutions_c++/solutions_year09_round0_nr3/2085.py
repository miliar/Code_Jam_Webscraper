#include <iostream>
#include <vector>
using namespace std;

int N;
int results = 0;
int limit;

void search(vector<char> &line, char * text, char cursor_text, int cursor_line) {
	char letter = text[cursor_text];
	
	for(int a = cursor_line; a < limit; ++a) {
		if (letter == line[a]) {
			if (cursor_text == 18) 
				results = (results + 1) % 10000;
			else 
				search(line, text, cursor_text+1, a+1);
		}
	}
}

int main() {
	cin >> N;
	getc(stdin); // receiving the \n
	
	char text[] = "welcome to code jam";
	
	for(int a = 1; a <= N; ++a) {
		char ch;
		vector<char> line;
		results = 0;
		
		while ((ch = getc(stdin)) != '\n') {
			line.push_back(ch);
		}
		
		limit = line.size();
				
		search(line, text, 0, 0);

		cout << "Case #" << a << ": ";
		printf("%.4d\n", results);
		
	}
}
