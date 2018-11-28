#include <iostream>
#include <string>
#include <vector>

using namespace std;

static char xlat[256] = { 0 };

static const char str1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
static const char str2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
static const char str3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

static const char xlat1[] = "our language is impossible to understand";
static const char xlat2[] = "there are twenty six factorial possibilities";
static const char xlat3[] = "so it is okay if you want to just give up";

void prepareTranslationTable()
{
	xlat['y'] = 'a';
	xlat['e'] = 'o';
	xlat['q'] = 'z';
	for (int i = 0; i < sizeof str1 - 1; ++i) {
		xlat[str1[i]] = xlat1[i];
	}
	for (int i = 0; i < sizeof str1 - 1; ++i) {
		xlat[str2[i]] = xlat2[i];
	}
	for (int i = 0; i < sizeof str1 - 1; ++i) {
		xlat[str3[i]] = xlat3[i];
	}
	for (int i = 'a'; i <= 'z'; ++i) {
		if (xlat[i] == 0) {
			xlat[i] = 'q';
			break;
		}
	}
}

int main()
{
	prepareTranslationTable();
	int numCases;
	cin >> numCases;
	cin.ignore();
	for (int i = 0; i < numCases; ++i) {
		cout << "Case #" << i + 1 << ": ";
		string line;
		getline(cin, line);
		for (string::iterator it = line.begin(); it != line.end(); ++it) {
			cout << xlat[*it];
		}
		cout << endl;
	}
}
