#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>
#include <set>

/*
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)*/



struct Node {
	Node(std::istream & is, char & ch) 
		: a(NULL)
		, b(NULL)
	{

		parseTree(is, ch);
	}
	void parseTree(std::istream & is, char & ch) {
		while (ch != '(') { is >> ch; }

		is >> prob;

		std::stringstream s;

		for (;;) {
			is >> ch;
			if (ch < 'a' || ch > 'z') break;
			s << ch;
		}
		
		feature = s.str();

		while (ch == ' ') { is >> ch; }

		if (ch == '(') {
			a = new Node(is, ch);
			b = new Node(is, ch);
		}
	}

	~Node() {
		delete a;
		delete b;
	}

	bool isLeaf() const { return (a == NULL) || (b == NULL); }

	double decide(const std::set<std::string> features, double p = 1.0) {
		p *= prob;
		if (isLeaf()) return p;
		if (features.find(feature) != features.end()) {
			return a->decide(features, p);
		} else {
			return b->decide(features, p);
		}
	}

	void print(int indent = 0) {
		for (int i = 0; i < indent; i++) std::cout << ' ';
		std::cout << prob << ' ' << feature << std::endl;
		if (a != NULL) a->print(indent+2);
		if (b != NULL) b->print(indent+2);

	}
	std::string feature;
	Node * a;
	Node * b;
	double prob;
};

void test(std::istream & is) {
	int lines;
	is >> lines;
	std::string buf;
	std::string line;
	std::getline(is, line);
	
	for (int i = 0; i < lines; i++) {
		std::getline(is, line);
		buf.append(line);
	}

	char ch;
	Node * root = new Node(std::stringstream(buf), ch);

	int nanimals;
	is >> nanimals;
	for (int anim = 0; anim < nanimals; anim++) {
		std::string animal;
		is >> animal;
		int nfeatures;
		is >> nfeatures;
		std::set<std::string> features;
		for (int f = 0; f < nfeatures; f++) {
			std::string feature;
			is >> feature;
			features.insert(feature);
		}
		printf("%0.7f\n", root->decide(features));

	}

}

int main(int argc, char* argv[])
{
	std::fstream fs("E:\\1codejam\\projecta\\Release\\A-large.in");

	int n;
	fs >> n;
	std::string line;
	std::getline(fs, line); 


	for (int i = 0; i < n; i++) {
		printf("Case #%d:\n", i+1);
		test(fs);
	}
	
	return 0;
}

