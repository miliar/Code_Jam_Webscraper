/*
 * in the name of god
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 */

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef long double ldb;

const ldb EPS= 1e-12;

bool mark[20];
int n=9;
int next[1000+10];
ldb dp[20];

struct cmp{
	
	inline bool operator () (const ldb &a1, const ldb &a2) const{
		return a1+EPS < a2;
	}
};
map <ldb, ldb, cmp> code;
/***********************************/
inline int dfs (int v){
	if (mark[v])
		return 0;

	int ret=1;

	mark[v]= true;

	ret+= dfs (next[v]);

	return ret;
}
/************************************/
inline void check (int id){
	
	int test[20];

	for (int i=1;i<=id;i++)
		test[i]= i;

	do{

		memset (mark, false, sizeof mark);

		for (int i=1;i<=id;i++)
			next[test[i]]= i;

		vector <int> Q;

		for (int i=1;i<=id;i++) if (!mark[i])
			Q.push_back (dfs (i));

		if (Q.size()>1){

			ldb tmp=0;

			for (int i=0;i<(int)Q.size();i++)
				tmp+= dp[Q[i]];

			code[tmp]++;
		}

	}while (next_permutation (test+1, test+id+1));

}
/*************************************/
inline ldb fact (int x){
	
	ldb ret=1;

	for (int i=2;i<=x;i++)
		ret*= i;

	return ret;
}	
/*************************************/
int main(){

/*	dp[1]=0;

	cin >> n;

	for (int i=2;i<=n;i++){
		check (i);

		ldb now=1;
		ldb N= fact(i);

		for (int j=1;j<=1000;j++){
			for (map <ldb,ldb> :: iterator it= code.begin(); it!=code.end() ; it++){
				dp[i]+= (it->second)/N * now * (j+(it->first));
			}
			now*= 1/(double)i;
		}

		code.clear();
	}

	cout << fixed << setprecision (10);

	for (int i=1;i<=n;i++)
		cout << i << " : " << dp[i] << endl;
*/

	int Q;
	cin >> Q;

	for (int i=1;i<=Q;i++){
		cin >> n;

		int k=n;

		for (int j=1;j<=n;j++){
			cin >> next[j];
			if (j==next[j])
				k--;
		}

		cout << "Case #" << i << ": ";
		cout << fixed << setprecision(6) << (double)k << endl;
	}
	return 0;
}
