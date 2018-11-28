#include <stdio.h>
#include <map>
#include <list>
#include <set>

using namespace std;

#define rows ((unsigned)4)
#define IT unsigned

char m[rows][rows],x[rows][rows],o[rows][rows];
IT dotCount;
pair<IT,IT> tpoint;
bool hast;
map<IT,pair<set<IT>,set<IT>>> xs,os;


int main(){
	FILE* input = fopen("in.txt","r"),*output = fopen("out.txt","w");
	unsigned T;
	printf("hi");
	fscanf(input,"%d",&T);
	for(unsigned t=0;t<T;t++){
		fprintf(output,"Case #%d: ",t+1);
		dotCount = 0;
		hast = false;
		xs.clear();
		os.clear();

		for(IT i=0;i<rows;i++){
			for(IT j=0;j<rows;j++){
				fscanf(input," %c ",&(m[i][j]));
				if(m[i][j] == 'X'){
					xs[i].first.insert(j);
					xs[j].second.insert(i);
				}else{
					if(m[i][j] == 'O'){
						os[i].first.insert(j);
						os[j].second.insert(i);
					}else{
						if(m[i][j] == '.'){
							dotCount++;
						} else {
							if(m[i][j] == 'T'){
								tpoint.first = i;
								tpoint.second = j;
								hast = true;
								xs[i].first.insert(j);
								xs[j].second.insert(i);
								os[i].first.insert(j);
								os[j].second.insert(i);
							}
						}
					}
				}
			}
		}
		for(IT i=0;i<rows;i++){
			if(m[i][i] == 'X'){
				xs[rows].first.insert(i);
			}else{
				if(m[i][i] == 'O'){
					os[rows].first.insert(i);
				}else{
					if(m[i][i] == 'T'){
						os[rows].first.insert(i);
						xs[rows].first.insert(i);
					}
				}
			}
			if(m[i][rows-i-1] == 'X'){
				xs[rows].second.insert(i);
			}else{
				if(m[i][rows-i-1] == 'O'){
					os[rows].second.insert(i);
				}else{
					if(m[i][rows-i-1] == 'T'){
						os[rows].second.insert(i);
						xs[rows].second.insert(i);
					}
				}
			}
		}
		if(dotCount >= 10 + hast)
			goto ans_game_not_compl;
		for(IT i=0;i<rows+1;i++){
			if(xs[i].first.size() == 4 || xs[i].second.size() == 4)
				goto ans_x_won;
			if(os[i].first.size() == 4 || os[i].second.size() == 4)
				goto ans_o_won;
		}
		if(dotCount > 0){
			goto ans_game_not_compl;
		}else{
			goto ans_draw;
		}


ans_x_won:
		fprintf(output,"X won");
		goto end;
ans_o_won:
		fprintf(output,"O won");
		goto end;
ans_draw:
		fprintf(output,"Draw");
		goto end;
ans_game_not_compl:
		fprintf(output,"Game has not completed");
		goto end;
end:
		fprintf(output,"\n");
	}
	fclose(input);
	fclose(output);
	return 0;
}