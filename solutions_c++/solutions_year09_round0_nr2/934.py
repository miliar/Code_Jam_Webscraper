#include <iostream>
#include <map>
#include <vector>
#include <cstdlib>

// basings will be inited by numbers originally,
// then with the help of this map we'll find the 
// correspondent letter
//map<int,char> BasinsLetters;

//bool debug = true;
bool debug = false;
#define MAX_ALT 10000
int BasinsCounter = 0;
int T;

using namespace std;

char letters [27];
// Point of the map
#define ind(y,x) ((y)*W+(x))
struct Point
{
    Point *neighbours[4]; //*north, *west, *east, *south;
    int x,y;
    int alt;
    int basin; // originally, letter

    void init(int xcoord, int ycoord, int altitude, Point *neighb[4])
    {
        x = xcoord, y = ycoord, alt = altitude;
        neighbours[0] = neighb[0];
        neighbours[1] = neighb[1];
        neighbours[2] = neighb[2];
        neighbours[3] = neighb[3];
    }
    void repr(bool shorten = false, bool fail_uninit = false);
};

void Point::repr(bool shorten, bool fail_uninit)
{
    if (shorten)
    {
        if (fail_uninit && basin == 0)
        {
            cerr << "Uninitialized basin" << endl;
            abort();
        }
        cout << letters[basin] << " ";
        //cout << basin << " ";
    }
    else
    {
        cout << "Point (" << x << "," << y << "," << alt << "," << basin << ") = " << this << endl;
        for (int i = 0; i < 4; i++)
            cout << "  n[" << i << "] = " << neighbours[i] << endl;
        cout << endl;
    }
}


// go to the nearest point in the basin and return basin number from the first point with the
// basin number inited
// Return:
//   0 - no inited basin number found. Use BasinsCounted.
//   > 0 - basin number
int findBasinNumber(Point *p)
{
    if(debug) cout << "find(" << p->x << "," << p->y << ")?" << endl;
    if(p->basin != 0)
    {
        if(debug) cout << "find(" << p->x << "," << p->y << "):" << p->basin << endl;
        return p->basin;
    }
    int minAlt = p->alt;
    // calculate minimum altitude among neighbours
    for(int i = 0; i < 4; i++)
    {
        if (p->neighbours[i] && p->neighbours[i]->alt < minAlt)
        {
            minAlt = p->neighbours[i]->alt;
        }
    }
    // we can't spread further
    // so we should initialize new basin.
    if (minAlt == p->alt)
    {
        // there will be 26 basins at most
        if(BasinsCounter == 26)
        {
            cerr << "Too many BasinsCounter (>26)" << endl;
            abort();
        }
        p->basin = ++BasinsCounter;
        if(debug) cout << "find(" << p->x << "," << p->y << "):" << p->basin << endl;
        return p->basin;
    }
    for(int i = 0; i < 4; i++)
    {
        if (p->neighbours[i] && p->neighbours[i]->alt == minAlt)
        {
            p->basin = findBasinNumber(p->neighbours[i]);
            if(debug) cout << "find(" << p->x << "," << p->y << "):" << p->basin << endl;
            return p->basin;
        }
    }

    cerr << "Go to the end of function" << endl;
    abort();
    return 0;
} // findBasinNumber

void repr_all(vector<Point> & points, int H, int W, bool fail_uninit)
{
    for (int h = 0; h < H; h++)
    {
        for (int w = 0; w < W; w++)
        {
            points[ind(h,w)].repr(true, fail_uninit);
        }
        cout << endl;
    }
}

void calc(vector<Point> & points, int H, int W)
{
    BasinsCounter = 0;
    for (int h = 0; h < H; h++)
    {
        for (int w = 0; w < W; w++)
        {
            // if basin is already inited, don't try to init it once more
            if (points[ind(h,w)].basin != 0)
                continue;
            findBasinNumber(&points[ind(h,w)]);
            if(debug) repr_all(points,H,W,false);
        }
    }
}


int main(void)
{
    // initiaizing data:
    letters[0] = '0';
    for (int i = 1; i < 27; i++)
    {
        letters[i] = 'a' - 1 + i;
    }
    // reading data from stdin
    cin >> T;
    for (int t = 0; t < T; t++)
    {
        int W, H;
        vector<Point> points;

        cout << "Case #" << t+1 << ":" << endl;
        cin >> H >> W;
        points.resize(H*W);
        for (int h = 0; h < H; h++)
        {
            for (int w = 0; w < W; w++)
            {
                int alt;
                cin >> alt;
                Point *n[4];
                // north
                if (h == 0)
                    n[0] = NULL;
                else
                    n[0] = &points[ind(h-1,w)];

                // west
                if (w == 0)
                    n[1] = NULL;
                else
                    n[1] = &points[ind(h,w-1)];

                // east
                if (w == W-1)
                    n[2] = NULL;
                else
                    n[2] = &points[ind(h,w+1)];

                // south
                if (h == H-1)
                    n[3] = NULL;
                else
                    n[3] = &points[ind(h+1,w)];

                points[ind(h,w)].init(w,h,alt,n);
                //points[ind(h,w)].repr();
            } // for (int w = 0; w < W; w++)
        } // for (int h = 0; h < H; h++)
        calc(points, H, W);
        repr_all(points, H, W, true);
        cout << endl;
    } // for (t = 0; t < T; t++);
    return 0;
} // main()
