#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>

using namespace std;

typedef long long LL;
#define PB push_back
#define all(v) (v).begin(),(v).end()
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define pii pair<int,int>
#define INF 200000000
#define MP make_pair
LL gcd(LL m,LL n){LL tmp;while(n!=0){tmp=m%n;m=n;n=tmp;}return m;}   
LL lcm(LL m,LL n){return (m*n)/gcd(m,n);}
string i2s(LL n){stringstream ss;ss<<n;return ss.str();}
LL s2i(string s){stringstream ss;ss<<s;LL n;ss>>n;return n;}



/*****************TRIE***************************/

//Global variable that counts total number of nodes in trie
int TNode=0;

//Trie class
class Trie{
public:
	int words; //frequency of a word
	int prefixes; //frequency of prefixes
	Trie* child[30]; //child node
	//constructor
	Trie(){
		words=0;
		prefixes=0;
		memset(child,0,sizeof(child));
	}
};

//create a new node
Trie* createNode()
{
	TNode++;
	Trie* newNode=new Trie;
	return newNode;
}	

//insert a word
void insertWord(string& s,int pos,Trie* T)
{
	if(pos==s.size()){
		//cout<<s<<endl;
		T->words++;
		return;
	}
	T->prefixes++;
	int k=s[pos]-'a';
	if(T->child[k]==NULL)
		T->child[k]=createNode();
	insertWord(s,pos+1,T->child[k]);
}

//search a word and count its number of occurences
int countWord(string& s,int pos,Trie* T)
{
	if(T==NULL) return 0;
	if(pos==s.size()) return T->words;
	return countWord(s,pos+1,T->child[s[pos]-'a']);
}	


//how many words have a given prefix
int countPrefix(string& s,int pos,Trie* T)
{
	if(T==NULL) return 0;
	if(pos==s.size()) return T->prefixes;
	return countPrefix(s,pos+1,T->child[s[pos]-'a']);
}




/************TRIE end ***********************/


Trie* T=new Trie;

int L,D,N;
set<string> ds;
string A;
map< pair<int,string>,int > dp;


int solve(int pos,string s)
{
	//cout<<s<<endl;
	if(s.size()==L) return countWord(s,0,T);
	if(pos==A.size()) return 0;
	if(countPrefix(s,0,T)==0) return 0;
	//if(dp.find(MP(pos,s))!=dp.end()) return dp[MP(pos,s)];
	int res=0;
	if(A[pos]=='('){
		int end=pos;
		for(int i=pos+1;i<A.size();i++) if(A[i]==')'){end=i; break;}			
		for(int i=pos+1;i<end;i++){
			res+=solve(end+1,s+A[i]);
		}
	}
	else
		res+=solve(pos+1,s+A[pos]);
	//dp[MP(pos,s)]=res;	
	return res;
}
int main()
{
	cin>>L>>D>>N;		
	string s;
	for(int i=0;i<D;i++){
		cin>>s;
		insertWord(s,0,T);
	}	
	
	for(int t=1;t<=N;t++)
	{
		//dp.clear();
		cin>>A;
		int res=solve(0,"");
		printf("Case #%d: %d\n",t,res);
	}	
}