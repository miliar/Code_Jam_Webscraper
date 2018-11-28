#include <stdio.h>

void sort(int list[], int from, int to){
	if (from < to){
		int temp[to-from+1],a=from,b=(from+to)/2+1,c=0;
		sort(list,a,b-1);
		sort(list,b,to);
		while(c<to-from+1)temp[c++]=list[list[a]>list[b]?(a>(from+to)/2?b++:a++):(b>to?a++:b++)];
		for(c=0;c<=to-from;c++) list[from+c] = temp[c];
	}
}

int main(){
	FILE* input, *output;
	input = fopen("b.in", "r");
	output = fopen("b.out", "w+");
	
	int t;
	fscanf(input, "%d", &t);
	for(int u = 0; u < t; u++){
		int l, time, n, c;
		fscanf(input, "%d", &l);
		fscanf(input, "%d", &time);
		fscanf(input, "%d", &n);
		fscanf(input, "%d", &c);
		int a[c], edge[n];
		for(int i = 0; i < c; i++){
			fscanf(input, "%d", &a[i]);
		}
		int ac = time;
		for(int i = 0; i < n; i++){
			edge[i] = a[i%c] * 2;
		}
		for(int i = 0; i < n; i++){
			if (edge[i] <= ac){
				ac -= edge[i];
				edge[i] = 0;
			}else{
				edge[i] -= ac;
				break;
			}
		}

		
		sort(edge, 0, n - 1);
		
		for(int i = 0; i < l; i++){
			edge[i] /= 2;
		}
		ac = 0;
		for(int i = 0; i < n; i++){
			ac += edge[i];
		}
		fprintf(output, "Case #%d: %d\n", u + 1, ac+time);
	}
	
	fclose(input);
	fclose(output);
	return 0;
}
