#include <cstdio>

int arr[1001][2];

int abs(int n){
	if(n < 0)return -n;
	return n;
}

void newprob(int tt){
	int n;
	scanf("%d",&n);
	int posa = 1;
	int posb = 1;
	int time = 0;
	int pa = 0;
	int pb = 0;
	for(int i=0;i<n;i++){
		int num;
		char str[2];
		scanf("%s %d",str,&num);
		arr[i][0] = str[0];
		arr[i][1] = num;
	}
	while(pa < n){
		if(arr[pa][0] == 'O')break;
		pa++;
	}
	while(pb < n){
		if(arr[pb][0] == 'B')break;
		pb++;
	}
	for(int i=0;i<n;i++){
		int aa = arr[pa][1];
		int bb = arr[pb][1];
		if(arr[i][0] == 'O'){
			int diff = abs(arr[i][1] - posa) + 1;
			time += diff;
			//printf("go %d\n",diff);
			posa = arr[i][1];
			if(posb < bb){
				if(posb + diff > bb){
					posb = bb;
				}else{
					posb += diff;
				}
			}else{
				if(posb - diff < bb){
					posb = bb;
				}else{
					posb -= diff;
				}
			}
			pa++;
			while(pa < n){
				if(arr[pa][0] == 'O')break;
				pa++;
			}
		}else{
			int diff = abs(arr[i][1] - posb) + 1;
			//printf("go %d\n",diff);
			time += diff;
			posb = arr[i][1];
			if(posa < aa){
				if(posa + diff > aa){
					posa = aa;
				}else{
					posa += diff;
				}
			}else{
				if(posa - diff < aa){
					posa = aa;
				}else{
					posa -= diff;
				}
			}
			pb++;
			while(pb < n){
				if(arr[pb][0] == 'B')break;
				pb++;
			}
		}
	}
	printf("Case #%d: %d\n",tt,time);
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)newprob(i+1);
	return 0;
}

/*
20
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
8 O 15 B 16 B 36 O 36 B 19 O 53 B 64 O 97
10 O 2 B 3 O 5 B 6 O 2 B 9 O 1 B 8 O 6 B 1
10 B 100 B 1 B 100 B 1 B 100 B 1 B 100 B 1 B 100 B 1
8 O 45 B 45 O 80 B 80 B 42 O 39 B 85 O 81
10 B 11 O 12 O 37 B 39 B 6 O 2 O 40 B 47 B 91 O 88
9 B 73 O 61 B 22 O 41 O 15 B 46 O 33 B 92 O 71
8 O 28 B 30 B 40 O 41 B 12 O 14 O 48 B 48
1 B 1
10 B 20 O 20 O 57 B 58 B 81 O 31 B 51 O 3 O 16 B 67
10 O 1 B 1 O 1 O 1 O 1 O 1 B 1 O 1 O 1 O 1
6 B 14 O 16 O 43 B 43 O 63 B 24
8 B 23 O 22 O 30 O 15 O 67 O 88 B 95 O 99
10 B 42 O 42 B 21 O 20 B 34 O 7 O 40 B 71 B 88 O 21
10 O 29 B 31 O 15 B 44 O 58 B 88 B 68 O 82 B 22 O 37
10 B 31 O 31 O 70 B 71 O 41 B 41 O 81 B 81 B 41 O 38
8 B 32 O 98 O 74 O 54 B 20 O 90 B 94 O 17
10 O 43 B 15 O 35 B 10 O 35 B 95 O 15 B 9 O 2 B 64
*/
