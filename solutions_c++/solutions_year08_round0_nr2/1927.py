#include <iostream>

using namespace std;

int fromAtoB[1441] = {0};
int fromBtoA[1441] = {0};
int atA[1441] = {0};
int atB[1441] = {0};

int fromAS[20] = {0};
int fromAR[20] = {0};

int fromBS[20] = {0};
int fromBR[20] = {0};

int main()
{
	int i,j,k,l,m,n;
	int N,NA,NB,T;
	char c;
	cin >> N;
	for(l = 0;l < N;l++) {
		for(i = 0;i < 1441;i++) {
			atA[i] = 0;
			atB[i] = 0;
		}

		cin >> T;
		cin >> NA >> NB;
		for(j = 0;j < NA;j++) {
			cin >> m >> c >> n;
			fromAS[j] = m * 60 + n + 1;
			cin >> m >> c >> n;
			fromAR[j] = m * 60 + n + 1;
		}
		for(j = 0;j < NB;j++) {
			cin >> m >> c >> n;
			fromBS[j] = m * 60 + n + 1;
			cin >> m >> c >> n;
			fromBR[j] = m * 60 + n + 1;
		}

		int minA = 100000;
		int minB = 100000;
		for(i = 1; i < 1441;i++) {
			atA[i] += atA[i - 1];
			atB[i] += atB[i - 1];
			for(j = 0;j < NA;j++) {
				if(fromAS[j] == i) {
					atA[i]--;
				}
				if(fromAR[j] == i) {
					atB[i+T]++;
				}
			}
			for(j = 0;j < NB;j++) {
				if(fromBS[j] == i) {
					atB[i]--;
				}
				if(fromBR[j] == i) {
					atA[i+T]++;
				}
			}
			if(atA[i] < minA)
				minA = atA[i];
			if(atB[i] < minB)
				minB = atB[i];
		}

		cout << "Case #" << (l + 1) << ": " << (-minA) << " " << (-minB) << endl;
	}
}
