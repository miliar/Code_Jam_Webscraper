#include <iostream>
#include <cstdio>

using namespace std;

int main(void){
	char a[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t;
	cin >> t;
	char c;
	c = getchar();

	for (int i=1;i<=t;i++){
		cout << "Case #" << i << ": ";
		c = getchar();
		while (c != '\n'){
			if (c == ' '){
				cout << c;
			}else{
				cout << a[c-'a'];
			}
			c = getchar();
		}
		if (i != t){
			cout << endl;
		}
	}
	return 0;
}
