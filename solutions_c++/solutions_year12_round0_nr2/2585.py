#include <cstdio>

int main() {
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("B-large.out", "w");
	int numCase, numGoogler, numSurprise, maxScore;
	int googlerScore[105];
	fscanf (in, "%d\n", &numCase);
	for (int i = 0; i < numCase; i++) {
		int numAnswer = 0;
		fscanf (in, "%d %d %d", &numGoogler, &numSurprise, &maxScore);

			for (int j = 0; j < numGoogler; j++) {
				fscanf (in, "%d", &googlerScore[j]);
				int maxPairScore = googlerScore[j] - maxScore;
				if ((maxPairScore >= 2 * (maxScore - 1)) && (maxScore - 1 >= 0))
					numAnswer++;
				else if ((maxPairScore >= 2 * (maxScore - 2)) && (maxScore - 2 >= 0) && (numSurprise > 0)) {
					numSurprise--;
					numAnswer++;
				}
				else if (maxScore == 0)
					numAnswer++;
				/*if ((googlerScore[j] >= (maxScore - 1) * 3 + 1) && (maxScore >= 1))
						numAnswer++;
				else if ((googlerScore[j] >= (maxScore - 2) * 3 + 2) && (numSurprise > 0) && (maxScore >= 2)) {
					numSurprise--;
					numAnswer++;
				}*/
			}
		fprintf (out, "Case #%d: %d\n", i + 1, numAnswer);
	}
}