#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;
int main(){
	FILE *out = fopen("a_out.txt", "w");
	int t = 0, c = 0;
	scanf("%d", &t);
	while(c++ < t){
		int turns = 0;
		scanf("%d", &turns);
		int orange[turns] , blue[turns];
		char ord[turns];
		fill_n(orange, turns, 0);
		fill_n(blue, turns, 0);
		char rob;
		int o_size = 0, b_size = 0;
		for(int i = 0, val = 0; i < turns; i++){
			scanf(" %c %d", &rob, &val);
			ord[i] = rob;
			if(rob == 'O')
				orange[o_size++] = val;
			else
				blue[b_size++] = val;
		}
		bool complete = false, go = (ord[0] == 'O');
		int o_curr = 1, b_curr = 1, i = 0, j = 0, steps = 0, ind = 1;
		while(!complete){
			if(go){
				if(o_size != 0){
					if(o_curr != orange[i]){
						int st = abs(orange[i] - o_curr) + 1, req = abs(blue[j] - b_curr);
						if(b_curr < blue[j])
							b_curr = (st < req)? b_curr + st : blue[j];
						else if(b_curr > blue[j])
							b_curr = (st < req)? b_curr - st : blue[j];
						o_curr = orange[i++];
						steps += st;
					}else{
						i++;
						if(b_curr < blue[j]) b_curr++;
						else if(b_curr > blue[j]) b_curr--;
						steps++;
					}
				}
				go = (ord[ind++] == 'O');
			}else{
				if(b_size != 0){
					if(b_curr != blue[j]){
						int st = abs(blue[j] - b_curr) + 1, req = abs(orange[i] - o_curr); 
						if(o_curr < orange[i])
							o_curr = (st < req)? o_curr + st : orange[i];
						else if(o_curr > orange[i])
							o_curr = (st < req)? o_curr - st : orange[i];
						b_curr = blue[j++];
						steps += st;
					}else{
						j++;
						if(o_curr < orange[i]) o_curr++;
						else if(o_curr > orange[i]) o_curr--;
						steps++;
					}
				}
				go = (ord[ind++] == 'O');
			}
			complete = (i >= o_size && j >= b_size)? true : false;
		}
		printf("Case #%d: %d\n", c, steps);
		fprintf(out, "Case #%d: %d\n", c, steps);
	}
	return 0;
}