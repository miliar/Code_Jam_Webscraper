//#include <stdio.h>
//#include <stdlib.h>
//#include <iostream>
//#include <string>
//#include <algorithm>
//#include <math.h>
//
//using namespace std;
//
//int N;
//int pr[1000005];
//int num[1000005];
//int gr[1000005];
//
//int main(){
//	freopen("in.txt","rt",stdin);
//	freopen("out.txt","wt",stdout);
//	scanf("%d",&N);
//	for (int po = 0; po < N; po++){
//		int A;
//		int B;
//		int P;
//		cin >> A;
//		cin >> B;
//		cin >> P;
//
//		int counter = 0;
//		for (int p = P; p < B; p++){
//			if ((p % 2) == 0 && p != 2) continue;
//			int t = sqrt((double)p)+4;
//			bool prime = true;
//			for (int l = 3; l < t && l < p; l += 2){
//				if ((p % l) == 0) {
//					prime = false;
//					break;
//				}
//			}
//			if (!prime) continue;
//			pr[counter] = p;
//			gr[counter] = counter;
//			int q = (A/p);
//			int w = (B/p);
//			if ((A%p) == 0) q--;
//			num[counter] = (w-q);
//			counter++;
//		}
//		for (int i = 0; i < counter; i++){
//			for (int j = i+1; j < counter; j++){
//				if (gr[i] == gr[j]) continue;
//				int pp = pr[i]*pr[j];
//				int q = (A/pp);
//				int w = (B/pp);
//				if ((A%pp) == 0) q--;
//				if ((w-q) > 0){
//					int o = gr[j];
//					for (int k = 0; k < counter; k++){
//						if (gr[k] == gr[j]){
//							num[gr[i]] += num[gr[k]];
//							num[gr[k]] = 0;
//							gr[k] = gr[i];
//						}
//					}
//				}
//			}
//		}
//		int total = B-A+1;
//		for (int i = 0; i < counter; i++){
//			if (num[i] == 0) continue;
//			total -= num[i] - 1;
//		}
//		printf("Case #%d: %d\n", po+1, total);
//	}
//	return 0;
//}
//
//
//
//
////#include <stdio.h>
////#include <stdlib.h>
////#include <iostream>
////#include <string>
////#include <algorithm>
////#include <math.h>
////
////using namespace std;
////
////int N;
////__int64 a[1000005];
////
////int main(){
////	freopen("in.txt","rt",stdin);
////	freopen("out.txt","wt",stdout);
////	scanf("%d",&N);
////	for (int po = 0; po < N; po++){
////		__int64 A;
////		__int64 B;
////		__int64 P;
////		cin >> A;
////		cin >> B;
////		cin >> P;
////
////		for (__int64 i = A; i <= B; i++){
////			a[i-A] = i;
////		}
////
////		for (__int64 p = P; p < B; p++){
////			if ((p % 2) == 0 && p != 2) continue;
////			int t = sqrt((long double)p)+4;
////			bool prime = true;
////			for (int l = 3; l < t && l < p; l += 2){
////				if ((p % l) == 0) {
////					prime = false;
////					break;
////				}
////			}
////			if (!prime) continue;
////			__int64 g = (A / p) * p;
////			while (g < A) g += p;
////			for ( ; g <= B; g += p){
////				if (a[g-A] != g){
////					__int64 old = a[g-A];
////					for (__int64 k = A; k <= B; k++){
////						if (a[k-A] == old){
////							a[k-A] == p;
////						}
////					}
////				}
////				a[g-A] = p;
////			}
////		}
////		int res = 0;
////		for (__int64 f = A; f <= B; f++){
////			if (a[f-A] == f) res++;
////		}
////
////		printf("Case #%d: %d\n", po+1, res);
////	}
////	return 0;
////}
////#include <stdio.h>
////#include <stdlib.h>
////#include <iostream>
////#include <string>
////#include <algorithm>
////#include <math.h>
////
////using namespace std;
////
////int N;
////__int64 a[1000005];
////
////
////
////int main(){
////	freopen("in.txt","rt",stdin);
////	freopen("out.txt","wt",stdout);
////	scanf("%d",&N);
////	for (int po = 0; po < N; po++){
////		__int64 A;
////		__int64 B;
////		__int64 P;
////		cin >> A;
////		cin >> B;
////		cin >> P;
////
////		for (__int64 i = A; i <= B; i++){
////			a[i-A] = i;
////		}
////		int counter = 0;
////
////		for (__int64 p = P; p < B; p++){
////			if ((p % 2) == 0 && p != 2) continue;
////			int t = sqrt((double)p)+4;
////			bool prime = true;
////			for (int l = 3; l < t && l < p; l += 2){
////				if ((p % l) == 0) {
////					prime = false;
////					break;
////				}
////			}
////			if (!prime) continue;
////			counter++;
////		}
////		printf("Case #%d: %d\n", po+1, counter);
////	}
////	return 0;
////}
////
////
////
////
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

int N;
int a[1000005];

int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	scanf("%d",&N);
	for (int po = 0; po < N; po++){
		int A;
		int B;
		int P;
		cin >> A;
		cin >> B;
		cin >> P;

		for (int i = A; i <= B; i++){
			a[i-A] = i;
		}

		for (int p = P; p < B; p++){
			if ((p % 2) == 0 && p != 2) continue;
			int t = sqrt((long double)p)+4;
			bool prime = true;
			for (int l = 3; l < t && l < p; l += 2){
				if ((p % l) == 0) {
					prime = false;
					break;
				}
			}
			if (!prime) continue;
			int g = (A / p) * p;
			while (g < A) g += p;
			for ( ; g <= B; g += p){
				if (a[g-A] != g){
					int old = a[g-A];
					for (int k = A; k <= B; k++){
						if (a[k-A] == old){
							a[k-A] = p;
						}
					}
				}
				a[g-A] = p;
			}
		}
		int res = 0;
		for (int i = A; i <= B; i++){
			if (a[i-A] < 0) continue;
			res++;
			int k = a[i-A];
			for (int j = A; j <= B; j++){
				if (a[j-A] == k){
					a[j-A] = -1;
				}
			}
		}

		printf("Case #%d: %d\n", po+1, res);
	}
	return 0;
}
