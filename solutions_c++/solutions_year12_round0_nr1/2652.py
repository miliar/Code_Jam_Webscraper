//SORU
//PROGRAM C++

/*
	ID: semihbasrik
	LANG: C++
	TASK:
*/
#include<iostream>
#include<fstream>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<climits>
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define wait system("pause");
#define lint long long int
#define ABS(a)	 ( (a)>0 ? (a) : -(a) )
#define KARE(a)	 ( (a)*(a) )
#define MAX(a,b) ( (a)>(b) ? (a) : (b) )
#define MIN(a,b) ( (a)<(b) ? (a) : (b) )
#define INF		 INT_MAX
#define cin fin
#define cout fout
using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

string str1="ejpmyslckdxnribtahwfvougzq";
string str2="ourlangeismbtdhwyxfcpkjvqz";
char L[300];
int T;

void print(int k,string str){
	cout<<"Case #"<<k<<": ";
	for(int i=0;i<str.size();i++)
		if(str[i]!=' ')	cout<<L[str[i]];
		else			cout<<" ";
	cout<<endl;
}

void solve(){
	int i;
	string str;

	for(i=0;i<str1.size();i++)
		L[str1[i]]=str2[i];
		
	cin>>T;
	getline(cin,str);
	for(i=1;i<=T;i++)
		getline(cin,str),print(i,str);
//	wait;
}

int main(){
	solve();
}
