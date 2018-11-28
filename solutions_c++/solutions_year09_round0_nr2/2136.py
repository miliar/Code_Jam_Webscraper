#include <iostream>
#include <cctype>

using namespace std;

int flow(int place, int H, int W, int *pMap);
// return -1 if doesn't flow out
void label(int place, int H, int W, int *pMap, char *pLabel, char &lastLabel, int &labelCount);

int main()
{
    int numOfMaps;
    cin >> numOfMaps;
    for (int i = 0; i < numOfMaps; i++)
    {
        int H,W;
        cin >> H >> W;
        int *pMap = new int[H*W];
        char *pLabel = new char[H*W];
        char lastLabel = 'A';
        for (int j = 0; j < H*W; j++)
        {
            cin >> pMap[j];
            pLabel[j] = '0';
        }

        int labelCount = 0;
        while (labelCount != H*W)
        {
            // Search for the largest
            int max = 0;
            int index = 0;
            for (int j = 0; j < H*W; j++)
            {
                if ( (pLabel[j] == '0')&&(pMap[j]>max) ) {
                    max = pMap[j];
                    index = j;
                }
            }
            // Label from the largest
            label(index,H,W,pMap,pLabel,lastLabel,labelCount);
        }

        // Relabel
        labelCount = 0;
        lastLabel = 'a';
        for (int j = 0; j < H*W && labelCount < H*W; j++)
        {
            if (isupper(pLabel[j])) {
                for (int k = j+1; k < H*W; k++)
                {
                    if (pLabel[k] == pLabel[j]) {
                        pLabel[k] = lastLabel;
                        labelCount++;
                    }
                }
                pLabel[j] = lastLabel;
                lastLabel++;
            }
        }
        cout << "Case #" << i+1 << ":" << endl;
        for (int j = 0; j < H; j++)
        {
            for (int k = 0; k < W; k++)
            {
                if (k == W-1) {
                    cout << pLabel[j*W+k];
                } else {
                    cout << pLabel[j*W+k] << " ";
                }
            }
            cout << endl;
        }
    }

    return 0;
}

int flow(int place, int H, int W, int *pMap)
{
    bool valid[4]={true, true, true, true};
    if (place < W) {valid[0] = false;}
    if (place >= W*(H-1)) {valid[1] = false;}
    if (place%W == 0) {valid[2] = false;}
    if (place%W == W-1) {valid[3] = false;}
    int returnIndex = -1, min = pMap[place];
    if (valid[0] && pMap[place-W]<min) {
        min = pMap[place-W];
        returnIndex = place-W;
    }
    if (valid[2] && pMap[place-1]<min) {
        min = pMap[place-1];
        returnIndex = place-1;
    }
    if (valid[3] && pMap[place+1]<min) {
        min = pMap[place+1];
        returnIndex = place+1;
    }
    if (valid[1] && pMap[place+W]<min) {
        returnIndex = place+W;
    }
    return returnIndex;
}

void label(int place, int H, int W, int *pMap, char *pLabel, char &lastLabel, int &labelCount)
{
    int nextFlow = flow(place,H,W,pMap);
    pLabel[place] = lastLabel;
    labelCount++;

    if (nextFlow == -1) {
        lastLabel++;
        return;
    }

    if (pLabel[nextFlow] == '0') {
        pLabel[nextFlow] = lastLabel;
        label(nextFlow,H,W,pMap,pLabel,lastLabel,labelCount);
    } else {
        // Search and replace all lastLabel to nextFlow label
        for (int i = 0; i < H*W; i++)
        {
            if (pLabel[i] == lastLabel) {
                pLabel[i] = pLabel[nextFlow];
            }
        }
    }
}


