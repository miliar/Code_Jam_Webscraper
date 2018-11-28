#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main(void) {
	int testCases, count;
	char translate[123], answer[101], temp;
	FILE *infile= fopen("input", "r+");
	translate[97]='y';
	translate[98]='h';
	translate[99]='e';
	translate[100]='s';
	translate[101]='o';
	translate[102]='c';
	translate[103]='v';
	translate[104]='x';
	translate[105]='d';
	translate[106]='u';
	translate[107]='i';
	translate[108]='g';
	translate[109]='l';
	translate[110]='b';
	translate[111]='k';
	translate[112]='r';
	translate[113]='z';
	translate[114]='t';
	translate[115]='n';
	translate[116]='w';
	translate[117]='j';
	translate[118]='p';
	translate[119]='f';
	translate[120]='m';
	translate[121]='a';
	translate[122]='q';
	//cout<<"here"<<endl;
	fscanf(infile, "%d",&testCases);
		//cout<<"here"<< testCases<<endl;
	fscanf(infile, "%c", &temp);
		//cout<<"here"<<endl;
	for(int i=1; i<=testCases; ++i) {
		printf("Case #%d: ",i);
		count=0;
		fscanf(infile, "%c", &temp);
		for(; temp!='\n'; ++count) {
			if(temp==32) {
				printf("%c",temp);
			} else{
				printf("%c",translate[temp]);
			}
			fscanf(infile, "%c", &temp);
		}
		printf("\n");
	}
	return 0;
}
