#include <stdio.h>
#include <string>
#include <set>
#include <vector>

std::vector<std::string> list;
std::vector<std::string> v;
int count = 0;

bool find(char* p, int n)
{
	for (std::vector<std::string>::const_iterator it=list.begin(); it!=list.end(); ++it) {
		const std::string& s = *it;
		if (strncmp(p, s.c_str(), n) == 0) {
			return true;
		}
	}
	return false;
}

char buf[10 * 1024 * 1024];
int vsize;
void search(int vi, char* p)
{
	if (vi == vsize) {
		if (find(buf, vi)) {
			count++;
		}
		return;
	}
	if (vi) {
		if (!find(buf, vi)) {
			return;
		}
	}

	std::string& s = v[vi];
	int ssize = s.size();
	for (int i=0; i<ssize; i++) {
		*p = s[i];
		search(vi + 1, p + 1);
	}
}

int main(int argc, char* argv[])
{
	FILE* fp = fopen(argv[1], "r");

	int L, D, N;
	fscanf(fp, "%d %d %d\n", &L, &D, &N);
	
	for (int i=0; i<D; i++) {
		fgets(buf, sizeof(buf), fp);
		int len = strlen(buf);
		std::string s(buf);
		//puts(s.c_str());
		list.push_back(s);
	}

	for (int i=0; i<N; i++) {
		v.clear();
		fgets(buf, sizeof(buf), fp);

		std::string s;
		char* p = buf;
		int b = 0;
		for (; *p!='\n' && *p!='\0'; p++) {
			if (*p=='(') {
				b=1;
			} else if (*p==')') {
				b=0;
				v.push_back(s);
				s.clear();
			} else {
				s += *p;
				if (!b) {
					v.push_back(s);
					s.clear();
				}
			}
		}

		count = 0;
		vsize = v.size();
		search(0, buf);
		printf("Case #%d: %d\n", i+1, count);
	}
}
