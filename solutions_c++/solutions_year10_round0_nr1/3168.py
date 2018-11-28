#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>

#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include <errno.h>
#include <math.h>

using namespace std;

int checkLight(long long snapper, long long clicks, long long cases){

	long long value = pow(2,snapper)-1;

	if(snapper ==1 && clicks%2 == 1){
		fprintf(stdout, "Case #%i: ON\n", cases);
		return 0;
	}

	if(clicks < value){
		fprintf(stdout, "Case #%i: OFF\n", cases);
		return 0;
	}


	if(((clicks)-(value)) == 0){
		fprintf(stdout, "Case #%i: ON\n", cases);
		return 0;
	}

	if(((clicks-value) % (value+1) ) == 0){
		fprintf(stdout, "Case #%i: ON\n", cases);
	}else{
		fprintf(stdout, "Case #%i: OFF\n", cases);
	}
	
}


int main(int argc, char* argv){

	//int fd = open("hola.txt", O_WRONLY|O_CREAT,0666);
	//close(1);
	//dup(fd);

	 long long cases, snapper,clicks, ca;
	 cin >> cases;
	 ca =1;
	while(cases!=0){
		cin >> snapper;
		cin >> clicks;
		checkLight(snapper, clicks, ca);
		ca++;
		cases--;
	}


}
