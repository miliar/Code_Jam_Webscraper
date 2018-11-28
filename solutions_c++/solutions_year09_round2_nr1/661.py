#include <iostream>
#include <string>
#include <string.h>
#include <map>
using namespace std;
const int SIZE= 100000;
class Node{
public:
	double wi;
	string fea;
	bool isleaf;
	bool used;
	void set(double d=0, string s="",bool leaf=true){
		wi=d;
		fea=s;
		isleaf=leaf;
		used=true;
	}
	void show(){
		printf("wi: %.2lf ; str: %s isleaf :%d\n",wi,fea.c_str(),isleaf);
	}
}; 
Node hp[SIZE];
int totline;
void init();
Node myget(int nd);
char mynext();
void showtree();
int cnt=0;
map<string ,bool > hash;
double dfs(int nd );
int main(){
	//freopen("../../dat.in","r",stdin);
	int cas;
	cin>>cas;
	int i;
	for (i=1;i<=cas;i++){
		init();
		//showtree();
		printf("Case #%d:\n",i);
		int j;
		int m;
		cin>>m;
		for (j=0;j<m;j++){
			string buff;
			cin>>buff;
			int k;
			cin>>k;
			hash.clear();
			int p;
			for (p=0;p<k;p++){
				string buff;
				cin>>buff;
				hash[buff]=true;
			}
			double ans = dfs(1);
			printf("%lf\n",ans);
		}
	}
	
	return 0;
}
double dfs(int nd ){
	if (hp[nd].isleaf){
		return hp[nd].wi;
	}
	if (hash[hp[nd].fea]){
		return hp[nd].wi*dfs(nd*2);
	}else{
		return hp[nd].wi*dfs(nd*2+1);
	}
}
void init(){
	cin>>totline;
	int i;
	for (i=0;i<SIZE;i++){
		hp[i].used=false;
	}
	cnt=0;
	hp[1]=myget(1);
}
void showtree(){
	int i;
	for (i=1;i<=10;i++){
		printf("nd %d: \n",i);
		hp[i].show();
	}
}
char mynext(){
	char ch;
	while (cin>>ch){
		if (!isspace(ch)){
			cin.putback(ch);
			break;
		}
	}
	return ch;
}
Node myget(int nd){
	char ch = mynext();
	cin>>ch; // '('
	double val;
	string fea="";
	cin>>val;
	ch=mynext();
	if (ch==')'){
		cin>>ch;
		Node tmp;
		tmp.set(val);
		return tmp;
	}else if (isalpha(ch)){
		cin>>fea;
	}
	ch=mynext();
	if (ch==')'){// leaf
		cin>>ch;
		Node tmp;
		tmp.set(val,fea);
		return tmp;
	}else if(ch=='('){
		hp[nd*2]=myget(nd*2);
		ch=mynext();
		if (ch==')'){ // only left child
			cin>>ch;
			Node tmp;
			tmp.set(val,fea,false);
			return tmp;
		}else if(ch=='(') { // has right child
			hp[nd*2+1]=myget(nd*2+1);
			ch=mynext();
			cin>>ch;
			Node tmp;
			tmp.set(val,fea,false);
			return tmp;
		}
	}
	
}