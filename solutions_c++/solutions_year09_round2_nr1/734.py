#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;


struct tree {
	float weight;
	string feature;
	tree* left;
	tree* right;
	
	tree() {
		left = NULL;
		right = NULL;
	}
};

void receive(tree* decision) {
	char ch;
	scanf("%c", &ch);
	while(ch != '(') scanf("%c", &ch);
	scanf("%f", &(*decision).weight);
	//cout << (*decision).weight << endl;
	//		cout.flush();
	scanf("%c", &ch);
	while(ch == ' ' || ch == '\n') scanf("%c", &ch);
		int in = 0;	
	if (ch != ')') {
		char attr[10];

		while(ch != ' ' && ch != '\n') {
			attr[in++] = ch;
			scanf("%c", &ch);
		}
		
		string tmp(attr, in);
		//cout << tmp << endl;
		//cout.flush();
		(*decision).feature = tmp;
		
		tree* left = new tree();
		(*decision).left = left;
		tree* right = new tree();
		(*decision).right = right;
		receive(left);
		receive(right);
		scanf("%c", &ch);
		while(ch != ')') scanf("%c", &ch);
		scanf("\n"); //receiving the )
	}
}

int has_feature(string feat, vector<string> attrs) {
	for(int a = 0; a < attrs.size(); ++a) {
		if (feat == attrs[a])
			return 1;
	}
	return 0;
}

void debug(vector<string> attrs) {
	for(int a = 0; a < attrs.size(); ++a) {
		cout << attrs[a] << endl;
	}
}


float transverse(vector<string> attrs, tree* decision) {
	if (decision != NULL) {
		float result = 1.0;
		result *= (*decision).weight;
		if (has_feature((*decision).feature, attrs)) {
			return result * transverse(attrs, (*decision).left);
		}
		else {
			return result * transverse(attrs, (*decision).right);
		}
	}
	else
		return 1.0;
}

int main () {
	int N;
	scanf("%d\n", &N);
	for(int a = 1; a <= N; ++a) {
		cout << "Case #" << a << ": " << endl;
		int lines;
		scanf("%d\n", &lines);
		tree* decision = new tree();
		receive(decision);
		
		int animals;
		scanf("%d\n", &animals);
		for(int c = 0; c < animals; ++c) {
			char ch;
			int in = 0;
			char name[10];
			scanf("%c", &ch);
			while(ch != ' ') {
				name[in++] = ch;
				scanf("%c", &ch);
			}
			int attrn;
			scanf("%d", &attrn);
			vector<string> attrs;
			for(int d = 0; d < attrn; ++d) {
				in = 0;
				char attrname[10];
				scanf("%c", &ch);
				while(ch == ' ' || ch == '\n') scanf("%c", &ch);
				while(ch != ' ' && ch != '\n') {
					attrname[in++] = ch;
					scanf("%c", &ch);
				}

				string s_attrname(attrname, in);
				attrs.push_back(s_attrname);
			}
			printf("%1.7f\n", transverse(attrs, decision));
		}
		
	}
	return 0;
}