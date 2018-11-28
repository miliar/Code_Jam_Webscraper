
#include "stdio.h"
#include "math.h"
#include "map"
#include "string"
#include "vector"

struct Node {
	std::string path_;
	std::vector<Node*> child;
	Node(std::string path) {
		path_ = path;
	}

	Node() {
		path_ = "";
	}
};

void Tokenize(const std::string& str, std::vector<std::string>& tokens, const std::string& delimiters = " ") {
    // Skip delimiters at beginning.
    std::string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    std::string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (std::string::npos != pos || std::string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}

int main() {
	

	freopen("A-large.in", "r", stdin);
	freopen("outlarge.txt", "w", stdout);
	int numCases;
	scanf("%d", &numCases);
	for(int caseNum=0; caseNum<numCases; ++caseNum) {
		Node root;
		int n, m;
		scanf("%d %d", &n, &m);
		for(int i=0; i<n; ++i) {
			char path[200];
			scanf("%s", path);
			std::string newPath = path;
			std::vector<std::string> tokens;
			Tokenize(newPath, tokens, "/");
			Node * current = &root;
			for(int j=0; j<tokens.size(); ++j) {
				bool found = false;
				for(int k=0; k<current->child.size() && !found; ++k) {
					if(current->child[k]->path_ == tokens[j]) {
						current = current->child[k];
						found = true;
					}
				}
				if(!found) {
					Node * newNode = new Node(tokens[j]);
					current->child.push_back(newNode);
					current = newNode;
				}
			}
		}


		int count = 0;
		for(int i=0; i<m; ++i) {
			char path[200];
			scanf("%s", path);
			std::string newPath = path;
			std::vector<std::string> tokens;
			Tokenize(newPath, tokens, "/");
			Node * current = &root;
			for(int j=0; j<tokens.size(); ++j) {
				bool found = false;
				for(int k=0; k<current->child.size() && !found; ++k) {
					if(current->child[k]->path_ == tokens[j]) {
						current = current->child[k];
						found = true;
					}
				}
				if(!found) {
					Node * newNode = new Node(tokens[j]);
					current->child.push_back(newNode);
					current = newNode;
					++count;
				}
			}
		}

		printf("Case #%d: %d\n", caseNum + 1, count);

	}
	return 0;
}

