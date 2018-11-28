#include <stdio.h>
#include <vector>
#include <string>

using namespace std;

int L, D, N;

class str{
public:
	char word[1000];
};

int Com(char *a, char *b){
	int i, cnt=0, state;
	for(i=0;i<strlen(b);i++){
		state=0;
		if(b[i]=='('){
			while(b[i]!=')'){
				if(b[i]==a[cnt]){
					state=1;
				}
				i++;
			}
			if(state==0) return 0;
			cnt++;
		}
		else if(b[i]==a[cnt]){
			cnt++;
		}
		else return 0;
	}
	return 1;
};


void main()
{
	int i, j;
	int result[5000]={0};
	FILE *file1;
	FILE *file2;
	file1 = fopen("A-large.in", "r");
	file2 = fopen("output.txt", "w");
	fscanf(file1, "%d%d%d", &L, &D, &N);
	str tmp;
	vector<str> words, a_words;

	for(i=0;i<D;i++){
		fscanf(file1, "%s", tmp.word);
		words.push_back(tmp);
	}
	for(i=0;i<N;i++){
		fscanf(file1, "%s", tmp.word);
		a_words.push_back(tmp);
		for(j=0;j<D;j++){
			result[i]+=Com(words[j].word, a_words[i].word);
		}
		fprintf(file2, "Case #%d: %d\n", i+1, result[i]);
	}
	fclose(file1);
	fclose(file2);
}
