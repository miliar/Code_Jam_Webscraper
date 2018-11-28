#include <stdio.h>
#include <iostream>

using namespace std;

char s[] = "yhesocvxduiglbkrztnwjpfmaq";

int T;
string st,ans;

int main() {
	scanf("%d",&T);
	getline(cin,st);
	for (int i = 0;i < T;i++) {
		getline(cin,st);
		ans = "";
		for (int j = 0;j < st.length();j++) {
			if (st[j] == ' ') ans = ans + " ";
			else ans = ans + s[ st[j]-'a' ];
		}
		printf("Case #%d: ",i+1);
		cout << ans << endl;
	}
	return 0;
}
