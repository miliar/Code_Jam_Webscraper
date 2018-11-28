#include <vector>
#include <fstream>
#include <string>
#include <cstring>
#include <iostream>

using namespace std;

class node {
public:
string path;
vector <node*> subNodep;
void add(string);
int count(); 
node(string);
};


node::node(string inputPath) {
path = inputPath;
}

void node::add(string _inputPath) {
string inputPath = _inputPath;
if (path == inputPath)

return;//the path already exists.
else {
bool inSubNode = false;
for (int i = 0;i < subNodep.size();i++) {
if (subNodep[i]->path == inputPath.substr(0,subNodep[i]->path.size())) {
inSubNode = true;
subNodep[i]->add(inputPath);
break;
}
}
if (!inSubNode) {
int i;
for (i = path.size() + 1;i < inputPath.size();i++)
if (inputPath[i] == '/') 
break;
node * newNode = new node(inputPath.substr(0,i));
subNodep.push_back(newNode);
newNode->add(inputPath);
}
}
}

int node::count() {
int ret = 0;
ret += subNodep.size();
for (int i = 0;i < subNodep.size();i++) {
ret += subNodep[i]->count();
cout << subNodep[i]->path << '\n';
}
return ret;	
}

int main() {
ifstream fin("a.txt");
ofstream fout("b.txt");
int T;
fin >> T;
for (int t = 0;t < T;t++) {

node *root = new node("");
int x1, x2;
int N, M;
fin >> N >> M;
char wtf[100];
fin.getline(wtf,255);
for (int n = 0;n < N;n++) {
char path[101];
fin.getline(path, 255);
string inputPath(path);
root->add(inputPath);
}
x1 = root->count();
for (int m = 0;m < M;m++) {
char path[101];
fin.getline(path, 255);
string inputPath(path);
root->add(inputPath);
}
x2 = root->count();
fout << "Case #" << t + 1 << ": ";
fout << x2 - x1 << "\n";
}
return 0;
}
