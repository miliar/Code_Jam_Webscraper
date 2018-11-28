#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>

using namespace std;

struct tree_node;
typedef tree_node* pnode;

string tree_str;
istringstream iss;

string a_name[100];
int f[100]; // # features of Animal i
bool list[100][10000];

tree_node *root;

map<string, int> feature_id;
string feature_name[10000];
int fcnt;

struct tree_node {
	double value;
	int feature; // default -1
	pnode left, right;
};

void build_tree(pnode &ptr){
	char c;
	iss >> ws >> c;
	if (c!='(')
		cout << "Error!" << endl;

	ptr = new tree_node;
	iss >> ptr->value;

	while (iss.peek()==' '){
		iss.get();
	}

	ptr->feature = -1;
	ptr-> left = NULL;
	ptr-> right= NULL;

	if (iss.peek()!=')'){
		ptr->feature = fcnt;
		iss >> feature_name[fcnt];
		feature_id[feature_name[fcnt]] = fcnt;
		fcnt++;
		build_tree(ptr->left);
		build_tree(ptr->right);
	}

	iss >> ws >> c;
	if (c!=')')
		cout << "Error!" << endl;

}

double calc(pnode src, int id){ // id: animal id
//	cout << "CALC" << src->value << " " << id << endl;
	double ans = src->value;
	if (src->feature != -1){
		if (list[id][src->feature]){
			return ans * calc(src->left, id);
		} else {
			return ans * calc(src->right, id);
		}
	}
	return ans;
}

void delete_tree(pnode ptr){
	if (ptr -> left !=NULL)
		delete_tree(ptr -> left);
	if (ptr -> right!=NULL)
		delete_tree(ptr -> right);
	delete ptr;
}

int main(){
	int T;
   	int L, A;
	string line[80];
	


	cin >> T; 

	for (int cnt = 1; cnt <=T; ++cnt){
		cout << "Case #" << cnt << ": " << endl;

//		cout << (char) cin.peek() << endl;
		cin >> L >> ws;
		tree_str = "";
		for (int i=0; i<L; ++i){
			getline(cin, line[i]);
			tree_str += line[i] + " ";
		}
		iss.str(tree_str);

//		cout << "TREE STRING " << tree_str << endl;
	
		fcnt = 0;
		feature_id.clear();

		// build tree now
		build_tree(root);
//		cout << "TREE BUILT" << endl;
		
		cin >> A;
		for (int i=0; i<A; ++i){
			for (int j=0; j<fcnt; ++j){
				list[i][j] = false;
			}
			cin >> a_name[i];
			cin >> f[i];
			for (int j=0; j<f[i]; ++j){
				string feature;
				cin >> feature;
				if (feature_id.find(feature)!=feature_id.end()){
					list[i][feature_id[feature]] = true;
				}
			}
//			cout << "ANIMAL: " << a_name[i] << " " << f[i] << endl;
		}
//		cout << "INPUT COMPLETED" << endl;

		cout.setf(ios::fixed);
		for (int i=0; i<A; ++i){
			cout << setprecision(7) << calc(root, i) << endl;
		}

		delete_tree(root);
	}
	
	return 0;
}
