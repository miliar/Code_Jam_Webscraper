#include <iostream>
#include <set>
using namespace std;

struct node {
	double weight;
	string feather;
	node * next1;
	node * next2;
	node(double w = 0, string f = "") {
		feather = f;
		weight = w;
		next1 = next2 = 0;
	}
};
struct dt {
	node * root;
	node * build(const string & line) {
		node * tmp = new node();
		int n = 0, pare = 0;
		int st, ed;
		bool fst = true;
		string num, f;
		for (int i = 0; i < line.length(); ++i) {
			if (line[i] == '(') {
				if (n == 1) st = i;
				n ++;
			} else if (line[i] == ')') {
				n --;
				if (n == 1) {
					ed = i;
					//cout << "subtree" << line.substr(st, ed - st + 1) << endl;
					if (fst) {
						tmp->next1 = build(line.substr(st, ed - st + 1));
						fst = false;
					} else
						tmp->next2 = build(line.substr(st, ed - st + 1));
				}
			} else if (n <= 1) {
				if (isalpha(line[i]))
					f += line[i];
				else if (!isspace(line[i]))
					num += line[i];
			}
		}
		//cout << "cur: " << f << " " << num << endl;
		tmp->weight = atof(num.c_str());
		tmp->feather = f;
		return tmp;
	}
	double getProb(const set<string> & st) {
		double ret = 1.;
		node * cur = root;
		while (cur != NULL) {
			ret *= cur->weight;
			if (st.find(cur->feather) != st.end())
				cur = cur->next1;
			else
				cur = cur->next2;
		}
		return ret;
	}
};

int main() {
	int t, n, l;
	char buf[1024];
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		scanf("%d ", &l);
		string dtstr = "";
		dt cdt;
		for (int i = 0; i < l; ++i) {
			gets(buf);
			dtstr += buf;
		}
		cdt.root = cdt.build(dtstr);
		printf("Case #%d:\n", kase + 1);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			int nf = 0;
			scanf("%s%d", buf, &nf);
			string sname(buf);
			set<string> fs;
			for (int j = 0; j < nf; ++j) {
				scanf("%s", buf);
				fs.insert(string(buf));
			}
			printf("%lf\n", cdt.getProb(fs));
		}
	}
	return 0;
}

