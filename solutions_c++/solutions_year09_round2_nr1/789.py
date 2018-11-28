#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <sstream>
#include <stack>
#include <set>
using namespace std;

double tree[2000];
bool check_tree[2000];
char comp[2000][200];
int see;
string str_in,str1;
char query[1000][1000];

void make_tree()
{
//	cout <<str_in<<endl;
	int i,n;
	string new_str;
	n = str_in.size();
	for(i=0;i<n;i++){
		if(str_in[i]=='(' || str_in[i]==')')
			new_str = new_str + " "+ str_in[i] +" ";
		else new_str = new_str + str_in[i];
	}
	stringstream in(new_str);
	memset(check_tree,false,sizeof check_tree);
	char str[100];
	double v;
	stack<int> stridx;
	int idx = 0;
	stridx.push(0);
	for(i=0;i<1000;i++)
		tree[i] = 1.0;
	check_tree[0] =true;
	while(in >> str){
		if(str[0]=='0' || str[0]=='1'){
			sscanf(str,"%lf",&v);
			//cout <<v <<endl;
			tree[idx] = v;
		}
		else if(str[0]=='('){
			idx = stridx.top();
			stridx.pop();
		}else if(str[0]==')'){
		}else{

			strcpy(comp[idx],str);
			idx *= 2;
			check_tree[idx+1] = true;
			check_tree[idx+2] = true;

			stridx.push(idx+2);
			stridx.push(idx+1);
		}
	}
	for(i=0;i<16;i++){
		//cout <<i<< " : "<<tree[i]  <<endl;
	}
}
double ret=0.0;
set<string > s;
void back(int idx,double prob){
	if(check_tree[idx]){
		if(comp[0]=='\0' || s.find(comp[idx]) != s.end() ){
			back(2*idx+1, prob * tree[idx]);
		}else{
		//	back(2*idx+1, prob * tree[idx]);
			back(2*idx+2,  prob * tree[idx]);
		}

	}else {
		ret+= prob * tree[idx];
	}
		
}
int main()
{
	int i,j;
	int kase =1 ;
	int t,idx;
	
	char str[100];
  	gets(str);
	t = atoi(str);
	int n;
	for(kase=1;kase<=t;kase++){
		ret = 0.0;
		gets(str);
		n = atoi(str);
		str_in="";
		for(i=0;i<n;i++){
			gets(str);
//			cout << "s : "<<str <<endl;
			str_in += string(str);
		}
		gets(str);
		int q = atoi(str);
		memset(comp,0,sizeof comp);
		make_tree();
		cout <<"Case #"<<kase <<": " <<endl;
		for(i=0;i<q;i++){
			gets(str);
			stringstream in (str);
			int nn;
			char str1[100];
			in >> str1;
			in >> nn;
			s.clear();
			for(j=0;j<nn;j++){
				in >> query[j];
				s.insert(query[j]);
			}		
			ret =0.0;
			back(0,1.0);
			printf("%.7lf\n",ret);
		}
	}
}
