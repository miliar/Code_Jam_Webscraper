#include<cstdio>
#include<cstdlib>
int compare(const void *a, const void *b) {
  return (*(int*)b-*(int*)a);
}
typedef struct {
    int scores[3];
} TRIPLET;
int main() {
    TRIPLET triplets[101];
    int i, casesQty, googlers, surprises, minScore, t, scores[101], bigger, zeros, grantedSurprises;
    scanf("%d", &casesQty);
    for(t = 1; t <= casesQty; t++) {
        scanf("%d %d %d", &googlers, &surprises, &minScore);
        for(i = 0; i < googlers; i++)
            scanf("%d", &scores[i]);
        qsort(scores, googlers, sizeof(int), compare);
        bigger = 0;
        zeros = 0;
        grantedSurprises = 0;
        for(i = 0; i < googlers; i++) {
            //printf("%d: %d (melhor que %d)\n", i, scores[i], minScore);
            triplets[i].scores[0] = triplets[i].scores[1] = triplets[i].scores[2] = scores[i]/3;
            if(scores[i]%3 == 2) {
                triplets[i].scores[0]++;
                triplets[i].scores[1]++;
            } else if(scores[i]%3 == 1) {
                triplets[i].scores[0]++;
            }
            if(triplets[i].scores[0] >= minScore)
                bigger++;
            else if(triplets[i].scores[0]+1 >= minScore && scores[i] >= 2 && surprises > 0) {
                surprises--;
                grantedSurprises++;
            }
            //printf("%d %d %d\n", triplets[i].scores[0], triplets[i].scores[1], triplets[i].scores[2]);
        }
        printf("Case #%d: %d\n", t, bigger + grantedSurprises);
    }
    return 0;
}
