#include <string>
#include <vector>
#include <algorithm>

using namespace std;


typedef struct node {
    int pos;
    struct node* nextOrder;
	struct node* myNext;
} cell;
typedef cell* pointer;

const int MAX = 200;
cell v[MAX];
int vp = 0;
pointer myAlloc() {
	return &(v[vp++]);
}

void myFree() {
	vp = 0;
}



pointer newCell() {
	pointer newC = myAlloc();

	newC->pos = 1;
	newC->nextOrder = NULL;
	newC->myNext = newC;

	return newC;
}

pointer newCell(int pos, pointer previousOrder, pointer myPrevious) {
	pointer newC = myAlloc();

	newC->pos = pos;
	previousOrder->nextOrder = newC;
	myPrevious->myNext = newC;
	newC->nextOrder = NULL;
	newC->myNext = newC;

	return newC;
}

void showWay(pointer pos) {
	for (pos = pos->myNext; pos != NULL; pos = pos->myNext) {
		printf("%d => ", pos->pos);
	}
	printf("NULL\n");
}

void showWholeWay(pointer pos) {
	for (pos = pos->nextOrder; pos != NULL; pos = pos->nextOrder) {
		printf("%d => ", pos->pos);
	}
	printf("NULL\n");
}




int main() {
	int T;
	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		int N;
		pointer posG, posO, posB; // geral, orange, blue
		pointer lastG, lastO, lastB; // ajudam a montar as listas
		pointer nextO, nextB; // pra achar a distancia
		int count = 0;

		// cabecas
		posG = newCell();
		posO = newCell();
		posB = newCell();
		lastG = posG;
		lastO = posO;
		lastB = posB;

		scanf("%d", &N);

		for (int j = 0; j < N; j++) {
			char c;
			int b;

			scanf(" %c %d", &c, &b);

			if (c == 'O') {
				lastO = newCell(b, lastG, lastO);
				lastG = lastO;
			}
			else {
				lastB = newCell(b, lastG, lastB);
				lastG = lastB;
			}
		}

		nextO = posO->myNext;
		nextB = posB->myNext;
		for (posG = posG->nextOrder; posG != NULL; posG = posG->nextOrder) {
			int distO = abs(nextO->pos - posO->pos), distB = abs(nextB->pos - posB->pos);

			if (posG == nextO) {
				count += distO + 1;
				posO = nextO;
				nextO = posO->myNext;

				if (distO < distB) {
					if (nextB->pos > posB->pos)
						posB->pos += distO + 1;
					else
						posB->pos -= distO + 1;
				}
				else
					posB->pos = nextB->pos;
			}

			else {
				count += distB + 1;
				posB = nextB;
				nextB = posB->myNext;

				if (distB < distO) {
					if (nextO->pos > posO->pos)
						posO->pos += distB + 1;
					else
						posO->pos -= distB + 1;
				}
				else
					posO->pos = nextO->pos;
			}
		}

		printf("Case #%d: %d\n", cs, count);

		myFree();
	}

	return 0;
}
