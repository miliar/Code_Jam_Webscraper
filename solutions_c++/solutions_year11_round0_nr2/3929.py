#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <memory.h>

typedef struct sCombine
{
	int m_combine;	// comining character
	int m_new;		// new char
} sCombine;

typedef struct sBase
{
	int	     m_nCombine;
	sCombine m_arrCombine[8]; // all the characters it can combine with

	int      m_nOppose;
	int	     m_arrOppose[8];  // all the base characters it opposes
} sBase;


int atoiX(char * &s)
{
	int num = 0;

	// skip leading spaces
	while ((*s == ' ') || (*s == '\t'))
		++s;

	while (isdigit(*s)) {
		num = num*10 + *s - '0';
		++s;
	}

	// skip trailing spaces
	while ((*s == ' ') || (*s == '\t'))
		++s;

	return num;
}

int doTestCase(FILE *fs, int caseNum)
{
	sBase arrBase[26];
	memset(arrBase, 0, sizeof(arrBase));

	char buf[8192];
	if (fgets(buf, sizeof(buf), fs) == NULL) {
		// could be also end of file
	}

	if (caseNum == 6)
	{
		int jj = 0;
	}

	// read base elements that combine
	char* s = buf;
	int numCombine = atoiX(s);

	while (numCombine--) {
		int char1 = *s++ - 'A';
		int char2 = *s++ - 'A';
		int char3 = *s++ - 'A';

		if (char1 > char2) {
			int temp = char1;
			char1 = char2;
			char2 = temp;
		}
		
		int index = arrBase[char1].m_nCombine;
		arrBase[char1].m_arrCombine[index].m_combine = char2;
		arrBase[char1].m_arrCombine[index].m_new     = char3;
		arrBase[char1].m_nCombine++;

		// skip blank
		++s;
	}

	// read elements that oppose
	int numOppose = atoiX(s);
	while (numOppose--) {
		int char1 = *s++ - 'A';
		int char2 = *s++ - 'A';

		if (char1 > char2) {
			int temp = char1;
			char1 = char2;
			char2 = temp;
		}
		
		int index = arrBase[char1].m_nOppose;
		arrBase[char1].m_arrOppose[index] = char2;
		arrBase[char1].m_nOppose++;
	}


	// now read number of characters that will follow
	int arrChar[112];
	int i   = 0;
	int numBase = atoiX(s);

	while (numBase--)
	{
START:
		if (*s == '\n') {
			break;
		}

		if (*s == 'E') {
			int kk = 0;
		}

		int char2   = *s++ - 'A';
		arrChar[i] = char2;

		// see if char1 combines with char2 or oppose
		if (i) {
			int combine = 0;
			int char1 = arrChar[i-1];
			if (char1 > char2) {
				int temp = char1;
				char1 = char2;
				char2 = temp;
			}

			// see if they combine
			for (int j=0; j < arrBase[char1].m_nCombine; ++j) {
				if (arrBase[char1].m_arrCombine[j].m_combine == char2) {

					// combine 
					arrChar[i-1] = arrBase[char1].m_arrCombine[j].m_new;

					// new character is a non base so it can't oppose
					combine = 1;
					break;
				}
			}

			if (combine) {
				continue;
			}
			
			// see if they oppose
			// get back char2 as it might have been swapped
			char2 = arrChar[i];
			for (int j = 0; j < i; ++j) {
				int char1 = arrChar[j];
				int char2X = char2;

				if (char1 > char2X) {
					int temp = char1;
					char1 = char2X;
					char2X = temp;
				}

				for (int k=0; k < arrBase[char1].m_nOppose; ++k) {
					if (arrBase[char1].m_arrOppose[k] == char2X) {
						// list becomes empty
						i = 0;
						goto START;
					}
				}
			}
		}

		++i;
	}
	
	printf("Case #%d: [", caseNum);

	for (int k=0; k < i; ++k)
	{
		printf("%c", arrChar[k] + 'A');
		if (k+1 != i)
			printf(", ");
	}
	printf("]\n");

	return 0;
}
	

int readFile(const char* file)
{
	// open file
	FILE* fs = fopen(file, "r");
	if (fs == NULL) {
		return 1;
	}

	// read number of test cases
	char buf[16];
	if (fgets(buf, sizeof(buf), fs) == NULL) {
		fclose(fs);
		return 1;
	}

	int numTestCases = atoi(buf);

	// now process all the cases
	for (int i = 1; i <= numTestCases; ++i) {
		doTestCase(fs, i);
	}

	fclose(fs);
	return 0;
}

int main(int argc, char *argv[])
{
	int i = 1;
	for (int i=1; i < argc; i++) {
		readFile(argv[i]);
	}

	return 0;
}
