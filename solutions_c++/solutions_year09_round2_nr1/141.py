#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<iomanip>
using namespace std;

struct node{
	node*lf;
	node*rt;
	string s;
	double v;
};

void rd(node*&r)
{
	r=new node;
	char ch;
	do{cin>>ch;}while(ch!='(');
	cin>>r->v;
	do{cin>>ch;}while(ch==' ');
	if(ch==')'){
		r->s="";
		r->lf=r->rt=NULL;
		return;
	}else{
		cin.putback(ch);
		cin>>r->s;
		rd(r->lf);
		rd(r->rt);
		do{cin>>ch;}while(ch!=')');
	}
}
void solve()
{
	int l;
	string s;
	cin>>l;
	node*root=NULL;
	rd(root);
	//cout<<root->v;
	int n;
	cin>>n;
	vector<string>vs;
	for(int i=0;i<n;i++){
		cin>>s;
		vs.clear();
		int m;
		cin>>m;
		for(int j=0;j<m;j++){
			string ss;
			cin>>ss;
			vs.push_back(ss);
		}
		double re=1.0;
		node *p=root;
		re=p->v;
		while(p->s!=""){
			if(find(vs.begin(),vs.end(),p->s)!=vs.end())
				p=p->lf;
			else
				p=p->rt;
			re*=p->v;
		}
		cout.setf(ios::fixed,ios::floatfield);
		cout<<showpoint<<setprecision(7)<<re<<endl;
	}

}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("a.txt","w",stdout);
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		cout<<"Case #"<<i+1<<":"<<endl;
		solve();
	}
	return 0;
}