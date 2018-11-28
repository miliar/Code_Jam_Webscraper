#include <fstream>

using namespace std;

ifstream in("in");
ofstream out("out");

bool test(char c){ return c == '\\' || c == '/' || c == '.'; }

#define FAIL {out << "Impossible\n"; return;}
#define Test(i, j) ((i) >= r || (j) >= c || test(s[i][j]))

void sol(){
	int r, c;
	in >> r >> c;
	char s[55][55];
	in.getline(s[0], 50);
	for(int i = 0; i < r; i++)
		in.getline(s[i], 55);
	for(int i = 0; i < r; i++)
		for(int j = 0; j < c; j++) if(s[i][j] == '#'){
			if(Test(i+1,j) || Test(i, j+1) || Test(i+1, j+1)) FAIL;
			s[i+1][j+1] = s[i][j] = '/';
			s[i+1][j] = s[i][j+1] = '\\';
		}
	for(int i = 0; i < r; i++) out << s[i] << endl;
}

int main(){
	int n;
	in >> n;
	for(int i = 0; i < n; i++)
		out << "Case #" << i + 1 << ":\n",
		sol();//, out << endl;
}
