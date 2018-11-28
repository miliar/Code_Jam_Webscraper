#include <string>
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <time.h>

#define F(i,b) for(int i=0;i<(b);i++)
#define FIAN(i,a,n) for(int i=a;i<n;i++)

using namespace std;

FILE * inputFile = fopen("D:\\Downloads\\Chrome\\B-small-attempt0.in", "r");
FILE * outputFile  = fopen("D:\\Downloads\\Chrome\\output.txt", "w");

int N,S,p,*t;
int fillArray(int N,int S,int p,int *t)
{
    int num=0, ss = S;
	F(i,N){
		if ( ((t[i]/3) >= p-1) && (t[i]%3 > 0)) {num++;}
		else if ( ((t[i]/3) + t[i]%3 > p-1)) {num++; ss--;}


		//if ((t[i]/3) + (t[i]%3) >= p) {num++;}
		//else if ((ss>0) && (1)) {num++; ss--;}	
	}
	
    return num;
}



void oneStep(void)
{
    fscanf(inputFile, "%d %d %d", &N, &S, &p);
	t = new int[N];
	F(i,N) fscanf(inputFile, "%d", t+i);
    fprintf(outputFile, "%d\n", fillArray(N,S,p,t));
}

int main()
{
    time_t timer = time(NULL);
    printf("%s\n", ctime(&timer));

    unsigned int T;
    fscanf(inputFile, "%d", &T);
    F(t,T){
        //TODO: solve here!
        fprintf(outputFile, "Case #%d: ", t+1);
        oneStep();
        timer = time(NULL);
        printf("step %d - %s\n", t, ctime(&timer));
    }

    fclose(inputFile);
    fclose(outputFile);

    timer = time(NULL);
    printf("%s\n", ctime(&timer));
   // qDebug("Time elapsed: %d ms", time1.elapsed());
    return 0;
}