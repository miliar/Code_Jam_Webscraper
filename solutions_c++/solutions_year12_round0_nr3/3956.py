#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
using namespace std;

int main(void) {
	char acBuf[32], acTmpBuf[32], *aPtr = acBuf, *bPtr;
	set<unsigned int> consideredNums;
	unsigned int t, tc = 0;

	scanf("%u\n", &t);
	while (t--) {
		fgets(acBuf, sizeof(acBuf), stdin);

		const unsigned int a = strtoul(aPtr, &bPtr, 10);
		*bPtr++ = 0;
		const unsigned int b = strtoul(bPtr, NULL, 10);
		const unsigned int totalNumLength = (bPtr - 1) - aPtr;
		unsigned int viablePairs = 0;

		if (totalNumLength > 1) {

			unsigned int currentNumber = a;
			do {
				consideredNums.clear();

				// Copy initial value back to back (to manage rotated nos.).
				sprintf(acTmpBuf, "%u", currentNumber);
				memcpy(&acTmpBuf[totalNumLength], acTmpBuf, totalNumLength);
				acTmpBuf[totalNumLength * 2] = 0;

				unsigned int rotation = 1;
				do {
					char *strPtr = &acTmpBuf[rotation];
					const int cmpResult = strncmp(strPtr, acTmpBuf, totalNumLength);
					if (cmpResult < 0) continue;
					else if (cmpResult == 0) break;

					const char nullPosValue = strPtr[totalNumLength];
					strPtr[totalNumLength] = 0;
					const unsigned int num = strtoul(strPtr, NULL, 10);
					strPtr[totalNumLength] = nullPosValue;

					if (consideredNums.insert(num).second)
						if ((num >= a) & (num <= b))
							++viablePairs;
				} while (++rotation < totalNumLength);

				// Find next suitable no. in a-b range.
				++currentNumber;
			} while (currentNumber <= b);
		}
		
		printf("Case #%u: %u\n", ++tc, viablePairs);
	}


	return 0;
}
