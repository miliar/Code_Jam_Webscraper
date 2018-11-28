// Theme Park.cpp: определяет точку входа для консольного приложения.
//

#include <stdio.h>
int T;

struct Group{
	long amount;
	Group* next;
};

int main()
{
	char* filename = "C-small-attempt0.in";
	FILE* f = fopen(filename, "r+");
	if(f==NULL) return 1;
	FILE* out = fopen("C-small.out", "w+");
	fscanf(f, "%d", &T);
	for(int t=0; t<T; t++){
		long R, k;
		int n;
		Group* que = NULL;

		//input data
		fscanf(f, "%d %d %d", &R, &k, &n);
		Group* last;
		que = new Group;
		que->next = NULL;
		last = que;
		fscanf(f, "%d", &(que->amount));
		for(int i=1; i<n; i++){
			last->next = new Group;
			last=last->next;
			fscanf(f, "%d", &(last->amount));
		}
		last->next = que;

		long money = 0;
		for(long r = 0; r<R; r++){
			long am=0;
			Group* beg = que;
			while( ((am+que->amount)<=k) && (que!=beg || am==0) ){
				am+=que->amount;
				money+=que->amount;
				que=que->next;
			}
		}

		//output
		
		fprintf(out, "Case #%d: %d\n", t+1, money);
		

		//free memory
		last = que;
		que=que->next;
		last->next = NULL;
		while(que!=NULL){
			Group* t = que;
			que=que->next;
			delete t;
		}
	}
	fclose(out);
	fclose(f);
	return 0;
}

