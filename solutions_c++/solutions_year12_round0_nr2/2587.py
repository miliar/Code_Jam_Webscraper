#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))

int score[31][2] = 
{
	{-1,0},//0
        {-1,1},//1
        {2,1},//2
        {2,1},//3
        {2,2},//4
        {3,2},//5
        {3,2},//6
        {3,3},//7
        {4,3},//8
        {4,3},//9
        {4,4},//10
        {5,4},//11
        {5,4},//12
        {5,5},//13
        {6,5},//14
        {6,5},//15
        {6,6},//16
        {7,6},//17
        {7,6},//18
        {7,7},//19
        {8,7},//20
        {8,7},//21
        {8,8},//22
        {9,8},//23
        {9,8},//24
        {9,9},//25
        {10,9},//26
        {10,9},//27
        {10,10},//28
        {-1,10},//29
        {-1,10}//30
};

int main(){

	int test;
	scanf("%d",&test);
	ree(caseNo,1,test){
		int n,s,p;
		scanf("%d%d%d",&n,&s,&p);
		vector<int> scores;
		rei(con,0,n){
			int scor;
			scanf("%d",&scor);
			pb(scores,scor);
		}
		srt(scores);
		int starLeft=s;
		int ret=0;
		rei(i,0,scores.size()){
			if(starLeft){
				if(score[scores[i]][0]>=p){
					starLeft--;
					ret++;
				}else if(score[scores[i]][1]>=p){
					ret++;
				}		
			
			}else{
				if(score[scores[i]][1]>=p){
					ret++;
				}
			}	
		}
		printf("Case #%d: %d\n",caseNo,ret);
	}	
	return 0;
}




