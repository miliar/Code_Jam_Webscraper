#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

const int inf = 0x3f3f3f3f;

#define Eo(x) {cerr << #x <<  " = " << x << endl;}
int n,l,ferlon,t;
string attr[2000];
string name[2560];
int tree[2000][2];
double w[2000];
string feat[2000];
char buff[2560];
int cc = 0;
void scantree(int q){
	char z = 0;
	while (z != '('){
		scanf("%c",&z);
//		Eo(z);
		}
	scanf("%lf", &w[q]);
//	cerr << w[q] << " " ;
	scanf("%s",buff);
//	cerr << (string)buff << endl;
	tree[q][0] = -1;
	tree[q][1] = -1;
	if (buff[0] != ')'){
//		cerr << "begin1" << endl;
		feat[q] = buff;
		cc++;
		tree[q][0] = cc;
		scantree(cc);
//		cerr << "begin2" << endl;
		cc++;
		tree[q][1] = cc;
		scantree(cc);
	//		cerr << "end" << endl;
	}

}
	set <string> st;
long double calcans(){
	long double p = 1;
	int q = 0;	
	while (tree[q][0] != -1){
		p *= w[q];
		if (st.find(feat[q]) != st.end())
			q = tree[q][0];
		else
			q = tree[q][1];
	}
	return p*w[q];
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&ferlon);
	int a;
	for ( int _ = 1; _ <= ferlon; _++){
		cout << "Case #" << _ << ":" << endl;
		tree[0][0] = tree[0][1] = 0;
		scanf("%d",&l);
		scantree(0);
		Eo(_);
		buff[0] = ')';
		while (buff[0] == ')'){
			scanf("%s", buff);
		}
		sscanf(buff,"%d",&a);
		Eo(a);
		for ( int i = 0; i < a; i++){
			cin >> name[i];
			cin >> t;
			st.clear();
			for ( int j = 0; j < t ; j++){
				cin >> attr[i];
				st.insert(attr[i]);
			}
			printf("%lf\n",(double)calcans());


		}
	}


	return 0;
}
