#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

string board[60];

void main2(void){
  int N,K,po,pb,to,tb,p,i,j,k,l;
  po = 1;
  pb = 1;
  to = 0;
  tb = 0;
  char color;
  K = 0;
  scanf("%d",&N);
  REP(i,N){
	scanf(" %c %d",&color,&p);
	if(color == 'O'){
	  int dis = abs(p-po);
	  int t = max(dis-to,0)+1;
	  K += t;
	  to = 0;
	  tb += t;
	  po = p;
	}else{
	  int dis = abs(p-pb);
	  int t = max(dis-tb,0)+1;
	  K += t;
	  tb = 0;
	  to += t;
	  pb = p;
	}
  }  
  gout<<K<<endl;
}

int main(void){
	int number_of_test_cases,i;
	scanf("%d",&number_of_test_cases);
	REP(i,number_of_test_cases) main2();
	return 0;
}
