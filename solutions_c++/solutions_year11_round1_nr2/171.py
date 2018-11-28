#include<sys/types.h>
#include<dirent.h>

#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define EPS 1e-6
#define PI 3.14159265358979323846

using namespace std;

int nword, norder;

int dic[100][10];
int len[100];

int order[100][26];
char term[26];

int has_letter[100][26];
int nletter[100];

int match[100][100];

int main()
{

	int ncase;
	scanf("%d", &ncase);

	for(int caseidx = 1; caseidx <= ncase; caseidx++){

		memset(has_letter, 0, sizeof(has_letter));
		memset(nletter, 0, sizeof(nletter));

		scanf("%d %d", &nword, &norder);

		for(int i = 0; i < nword; i++){
			scanf("%s", term);

			len[i] = strlen(term);
			for(int j = 0; j < len[i]; j++){
				dic[i][j] = term[j] - 'a';

				has_letter[i][dic[i][j]] = 1;
			}

			for(int j = 0; j < 26; j++){
				nletter[i] += has_letter[i][j];
			}
		}

		/*
		for(int i = 0; i < nword; i++){
			cout << "len = " << len[i] << endl;
			for(int j = 0; j < len[i]; j++){
				cout << dic[i][j] << " " ;
			}
			cout << endl;
		}
		*/

		printf("Case #%d:", caseidx);


		for(int i = 0; i < norder; i++){
			scanf("%s", term);
			for(int j = 0; j < 26; j++) order[i][j] = term[j] - 'a';

			for(int k = 0; k < nword; k++){
				for(int j = k + 1; j < nword; j++){
					if(len[k] - len[j])	match[j][k] = match[k][j] = -1;
					else	match[j][k] = match[k][j] = 0;
				}
			}


			for(int j = 0; j < 26; j++){

				int cur = order[i][j];

				for(int k = 0; k < nword; k++){
					for(int m = k + 1; m < nword; m++){
						if(match[k][m] < j)	continue;

						if(has_letter[k][cur] - has_letter[m][cur])	continue;
						if(!(has_letter[k][cur] + has_letter[m][cur])){
							match[k][m]++;
							match[m][k]++;
							continue;
						}

						int good = 1;
						for(int n = 0; good && n < len[k]; n++){
							if(dic[m][n] == cur && (dic[k][n] - cur)) good = 0;
							if(dic[k][n] == cur && (dic[m][n] - cur)) good = 0;
						}
						match[k][m] += good;
						match[m][k] += good;

					}
				}
			}


			int ret = 0;
			int ma = 0;

			for(int j = 0; j < nword; j++){

				int rem = nletter[j];
				int ans = 0;

				for(int k = 0; k < 26 && rem; k++){

					int cur = order[i][k];

					if(has_letter[j][cur]){
						rem--;
						continue;
					}

					int lose = 0;
					for(int m = 0; !lose && m < nword; m++){
						if(m == j)	continue;
						if(has_letter[m][cur] && match[m][j] >= k)
							lose = 1;

					}

					ans += lose;
				}
				if(ans > ma){
					ret = j;
					ma = ans;
				}
			}//for each test word

			printf(" ");
			for(int j = 0; j < len[ret]; j++){
				printf("%c", dic[ret][j] + 'a');
			}
			

		}// for each order
		printf("\n");
		/*
		for(int i = 0; i < norder; i++){
			for(int j = 0; j < 26; j++){
				cout << order[i][j] << " ";
			}
			cout << endl;
		}
		*/

	}
	
	return 0;
}

// vi: ts=2 sw=2
