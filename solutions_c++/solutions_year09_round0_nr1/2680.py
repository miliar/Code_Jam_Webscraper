//#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;
int globalcount;
ifstream cin;
ofstream cout;
struct node {
	map<char,int> edges;
	char value;
};
map<int,node*> firstchar;
map<int,node> nodes;
int L,D,N;
void therecursion(string& x,node* mm,int occ,int dep) {
	if (occ>=x.length()) if(dep==L)  { globalcount++; return; }
	if (dep>=L) return;
	int j=occ,i=occ;
	if (x[j] == '(') {
		j++;
		while (x[i]!=')') {i++;}
		while (x[j]!=')') {
			if (mm->edges.find(x[j])!=mm->edges.end()) {
				therecursion(x,&nodes[mm->edges[x[j]]],i+1,dep+1); 
			}
			j++;
		}
	} else {
		if (mm->edges.find(x[j])!=mm->edges.end()) therecursion(x,&nodes[mm->edges[x[j]]],occ+1,dep+1);
	}
}
int main() {
	cin.open("A-small-attempt1.in");
	cout.open("A-small.out");
	cin >> L >> D >> N;
	string temp;
	int totalnodes=0;
	int tcounter=0;
	map<int,node>::iterator it;
	map<int,node*>::iterator it3;
	for (int i=0; i<D; i++) {
		cin >> temp;
		it3 = firstchar.find((int)temp[0]);
		node* znode;
		if (it3==firstchar.end()) {
			node tsp;
			tsp.value = temp[0];
			nodes[tcounter] = tsp;
			it = nodes.find(tcounter);
			tcounter++;
			firstchar[(int)temp[0]] =&it->second;
			znode = &it->second;
		} else {
			znode = it3->second;
		}
		int j=1;
		map<char,int>::iterator it2;
		while(j<L) {
			it2 = znode->edges.find(temp[j]);
			if (it2 == znode->edges.end()) {
				node tsp;
				tsp.value = temp[j];
				nodes[tcounter] = tsp;
				znode->edges[temp[j]] = tcounter;
				znode = &nodes.find(tcounter)->second;
				tcounter++;
			} else {
				znode = &nodes.find(it2->second)->second;
			}
			j++;
		}
	}
	for (int i=0; i<N; i++) {
		globalcount = 0;
		cin >> temp;
		int j=1,z=1;
		if (temp.length() > 0) {
			if (temp[0] == '(') {
				while (temp[j]!=')') {j++;}
				while (temp[z]!=')') {
					it3 = firstchar.find(temp[z]);
					map<char,int>::iterator it2;
					if (it3!=firstchar.end()) {
						therecursion(temp,it3->second,j+1,1);  
					}
					z++;
				}
			} else {
				it3 = firstchar.find(temp[0]);
				if (it3!=firstchar.end())
					therecursion(temp,it3->second,1,1);
			}
		}
		cout << "Case #" << i+1 << ": " << globalcount << endl;
	}
}