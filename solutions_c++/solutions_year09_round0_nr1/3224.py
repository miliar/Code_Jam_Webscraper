#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
using namespace std;

#define MAXLENGTH	10
#define MAXLINES	25
#define MAXCASES	10

struct sCase
{
	char set[30];
	int pos;
};

struct sWord
{
	char* word;
	int checked;
	bool b;
};

void main(int argc, char* argv[])
{
	int L, D, N, K, iTotal, d;
	char *posl, *posr;
	char* szBase, *szWord, *szSub;
	char szCase[1024];
	sCase* pCase;
	sWord* pWord;
	vector<sCase*> vCase;
	vector<char*> vAll;
	vector<sWord*> vSubset;

	//Open files
	FILE* fpInput = fopen(argv[1], "rb");
	FILE* fpOutput = fopen(argv[2], "wb");
	
	//Read variables
	fscanf(fpInput, "%d %d %d\n", &L, &D, &N);

	//Populate words table
	for(int i=0;i<D;i++)
	{
		szWord = (char*)malloc(sizeof(char)*(MAXLENGTH+5));
		fscanf(fpInput, "%s", szWord);
		vAll.push_back(szWord);
	}

	//Process test cases
	for(int j=0;j<N;j++)
	{
		vSubset.clear();
		vCase.clear();

		fscanf(fpInput, "%s\n", szCase);
		szBase = (char*) malloc(sizeof(char)*MAXLENGTH+5);
		for(int a=0, b=0;a<L;a++) {
			if(szCase[b] == '(') {
				szBase[a] = '0';
				pCase = new sCase;
				pCase->pos = a;
				posl=szCase+b;
				posr=strchr(posl, ')');
				strncpy(pCase->set, posl+1, posr-posl-1);
				pCase->set[posr-posl-1] = '\0';
				b+=(int)(posr-posl+1);
				vCase.push_back(pCase);
			}
			else {
				szBase[a] = szCase[b];
				b++;
			}
		}
		szBase[L] = '\0';


		bool b1;
		vector<char*>::iterator it1;
		for(it1=vAll.begin();it1!=vAll.end();it1++) {
			b1 = false;
			for(int a=0;a<L;a++) {
				if((szBase[a] != 48) && (szBase[a] != (*it1)[a])) {
					 a = L; b1 = true; continue;
				}
			}

			if(!b1)
			{
				pWord = new sWord;
				pWord->word = (char*)malloc(sizeof(char)*(MAXLENGTH+5));
				strcpy_s(pWord->word, MAXLENGTH+4, (*it1));
				pWord->checked = 0; 
				pWord->b = false;
				vSubset.push_back(pWord);
			}
		}

		if(!vSubset.empty()) {
			vector<sCase*>::iterator it2;
			for(it2=vCase.begin();it2!=vCase.end();it2++) {
				char* sSet = (*it2)->set;
				vector<sWord*>::iterator it3;
				for(it3=vSubset.begin(); it3!=vSubset.end();it3++) {
					if(strchr(sSet, (*it3)->word[(*it2)->pos]) == NULL) {
						(*it3)->b = true;
					}
					else (*it3)->checked++;
				}
			}
		}

		if(!vSubset.empty()) {
			vector<sWord*>::iterator it4;
			for(it4=vSubset.begin();it4!=vSubset.end() && !vSubset.empty();) {
				if((*it4)->b || (*it4)->checked < vCase.size()) {
					it4 = vSubset.erase(it4);
				}
				else it4++;	
			}
		}

		fprintf(fpOutput, "Case #%d: %d\n", j+1, vSubset.size());
	}
	
	//Close Files
	fclose(fpInput);
	fclose(fpOutput);
}
