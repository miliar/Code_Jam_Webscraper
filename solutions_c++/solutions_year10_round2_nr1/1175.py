#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <fstream>
#include <numeric>
#include <bitset>
#include<string.h>

using namespace std;

#define pb push_back
#define mp(X,Y) make_pair(X,Y)
#define sz(c) int((c).size())
#define all(c) (c).begin(),(c).end()
#define tr(c,it) for(typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define present(c,X) ((c).find(X)!=(c).end())
#define cpresent(c,X) (find(all(c),X)!=(c).end())
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define vi vector<int> 
#define vit vector<int>::interator 
#define vvi vector< vector<int> > 
#define pp  pair<int,int>
#define vpp vector<pair<int,int> >

const double pi=acos(-1.0);
const double eps=1e-11;
typedef long long int64;
typedef unsigned long long uint64;

bool isUpperCase(char c){return c>='A' && c<='Z';}
bool isLowerCase(char c){return c>='a' && c<='z';}
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}
bool isDigit(char c){return c>='0' && c<='9';}
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}

template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}


int casenumber;
#define printg casenumber++, printf("Case #%d: ",casenumber), printf
#define gout casenumber++, printf("Case #%d: ",casenumber), cout

struct node
{
	string s;
	map<string,node*> m;

}*p;
node * root;
int total=0;
void addnode(node *curr,vector<string> str,int k)
{
	
	if(k==str.size())return;
	map<string,node*> b=curr->m;
	
	if(b.find(str[k])==b.end())
	{
	
		node *temp=new node;
		temp->s=str[k];
		b[str[k]]=temp;
		
		curr->m=b;
		
		addnode(b[str[k]],str,k+1);
		//cout<<"dsfs"<<endl;
	}
	else
	{
		addnode(b[str[k]],str,k+1);
	}
}

void findnode(node *curr,vector<string> str,int k)
{
	if(k==str.size())return;
	map<string,node*> b=curr->m;
	//cout<<"s"<<b.size()<<endl;
	if(b.find(str[k])==b.end())
	{
		//cout<<"not found"<<endl;
		total=total+str.size()-k;
		//cout<<total<<endl;
		addnode(curr,str,k);
	}
	else
	{
		//cout<<"found"<<endl;
		findnode(b[str[k]],str,k+1);
	}
}


void main2(void)
{
	int n,m;
	cin>>n>>m;
	total=0;
	vector<vector<string> > vs;
	p=new node;
	p->s="/";
	root=p;
	for(int i=0;i<n;i++)
	{
		char s[105];
		cin>>s;
		vector<string> temp;
		char * str=strtok(s,"/");
		while(str!=NULL)
		{
			temp.pb(str);
			str=strtok(NULL,"/");
		}
		//cout<<endl<<endl;	
		///tr(temp,it)
		//cout<<(*it)<<" ";
		//cout<<endl;
		
		addnode(p,temp,0);

	}
//cout<<"added"<<endl;
	vector<vector<string> > vp;
	for(int i=0;i<m;i++)
	{
		char s[105];
		cin>>s;
		vector<string> temp;
		char * str=strtok(s,"/");
		while(str!=NULL)
		{
			temp.pb(str);
			str=strtok(NULL,"/");
		}	
		//tr(temp,it)
		//cout<<(*it)<<" ";
		//cout<<endl;
		findnode(root,temp,0);
	}
	
	gout<<total<<endl;
}


int main(void){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int number_of_test_cases,i;
	scanf("%d",&number_of_test_cases);
	for(int i=0;i<number_of_test_cases;i++) main2();
	return 0;
}

