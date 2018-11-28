#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define _CRT_SECURE_NO_WARNINGS
using namespace std;

typedef long long ll;
const double pi=acos(-1.0);
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
typedef map<string, int> simp;
#define sz(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define rep(i,b) for(int i=0;i<b;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
template<class T> inline void Swap(T &a,T &b){T c=a;a=b;b=c;}
#define Sort(v) sort((v).begin(), (v).end())
#define Uni(v) Sort(v),(v).erase(unique((v).begin(), (v).end()), (v).end())
#define cl(a,b) memset(a,b,sizeof(a))

const int oo=1000000;

#pragma warning(disable:4996)

#define QX "B"


struct Node {
	Node(string orc) {
		s=orc;
		next=NULL;
	};
	void DelMe() {
		if (next) next->DelMe();
		delete this;
	};
	string s;
	Node* next;
};

Node* getLast(Node* node) {
	Node* ret=NULL;
	while(node) {ret=node;node=node->next;}
	return ret;
}

struct Head {
	Head(Node* data, Head* after) {
		d=data;
		prev=after;
		next=NULL;
		if (after){
			after->next = this;
		}
	}
	Node* d;
	Head* prev;
	Head* next;
};

Head* front;
Head* rear;
Head* Remove(Head* head){
	if (!head->next) {
		rear=head->prev;
	}
	if (!head->prev) {
		front=head->next;
	}
	if (head->prev)
		head->prev->next=head->next;
	if (head->next)
		head->next->prev=head->prev;
	if (head->d)
		head->d->DelMe();
	Head* nn=head->next;
	delete head;
	return nn;
}

void ClearH(){
	Head* ph=front;
	while(ph){
		if (!ph->d->next) {
			ph=Remove(ph);
		} else
			ph=ph->next;
	}
}

int main()
{
//	freopen("test.in","r",stdin);
	freopen("" QX "-small-attempt0.in","r",stdin);freopen("" QX "-small-attempt0.out","w",stdout);
//	freopen("" QX "-small-attempt1.in","r",stdin);freopen("" QX "-small-attempt1.out","w",stdout);
//	freopen("" QX "-large.in","r",stdin);freopen("" QX "-large.out","w",stdout);

    int T=0;
	scanf("%d",&T);
	for (int caseId=1;caseId<=T;caseId++)
	{
        // input
        int n,m;
        cin>>n>>m;
        string line;
        getline(cin, line);
		map<string,int> res;
		vector<string> words;
        rep(i,n){
			getline(cin, line);
			words.insert(words.end(),line);
		}

        char buf[4000];
		cl(buf,0);
		Head* mz[1024];
        rep(i,m){
			front=NULL;
			rear=NULL;
			Head* la[12];
			cl(la,0);
			rep(i,n){
				line=words[i];
				res[line]=0;
				int len=line.length();
				Node* node=new Node(line);
				if (!la[len]) {
					Head* head=new Head(node, rear);
					rear=head;
					if (!front) front = head;
					la[len]=head;
				} else {
					getLast(la[len]->d)->next=node;
				}
			}
			ClearH();

			getline(cin, line);
			rep(j,line.length()){
				if (!front)
					break;
				char ch=line[j];
				Head* ph=front;
				Head* oldr=rear;
				while(ph){
					bool hit=false;
					cl(mz,0);
					Node* p=ph->d;
					while(p){
						Node* tp=p->next;
						int tmz=0;
						rep(l,p->s.length()){
							if (p->s[l]==ch) tmz+=(1<<l);
						}
						p->next=NULL;
						if (tmz>0) hit=true;
						if (!mz[tmz]){
							Head* head=new Head(p, rear);
							rear=head;
							mz[tmz]=head;
						} else {
							getLast(mz[tmz]->d)->next=p;
						}
						p=tp;
					}
					if (hit && mz[0]) {
						Node*p=mz[0]->d;
					    while(p){
							res[p->s]=res[p->s]+1;
							p=p->next;
						}
					}
					ph->d=NULL;
					if (ph==oldr) {Remove(ph);ph=NULL;}
					else ph=Remove(ph);
				}
				ClearH();
			}
			string maxl;
			int maxn=-1;
			rep(i,n){
				if (maxn<res[words[i]]){
					maxn=res[words[i]];
					maxl=words[i];
				}
			}
			strcat(buf,maxl.c_str());
			if (i!=m-1)
				strcat(buf," ");
		}
        // output
        cout << "Case #"<<caseId<<": "<<buf<<"\n";
	}
    return 0;
}