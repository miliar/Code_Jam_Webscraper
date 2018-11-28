#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <map>

#define min(a,b) (((a)>(b))?(b):(a))
#define max(a,b) (((a)<(b))?(b):(a))

//#define dprintf(...) printf(__VA_ARGS__)
#define dprintf(...)

using namespace std;

int main(void) {
	int cases=0;
	int i=0,k=0;
	char null[2500];
	char null_bitmap[50];
	char trans[2500];
	char tmp1,tmp2,tmp3;
	char buffer[10240];
	char out[1024];
	int out_ind;
	char* bufp;
	map<char,int> null_stack;
	map<char,int>::iterator null_it;
	long int j=0, n=0;
	if(!scanf("%d\n",&cases)) return 1;
	dprintf("DEBUG: %d cases\n",cases);
	for(i=0;i<cases;i++) {
		if(gets(buffer)==NULL) return 2;
		n = strtol(buffer, &bufp, 10);
		dprintf("DEBUG: %ld forms\n", n);
		bzero(trans,2500*sizeof(char));
		for(j=0;j<n;j++) {
			while(isblank(*bufp)) (bufp)++;
			tmp1=(*(bufp++));
			tmp2=(*(bufp++));
			tmp3=min(tmp1,tmp2);
			tmp1=max(tmp1,tmp2);
			tmp2=tmp3;
			tmp3=(*(bufp++));
			trans[(tmp1-'A') + (tmp2-'A')*('Z'+1)]=tmp3;
			dprintf("DEBUG: %c + %c -> %c\n", tmp1, tmp2, tmp3);
		}
		n = strtol(bufp, &bufp, 10);
		dprintf("DEBUG: %ld zeros\n", n);
		bzero(null,2500*sizeof(char));
		bzero(null_bitmap,50*sizeof(char));
		null_stack.clear();
		for(j=0;j<n;j++) {
			while(isblank(*bufp)) (bufp)++;
			tmp1=(*(bufp++));
			tmp2=(*(bufp++));
			tmp3=min(tmp1,tmp2);
			tmp1=max(tmp1,tmp2)-'A';
			tmp2=tmp3-'A';
			null[tmp1 + tmp2*('Z'+1)]=1;
			null_bitmap[tmp1]=1;
			null_bitmap[tmp2]=1;
			dprintf("DEBUG: %c x %c\n", tmp1+'A', tmp2+'A');
		}
		n = strtol(bufp, &bufp, 10);
		out[0]=0;
		out_ind=0;
		dprintf("DEBUG: %ld letters\n", n);
//		for(j=0;j<n;j++) {
			while(isblank(*bufp)) (bufp)++;
			tmp1=(*(bufp++));
			while(tmp1!=0) {
				out[out_ind]=tmp1;
				dprintf("",out[out_ind+1]=0);
				dprintf("DEBUG: Got letter '%c'\n", tmp1);
				while((out_ind>0) && (tmp2=trans[max(out[out_ind],out[out_ind-1])-'A'+(min(out[out_ind],out[out_ind-1])-'A')*('Z'+1)])) {
					out[out_ind]=0;
					out_ind--;
					if(null_bitmap[out[out_ind]-'A']==1) {
						null_it=null_stack.find(out[out_ind]);
						if(null_it->second<2) {
							null_stack.erase(null_it);
						} else {
							null_it->second--;
						}
					}
					out[out_ind]=tmp2;
				}
				dprintf("DEBUG: After merging '%s'\n", out);
				if(null_bitmap[out[out_ind]-'A']==1) {
					for(null_it=null_stack.begin();null_it!=null_stack.end(); null_it++) {
						if(null[max(out[out_ind],null_it->first)-'A'+(min(out[out_ind],null_it->first)-'A')*('Z'+1)]==1) {
							out_ind=-1;
							out[0]=0;
							null_stack.clear();
						}
					}
					if(out_ind!=-1) {
						if((null_it=null_stack.find(out[out_ind]))==null_stack.end()) {
							null_stack.insert(make_pair(out[out_ind],1));
						} else {
							null_it->second++;
						}
					}
				}
				out_ind++;
				tmp1=(*(bufp++));
			}
//		}
		printf("Case #%d: [", i+1);
		if(out_ind>0) {
			printf("%c",out[0]);
		}
		for(k=1;k<out_ind;k++) {
			printf(", %c",out[k]);
		}
		printf("]\n");
	}
	return 0;
}


