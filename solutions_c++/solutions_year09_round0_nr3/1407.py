#include <iostream>
#include <cstring>
#include <cstdlib>

#define f(x,y) for (int x = 0; x < y; ++x)

using namespace std;

int n;

char *mess = "welcome to code jam";

int main() {
	char nstr[100];
	cin.getline(nstr, 100);
	n = atoi(nstr);
	
	f(counter,n) {
		char str[505];
		cin.getline(str, 502);
		
		int ways[20];
		f(i,20) ways[i] = 0;
		ways[0] = 1;
		
		f(i,strlen(str)) for (int j = 18; j >= 0; --j) {
			if (str[i] == mess[j]) ways[j+1] = (ways[j]+ways[j+1])%10000;
		}
		
		cout << "Case #" << (counter+1) << ": ";
		if (ways[19] < 1000) cout << "0";
		if (ways[19] < 100) cout << "0";
		if (ways[19] < 10) cout << "0";
		cout << ways[19] << endl;
	}
}

