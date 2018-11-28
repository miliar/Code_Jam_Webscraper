#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>

#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>

int base='a';
using namespace std;

int main(){
	ifstream cin;
	ofstream cout;
	cin.open("A-small-attempt0.in");
	cout.open("output.txt");	
	int R[30];
	

	for(int i=0;i<30;i++)
		R[i]=-1;
R['q'-base]='z'-base;
R[' '-base]=' '-base;
R['v'-base]='p'-base;
	string s[3]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string a[3]={"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
	
	for(int i=0;i<3;i++){
		for(int j=0;j<s[i].size();j++){
			char b=s[i][j],c=a[i][j];
			int d=int(b),e=int(c);
			if(R[d-base]==-1)
				R[d-base]=e-base;
		}
	}
	int count=0,diff=0;
	for(int i=0;i<26;i++){
		count=count+i;
		diff=diff+R[i];
	}
	


	R['z'-base]=count-diff-1;
string h;
	int n;
	cin >> n;getline(cin,h);
	for(int i=0;i<n;i++){
		
		getline(cin,h);
		cout<<"Case #"<<i+1<<": ";
		for(int i=0;i<h.size();i++){
			char  c=R[int(h[i])-base]+base;
			cout <<c;
		}
		cout <<endl;
	
	}


	
	return 0;
}


	