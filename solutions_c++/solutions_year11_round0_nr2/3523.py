#include <cstdio>
#include <queue>
#include <set>
#include <map>
using namespace std;

struct base {
	char one, two;
};
struct combiner : public base {
	char combine;

	combiner(char one_, char two_, char combine_) {
		if(one_ > two_) {
			one = two_;
			two = one_;
		} else {
			one = one_;
			two = two_;
		}
		combine = combine_;
	}

	combiner(char one_, char two_) {
		if(one_ > two_) {
			one = two_;
			two = one_;
		} else {
			one = one_;
			two = two_;
		}
	}
};

struct distroyer : public base {
	distroyer(char one_, char two_) {
		if(one_ > two_) {
			one = two_;
			two = one_;
		} else {
			one = one_;
			two = two_;
		}
	}
};

struct base_comparer {
	bool operator() (const base &lhs, const base &rhs) const {
		if(lhs.one == rhs.one)
			return lhs.two < rhs.two;
		else 
			return lhs.one < rhs.one;
	}
};

bool isBaseElement(char c) {
	if(c == 'Q' || c == 'W' || c == 'E' || c == 'R' ||
	   c == 'A' || c == 'S' || c == 'D' || c == 'F')
	   return true;
	return false;
}

int main(void)
{
	int cases;
	
	char buf[2048];

	set<combiner, base_comparer> comb;
	set<distroyer, base_comparer> dist;

	queue<char> input;
	deque<char> string_list;
	map<char, int> base_element;

	FILE *fp = fopen("B-large.in", "r");
	FILE *fp2 = fopen("B-large.out", "w");

	fgets(buf, 2047, fp);
	//fgets(buf, 2047, stdin);
	sscanf(buf, "%d", &cases);
	for(int i=1; i<=cases; ++i) {
		comb.clear();
		dist.clear();
		string_list.clear();
		base_element.clear();

		char *buffer = buf;
		fgets(buffer, 2047, fp);
		//fgets(buf, 2047, stdin);

		int strings;
		sscanf(buffer, "%d", &strings);
		if(buffer[2] == ' ') buffer++;
		buffer += 2;

		// combine
		while(strings--) {
			char one, two, three;
			sscanf(buffer, "%c%c%c", &one, &two, &three);
			comb.insert(combiner(one, two, three));

			buffer += 4;
		}

		sscanf(buffer, "%d", &strings);
		if(buffer[2] == ' ') buffer++;
		buffer += 2;

		// oppose
		while(strings--) {
			char one, two;
			sscanf(buffer, "%c%c", &one, &two);
			dist.insert(distroyer(one, two));

			buffer += 3;
		}

		sscanf(buffer, "%d", &strings);
		while(*buffer != ' ') buffer++;
		
		while(strings--)
			input.push(*(++buffer));

		// main engine
		while(!input.empty()) {
			char invoked = input.front();

			if(!string_list.empty()) {
				char last = string_list.back();
				
				set<combiner, base_comparer>::iterator it1 = comb.find(combiner(last, invoked));
				if(it1 != comb.end()) {
					string_list.pop_back();
					string_list.push_back(it1->combine);
					base_element[last] = base_element[last] - 1;
					if(base_element[last] <= 0)
						base_element.erase(last);
				}
				else {
					bool for_flag = true;
					for(map<char, int>::iterator it = base_element.begin();
						it != base_element.end() && for_flag; ++it)
					{
						set<distroyer, base_comparer>::iterator it2 = dist.find(distroyer(invoked, it->first));
						if(it2 != dist.end())
							for_flag = false;
					}

					if(!for_flag) {
						string_list.clear();
						base_element.clear();
					} else {
						if(isBaseElement(invoked))
							base_element[invoked] = base_element[invoked] + 1;
						string_list.push_back(invoked);
					}
				}				
			} else {
				if(isBaseElement(invoked))
					base_element[invoked] = 1;
				string_list.push_back(invoked);
			}
			input.pop();
		}

		printf("Case #%d: [", i);
		fprintf(fp2, "Case #%d: [", i);
		for(unsigned i = 0; i < string_list.size(); ++i) {
			if(i == 0) {
				printf("%c", string_list[i]);
				fprintf(fp2, "%c", string_list[i]);
			} else {
				printf(", %c", string_list[i]);
				fprintf(fp2, ", %c", string_list[i]);
			}
		}
		printf("]\n");
		fprintf(fp2, "]\n");
	}

	fclose(fp);
	fclose(fp2);
	return 0;
}