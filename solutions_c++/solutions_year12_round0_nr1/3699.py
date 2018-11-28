#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

//const char G[] =
//	"y qee"
//	"ejp mysljylc kd kxveddknmc re jsicpdrysi"
//	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
//	"de kr kd eoya kw aej tysr re ujdr lkgc jv";

//const char S[] =
//	"a zoo"
//	"our language is impossible to understand"
//	"there are twenty six factorial possibilities"
//	"so it is okay if you want to just give up";

//char translation[128];
//bool Gv[128];
//bool Sv[128];

char M[] = "yhesocvxduiglbkrztnwjpfmaq";

void my_t(char & c){
	if(isalpha(c))
		c=M[c-'a'];
}

int main(){
//	for(size_t i=0; i<sizeof(G)-1; ++i){
//		char g = G[i];
//		char s = S[i];
//		translation[g] = s;
//		Gv[g] = Sv[s] = true;
//	}

//	for(char c='a'; c<='z'; ++c){
//		cout << c << ' ' << translation[c] << ' ' << Gv[c] << ' ' << Sv[c] << '\n';
//	}

//	for(char c='a'; c<='z'; ++c){
//		cout << translation[c];
//	}

//	cout << '\n';

	size_t T;
	cin >> T;

	string hack;
	getline(cin, hack);

	for(size_t Ti=1; Ti<=T; ++Ti){
		string ans;
		getline(cin, ans);
		for_each(ans.begin(), ans.end(), my_t);

		cout << "Case #" <<Ti << ": " << ans << '\n';
	}

}
