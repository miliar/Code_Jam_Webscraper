#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <iostream>
#include <iostream>
using namespace std;
struct node{
	double p;
	string name;
	int left,right;
};
vector< node > tree;
double fuck(map<string,int> t){
	double ans=1;
	int p=0;
	while(1){
		//cout<<p<<endl;
		ans*=tree[p].p;
		if(t[tree[p].name]==true){
			p=tree[p].left;
		}
		else
			p=tree[p].right;
		if(p==-1)
			break;
	}
	return ans;
}
int parse(string t){
	if(t.size()==0)
		return -1;
	if(t[0]==' ')
		return parse(t.substr(1,t.size()-1));
	if(t[t.size()-1]==' ')
		return parse(t.substr(0,t.size()-1));
	int rtn=tree.size();
	node tmp;
	tree.push_back(tmp);
	//cout<<rtn<<endl;;
	stringstream xxoo(t);
	char c;
	xxoo >> c;
	double p;
	xxoo >> p;
	tree[rtn].p=p;
	xxoo>>tree[rtn].name;
	string t1, t2;
	{
		int i=0;
		int kh=0;
		for(; i<(int)t.size(); i++){
			if(t[i]=='(')
				kh++;
			if(t[i]==')')
				kh--;
			if(kh>=2){
				t1+=t[i];
			}
			if(kh==1&&t[i]==')'){
				t1+=t[i];
				break;
			}
		}
		i++;
		for(; i<(int)t.size()-1; i++){
			t2+=t[i];
		}
	}
	int x=parse(t1);
	tree[rtn].left=x;
	x=parse(t2);
	tree[rtn].right=x;
	return rtn;
}
int main(){
	int n;
	cin >> n;
	for(int kase=1; kase<=n; kase++){
		int line;
		cin >> line;
		string str;
		getline(cin,str);
		string s;
		while(line--){
			getline(cin,str);
			s+=str;
		}
		string p;
		for(int i=0; i<(int )s.size(); i++){
			if(s[i]=='('||s[i]==')'){
				p+=' ';
				p+=s[i];
				p+=' ';
			}
			else
				p+=s[i];
		}
		tree.clear();
		parse(p);

		//cout<<tree[0].right<<endl;
		//cout<<tree[0].left<<endl;
		cin >> line;
		cout<<"Case #"<<kase<<":"<<endl;
		while(line--){
			map<string,int> happen;
			cin >> str;
			int t;
			cin >> t;
			while(t--){
				cin >> str;
				happen[str]=1;
			}
			printf("%.10lf\n", fuck(happen));
		}
	}
}

