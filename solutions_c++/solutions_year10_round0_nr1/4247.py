

#include <stdio.h>
#include <string>
#include <vector>

using namespace std;
//global
FILE *fout;

int cases;

//each
struct snapper{
	bool isON;
	bool hasPower;
};
struct tcase{
	int N,K;
	snapper ps[31];
} ;

struct tcase ts[10000];


void readFile(char *filename){
	FILE *fp = fopen(filename,"r");
	//cases
	fscanf(fp,"%d\n",&cases);
	//each case
	for (int i = 0 ; i< cases ;i ++){
		fscanf(fp,"%d %d\n",&ts[i].N,&ts[i].K);
	}
	fclose(fp);
}
void handle(int t){
	struct tcase *tc = &ts[t];
	for (int i = 0 ; i< tc->N;i++){
		tc->ps[i].hasPower = false;
		tc->ps[i].isON = false;
	}

	for (int i = 0 ; i< tc->K;i++){
		tc->ps[0].hasPower = !tc->ps[0].hasPower;
		tc->ps[0].isON = !tc->ps[0].isON;
		for (int j = 1;j<=tc->N;j++){
			if (tc->ps[0].hasPower){
				//somebody will power
				tc->ps[j].hasPower = tc->ps[j-1].isON && tc->ps[j-1].hasPower;
				if (!tc->ps[j].hasPower){
					break;
				}
			}else{
				//everybody lose power
				//has switch case
				if (tc->ps[j].hasPower){
					//do switch
					tc->ps[j].hasPower = false;
					tc->ps[j].isON = !tc->ps[j].isON;
				}
			}
		}
	}
	//test light
	if (tc->ps[tc->N-1].hasPower && tc->ps[tc->N-1].isON){
		fprintf(fout,"Case #%d: %s\n",t+1,"ON");
	}else{
		fprintf(fout,"Case #%d: %s\n",t+1,"OFF");
	}

}
void func1(){
	//readFile("a.txt");
	readFile("A-small-attempt4.in");
	//readFile("A-large-practice.in");

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