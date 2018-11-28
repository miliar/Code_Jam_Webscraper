#include <list>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;


int main()
{
	FILE* code_file;
	FILE* outFile;
	int caseNum, trueNum, lastDig;
	list<int> origList, copyList, finalList, sortList;
	int i, j, theCase;
	int oSize, sSize, fSize;
	int highDig, nextHigh, tmpDig;
	list<int>::iterator origIte, sortIte, copyIte, finalIte;

	code_file = fopen("B-small-attempt0.in", "r");
	outFile = fopen("outResult", "w");

	if (!code_file)
		exit(1);

	fscanf(code_file, "%d", &caseNum);

	for (theCase = 0; theCase < caseNum; theCase++) {
		fscanf(code_file, "%d", &trueNum);

		origList.clear();
		finalList.clear();
		sortList.clear();
		copyList.clear();

		while (trueNum > 0) {
			origList.push_front(trueNum % 10);
			trueNum /= 10;
			/*origList.push_back(1);
			origList.push_back(0);
			origList.push_back(2);
			origList.push_back(5);*/
		}
		oSize = origList.size();


		for (i = 2; i <= oSize + 1; i++) {
			copyList = origList;
			sortList.clear();
			if ( i != oSize+1) {
				//origIte = --(origList.end());
				for (j = 0; j < i; j++) {
					sortList.push_front(copyList.back());
					copyList.pop_back();
				}
				highDig = sortList.front();
				sortList.sort();

				nextHigh = 0;
				for (sortIte = sortList.begin(); sortIte != sortList.end(); sortIte++) {
					if (*sortIte > highDig) {
						nextHigh = *sortIte;
						sortList.erase(sortIte);
						break;
					}
				}

				if (nextHigh > 0) {
					finalList = copyList;
					finalList.push_back(nextHigh);
					for (sortIte = sortList.begin(); sortIte != sortList.end(); sortIte++) {
						finalList.push_back(*sortIte);
					}
					break;
				}
			}
			else {
				sortList = copyList;
				sortList.push_front(0);
				sortList.sort();
				for (sortIte = sortList.begin(); sortIte != sortList.end(); sortIte++) {
					if (*sortIte != 0) {
						*sortList.begin() = *sortIte;
						*sortIte = 0;
						finalList = sortList;
						break;
					}
				}
			}
		}

		fprintf(outFile, "Case #%d: ", theCase+1);
		printf("Case #%d: ", theCase+1);
		for (finalIte = finalList.begin(); finalIte != finalList.end(); finalIte++) {
			printf("%d", *finalIte);
			fprintf(outFile, "%d", *finalIte);
		}
		printf("\n");
		fprintf(outFile, "\n");

	}

	system("pause");

	return 0;
}