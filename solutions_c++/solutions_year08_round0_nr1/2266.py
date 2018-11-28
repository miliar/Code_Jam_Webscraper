#include <stdio.h>
#include <string>
#include <map>
#define NENGINES 105
#define NQUERIES 1005
using namespace std;
char eng[NENGINES][105];
char qry[NQUERIES][105];

int main (void) {
	FILE * fi = fopen("A.in","rt");
	FILE * fo = fopen("A.out","wt");

	long n;
	fscanf(fi,"%ld",&n);
	for (long i=1; i<=n; i++) {
		long s;
		map<string,long> mel;
		fscanf(fi,"%ld\n",&s);
		for (long j=0; j<s; j++) {
			fgets(eng[j],105,fi);
			eng[j][strlen(eng[j])-1]='\0';
//			fscanf(fi,"%s\n",eng[j]);
//			fprintf(stderr,"READ: engine %s\n",eng[j]);
			string p=eng[j];
			mel[p]=j;
		};
		long q;
		fscanf(fi,"%ld\n",&q);
		for (long j=0; j<q; j++) {
			fgets(qry[j],105,fi);
			qry[j][strlen(qry[j])-1]='\0';
//			fscanf(fi,"%s\n",qry[j]);
		}
		long switches=0;
		char act[NENGINES]; long used=0;
		memset(act,0,sizeof(act));
		for (long j=0; j<q; j++) {
			if (!act[mel[qry[j]]]) {
				act[mel[qry[j]]]=1;
//				fprintf(stderr,"new search engine (%s) unusable because of %ld\n",qry[j],j);
				used++;
				if (used==s) {
//					fprintf(stderr,"group until %ld exclusively will be searched by %s\n",j,qry[j]);
					switches++;
					memset(act,0,sizeof(act));
					used=1;
					act[mel[qry[j]]]=1;
				}

			} //else fprintf(stderr,"engine (%s) already unusable, reencountered at %ld\n",qry[j],j);
		}
//		fprintf(stderr,"last group will be searched by whatever was not used\n");
		fprintf(fo,"Case #%ld: %ld\n",i,switches);
	}

	fclose(fi); fclose(fo);
	return 0;
}
