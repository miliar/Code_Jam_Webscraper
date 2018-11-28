#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <sys/stat.h> 
using namespace std;

#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
typedef long long int64;//NOTES:int64
typedef long long ll;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64
const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
typedef pair<int,int> ipair;//NOTES:ipair
template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber(
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T sqr(T x){return x*x;}//NOTES:sqr
//Point&Line
double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}//NOTES:dist(
double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}//NOTES:distR(
template<class T> T cross(T x0,T y0,T x1,T y1,T x2,T y2){return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);}//NOTES:cross(
int crossOper(double x0,double y0,double x1,double y1,double x2,double y2)//NOTES:crossOper(
  {double t=(x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);if (fabs(t)<=eps) return 0;return (t<0)?-1:1;}
bool isIntersect(double x1,double y1,double x2,double y2,double x3,double y3,double x4,double y4)//NOTES:isIntersect(
  {return crossOper(x1,y1,x2,y2,x3,y3)*crossOper(x1,y1,x2,y2,x4,y4)<0 && crossOper(x3,y3,x4,y4,x1,y1)*crossOper(x3,y3,x4,y4,x2,y2)<0;}
bool isMiddle(double s,double m,double t){return fabs(s-m)<=eps || fabs(t-m)<=eps || (s<m)!=(t<m);}//NOTES:isMiddle(
//Translator
bool isUpperCase(char c){return c>='A' && c<='Z';}//NOTES:isUpperCase(
bool isLowerCase(char c){return c>='a' && c<='z';}//NOTES:isLowerCase(
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}//NOTES:isLetter(
bool isDigit(char c){return c>='0' && c<='9';}//NOTES:isDigit(
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}//NOTES:toLowerCase(
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}//NOTES:toUpperCase(
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt(
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt64(
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble(
template<class T> void stoa(string s,int &n,T A[]){n=0;istringstream sin(s);for(T v;sin>>v;A[n++]=v);}//NOTES:stoa(
template<class T> void atos(int n,T A[],string &s){ostringstream sout;for(int i=0;i<n;i++){if(i>0)sout<<' ';sout<<A[i];}s=sout.str();}//NOTES:atos(
template<class T> void atov(int n,T A[],vector<T> &vi){vi.clear();for (int i=0;i<n;i++) vi.push_back(A[i]);}//NOTES:atov(
template<class T> void vtoa(vector<T> vi,int &n,T A[]){n=vi.size();for (int i=0;i<n;i++)A[i]=vi[i];}//NOTES:vtoa(
template<class T> void stov(string s,vector<T> &vi){vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));}//NOTES:stov(
template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for (int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}//NOTES:vtos(
//Fraction
template<class T> struct Fraction{T a,b;Fraction(T a=0,T b=1);string toString();};//NOTES:Fraction
  template<class T> Fraction<T>::Fraction(T a,T b){T d=gcd(a,b);a/=d;b/=d;if (b<0) a=-a,b=-b;this->a=a;this->b=b;}
  template<class T> string Fraction<T>::toString(){ostringstream sout;sout<<a<<"/"<<b;return sout.str();}
  template<class T> Fraction<T> operator+(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b+q.a*p.b,p.b*q.b);}
  template<class T> Fraction<T> operator-(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b-q.a*p.b,p.b*q.b);}
  template<class T> Fraction<T> operator*(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.a,p.b*q.b);}
  template<class T> Fraction<T> operator/(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b,p.b*q.a);}

void trim(char* str1){char *str2=str1,*str3=str1+strlen(str1)-1;while(*str2==' ')str2++;while(*str3==' ')str3--;while(str2<=str3){*(str1++)=*(str2++);}*str1=0;}
void trim(string* str1){int tmp=str1->find_first_not_of(" \t\r\f\v\n");*str1=str1->substr(tmp,str1->find_last_not_of(" \t\r\f\v\n")+1-tmp);}

int i1,i2,i3,i4;
#define FOR(i,count) for(i=0;i<count;i++)
#define FOR1(i,count) for(i=1;i<=count;i++)
#define REP(i,count) for(i=count,i>0;i--)
#define EACHCHAR(i,str) for(i=0;str[i];i++)

char location[]="..\\..\\";
char filename[]="A-small-attempt3";//"A-large";
char informat[]=".in";
char outformat[]=".out";

void openfiles(){
	char infile[256];
	char outfile[256];
	struct stat stFileInfo;
	infile[0]=outfile[0]=0;
	strcpy(infile,location);
	strcat(infile,filename);
	strcpy(outfile,infile);
	strcat(outfile,outformat);
	strcat(infile,informat);
	if(stat(infile,&stFileInfo)){//needs sys/stat.h
		printf("Error opening input file");
		getchar();
		exit(1);
	}
	freopen(infile,"r",stdin);
	freopen(outfile,"w",stdout);	
}
//endoftemplate

void globalinit(){
	
}
map<char,char> data;
map<char,char>::iterator it;
char mystr[2000];
char base;
int len;
void init(){
	base=0;
	gets(mystr);
	len=strlen(mystr);
	EACHCHAR(i1,mystr){
		if((it=data.find(mystr[i1]))!=data.end()){
			mystr[i1]=it->second;
		}else{
			if(base<2){
				data.insert(make_pair<char,char>(mystr[i1],1-base));
				mystr[i1]=1-base;
			}else{
				data.insert(make_pair<char,char>(mystr[i1],base));
				mystr[i1]=base;
			}
			base++;
		}
	}
	data.clear();
}

int64 solve(){
	if(base==1)
		base=2;
	int64 ret=0;
	FOR(i1,len){
		ret*=base;
		ret+=mystr[i1];
	}

	return ret;
}
int main(){
	globalinit();
	openfiles();	
	int testcase;
	scanf("%d",&testcase);
	gets(mystr);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		
		init();
		int64 ret=solve();
		printf("Case #%d: %lld\n",caseId,ret);
		fflush(stdout);
	}
	return 0;
}