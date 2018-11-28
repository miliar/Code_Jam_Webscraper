#include<iostream>
using namespace std;

char sm[10][10];
int cc;
bool res;

bool check(int sx, int sy, int spx, int spy){
	bool de = false, tp = false;
	
	for(int fh1=0;fh1<4;fh1++){
		if(sm[sx][sy]=='T');
		else if(sm[sx][sy]=='.')
			return 0;
		else{
			if(de&&tp!=(sm[sx][sy]=='O'))
				return 0;
			de = 1;
			tp = (sm[sx][sy]=='O');
		}
		sx += spx;
		sy += spy;
	}
	res = tp;
	return 1;
}
int t,h1,h2;
int main(){
	freopen("A-large (1).in","r",stdin);
	freopen("a_ans_large.txt","w",stdout);
	cin>>t;
	while(t--){
		for(h1=0;h1<4;h1++){
			scanf("%s",sm[h1]);
		}
		
		printf("Case #%d: ",++cc);
		
		if(check(0,0,1,1)){
			printf(res?"O won\n":"X won\n");
			continue;
		}
		if(check(0,3,1,-1)){
			printf(res?"O won\n":"X won\n");
			continue;
		}
		
		bool draw = true;
		
		for(h1=0;h1<4;h1++){
			if(check(h1,0,0,1)||check(0,h1,1,0)){
				printf(res?"O won\n":"X won\n");
				draw = false;
				break;
			}
		}
		
		if(draw){
			
			for(h1=0;h1<4;h1++)
				for(h2=0;h2<4;h2++){
					if(sm[h1][h2]=='.'){
						draw = false;
					}
				}
			printf(draw?"Draw\n":"Game has not completed\n");
		}
		
	}
	//system("pause");
}
