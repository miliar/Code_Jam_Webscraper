//google code jam qualification b
#include <stdio.h>

const int maxCD=256;
const int maxn=128;

class Relation{
public:
	bool canCombine, isOpposed;
	char combineResult;
	void init(){
		this->canCombine=this->isOpposed=false;
	}
};

Relation list[maxCD][maxCD];
char seq[maxn];
int n;

void inputData(){
	for (int i=0; i<maxCD; i++)
		for (int j=0; j<maxCD; j++)
			list[i][j].init();

	int c,d, p,q;
	char str[10];

	scanf("%d%*c", &c);
	for (int i=0; i<c; i++){
		scanf("%s", str);
		p=str[0];
		q=str[1];
		list[q][p].canCombine=list[p][q].canCombine=true;
		list[q][p].combineResult=list[p][q].combineResult=str[2];
	}

	scanf("%d%*c", &d);
	for (int i=0; i<d; i++){
		scanf("%s", str);
		p=str[0];
		q=str[1];
		list[q][p].isOpposed=list[p][q].isOpposed=true;
	}

	scanf("%d%*c%s", &n, seq);
}

int main(){
	int caseIndex, caseT;
	scanf("%d", &caseT);
	char temp[maxn];

	for (caseIndex=1; caseIndex<=caseT; caseIndex++){
		inputData();

		int nextIndex=0;

		for (int i=0; i<n; i++){
			temp[nextIndex++]=seq[i];
			if (nextIndex>1){
				int p=temp[nextIndex-1], q=temp[nextIndex-2];
				Relation *rel=&list[p][q];
				if (rel->canCombine==true){
					temp[nextIndex-2]=rel->combineResult;
					nextIndex--;
				}else 
					for (int j=0; j<nextIndex-1; j++){
						q=temp[j];
						if (list[p][q].isOpposed==true)
							nextIndex=0;
					}
			}
		}

		printf("Case #%d: [", caseIndex);
		for (int i=0; i<nextIndex; i++){
			if (i>0) printf(", ");
			printf("%c", temp[i]);
		}
		printf("]\r\n");
	}
	return 0;
}