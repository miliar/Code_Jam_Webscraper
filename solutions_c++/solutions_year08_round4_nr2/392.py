#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <sstream>
using namespace std;

ifstream fin("B-small-attempt3.in");
//ifstream fin("B-large.in");
ofstream fout("B.txt");

double calcl(int x,int y,int x2,int y2){
	return sqrt((x-x2)*(x-x2)+(y-y2)*(y-y2)+0.0);
}

double calc(int x1,int y1,int x2,int y2,int x3,int y3){
	double l1=calcl(x1,y1,x2,y2);
	double l2=calcl(x1,y1,x3,y3);
	double l3=calcl(x2,y2,x3,y3);
	double p=l1+l2+l3;
	p/=2;
	return sqrt(p*(p-l1)*(p-l2)*(p-l3));
}

int main(){
	int T,Test;
	fin>>T;
	for (Test=1;Test<=T;Test++){
		int N,M,A;
		fin>>N>>M>>A;
/*		int flag=0;
		if (N<M) {
			swap(N,M);
			flag=1;
		}
		int x,y;
		for (x=N;x>1;x--){
			if (A%x==0){
				break;
			}
		}
		y=A/x;
		if (y<=M){
			if (flag){
				fout<<"Case #"<<Test<<": 0 0 0 "<<y<<" "<<x<<" 0"<<endl;
			}else{
				fout<<"Case #"<<Test<<": 0 0 0 "<<x<<" "<<y<<" 0"<<endl;
			}
		}else{
			fout<<"Case #"<<Test<<": IMPOSSIBLE"<<endl;
		}
	}
*/
		cout<<"Case "<<Test<<endl;
		int flag=0;
		for (int x1=0;x1<=0;x1++){
			for (int y1=0;y1<=0;y1++){
				for (int x2=x1;x2<=N;x2++){
					for (int y2=y1;y2<=M;y2++){
						for (int x3=x1;x3<=N;x3++){
							for (int y3=y1;y3<=M;y3++){
								double res=calc(x1,y1,x2,y2,x3,y3)*2;
								if (abs(res-A)<1e-6){
									fout<<"Case #"<<Test<<": "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl;
									flag=1;
									break;
								}
							}
							if (flag) break;
						}
						if (flag) break;
					}
					if (flag) break;
				}
				if (flag) break;
			}
			if (flag) break;
		}
		if (!flag){
			fout<<"Case #"<<Test<<": IMPOSSIBLE"<<endl;
		}
	}
	fout.close();
	return 0;
}