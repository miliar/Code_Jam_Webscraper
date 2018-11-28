#include <cstdio>
#include <set>
#include <string>
#include <cstring>
#include <cassert>
using namespace std;

static const char *readline() {
	static char buf[10000];
	fgets(buf, sizeof(buf)-2, stdin);
	return buf;
}

struct node {
	double mult;

	std::string feature;
	node *T, *F;

	node() {
		mult = 0;
		T=F=NULL;
	}
};

static void cleanup(node *n) {
	if(n==NULL) return;
	cleanup(n->T);
	cleanup(n->F);
	delete n;
}

static void skip_white(const char *&Z) {
	while(*Z == ' ' || *Z == '\n' || *Z == '\r' || *Z == '\t')
		Z++;
}
static string read_text(const char *&Z) {
	string res;
	while(*Z != ' ' && *Z != '\n' && *Z != '\r' && *Z != '\t' && *Z != '(' && *Z != ')') {
		res += *Z;
		Z++;
	}
	return res;
}
static node *parse(const char *&Z) {
	node *res = new node;

	skip_white(Z);
	assert(*Z == '('); Z++;
	skip_white(Z);
	sscanf(read_text(Z).c_str(), "%lf", &res->mult);
	//printf("mult=%lf\n", res->mult);
	skip_white(Z);

	/* bez poddrzewa */
	if(*Z == ')') {
		Z++;
		//printf("no feature >>%s<<\n", Z);
		return res;
	}

	res->feature = read_text(Z);
	skip_white(Z);

	//printf("feature %s >>%s<<\n", res->feature.c_str(), Z);

	res->T = parse(Z);
	skip_white(Z);
	res->F = parse(Z);
	skip_white(Z);
	assert(*Z == ')'); Z++;
	return res;
}

static double walk(node *node, const set<string> &features) {
	if(node == NULL)
		return 1.0;
	if(node->feature.empty())
		return node->mult;
	if(features.find(node->feature) != features.end()) {
		return node->mult * walk(node->T, features);
	} else {
		return node->mult * walk(node->F, features);
	}
}

static void solve() {
	string text;
	int L; sscanf(readline(), "%d", &L);
	for(int i=0; i<L; i++)
		text += readline();
	//printf("text: >>%s<<\n", text.c_str());

	node *tree = NULL;
	{
		const char *Z = text.c_str();
		tree = parse(Z);
		skip_white(Z);
		assert(*Z == 0);
	}

	int C; sscanf(readline(), "%d", &C);
	for(int Ci=0; Ci<C; Ci++) {
		set<string> features;

		int n;
		const char *Z = readline();
		skip_white(Z);
		string animal = read_text(Z);
		skip_white(Z);
		sscanf(read_text(Z).c_str(), "%d", &n);
		for(int i=0; i<n; i++) {
			skip_white(Z);
			features.insert( read_text(Z) );
		}
		skip_white(Z);
		assert( *Z == 0 );

		printf("%lf\n", walk(tree, features));
	}

	cleanup(tree);
}


int main() {
	int _Nc; sscanf(readline(), "%d", &_Nc);
	for(int _Ni=1; _Ni<=_Nc; _Ni++) {
		printf("Case #%d:\n", _Ni);
		solve();
	}
	return 0;
}
