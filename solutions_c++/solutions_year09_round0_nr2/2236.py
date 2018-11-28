#include <cstdio>

#define NORTH 0
#define EAST 1
#define WEST 2
#define SOUTH 3
#define NO_DIRECTION 4

int highPriority(int* map, int x, int y, int xLength, int yLength){
    int retDirection = NO_DIRECTION;
    int minH = map[y*xLength + x];
    if (y > 0 && map[(y-1)*xLength + x] < minH){
        minH = map[(y-1)*xLength + x];
        retDirection = NORTH;
    }
    if (x > 0 && map[y*xLength + x -1] < minH){
        minH = map[y*xLength + x -1];
        retDirection = WEST;
    }
    if (x < xLength - 1 && map[y*xLength + x + 1] < minH){
        minH = map[y*xLength + x + 1];
        retDirection = EAST;
    }
    if (y < yLength - 1 && map[(y+1)*xLength + x] < minH){
        minH = map[(y+1)*xLength + x + 1];
        retDirection = SOUTH;
    }
    return retDirection;
}

void flow(int* map, int x, int y
                  , int xLength, int yLength, char* chMap, char ch){
    chMap[y*xLength + x] = ch;
    //Flow upwards, forever more!
    if (y < yLength-1 && map[(y+1)*xLength + x] >map[y*xLength + x] 
                      && highPriority (map, x, y+1, xLength, yLength) == NORTH 
                      && chMap[(y+1)*xLength + x] == '.'){
        flow(map, x, y+1, xLength, yLength, chMap, ch);
    }
    if (x < xLength-1 && map[y*xLength+x+1] >map[y*xLength + x] 
                      && highPriority (map, x+1, y, xLength, yLength) == WEST
                      && chMap[y*xLength + x + 1] == '.'){
        flow(map, x + 1, y, xLength, yLength, chMap, ch);
    }
    if (x > 0 && map[y*xLength+x-1] >map[y*xLength + x] 
                        && highPriority (map, x-1, y, xLength, yLength) == EAST
                        && chMap[y*xLength + x - 1] == '.'){
        flow(map, x-1, y, xLength, yLength, chMap, ch);
    }
    if (y > 0 && map[(y-1)*xLength+x] >map[y*xLength + x] 
                        && highPriority (map, x, y-1, xLength, yLength) == SOUTH 
                        && chMap[(y-1)*xLength + x] == '.'){
        flow(map, x, y - 1, xLength, yLength, chMap, ch);
    }
    //Flow downwards
    if (highPriority(map, x, y, xLength, yLength) == NORTH 
                                            && chMap[(y-1)*xLength + x] == '.'){
        flow(map, x, y-1, xLength, yLength, chMap, ch);
    } else if (highPriority(map, x, y, xLength, yLength) == WEST
                                            && chMap[y*xLength + x - 1] == '.'){
        flow(map, x-1, y, xLength, yLength, chMap, ch);
    } else if (highPriority(map, x, y, xLength, yLength) == EAST
                                            && chMap[y*xLength + x + 1] == '.'){
        flow(map, x + 1, y, xLength, yLength, chMap, ch);
    } else if (highPriority(map, x, y , xLength, yLength) == SOUTH
                                            && chMap[(y+1)*xLength + x] == '.'){
        flow(map, x, y + 1, xLength, yLength, chMap, ch);
    }
}

void printBest(int* map, int xLength, int yLength, FILE* output){
    char* chMap = new char[xLength * yLength];
    for (int i=0; i<xLength * yLength; i++){
        chMap[i] = '.';
    }
    char ch = 'a' - 1;
    for (int i=0; i<yLength; i++){
        for (int j=0; j<xLength; j++){
            if (chMap[i*xLength + j] == '.'){
                ch++;
                flow(map, j, i, xLength, yLength, chMap, ch);
            }
        }
    }
    for (int i=0; i<yLength; i++){
        for (int j=0; j<xLength; j++){
            fprintf(output, "%c ", chMap[i*xLength + j]);
        }
        fprintf(output, "\n");
    }
}

int main(){
    FILE* input = fopen("B-Large.in", "r");
    FILE* output = fopen("B-Small.out", "w");
    int xLength;
    int yLength;
    int numTests;
    int* basin = NULL;
    if (input != NULL){
        fscanf(input, "%d\n", &numTests);
        for (int i=0; i<numTests; i++){
            fscanf(input, "%d %d\n", &yLength, &xLength);
            basin = new int[yLength * xLength];
            for (int j=0; j<yLength * xLength; j++){
                fscanf(input, "%d", &basin[j]);
            }
            fprintf(output, "Case #%d:\n", i+1);
            printBest(basin, xLength, yLength, output);
            delete[] basin;
        }
    }
}
