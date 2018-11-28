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

#define INF (1<<29)
int a[110];
int dp[110][300]; // pos, prev

void main2(void){
  int C, D, N, i, j, l, k;
  char com[128][128];
  char opp[128][128];
  REP(i,128){
	REP(j,128)
	  {
		com[i][j] =0;
		opp[i][j] =0;
	  }
  }
  char ans[100];
  char input[100];
  cin>>C;
  REP(i,C){
	cin>>input;
	com[input[0]][input[1]]=input[2];
	com[input[1]][input[0]]=input[2];
  }
  cin>>D;
  REP(i,D){
	cin>>input;
	opp[input[0]][input[1]]=1;
	opp[input[1]][input[0]]=1;
  }
  cin>>N;
  cin>>input;
  j=0;
  REP(i,N){
	if(j!=0 && com[input[i]][ans[j-1]]){
	  ans[j-1] = com[input[i]][ans[j-1]];
	  continue;
	}else{
	  ans[j]=input[i];
	  j++;
	}
	REP(k,j-1){
	  if(opp[ans[k]][ans[j-1]])
		{
		  j =0;
		  break;
		}
	}
  }
  char res[400];
  ans[j]='\0';
  //  cout<<ans;
  res[0]='[';
  k =1;
  if(j==0){
	res[1]=']';
	res[2]='\0';
  }
  else{
	REP(i,j){
	res[k++]=ans[i];
	res[k++]=',';
	res[k++]=' ';
	}
	res[k-2]=']';
	res[k-1]='\0';
  }
  gout << res << endl;
}

int main(void){
	int number_of_test_cases,i;
	scanf("%d",&number_of_test_cases);
	REP(i,number_of_test_cases) main2();
	return 0;
}
