#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <conio.h>

using namespace std;


typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
 

typedef pair<int,int> pii;

#define PI 3.141592654
#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define MAX(x,y) x > y ? x : y
#define MIN(x,y) x < y ? x : y
#define SQR(a) a*a

//Maybe come up an an approximation for equal 
template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline T hyp(T s1,T s2) { return sqrt(SQR(s1) + SQR(s2)); }
template<typename T> inline bool aprx(T a,T b)  //Approximately equal
{
	T precision=0.0001;

	if(abs(a - b) <= precision)
		return true;

	return false;
} 
 
 

//Use example: double x = conv<double>(str);
template<typename T, typename S> T conv(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}


struct SPoint {
	double x, y;
	void set(double _x,double _y){ x = _x; y = _y; }
};

void ParseBuf(char buf[],vector<string> &vs)
{
	char *p;
	char val[300];
	int i=0, j=0;

	p = buf;
 
	while(true)
	{

		if(*p == ' ' || *p == '\0'){
			if(j == 0){
				val[i] = '\0';
				vs.push_back(val);
				i = 0;
			}
			if(*p == '\0') break;
			p++;
			j++;			
		}
		else{
			val[i++] = *(p++);
			j = 0;
		}	 
	}
}

int readTime() {
	int h, m;
	scanf("%d:%d", &h, &m);
	return m+60*h;
}

bool order(long &a,long &b)
{
	if(a < b) return true;
	return false;
}

bool revord(long &a, long &b)
{
	if(a < b) return false;
	return true;
}

 
int main()
{
	char ch;
	string FileIn, FileOut; 
    int t;
    char buf[5000], *str;
 
	//scanf("%d", &t);
	

	while(true){
		printf("Press S for Small and L for Large Input File: ");
        ch = _getche();
		if(toupper(ch) == 'L'){
			FileIn = "Linput.txt";
			FileOut = "Loutput.txt";
			break;
		}
		else if(toupper(ch) == 'S')
		{
			FileIn = "Sinput.txt";
			FileOut = "Soutput.txt"; 
			break;
		}
		else if(ch == 27)
			exit(0);
		printf("\n");

	}

	printf("Inputting: %s!\n",FileIn.c_str());
	freopen(FileIn.c_str(),"rt",stdin);
	freopen(FileOut.c_str(),"wt",stdout);
	 
 
	vector<long> vx, vy;
	vector<string> vecin;
	int dim, sz;
	long val;
	int64 sum;
	//scanf("%d", &t);
	gets(buf);
	t = atoi(buf);
	For(test,1,t)
	{

		gets(buf);
		dim = atoi(buf);
		gets(buf);
		ParseBuf(buf,vecin);
		Rep(i,vecin.size()){
			val = atol(vecin[i].c_str());
			vx.push_back(val);
		}
		vecin.clear();
		gets(buf);
		ParseBuf(buf,vecin);
		Rep(i,vecin.size()){
			val = atol(vecin[i].c_str());
			vy.push_back(val);
		}
		vecin.clear();

		sort(vx.begin(),vx.end(),order);

		//reverse(vx);
		sort(vy.begin(),vy.end(),order);

		sum = (int64)0;
		sz = vx.size();
		Rep(j,vx.size()){
			sum += (int64)vx[j] * (int64)vy[sz - 1];
			sz--;
		}
		//scanf("%lf%lf%lf%lf%lf%lf",&x1, &y1, &x2, &y2, &x3, &y3);
		 

		printf("Case #%d: %lld\n", test, sum);

		vx.clear();
		vy.clear();

	}

	exit(0);
}