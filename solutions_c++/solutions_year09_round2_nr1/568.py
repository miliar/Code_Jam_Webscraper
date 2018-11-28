/* Rajat Goel [C++] */
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
const int    INF =     0x7FFFFFFF;
const double EPS =     1e-7;
typedef pair<int,int>  pii;
typedef long long      int64;
typedef long double    LD;
#define loop(i,n)      for(int i=0;i<n;i++)
#define foreach(i,a)   for(typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define present(x,in)  (find((in).begin(),(in).end(),x) != (in).end())
#define all(a)         (a).begin(),(a).end()
#define cast(a,b)      { ostringstream myOut; myOut << a ; istringstream myIn ( myOut.str() ); myIn >> b; }
inline int fCMP(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

typedef struct _node {
	LD value;
	char feature[1024];
	struct _node *left, *right;
} node;

string compact(string str) {
	string ans = "";
	loop(i, str.size()) {
		if (str[i]==' ' && i < str.size()-1 && str[i+1]==' ') continue;
		if (str[i]==' ' && i > 0 && str[i-1]=='(') continue;
		if (str[i]==' ' && i < str.size()-1 && str[i+1]==')') continue;
		ans += str[i];
	}
	while(ans[0]==' ') ans = ans.substr(1);
	while(ans[ans.size()-1]==' ') ans = ans.substr(0, ans.size()-1);
	return ans;
}

node* parse(string str) {
	//cout << "Parsing :" << str << endl;
	if(!str.size()) return NULL;
	assert(str[0]=='(' && str[str.size()-1]==')');

	str = str.substr(1, str.size()-2);
	LD val; char feat[1024];
	node* tmp = (node*)malloc(sizeof(node));
	if (sscanf(str.c_str(), "%Lf %s ", &val, feat) == 1) {
		tmp->value = val;
		strcpy(tmp->feature, "");
		tmp->left = tmp->right = NULL;
	} else {
		tmp->value = val;
		strcpy(tmp->feature, feat);
		int i = 0, cnt = 0, p1_st, p1_end, p2_st, p2_end;
		while(str[i]!='(') i++;
		p1_st = i;
		i++; cnt++;
		while(cnt!=0) {
			if (str[i]=='(') cnt++;
			if (str[i]==')') cnt--;
			i++;
		}
		p1_end = i-1;
		while(str[i]!='(') i++;
		p2_st = i;
		i++; cnt++;
		while(cnt!=0) {
			if (str[i]=='(') cnt++;
			if (str[i]==')') cnt--;
			i++;
		}
		p2_end = i-1;
		//cout << "Sending :" << str.substr(p1_st, p1_end-p1_st+1) << " & " << str.substr(p2_st, p2_end-p2_st+1) << endl;
		tmp->left = parse(str.substr(p1_st, p1_end-p1_st+1));
		tmp->right = parse(str.substr(p2_st, p2_end-p2_st+1));
	}
	return tmp;
}

LD solve(node *ptr, vector<string> &prop) {
	if (!ptr) return (LD)1.0;

	if (present(ptr->feature, prop)) {
		return ptr->value * solve(ptr->left, prop);
	} else {
		return ptr->value * solve(ptr->right, prop);
	}
}

int main() {
	int T;
	cin >> T;
	for(int cas=1;cas<=T;cas++) {
		cout << "Case #" << cas << ":\n";
		int L, N, cnt;
		cin >> L;
		string query="", tmp_str, animal;
		vector<string> prop;
		loop(i, L+1) {
			getline(cin, tmp_str);
			query += tmp_str;
		}
		query = compact(query);
		//cout << query << endl;
		node* root = parse(query);
		cin >> N;
		loop(i, N) {
			prop.clear();
			cin >> animal >> cnt;
			loop(j, cnt) {
				cin >> tmp_str;
				prop.push_back(tmp_str);
			}
			printf("%.7Lf\n", solve(root, prop));
		}
	}
	return 0;
}
