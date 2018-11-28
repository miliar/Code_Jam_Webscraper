#include <cstdio>
#include <list>
#include <set>
#include <string>
#include <vector>

const int MAX_N = 1005;
int T, N;
char buf[MAX_N];

char convert(char c) {
	switch (c) {
		case 'o': return '0';
		case 'i': return '1';
		case 'e': return '3';
		case 'a': return '4';
		case 's': return '5';
		case 't': return '7';
		case 'b': return '8';
		case 'g': return '9';
		default: return c;
	}
}

std::vector<std::list<std::string> > lists;

void iter(std::string next) {
	bool added = false;
	for (int i = 0; i < lists.size(); ++i) {
		std::list<std::string> &cur_list = lists[i];

		bool in_already = false;
		for (std::list<std::string>::iterator i = cur_list.begin(); i != cur_list.end(); ++i) {
			std::string a = *i;
			i++;
			if (i == cur_list.end()) break;
			std::string b = *i;
			i--;
			if (a[a.size()-1] == next[0] && b[0] == next[next.size()-1]) {
				in_already = true;
				cur_list.insert(++i, next);
				break;
			}
		}
		if (in_already) {
			added = true;
			break;
		}
		added = true;
		if (cur_list.front()[0]==next[next.size()-1]) cur_list.push_front(next);
		else if (cur_list.back()[cur_list.back().size()-1] == next[0]) cur_list.push_back(next);
		else added = false;

		if (added) break;
	}
	if (!added) {
		lists.push_back(std::list<std::string>());
		lists.back().push_front(next);
	}
}


void printLists() {
	printf("START\n");
	for (int i = 0; i < lists.size(); ++i) {
		std::list<std::string> &cur_list = lists[i];
		for (std::list<std::string>::iterator j = cur_list.begin(); j != cur_list.end(); ++j) {
			printf("%s:", j->c_str());
		}
		printf("\n");
	}
	printf("END\n");
}

int main() {
	scanf(" %d ", &T);
	for (int t = 1; t <= T; ++t) {
		scanf(" %d ", &N);
		scanf(" %s ", buf);
		std::string str(buf);
		lists.clear();

		std::set<std::string> digraphs;
		for (int i = 0; i < str.size()-1; ++i) {
			std::string toinsert = str.substr(i, 2);
			digraphs.insert(toinsert);
			std::string leet = toinsert;
			leet[0] = convert(leet[0]);
			toinsert[1] = convert(toinsert[1]);
			digraphs.insert(leet);
			digraphs.insert(toinsert);
			toinsert[0] = convert(toinsert[0]);
			digraphs.insert(toinsert);
		}


		while (!digraphs.empty()) {
			std::string next = *digraphs.begin();
			digraphs.erase(next);
			//printf("Adding %s\n", next.c_str());
			iter(next);
			//printLists();
		}

		int prevsz = -1;
		int counter = 0;
		while (1) {
			std::set<std::string> strs;
			for (int i = 0; i < lists.size(); ++i) {
				std::string str;
				std::list<std::string> &cur_list = lists[i];
				for (std::list<std::string>::iterator j = cur_list.begin(); j != cur_list.end(); ++j) {
					if (str.size() > 0 && str[str.size()-1] == (*j)[0]) str.resize(str.size()-1);
					str += *j;
				}

				strs.insert(str);
			}
			lists.clear();
			for (std::set<std::string>::iterator i = strs.begin(); i != strs.end(); ++i) {
				//printf("Adding %s\n", i->c_str());
				iter(*i);
				//printLists();
			}
			if (prevsz == lists.size()) counter++;
			else counter = 0;
			if (counter == 3) break;
			prevsz = lists.size();
		}
		int total = 0;
		for (int i = 0; i < lists.size(); ++i)
			total += lists[i].begin()->size();
		printf("Case #%d: %d\n", t, total);

	}
}