#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
using namespace std;
char dtree[100*100];
struct Node {
	int leftch;
	int rightch;
	string feature;
	double prob;
};
Node tree[2000];
int tree_id;
int length;
int input_id;
//char animals[150][150][20];
//int  ap_an[150];

void skip_space()
{
	while (dtree[input_id] == ' ')
		++input_id;
}

string get_feat()
{
	skip_space();
	string ret = "";
	while (dtree[input_id] >= 'a' && dtree[input_id] <= 'z') {
		ret += dtree[input_id];
		++input_id;
	}
	return ret;
}

double get_prob()
{
	skip_space();
	char number[20];
	int index = 0;
	while (dtree[input_id] == '.'
			|| isdigit(dtree[input_id])) {
		number[index] = dtree[input_id];
		++input_id;
		++index;
	}
	number[index] = '\0';
	return atof(number);
}

int make_tree() {
	skip_space();
	if (dtree[input_id] == '(') {
		++input_id;
	}
	int cur_id = tree_id++;
	
	tree[cur_id].prob = get_prob();
	
	skip_space();
	if (dtree[input_id] == ')') {
		////cout << "curId: " << cur_id << " root" << endl;
		////cout << "prob: " << tree[cur_id].prob << endl;
		tree[cur_id].feature = "";
		tree[cur_id].leftch = tree[cur_id].rightch = -1;
		++input_id;
		return cur_id;
	}
	tree[cur_id].feature = get_feat();
	tree[cur_id].leftch = make_tree();
	tree[cur_id].rightch = make_tree();
	//cout << "curId: " << cur_id << endl;
	//cout << "prob: " << tree[cur_id].prob << endl;
	//cout << "feature: " << tree[cur_id].feature << endl;
	//cout << "leftch: " << tree[cur_id].leftch << endl;
	//cout << "rightch: " << tree[cur_id].rightch << endl;
	skip_space();
	if (dtree[input_id] == ')') {
		++input_id;
	}
	return cur_id;
}


int main()
{
	freopen("a_small.in", "r", stdin);
	freopen("a_small.out", "w", stdout);
	//ifstream fin("a_small.in");
	//ofstream fout("a_small.out");
	int testcase;
	scanf("%d", &testcase);
	for (int test_case=1; test_case<=testcase; ++test_case) {
		int input_lines;
		memset(tree, 0, sizeof tree);
		dtree[0] = '\0';
		scanf("%d", &input_lines); getchar();
		while (input_lines--) {
			char input[256];
			gets(input);
			strcat(dtree, input);
		}
		tree_id = 0;
		length = strlen(dtree);
		input_id = 0;
		make_tree();
		int i, j, num_ani, num_fea;
		char ani[20], fea[100][20];
		scanf("%d", &num_ani);
		double prob = 1.0;
		printf("Case #%d:\n", test_case);
		for (i=0; i<num_ani; ++i) {
			scanf("%s %d", ani, &num_fea);
			prob = 1.0;
			int tree_point = 0;
			for (j=0; j<num_fea; ++j) {
				scanf("%s", fea[j]);
			}
			while (tree[tree_point].feature != "") {
				prob *= tree[tree_point].prob;
				for (int t=0; t<num_fea; ++t) {
					if (strcmp(tree[tree_point].feature.c_str(), fea[t]) == 0)
						break;
				}
				if (t < num_fea) {
					tree_point = tree[tree_point].leftch;
				}
				else {
					tree_point = tree[tree_point].rightch;
				}
			}
			prob *= tree[tree_point].prob;
			printf("%0.6lf\n", prob);
		}
	}

	return 0;
}