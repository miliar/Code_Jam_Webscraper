#include <stdio.h>
#include <string>
#include <map>
#undef debug
using namespace std;
char* chomp(char* str)
{
	char *s = str;
	while (*s != '\0' && *s != '\n')
		s++;
	*s = '\0';
	return str;
}
int main()
{
	char buff[150];
	bool passed[150];
	int nt, n, ans, rest, id, it=0;
	string s;
	map<string, int> se_id;
	fgets(buff, 150, stdin);
	sscanf(buff, "%d", &nt);
	while (nt-- > 0) {
		fgets(buff, 150, stdin);
		sscanf(buff, "%d", &n);
		se_id.clear();
		while (n-- > 0) {
			fgets(buff, 150, stdin);
			s = chomp(buff);
			se_id[s] = n;
		}
		fgets(buff, 150, stdin);
		sscanf(buff, "%d", &n);
		ans = 0;
		rest = se_id.size();
		for (int i = 0; i < se_id.size(); i++) {
			passed[i] = false;
		}
#ifdef debug
		for (map<string, int>::iterator itr = se_id.begin(); itr != se_id.end(); itr++) {
			printf("dbg: '%s' %d\n", (itr->first).c_str(), itr->second);
		}
#endif
		while (n-- > 0) {
			fgets(buff, 150, stdin);
			s = chomp(buff);
			id = se_id[s];
			if (!passed[id]) {
				passed[id] = true;
				rest--;
			}
			if (rest == 0) {
				ans++;
				rest = se_id.size() - 1;
				for (int i = 0; i < se_id.size(); i++)
					passed[i] = false;
				passed[id] = true;
			}
#ifdef debug
			printf("dbg: id(%d) rest(%d)\n", id, rest);
#endif
		}
		printf("Case #%d: %d\n", ++it, ans);
	}
	return 0;
}
