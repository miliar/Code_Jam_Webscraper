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
  int K,N,i,j;
  char input[101][101];
  int frac[101][2];
  double WP[101],OWP[101],OOWP[101];
  cin>>N;
  REP(i,N)
	{
	  cin>>input[i];
	}
  gout<<endl;
  REP(i,N)
	{
	  frac[i][0]=frac[i][1]=0;
	  REP(j,N)
		{
		  switch(input[i][j]){
		  case '.': break;
		  case '1':frac[i][0]++;frac[i][1]++;break;
		  case '0':frac[i][1]++;break;
		  default:cerr<<"err!";
		  }
		}
	  WP[i]=double(frac[i][0])/double(frac[i][1]);
	}
  int opnum;
  double owpsum;
  REP(i,N)
	{
	  opnum =0;
	  owpsum =0;
	  REP(j,N)
		{
		  if(input[i][j]=='.')
			continue;
		  opnum++;
		  if(input[i][j]=='1')
			{
			  owpsum += double(frac[j][0])/double(frac[j][1]-1);
			}
		  if(input[i][j]=='0')
			{
			  owpsum += double(frac[j][0]-1)/double(frac[j][1]-1);
			}		  
		}
	  OWP[i]=owpsum/opnum;
	}
  REP(i,N)
	{
	  opnum =0;
	  owpsum =0;
	  REP(j,N)
		{
		  if(input[i][j]=='.')
			continue;
		  opnum++;
		  owpsum += OWP[j];
		}
	  OOWP[i]=owpsum/opnum;
	}
  REP(i,N)
	{
	  cout<<0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]<<endl;
	}
}

int main(void){
	int number_of_test_cases,i;
	scanf("%d",&number_of_test_cases);
	REP(i,number_of_test_cases) main2();
	return 0;
}
