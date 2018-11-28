#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <deque>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <cstdio>

#define MAX(x,y) ((x)>(y))?(x):(y)
#define MIN(x,y) ((x)<(y))?(x):(y)
#define ABS(x)   ((x)>0)  ?(x):(-x)
#define SQR(x)    (x)*(x)



using namespace std;

main(){
	int N;
	cin >> N;
	string ss;
	getline(cin, ss);
	for(int n=0; n<N; n++){
		getline(cin, ss);
		string s="0";	
		s+=ss;
		int pos=s.size()-1;
		string t="";
		while(s[pos-1]>=s[pos]){ //?
			t+=s[pos];
			pos--;
		}
		t+=s[pos];
		char x=s[pos-1];
		int pos2=0;
		while(x>=t[pos2]) pos2++;//?
		s[pos-1]=t[pos2];
		t[pos2]=x;
		cout << "Case #" << n+1 << ": ";
		int pos3=0;
		if(s[pos3]=='0') pos3++;
		while(pos3<pos) {
			cout << s[pos3];
			pos3++;
		}
		cout << t << endl;
	}
}

