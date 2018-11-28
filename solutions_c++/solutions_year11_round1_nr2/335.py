//Jakub Kędzierski
// SZABLON BY UW:
#include <iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
 
using namespace std;
 
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define INFTY 100000000
#define MAX int('z')-int('a')
#define FI first
#define SE second
 
typedef vector<int> VI;
typedef list<int> LI;
typedef priority_queue<int> PQI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
template <class T>
inline int size(const T&a) { return a.size()-1; }
typedef vector<string> VS;
 
ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b?a/b+1:a/b; }
 
VS parse(string s)
{
  string a;
  VS wyn;
  REP(i,s.size())
    if (s[i]!=' ') a+=s[i];
    else if (!a.empty()) { wyn.PB(a); a=""; }
  if (!a.empty()) wyn.PB(a);
  return wyn;
}
 
VS parse(string s,char ch)
{
  string a;
  VS wyn;
  REP(i,s.size())
    if (s[i]!=ch) a+=s[i];
    else if (!a.empty()) { wyn.PB(a); a=""; }
  if (!a.empty()) wyn.PB(a);
  return wyn;
}
 
int toi(char ch) { return int(ch)-int('0'); }
 
void tolower(string &s) { REP(i,s.size()) s[i]=tolower(s[i]); }
 
int chg(char ch) { return int(ch)-int('a'); }
// KONIEC SZABLONU UW
vector <string> slowa;
vector <string> t;
string alf;


bool znajdz(char zn)
{
	for(int i=0;i<t.size();i++)
		for(int j=0;j<t[i].size();j++)
			if(t[i][j]==zn)
				return true;
				return false;
}

int szukaj(string slowo)
{
 t.clear();
 int wynik=0;
 //przepisanie
 for(int i=0;i<slowa.size();++i)
		 if(slowo.size()==slowa[i].size())
			 t.push_back(slowa[i]);
 //wszystkie o takiej dlugosci
 bool uzyta=false;
 string tmp;
 if(t.size()<=1)
	 return 0;
 for(int i=0;i<alf.size();++i)
 {
	 if(znajdz(alf[i])){
	 for(int j=0;j<slowo.size();++j)
		 if(alf[i]==slowo[j]){uzyta=true;
			 for(int k=0;k<t.size();++k)
				 if(t[k][j]!=slowo[j])
				 {
//					cout<<"Usuwam "<<t[k]<<endl;
					t[k]=t[t.size()-1];
					t.pop_back();
					k--;
					if(t.size()<=1)return wynik;
				 }
		 }
		if(!uzyta){
//		cout<<"Dla słowa "<<slowo<<" chcial strzelic w "<<alf[i]<<endl;
		wynik++;}
		for(int j=0;j<t.size();++j)
			if(t[j]!=slowo)
				for(int k=0;k<t[j].size();++k)
					if((t[j][k]==alf[i])&&(slowo[k]!=alf[i]))
					{
						t[j]=t[t.size()-1];
						t.pop_back();
						j--;
						if(t.size()<=1)return wynik;
						break;
					}
		uzyta=false;
		}
 }
 return wynik;
}

int main()
{
  int T,N,M;
  cin>>T;
  for(int cas=1;cas<=T;++cas)
  {
	slowa.clear();
	cin>>N>>M;
	string tmp;
	for(int i=0;i<N;++i)
		{cin>>tmp;slowa.push_back(tmp);}
    cout<<"Case #"<<cas<<":";
	for(int j=0;j<M;j++)
	{
	cin>>alf;
	int maks=-1,temp;
	string szuk="";
    for(int i=0;i<slowa.size();++i){
		temp=szukaj(slowa[i]);
//		cout<<"Dla "<<slowa[i]<<" mam: "<<temp<<endl;
		if(temp>maks){maks=temp;szuk=slowa[i];}}
	cout<<" "<<szuk;
	}
	cout<<endl;
  }
  return 0;
}

