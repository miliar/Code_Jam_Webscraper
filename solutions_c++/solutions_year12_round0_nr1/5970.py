#include <iostream>
#include <string>

using namespace std;

//char map[] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
char map[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main() {
	int n = 0;
	cin >> n;
	cin.ignore();
	for (int j = 0; j < n; j++) {
		char in[101], out[101];
		cin.getline(in, 101, '\n');
		for (int i = 0; i < 101; i++) {
			if (in[i] >= 'a' && in[i] <= 'z')
				out[i] = map[in[i] - 'a'];
			else if (in[i] == ' ')
				out[i] = ' ';
			else
				out[i] = in[i];
		}
		cout << "Case #" << j+1 << ": " << out << endl;
	}
}

