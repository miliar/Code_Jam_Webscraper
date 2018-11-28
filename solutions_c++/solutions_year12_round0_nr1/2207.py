#include <iostream>
#include <string>
#include <sstream>

using namespace std;
int main () {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	string s, q;
	scanf("%d\n", &t);
	char letters[26]; 
	s = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq";	
	q = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz"; 
	
	for(int i = 0; i < s.size(); ++i)
	{
		letters[s[i]-'a'] = q[i];
	}
	for (int i = 0; i < t; ++i)
	{
		char st[1000];
		gets(st);
		printf("Case #%d: ", i+1);
		int l = strlen(st);
		for (int j = 0; j < l; ++j)
			printf("%c", ((st[j] == ' ') ? ' ' : letters[st[j] - 'a']));
		printf("\n");
		
	}
	return 0;
}
