#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/

struct node{
	double weight;
	string feat;
	node *left,*right;
};
int readfl(double &ret,string s, int st){
	int x=st;
	string temp;
	while (!isdigit(s[st])) st++;
	while (isdigit(s[st]) || s[st]=='.') temp+=s[st++];
	//cout << temp << ?' ' << st << endl;
	istringstream sin(temp);
	sin >> ret;
	return st;
}
node* make_tree(string &s, int st, int en){
	st++;
	node *ret= new node;
	st= readfl(ret->weight,s,st);
	int s1,s2;
	while (st<en && (s[st]<'a' || s[st]>'z')) st++;
	if (st==en) return ret;
	while (s[st]>='a' && s[st]<='z') ret->feat+=s[st++];
	while (s[st]==' ') st++;
	if (s[st]=='(') s1=st;
	int x=1;
	For(i,st+1,en){
		if (s[i]=='(') x++;
		if (s[i]==')') x--;
		if (x==0) { s2=i; break;}
	}
	ret->left = make_tree(s,s1,s2);
	st=s2+1;
	while (s[st]==' ') st++;
	if (s[st]=='(') s1=st;
	x=1;
	For(i,st+1,en){
		if (s[i]=='(') x++;
		if (s[i]==')') x--;
		if (x==0) { s2=i; break;}
	}
	ret->right= make_tree(s,s1,s2);
	return ret;
}
double traverse(node *root, set<string> &att){
	//cout << root->feat << ' '<< root->weight << ' ' << (bool)(att.find(root->feat)!=att.end()) << endl;
	if (root->feat=="") return root->weight;
	if (att.find(root->feat) != att.end())
		return root->weight* traverse(root->left,att);
	else
		return root->weight * traverse(root->right,att);
	return 1;
}
void fre(node *cur){
	if (cur->feat=="") free(cur);
	fre(cur->right); fre(cur->left) ;
	fre(cur);
}
int main(){
	int t,n,k;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
			scanf("%d\n",&n);
			string s; char buf[100];
			For(i,0,n){
				scanf("%[^\n]\n",buf);
				s+=buf;
				s+=" ";
			}
			n=s.size();
			int st=n,en=-1;
			For(i,0,n) {if (s[i]=='(') st<?=i ; if (s[i]==')') en>?=i;}
			node * root=make_tree(s,st,en);

			cerr << "DONE making the tree \n";
			scanf("%d",&n);
			printf("Case #%d:\n",cas);
			For(i,0,n){
				scanf("%s",buf);
				scanf("%d",&k);
				set<string> S;
				while (k--){
					scanf("%s",buf);
					S.insert(buf);
				}
				//cerr << "begining to traverse \n";
				printf("%.6lf\n",traverse(root,S));
			}
			//fre(root);
	}
	return 0;
}

/*
int t;
int main(){
	scanf("%d",&t);
	int n,orig,best,num;
	int cas=1;
	char buf[100];
	while (t--){
		scanf("%s",buf);
		n=strlen(buf);
	
		vector<int> a;
		For(i,0,n)
			a.pb(buf[i]-'0');
		bool test= next_permutation(ALL(a));
		//cout << test << ' ';
		//For(i,0,a.size()) cout << a[i] << ' '; 
		if (test){
		}
		else{
			a.pb(0);
			sort(ALL(a));
			For(i,0,a.size())
				if (a[i]!=0) {
					swap(a[0],a[i]);
					break;
				}

		}
		printf("Case #%d: ",cas);
		For(i,0,a.size()) printf("%c",a[i]+'0');
		putchar(10);
		cas++;
	}
	return 0;
}
*/
