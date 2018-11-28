#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <map>
#include <bitset>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PI;
typedef pair<double,double> PD;

#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); ......x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)(x).size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

#define DEBUG 1
#define DEBUG_ON
#define INF 10000000; 


#define NEWLINE cout<<"\n"
#define REPORT(x) cout<<#x<<"="<<(x)<<endl;
#define ASSURE(x) cout<<#x<<endl<<flush
#define ASSERT(x) if(!(x)) REPORT("warunek nie spelniony!!")
template <typename T>
void write(T begin, T end)
{
	T ptr = begin;
	while(ptr!=end){
		cout<<*(ptr++)<<" ";
	}
	cout<<endl;
} 
template <>
void write(pair<int,int> * begin, pair<int,int> * end){
	pair<int,int>* ptr = begin;
	while(ptr!=end){
		cout<<"("<<(ptr->first)<<","<<(ptr->second)<<") ";
		++ptr;
	}
	cout<<endl;

}	
template <typename T>
T to(const std::string & s)
{
    std::istringstream stm(s);
    T result;
    stm >> result;
    return result;
}



template<class T, class K>
ostream& operator<<(ostream& out, const pair<T,K> & p){
	out<<"("<<p.first<<","<<p.second<<")";
	return out;
}


char * T[4];
bool notX(int i, int j){
    return T[i][j]=='O' || T[i][j]=='.';
}
bool notO(int i, int j){
    return T[i][j]=='X' || T[i][j]=='.';
}
bool incomplete(){
    for(int i=0;i<4;++i){
        for(int j=0;j<4;++j){
            if(T[i][j] == '.') return true;
        }
    }
    return false;
}
void testCase(int case_index){
    char res[100];
    res[0] = '\0';
    char c;

    for(int i=0;i<4;++i) scanf("%s",T[i]);

    bool winO=false,winX=false;
    for(int i=0;i<4;++i){
        bool row_win_X=true,row_win_O=true;
        bool col_win_X=true,col_win_O=true;
        for(int j=0;j<4;++j){
            if(notX(i,j)) row_win_X=false;
            if(notO(i,j)) row_win_O=false;
            if(notO(j,i)) col_win_O=false;
            if(notX(j,i)) col_win_X=false;
        }
        if(row_win_X || col_win_X) winX=true;
        if(row_win_O || col_win_O) winO=true;
    }

    if(! (notX(1,1)||notX(2,2)||notX(3,3)||notX(0,0)) || !(notX(3,0)||notX(2,1)||notX(1,2)||notX(0,3))) winX = true;
    if(! (notO(1,1)||notO(2,2)||notO(3,3)||notO(0,0)) || !(notO(3,0)||notO(2,1)||notO(1,2)||notO(0,3))) winO = true;

    if(winO) strcpy(res, "O won");
    else if(winX) strcpy(res, "X won");
    else if(incomplete()) strcpy(res, "Game has not completed");
    else strcpy(res, "Draw");


    //not completed

    printf("Case #%d: %s\n",case_index+1,res);
}
int main(){
    int n=0;
	scanf("%d",&n);
    REP(i,4) T[i] = new char[5];
    REP(i,n) testCase(i);


	
	return 0;
}
