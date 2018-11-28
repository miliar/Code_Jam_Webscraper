#include <iostream>
#include <cstdio>

using namespace std;
int r,c,d;
int mass[10][10];
int cut[10][10];

bool calc(int si, int sj, int k){
	int i,j;
	double ci, cj;
	double wi,wj;
	wi=0; wj=0;
	/*if ((si==1)&&(sj==1)&&(k==5))
		cout << "here";*/
	ci = (double)(si+si+k-1)/2;
	cj = (double)(sj+sj+k-1)/2;

	for (i=si; i<si+k; i++)
		for (j=sj; j<sj+k; j++){
			if (!(((i==si)&&(j==sj))||((i==si)&&(j==sj+k-1))||((i==si+k-1)&&(j==sj))||((i==si+k-1)&&(j==sj+k-1)))){
				wi+= (double)mass[i][j] * ((double)i-ci);
				wj+= (double)mass[i][j] * ((double)j-cj);
			}
		}

	if ((wi==0)&&(wj==0))
		return true;
	else
		return false;
}

int main(){
	int tc, tn;
	int i,j,k;
	int si,sj;
	bool can;
	int res;
	char tmp[1];

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tc;
	for (tn=0; tn<tc; tn++){
		cin >> r >> c >> d;
		for (i=0; i<r; i++)
			for (j=0; j<c; j++){
				cin >> tmp[0];
				mass[i][j]=atoi(tmp)+d;
			}

		/*for (i=0; i<r; i++){
			for (j=0; j<c; j++)
				cout << mass[i][j];
			cout << endl;
		}*/

		res = 0;
		k = min(r,c);
		for (;k>=3;k--)
			for (i=0; i+k<=r; i++)
				for (j=0; j+k<=c; j++){
					can = calc(i,j,k);
					if (can){
						res = k;
						k=0;
						i=r;
						j=c;
					}
				}

				if (res>0)
					printf("Case #%d: %d\n", tn+1, res);
				else
					printf("Case #%d: IMPOSSIBLE\n", tn+1);
	}


	return 0;
}