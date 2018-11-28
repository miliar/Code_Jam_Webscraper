#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
using namespace std;

ifstream fin("A-small-attempt2.in");
//ifstream fin("A-large.in");
ofstream fout("A-small-attempt1.out");
//ofstrema fout("A-large.out");

int T,ssn;
struct seg{
	int x1,y1,x2,y2;
};

seg ss[100000];

void SolveCase(){
	fin>>T;
	ssn=0;
	ss[0].x1=ss[0].y1=0;
	int x1,y1;
	x1=y1=0;
	int f=0;
	for (int i=0;i<T;i++){
		string str;
		fin>>str;
		int rep,step;
		fin>>rep;
		for (int j=0;j<rep;j++){
			step=0;
			for (int k=0;k<str.size();k++){
				if (str[k]=='L') f--;
				if (f<0) f=3;
				if (str[k]=='R') f++;
				if (f>3) f=0;
				if (str[k]=='F'){
					step=1;
					ss[ssn].x1=x1;
					ss[ssn].y1=y1;
					if (f==0){
						ss[ssn].x2=x1+step;
						ss[ssn].y2=y1;
					}
					if (f==1){
						ss[ssn].y2=y1+step;
						ss[ssn].x2=x1;
					}
					if (f==2){
						ss[ssn].x2=x1-step;
						ss[ssn].y2=y1;
					}
					if (f==3){
						ss[ssn].y2=y1-step;
						ss[ssn].x2=x1;
					}
					x1=ss[ssn].x2;
					y1=ss[ssn].y2;
					ssn++;
				}
			}
		}
	}

	int minx=100000000,maxx=-100000000,miny=100000000,maxy=-100000000;
	for (int i=0;i<ssn;i++){
		minx=min(minx,ss[i].x1);
		miny=min(miny,ss[i].y1);
		minx=min(minx,ss[i].x2);
		miny=min(miny,ss[i].y2);
		maxx=max(maxx,ss[i].x1);
		maxy=max(maxy,ss[i].y1);
		maxx=max(maxx,ss[i].x2);
		maxy=max(maxy,ss[i].y2);
	}
	int res=0;
	for (double x=minx+0.5;x<maxx;x+=1){
		for (double y=miny+0.5;y<maxy;y+=1){
			int c0,c1,c2,c3;
			c0=c1=c2=c3=0;
			for (int i=0;i<ssn;i++){
				if (ss[i].x1>ss[i].x2) swap(ss[i].x1,ss[i].x2);
				if (ss[i].y1>ss[i].y2) swap(ss[i].y1,ss[i].y2);

				if (ss[i].x1<x&&ss[i].x2>x&&ss[i].y1<y){
					c2++;
				}
				if (ss[i].x1<x&&ss[i].x2>x&&ss[i].y1>y){
					c0++;
				}
				if (ss[i].y1<y&&ss[i].y2>y&&ss[i].x1<x){
					c3++;
				}
				if (ss[i].y1<y&&ss[i].y2>y&&ss[i].x1>x){
					c1++;
				}
			}
			if (((c0>0&&c2>0)&&(c0%2==0)&&(c2%2==0))||((c1>0&&c3>0)&&(c1%2==0)&&(c3%2==0))){
				res++;
			}
		}
	}
	fout<<res<<endl;
	cout<<res<<endl;
}

int main(){
	int TestCase;
	fin>>TestCase;
	for (int Test=1;Test<=TestCase;Test++){
		fout<<"Case #"<<Test<<": ";
		SolveCase();
	}
	fout.close();
	return 0;
}
