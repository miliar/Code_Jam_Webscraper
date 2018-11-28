#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<queue>
//struct fold;
using namespace std;

int A, B;
int N,casn;
struct fold {
    string name;
    vector<fold*> sub;
    bool has(string a) {
    	//cout<<"katsotaan löytyykö "<<a<<" kansiosta "<<name<<endl;
    	for(int i=0;i<sub.size();i++) if(sub[i]->name==a) return true;
    	return false;
    }
    fold* get(string a) {
    	for(int i=0;i<sub.size();i++) if(sub[i]->name==a) return sub[i];

    }
    fold* add(string a) {
    	//cout<<"add "<<a<<" in "<<name<<endl;
        fold* nw=new fold();
        nw->name=a;
        sub.push_back(nw);
        return sub[sub.size()-1];
    }
};

fold* root;

void read() {
	root=new fold();
	root->name="r";
    cin>>A>>B;
}
vector<string> split(string a) {
    vector<string> ret;
    string cur="";
    for(int i=1;i<a.size();i++) {
        if(a[i]!='/') cur.push_back(a[i]);
        else { ret.push_back(cur);cur="";}

    }
    if(cur!="") ret.push_back(cur);
    return ret;
}
int ans=0;
void solve() {
    for(int i=0;i<A;i++) {
        string name;
        cin>>name;
        vector<string> f = split(name);
        fold* cur=root;
        for(int j=0;j<f.size();j++) {
        	if(cur->has(f[j])) {
                cur=cur->get(f[j]);
            } else cur=cur->add(f[j]);
        }
    }
    for(int i=0;i<B;i++) {
        string name;
        cin>> name;
        vector<string> f = split(name);
        fold* cur=root;
        //cout<<cur->name<<endl;
        //cout<<"hoo "<<f.size()<<endl;
        for(int j=0;j<f.size();j++) {
        	if(cur->has(f[j])) {
                cur=cur->get(f[j]);
            } else {
          //  	cout<<"Ei löydy "<<f[j]<<endl;
                cur=cur->add(f[j]);
                ans++;
            }

        }

        
    }
        
}

void write() {
    cout<<"Case #"<<casn<<": "<<ans<<endl;

}


int main() {
	cin>>N;
	for(casn=1;casn<=N;casn++) {
	ans=0;
	read();
	solve();
	write();
    }
}
