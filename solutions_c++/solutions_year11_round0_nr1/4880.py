#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

//int btn[128];		//botton
char clr[128];	//color
//int blue[128],ora[128];
vector<int> blue,ora;

int main(){
	FILE *fp = fopen("output1.txt","w");
	
	int T,N;
	
	scanf("%d",&T);
	for(int t = 0;t < T; ++t){
		scanf("%d",&N);
		//memset(blue,0,sizeof(int) * 128);
		//memset(ora,0,sizeof(int) * 128);
		blue.clear();
		ora.clear();
		int start = 0;
		
		for(int i = 0; i < N; ++i){
			char c;
			int temp;
			cin >> c >> temp;
			//printf("%c %d\n",c,temp);
			if(c == 'O'){
				ora.push_back(temp);
				
			}
			else{
				blue.push_back(temp);
				
			}
			clr[i] = c;
		}
		
		int ret = 0;
		int cur = start;
		int b_pre, o_pre, b_cur, o_cur ;
		b_pre = o_pre = 1;
		b_cur = o_cur = 0;
		
		
		for(int i = 0; i < N; ++i){
			
			if(clr[i] == 'B'){
				
				int dist = abs(b_pre - blue[b_cur]);
				ret += dist + 1;		//one second for pressing button
				
				//cout << ret << endl;
				
				if(o_cur != ora.size()){
					int ddist = abs(o_pre - ora[o_cur]);
					if(ddist < dist + 1)
						o_pre = ora[o_cur];
					else{
						if(ora[o_cur] > o_pre)
							o_pre += dist + 1;
						else
							o_pre -= dist + 1;																	
					}
				}
				
				b_pre = blue[b_cur];	
				b_cur++;						
			}
			
			//orange
			else{
				int dist = abs(o_pre - ora[o_cur]);
				ret += dist + 1;		//one second for pressing button
				
				//cout << ret << endl;
				
				
				if(b_cur != blue.size()){
					int ddist = abs(b_pre - blue[b_cur]);
					//cout << b_pre << ' ' << blue[b_cur] << endl;
					if(ddist < dist + 1)
						b_pre = blue[b_cur];
					else{
						if(blue[b_cur] > b_pre)
							b_pre += dist + 1;
						else
							b_pre -= dist + 1;																	
					}
				}
				
				o_pre = ora[o_cur];	
				o_cur++;				
				
			}
		}
		
		fprintf(fp,"Case #%d: %d\n",t + 1,ret);
	}
	
	
	
	
	return 0;
}