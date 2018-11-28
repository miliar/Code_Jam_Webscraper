#include <cstdio>
using namespace std;
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>


vector<int> tmp;
string q, s;
int k;

int get(){
	q = s;
	for (int i = 0; i < s.size(); i += k){
		for (int j = 0; j < k; j++)
			q[i+j] = s[i+tmp[j]];
	}
	int rez = 1;
	for (int i = 1; i < q.size(); i++)
		if (q[i]!=q[i-1]) rez++;
//	cout<<q<<"     "<<rez<<endl;
	return rez;
}

int main(){
	freopen("perm.in", "rt", stdin);
	freopen("perm.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		cin>>k>>s;
//		cout<<k<<" "<<s<<endl;
		tmp.clear();
		for (int i = 0; i < k; i++) tmp.push_back(i);
		int rez = s.size();
		do{
			int e = get();
			if (rez>e) rez = e;
		} while (next_permutation(tmp.begin(), tmp.end()));
		printf("Case #%d: %d\n", t, rez);
	}
	fclose(stdin);
	fclose(stdout);
}
