
#include <stdio.h>

int main(){
	FILE *in = fopen("input.txt", "rt");
	FILE *out = fopen("output.txt", "wt");
	int t, c=1;
	fscanf(in, "%d", &t);
	while(t--){
		fprintf(out, "Case #%d: ", c++);
		int n, s, p;
		int res=0;
		fscanf(in, "%d %d %d", &n, &s, &p);
		int **ti = new int*[n];
		for(int i=0; i<n; i++){
			ti[i] = new int[4];
			fscanf(in, "%d", &ti[i][0]);
		
			ti[i][1]=ti[i][2]=ti[i][3]=ti[i][0]/3;
			ti[i][0]-=(ti[i][0]/3)*3;
			if(ti[i][0]==1) ti[i][1]++;
			else if(ti[i][0]==2){
				ti[i][1]++;
				ti[i][2]++;
			}
		}
		for(int i=0; i<n; i++){
			
			if(s){
				if(ti[i][0]==0 && ti[i][1]!=10 && ti[i][3]!=0 && ti[i][1]==p-1){
					ti[i][1]++;
					ti[i][3]--;
					s--;
				}
				else if(ti[i][0]==1 && ti[i][2]!=10 && ti[i][3]!=0 && ti[i][1]==p-1){
					ti[i][2]++;
					ti[i][3]--;
					s--;
				}
				else if(ti[i][0]==2 && ti[i][1]!=10 && ti[i][2]!=0 && ti[i][1]==p-1){
					ti[i][1]++;
					ti[i][2]--;
					s--;
				}
			}
			if(ti[i][1]>=p) res++;
		}
		for(int i=0; i<n; i++){
			
			if(s){
				if(ti[i][0]==0 && ti[i][1]!=10 && ti[i][3]!=0 && ti[i][1]>=p-1){
					ti[i][1]++;
					ti[i][3]--;
					s--;
				}
				else if(ti[i][0]==1 && ti[i][2]!=10 && ti[i][3]!=0 && ti[i][1]>=p-1){
					ti[i][2]++;
					ti[i][3]--;
					s--;
				}
				else if(ti[i][0]==2 && ti[i][1]!=10 && ti[i][2]!=0 && ti[i][1]>=p-1){
					ti[i][1]++;
					ti[i][2]--;
					s--;
				}
			}
			if(ti[i][1]>=p) res++;
		}

		for(int i=0; i<n; i++){
			if(s){
				if(ti[i][0]==0 && ti[i][1]!=10 && ti[i][3]!=0){
					ti[i][1]++;
					ti[i][3]--;
					s--;
				}
				else if(ti[i][0]==1 && ti[i][2]!=10 && ti[i][3]!=0){
					ti[i][2]++;
					ti[i][3]--;
					s--;
				}
				else if(ti[i][0]==2 && ti[i][1]!=10 && ti[i][2]!=0){
					ti[i][1]++;
					ti[i][2]--;
					s--;
				}
			}
		}
			

		fprintf(out, "%d\n", res/2);
	}
	return 0;
}