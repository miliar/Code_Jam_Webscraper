// CodeJam-Watersheds.cpp : Defines the entry point for the console application.
//

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>

struct Cell
{
    struct Cell()
    {
        chBasin = 0;
    }

    int
        Altitude;

    Cell
        *pBasin;

    std::vector<Cell *>
        arypFlowFrom;

    char
        chBasin;
};

void propogate_basins(Cell ***pppCells, Cell *pCurr, Cell *pBasin)
{
    pCurr->pBasin = pBasin;

    std::vector<Cell *>::iterator
        iter = pCurr->arypFlowFrom.begin();

    while (iter != pCurr->arypFlowFrom.end())
    {
        propogate_basins(pppCells, *iter, pBasin);
        iter++;
    }
}

int main(int argc, char *argv[])
{
    FILE
        *fpi = fopen("B-large.in", "r"),
        *fpo = fopen("B-large.out", "w");

    int
        T,
        H,
        W;

    fscanf(fpi, "%d", &T);

    for (int n = 0; n < T; n++)
    {
        std::vector<Cell *>
            arypBasins;

        fscanf(fpi, "%d %d", &H, &W);

        Cell
            ***pppCells = new Cell **[H];

        for (int r = 0; r < H; r++)
        {
            pppCells[r] = new Cell *[W];
            for (int c = 0; c < W; c++)
            {
                pppCells[r][c] = new Cell;
                fscanf(fpi, "%d", &pppCells[r][c]->Altitude);
            }
        }

        for (int r = 0; r < H; r++)
            for (int c = 0; c < W; c++)
            {
                Cell
                    *pCurr   = pppCells[r][c],
                    *pBest   = pCurr,
                    *pTest;

                if (r > 0)
                {
                    pTest = pppCells[r - 1][c];
                    if (pTest->Altitude < pBest->Altitude)
                        pBest = pTest;
                }

                if (c > 0)
                {
                    pTest = pppCells[r][c - 1];
                    if (pTest->Altitude < pBest->Altitude)
                        pBest = pTest;
                }

                if (c < W - 1)
                {
                    pTest = pppCells[r][c + 1];
                    if (pTest->Altitude < pBest->Altitude)
                        pBest = pTest;
                }

                if (r < H - 1)
                {
                    pTest = pppCells[r + 1][c];
                    if (pTest->Altitude < pBest->Altitude)
                        pBest = pTest;
                }

                if (pBest == pCurr)
                    arypBasins.push_back(pCurr);
                else
                    pBest->arypFlowFrom.push_back(pCurr);
            }

        std::vector<Cell *>::iterator
            iter = arypBasins.begin();

        while (iter != arypBasins.end())
        {
            propogate_basins(pppCells, *iter, *iter);
            iter++;
        }

        char
            chBasin = 'a';

        fprintf(fpo, "Case #%d:\n", n + 1);
        for (int r = 0; r < H; r++)
        {
            for (int c = 0; c < W; c++)
            {
                Cell
                    *pBasin = pppCells[r][c]->pBasin;

                if (pBasin->chBasin == 0)
                    pBasin->chBasin = chBasin++;

                fprintf(fpo, "%c ", pppCells[r][c]->pBasin->chBasin);
            }

            fprintf(fpo, "\n");
        }
    }

	return 0;
}
