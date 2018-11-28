#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

int process(int tc);

int main()
{
	int tc;
	scanf("%d\n", &tc);

	for(int i = 0; i < tc; i++)
		process(i + 1);
	return 0;
}

int process(int tc)
{
	int c, d, n;
	map<string, char> rule;
	map<char, char> opp;
	string s;
	string out;
	int in[500];

	memset(in, 0, 500);
	
	cin >> c;
	for(int i = 0; i < c; i++) {
		string buf, buf2;
		cin >> buf;
		buf2 += buf[0];
		buf2 += buf[1];
		rule[buf2] = buf[2];
		buf2 = "";
		buf2 += buf[1];
		buf2 += buf[0];
		rule[buf2] = buf[2];
	}

	cin >> d;
	for(int i = 0; i < d; i++) {
		string buf;
		cin >> buf;
		opp[buf[0]] = buf[1];
		opp[buf[1]] = buf[0];
	}

	cin >> n;
	cin >> s;

	for(int i = 0; i < n; i++) {
		string buf;
		int k = out.length();

		if(k > 0) {
			buf += out[k - 1];
			buf += s[i];
			if(rule.count(buf)) {
				in[out[k - 1]]--;
				out[k - 1] = rule[buf];
				in[out[k - 1]]++;
			}
			else if(in[opp[s[i]]] > 0) {
				out = "";
				memset(in, 0, 500);
			}
			else {
				out += s[i];
				in[s[i]]++;
			}
		}
		else {
			out += s[i];
			in[s[i]]++;
		}
	}

	printf("Case #%d: [", tc);

	for(int i = 0; i < out.length(); i++) {
		if(i != out.length() - 1)
			printf("%c, ", out[i]);
		else
			printf("%c", out[i]);
	}

	printf("]\n");				
}
