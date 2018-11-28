/*
ID: twinkle
PROG: Bot Trust
LANG: C++
*/

#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;


#define read() freopen("test.in","r",stdin)
#define write() freopen("test.out","w",stdout)

int abs(int a){
	if(a < 0)return -a;
	return a;
}



int main(){
	//read();
	//write();
	int T,p,sec,ans,po,pl,tmp,N;
	char r,lastr;
	cin >> T;
	for(int Case = 1; Case <= T; Case ++){
		cout << "Case #"<<Case<<": ";
		cin >> N;
		lastr = '0';
		sec = ans = 0;
		pl = po = 1;
		for(int i = 1;i <= N;i ++){
		 cin >> r >> p;
		 if(r == 'O'){
		  if(r == lastr){
		   tmp = abs(p-po) + 1;
		   po = p;
		   sec += tmp;
		   ans += tmp;
		  }
		  else{
		   lastr = r;
		   tmp = abs(p - po) - sec;
		   if(tmp < 0)tmp = 0;
		   tmp ++;
		   sec = tmp;
		   po = p;
		   ans += tmp;
		  }
		 }
		 else{
		  if(r == lastr){
		   tmp = abs(p - pl) + 1;
		   pl = p;
		   sec += tmp;
		   ans += tmp;
		  }
		  else{
		   lastr = r;
		   tmp = abs(p - pl) - sec;
		   if(tmp < 0)tmp = 0;
		   tmp ++;
		   sec = tmp;
		   pl = p;
		   ans += tmp;
		  }
		 }
		}
		cout << ans << endl;
	}


	return 0;
}

/*
Input 
 	
Output 
 
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
Case #1: 6
Case #2: 100
Case #3: 4
*/
