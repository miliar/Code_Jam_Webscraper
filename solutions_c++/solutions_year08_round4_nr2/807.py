#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
using namespace std;


int main(){
	int casos;
	cin >> casos;
	for (int caso=0 ; caso<casos ; caso++){
		int n,m,a;
		cin >> n >> m >> a;
		cout << "Case #" << (caso+1) << ": ";
		bool encontrado=false;
		bool ex=true;
		//cout << n*m << " " << a  << " " << (n*m<=a)<< endl;
		if (((n*m)<a)){
		//cout << n*m << " " << a  << " " << (n*m>a)<< endl;
			ex=false;
		//	cout << "Sa\n";
		}
		for (int x1=0 ; x1<=n && !encontrado && ex; x1++){
			for (int x2=0 ; x2<=n  && !encontrado; x2++){
				for (int x3=0 ; x3<=n  && !encontrado; x3++){
					for (int y1=0 ; y1<=m  && !encontrado; y1++){
						for (int y2=0 ; y2<=m  && !encontrado; y2++){
							for (int y3=0 ; y3<=m  && !encontrado; y3++){
								//cout << " Da caso" << (caso+1) << " " << x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2) << endl;
								if (fabs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))==a){
									//cout << "EEEEEEEEEEEEEEEEEEEEEEEEE\n";
									cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
									encontrado=true;
								}
							}
						}
					}
				}
			}
		}
		if (!encontrado)
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}


