#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <boost/foreach.hpp>
#include <boost/algorithm/string.hpp>
#include <stdio.h>

std::string solve() {
	char co[255][255];
	char op[255][255];
	memset(co, 0, sizeof(co));
	memset(op, 0, sizeof(op));
	int c;
	scanf("%d", &c);
	for (int i = 0; i < c; ++i) {
		char buf[4];
		scanf("%s", buf);
		co[buf[0]][buf[1]] = buf[2];
		co[buf[1]][buf[0]] = buf[2];
	}
	int d;
	scanf("%d", &d);
	for (int i = 0; i < d; ++i) {
		char buf[3];
		scanf("%s", buf);
		op[buf[0]][buf[1]] = 1;
		op[buf[1]][buf[0]] = 1;
	}
	std::vector<char> data;
	int n;
	scanf("%d", &n);
	char buf[1024];
	scanf("%s", buf);
	BOOST_FOREACH(char cur, std::string(buf)) {
		while (data.size() > 0 && co[data.back()][cur]) {
			cur = co[data.back()][cur];
			data.pop_back();
		}
		if (cur) {
			for (int i = 0; i < data.size(); ++i)
				if (op[data[i]][cur]) {
					data.clear();
					cur = 0;
					break;
				}
			if (cur)
				data.push_back(cur);
		}

	}
	if (data.empty())
		return "[]";
	std::ostringstream oss;
	std::copy(data.begin(), data.end() - 1, std::ostream_iterator<char>(oss, ", "));
	oss << data.back();
	return "[" + oss.str() + "]";
}

char s[1024];
int main(int argc, char* argv[]) {
    freopen(argv[1], "r", stdin);
    strcat(s, argv[1]);
    strcat(s, ".out");
    freopen(s, "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: %s\n", i+1, solve().c_str());
    }
        
}