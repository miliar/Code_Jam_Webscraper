#include <stdio.h>
#include <string>

using namespace std;

string word[5010];
int L, D, N;
int count_dab(string sig)
{
	int dab = D;
	int chkAl[26]={0};
	int chkWord[5010]={0};
	int i, j, x, sw;
	int M = sig.size();
	x=0;
	sw=0;
	for (i=0;i<M;++i){
		if (sig[i]=='('){
			sw=-1;
		}
		else if (sig[i]==')'){
			sw=1;
		}
		else if (sw == -1){
			chkAl[sig[i]-'a'] = 1;
		}

		if (sw==0){
			for (j=0;j<D;++j){
				if (word[j][x] != sig[i]){
					if (chkWord[j]==0){
						--dab;
						chkWord[j] = 1;
					}
				}
			}
			++x;
		}
		if (sw==1){
			for (j=0;j<D;++j){
				if (chkAl[word[j][x]-'a']==0){
					if (chkWord[j]==0){
						--dab;
						chkWord[j] = 1;
					}
				}
			}
			for (j=0;j<26;++j) chkAl[j] = 0;
			sw=0;
			++x;
		}
	}
	return dab;
}
int main(void)
{
	int i;

	FILE *fin = fopen("input.txt", "r");
	fscanf(fin, "%d %d %d", &L, &D, &N);
	char tmp[20];
	fgets(tmp, 20, fin);
	for (i=0;i<D;++i){
		fgets(tmp, 20, fin);
		tmp[L] = 0;
		word[i] = tmp;
	}

	FILE *fout= fopen("output.txt", "w");
	string sig;
	char tmpsig[500];
	for (i=1;i<=N;++i){
		fgets(tmpsig,500,fin);
		sig = tmpsig;
		sig[sig.size()-1] = 0;
		fprintf(fout, "Case #%d: %d\n", i, count_dab(sig));
	}
	fclose(fin);
	fclose(fout);
	return 0;
}