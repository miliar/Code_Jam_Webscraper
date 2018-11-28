#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <bitset>
using namespace std;

int cmp(const void *a, const void *b) {
	if ((*(long *)a) < (*(long *)b)) {
		return -1;
	} else if ((*(long *)a) > (*(long *)b)) {
		return 1;
	} else return 0;
}

long jumlah(long angka1, long angka2) {
	long hasil = 0;
	bitset<32> temp1 = angka1;
	bitset<32> temp2 = angka2;
	bitset<32> tempH = 0;
	for (int z=0; z<32; z++) {
		if (temp1[z] == 1 && temp2[z] == 0) {
			tempH[z] = 1;
		} else if (temp1[z] == 0 && temp2[z] == 1) {
			tempH[z] = 1;
		} else if (temp1[z] == 0 && temp2[z] == 0) {
			tempH[z] = 0;
		} else if (temp1[z] == 1 && temp2[z] == 1) {
			tempH[z] = 0;
		}
	}
	for (int z=31; z>=0; z--) {
		hasil = hasil * 2 + tempH[z];
	}	
	return hasil;
}

int main() {	
	int T = 0;
	scanf("%d\n",&T);
	for (int i=0; i<T; i++) {
		int N = 0;
		scanf("%d\n",&N);

		long data[1001];
		for (int j=0; j<1001; j++) {
			data[j] = 0;
		}

		for (int j=0; j<N; j++) {
			scanf("%ld",&data[j]);
		}
		scanf("\n");
		qsort(data,N,sizeof(long),cmp);

		long totalAsli = 0;
		for (int j=0; j<N; j++) {
			totalAsli += data[j];
		}
		long setengahAsli = totalAsli / 2;
		
		bool keluar = false;
		long tempTotal = jumlah(0, data[0]);
		long tempTotalAsli = totalAsli-data[0];
		int pos=1;
		bool nangis = false;
		while (!keluar) {
			long tempTotalKo = 0;
			for (int j=pos; j<N;j++) {
				tempTotalKo = jumlah(tempTotalKo,data[j]);
			}
			if (tempTotal == tempTotalKo && tempTotalKo != 0) {
				keluar = true;
				if (tempTotalAsli < setengahAsli) {
					nangis = true;
				}
			} else {
				tempTotal = jumlah(tempTotal, data[pos]);
				tempTotalAsli -= data[pos];
			}
			pos++;
			if (pos == N && !keluar) {
				keluar = true;
				nangis = true;
			}
		}
		if (nangis) {
			printf("Case #%d: NO\n",i+1);
		} else {
			printf("Case #%d: %ld\n",i+1,tempTotalAsli);
		}
	}
	//while (scanf("%d %d %d\n",&d1,&d2,&d3) != EOF) {
		//jawaban
		//printf("Case #%d: %d\n",d1,d2);
	//}
	//getch(); 
	return 0;
}