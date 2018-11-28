#include <stdio.h>
using namespace std;

int n,t,na,nb;
int aaa[200][4],bbb[4];
int res[2];

int find(int start, int& type) {
	int r = 0;
	for (int j=0;j<na+nb;j++) {
		if ((aaa[j][0] >= start) && (aaa[j][3] == 0) && ((type < 0) || (aaa[j][2] != type))) {
			r++;
			aaa[j][3] = -1;
			type = aaa[j][2];
			//printf("Find: %06d | %d | %d\n",start,j,type);
			r += find(aaa[j][1] + t,type);
			type = aaa[j][2];
			break;
		}
	}
	return r;
}

int main() {
	int a,b,c,d;
	scanf("%d\n",&n);
	for (int i=0;i<n;i++) {
		scanf("%d\n",&t);
		t *= 60;
		scanf("%d %d\n",&na,&nb);
		for (int j=0;j<na+nb;j++) {
			scanf("%d:%d %d:%d",&a,&b,&c,&d);
			aaa[j][0] = a*3600 + b*60; 
			aaa[j][1] = c*3600 + d*60;
			if (j < na) {
				aaa[j][2] = 0;
			}
			else {
				aaa[j][2] = 1;
			}
			aaa[j][3] = 0;
		}
		
		//Sorting
		for (int j=0;j<na+nb-1;j++) {
			for (int k=j+1;k<na+nb;k++) {
				if ((aaa[j][1] > aaa[k][1]) || ((aaa[j][1] == aaa[k][1]) && (aaa[j][0] > aaa[k][0]))) {
					bbb[0] = aaa[j][0];
					bbb[1] = aaa[j][1];
					bbb[2] = aaa[j][2];
					bbb[3] = aaa[j][3];
					aaa[j][0] = aaa[k][0];
					aaa[j][1] = aaa[k][1];
					aaa[j][2] = aaa[k][2];
					aaa[j][3] = aaa[k][3];
					aaa[k][0] = bbb[0];
					aaa[k][1] = bbb[1];
					aaa[k][2] = bbb[2];
					aaa[k][3] = bbb[3];
				}
			}
		}
		
		/*for (int j=0;j<na+nb;j++) {
			a = aaa[j][0] / 3600;
			b = (aaa[j][0] % 3600) / 60;
			c = aaa[j][1] / 3600;
			d = (aaa[j][1] % 3600) / 60;
			printf("%02d:%02d - %02d:%02d | %d\n",a,b,c,d,aaa[j][2]);
		}*/
		
		//Decision
		res[0] = 0;
		res[1] = 0;
		int type = -1;
		while (int r = find(0,type)) {
			res[type]++;
			type = -1;
			//printf("----------------------\n");
			//printf("%d %d\n",res[0],res[1]);
			//printf("----------------------\n");
		}
		printf("Case #%d: %d %d\n",i+1,res[0],res[1]);
	}
}
