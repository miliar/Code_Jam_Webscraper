#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
using namespace std;

struct node {
	int tm,pos;
};
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;
	node rob[2];

	int n;
	string str;
	int nca;

	cin>>nca;
	for(int cid=1;cid<=nca;cid++){
		cin>>n;
		int tot=0;
		
		rob[0].pos = 1;
		rob[0].tm = 0;
		rob[1].pos = 1;
		rob[1].tm = 0;

		while(n--)
		{
			cin>>str>>k;
			int side = 0;
			i = ((str == "O") ? 0 : 1);
			
			int dist = abs( k - rob[i].pos);
			int cur_time = dist + rob[i].tm  ;

			//should stay
			if( tot >=   cur_time   ){
				rob[i].tm = ++tot  ; 
			}else {
				tot = rob[i].tm = cur_time + 1 ;
			}

			rob[i].pos = k ;
		}

		printf("Case #%d: %d\n",cid,tot);
	}
}