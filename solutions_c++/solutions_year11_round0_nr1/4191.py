#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
 
using namespace std;
 
struct robot{
        int idx;
        int button;
		robot() {}
        robot(int a,int b) : idx(a),button(b){}
};
int n;
vector<robot> or,bl;

int solve(){
	int ret = 0;
	int nxt = 0;
	int i=0,j=0;
	int on = 1, bn = 1;
	int osize=or.size(),bsize=bl.size();
	while(1){
		if( nxt == n)
			break;
		ret++;
		bool flag = false;
		if( i<osize){
			if( nxt == or[i].idx ){
				if( on == or[i].button){
					flag = true;
					i++;
				}
				else if( on < or[i].button)
					on++;
				else
					on--;
			}
			else{
				if( on < or[i].button)
					on++;
				else if( on > or[i].button)
					on--;
			}
		}
		if( j<bsize){
			if( nxt == bl[j].idx){
				if(bn == bl[j].button){
					flag = true;
					j++;
				}
				else if( bn < bl[j].button)
					bn++;
				else
					bn--;
			}
			else{
				if( bn < bl[j].button)
					bn++;
				else if( bn > bl[j].button)
					bn--;
			}
		}
		if(flag)
			nxt++;
	}
	return ret;
}
int main(void){
        int t;
        scanf("%d",&t);
        for(int te=1;te<=t;te++){
                printf("Case #%d: ",te);
                scanf("%d",&n);
				or.clear();	bl.clear();
                for(int i=0;i<n;i++){
                        char a;
                        int b;
                        scanf(" %c %d",&a,&b);
                        robot temp(i,b);
						if( a == 'O')
							or.push_back(temp);
						else
							bl.push_back(temp);
                }
                printf("%d\n",solve());
        }
} 