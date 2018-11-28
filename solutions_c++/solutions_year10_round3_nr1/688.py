// 2010A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <cassert>
#include <cmath>
#include <string>
#include <set>
using namespace std;

typedef struct point{
	int x,y;
}point;
vector<point> v;
bool cmp(point& a,point& b){
	if(a.x < b.x)
		return true;
	return false;
}
int solve(){
	sort(v.begin(),v.end(),cmp);
	int ret = 0;
	for(int i=0; i<v.size(); i++){
		int tmp = v[i].y;
		for(int j=i+1; j<v.size(); j++ ){
			if(v[j].y<tmp)
				ret++;
		}
	}
	return ret;
}
int main(int argc, char *argv[])
{
    freopen("A-large (1).in","r",stdin);
 //    freopen("B-large-practice (1).in","r",stdin);
    freopen("out.txt","w",stdout);
      
    int T;

    scanf("%d",&T);
    
    int CASE = 1;
    while(T--)
    {

		  int N;
          scanf("%d\n",&N);
		  v.clear();
		  for(int i=0; i<N; i++){
			int tmp1,tmp2;
			scanf("%d %d",&tmp1,&tmp2);
			point t;
			t.x = tmp1;
			t.y = tmp2;
			v.push_back(t);
		  }
		  int res = solve();
		  
		  printf("Case #%d: %d\n",CASE,res);
		  
          CASE++;
    }

    return 0;
}
