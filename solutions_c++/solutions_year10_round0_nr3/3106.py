#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>

using namespace std;

void solve(int caseindex, unsigned long r, unsigned long k, unsigned int n, unsigned long g[]) {
	int startgi = 0;
	unsigned long euros = 0;
	for(int i =0; i< r;i++) {
		int passcount= 0;
		int initg = startgi;
		while(( passcount + g[startgi]) <= k) {
			passcount += g[startgi];
			if(startgi == (n -1)) {
				startgi =0;
			}	
			else 	
				startgi++;
			if(startgi == initg)
				break;

		}
		euros += passcount; 
	}
	cout <<	"Case #" << caseindex <<": "<<euros<<endl;
}


int main(int argc,char **argv) {

	FILE *fp = fopen(argv[1],"r");
	int count,i,j;
    	fscanf(fp,"%d",&count);	
/*	int start = atoi(argv[2]);
	int uppto = atoi(argv[3]);

	for(i =start; i < start +uppto ; i++) {
*/
	for(i=1 ; i <= count; i++) {
		unsigned long r,k,n;
		fscanf(fp,"%ld%ld%ld",&r,&k,&n);
		unsigned long groups[n];
		for(j =0; j < n; j++) {
			fscanf(fp,"%ld",&groups[j]);
		}
        	solve(i,r,k,n ,groups);
	}
	
}
