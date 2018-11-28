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
#include <math.h>
#include <stdlib.h>
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




char location[]="..\\..\\";
char filename[]="A-large";//"A-large-practice";
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
struct tItem{

tItem* etrue;
tItem* efalse;
double val;
char name[500];
};
stack<tItem*> parentstack;
set<string> features;
char stmp[500];
bool truetree=true;
tItem root;
void globalinit(){}
void trim(char* stmp1){
	char* stmp2=stmp1;
	char* stmp3=stmp1+strlen(stmp1)-1;
	while(*stmp2==' ')
		stmp2++;
	while(*stmp3==' ')
		stmp3--;
	while(stmp2<=stmp3){
		*(stmp1++)=*(stmp2++);
	}
	*stmp1=0;
}
void init(){
	int lines;
	char* pstr2;
	tItem* titem;
	scanf("%d",&lines);
	gets(stmp);//skip lineend
	titem=&root;
	titem->etrue=NULL;
	parentstack.push(&root);
	for(int n=0;n<lines;n++){
		gets(stmp);
		trim(stmp);
		if(stmp[0]=='('){
			titem=new tItem;
			_atodbl((_CRT_DOUBLE *)&titem->val,&stmp[1]);

			titem->name[0]=0;
			titem->efalse=NULL;
			titem->etrue=NULL;
			int i=1;
			while(stmp[i++]==' ');
			for(;stmp[i]!=0;i++){
			if(stmp[i]==' '){
					if(pstr2=strchr(&stmp[i+1],')')){
						memcpy(&(titem->name),&stmp[i+1],pstr2-&stmp[i+1]);
						titem->name[pstr2-&stmp[i+1]]=0;
					}else{
						strcpy((char*)&(titem->name),&stmp[i+1]);
					}break;
				}
			}
					if(parentstack.top()->etrue){
						parentstack.top()->efalse=titem;
					}else{
						parentstack.top()->etrue=titem;
					}
				parentstack.push(titem);
				int j=1;
				while(*(stmp+strlen(stmp)-j)==')'){
					parentstack.pop();
					j++;
				}
		}else{
			parentstack.pop();
		}
	}
}

int64 solve(){
	int64 ret=0;
	int count,count2;
	scanf("%d",&count);
	for(int i=0;i<count;i++){
		scanf("%s%d",&stmp,&count2);
		for(int n=0;n<count2;n++){
			scanf("%s",&stmp);
			features.insert(stmp);
		}
		
		tItem* titem;
		titem=root.etrue;
		double val=titem->val;
		set<string>::iterator it;
		while(titem->name[0]!=0){
			if((it=features.find(titem->name))!=features.end()){
				titem=titem->etrue;	
			}else{
				titem=titem->efalse;	
			}
			val*=titem->val;
		}
		features.clear();
		printf("%1.7Lf\n",val);
	}

	return ret;
}
int main(){
	globalinit();
	openfiles();	
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		
		init();
		printf("Case #%d:\n",caseId);
		int64 ret=solve();
		fflush(stdout);
	}
	return 0;
}