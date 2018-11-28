

#include <stdio.h>
#include <string>
#include <vector>

using namespace std;
//global
FILE *fout;

int cases;

//each

struct tcase{
	int R,K,N;
	unsigned int a[1000];
} ;

struct tcase ts[50];

void handle(int t){
	struct tcase *tc = &ts[t];
	unsigned int start = 0;
	unsigned int end = 0;
	unsigned int *arr = tc->a;
	unsigned int r = tc->R;
	unsigned int n = tc->N;
	unsigned int k = tc->K;
	unsigned int sum = 0;
	unsigned long income = 0;
	for (unsigned int i = 0;i< r;++i){
		while (1){
			sum +=arr[end];
			if (sum <=k){
				++end;
				if (end == n){
					end = 0;
				}
				if (end == start){
					break;
				}
			}else{
				sum -=arr[end];
				break;
			}		
		}

		income += sum;
		sum = 0;
		start = end;
	}
	fprintf(fout,"Case #%d: %.ld\n",t+1,income);
	fflush(fout);
}
void readFile(char *filename){
	FILE *fp = fopen(filename,"r");
	//cases
	fscanf(fp,"%d\n",&cases);
	//each case
	for (int i = 0 ; i< cases ;i++){
		fscanf(fp,"%d %d %d\n",&ts[i].R,&ts[i].K,&ts[i].N);
		for (int j = 0 ; j < ts[i].N;j++){
			fscanf(fp,"%d",&ts[i].a[j]);
		}
	}
	fclose(fp);
}

void func1(){
	//readFile("a.txt");
	readFile("C-small-attempt0.in");
	//readFile("A-large.in");

	fout = fopen("out.txt","w");

	for (int i = 0 ;i<cases;i++){
		handle(i);
	}
	fflush(fout);
	fclose(fout);
}

int main(int argc, char* argv[])
{
	func1();
}