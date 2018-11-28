
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <stack>
#include <queue>

using namespace std;

// TOshima


class node
{
    private:
    public:
        int x;
        int y;
        node(int ix, int iy)
        {
            x = ix;
            y = iy;
        }
};

int main()
{
    int T, H, W;
    int caseId, i, x, y; // 0,0 is top left
    int input;
    int altitude [100][100];
    int flow [100][100];
    int top, bottom, left, right;
    int minAlt, currentFlow;
    int visited [100][100];
    int currentX, currentY;
    char labels [100][100]; // basin labels output
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string letter;

    // input output streams
    freopen ("B-large.in", "r", stdin);
    freopen ("output.txt", "w", stdout);

    // number of cases
    scanf ("%d", &T);
    if (T < 1)
        printf ("Error: input file not found\n");

    for (caseId=1; caseId<=T; caseId++)
    //for (caseId=1; caseId<=1; caseId++)
    {
        scanf("%d%d", &H, &W);

        // read altitudes from input file
        for (y=0; y<H; y++)
        {
            for (x=0; x<W; x++)
            {
                scanf("%d", &input);
                //printf ("%d\n", input);

                altitude [x][y] = input;
            }
        }


        // calculate flow directions
        // 0 North / 1 West / 2 East / 3 South / 4 Sink
        for (y=0; y<H; y++)
        {
            for (x=0; x<W; x++)
            {
                // sort out boundaries
                if (y > 0) top = altitude[x][y-1];
                else top = 99999;

                if (y < H-1) bottom = altitude[x][y+1];
                else bottom = 99999;

                if (x > 0) left = altitude[x-1][y];
                else left = 99999;

                if (x < W-1) right = altitude[x+1][y];
                else right = 99999;

                minAlt = altitude[x][y]; // get lowest altitude
                flow[x][y] = 4; // sink

                // could have used vector or so?
                if (top < minAlt)
                {
                    minAlt = top;
                    flow[x][y] = 0;
                }
                if (left < minAlt)
                {
                    minAlt = left;
                    flow[x][y] = 1;
                }
                if (right < minAlt)
                {
                    minAlt = right;
                    flow[x][y] = 2;
                }
                if (bottom < minAlt)
                {
                    minAlt = bottom;
                    flow[x][y] = 3;
                }
                //printf ("%d", flow[x][y]);
            }
            //printf ("\n");
        }
            //printf ("\n");
            //printf ("\n");


        // clear
        for (y=0; y<H; y++)
        {
            for (x=0; x<W; x++)
            {
                visited[x][y] = false;
            }
        }


        // label sources
        // for each cell
        i=0;
        for (y=0; y<H; y++)
        {
            for (x=0; x<W; x++)
            {
                if (!visited[x][y])
                //if (flow[x][y] == 4)
                {
                    // need to add this to make sure letters are in order
                    // direct to source
                    currentX = x;
                    currentY = y;
                    currentFlow = flow[currentX][currentY];
                    //printf ("TEST %d %d\n", x, y);
                    while (currentFlow < 4)
                    {
                        currentFlow = flow[currentX][currentY];

                        // move to neighbouring cell
                        switch (currentFlow)
                        {
                            case 0:
                                currentY--;
                                break;
                            case 1:
                                currentX--;
                                break;
                            case 2:
                                currentX++;
                                break;
                            case 3:
                                currentY++;
                                break;
                        }
                        //printf ("TEST %d \n", currentFlow);
                    }
                    // so currentX, currentY is a new source cell

                    //printf ("\nTEST %d %d %d\n", currentX, currentY, currentFlow);
                    labels[currentX][currentY] = alphabet[i];
                    i++;

                    queue<node> s;
                    s.push(node (currentX, currentY));

                    // bf search
                    while (s.empty() == false)
                    {
                        node top = s.front();
                        s.pop();

                        // within bounds?
                        if (top.x < 0 || top.x > W) continue;
                        if (top.y < 0 || top.y > H) continue;
                        if (visited[top.x][top.y]) continue;

                        visited[top.x][top.y] = true;

                        // so flows into source
                        labels[top.x][top.y] = labels[currentX][currentY];

                        // add neighbours which flow here
                        if (top.y > 0)
                        {
                            if (flow[top.x][top.y-1] == 3)
                            {
                                s.push (node(top.x, top.y-1));
                            }
                        }
                        if (top.y < H-1)
                        {
                            if (flow[top.x][top.y+1] == 0)
                            {
                                s.push (node(top.x, top.y+1));
                            }
                        }
                        if (top.x > 0)
                        {
                            if (flow[top.x-1][top.y] == 2)
                            {
                                s.push (node(top.x-1, top.y));
                            }
                        }
                        if (top.x < W-1)
                        {
                            if (flow[top.x+1][top.y] == 1)
                            {
                                s.push (node(top.x+1, top.y));
                            }
                        }
                    }// end bfs
                }// end if cell visited yet
            }
        }// end for each cell

        // output
        printf ("Case #%d:\n", caseId);
        for (y=0; y<H; y++)
        {
            for (x=0; x<W; x++)
            {
                letter = labels[x][y];
                printf ("%s ", letter.c_str());
            }
            printf ("\n");
        }
    }// end for each case

    return 0;
}

