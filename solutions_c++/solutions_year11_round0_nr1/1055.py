#include <iostream>
#include <fstream>
#include <string>
#include <queue>

#include <stdlib.h>

#define DERR(x)   \
{  \
    cout << "error: " << (x) << endl; \
    exit(1); \
}

#define ORANGE 1
#define BLUE 2

static int debug = 0;

using namespace std;

typedef struct goal_
{
    int color;
    int loc;
    struct goal_ *pre;
    bool finish;
} goal_t;

int main(int argc, char* argv[])
{
    int T;
    int N, loc;
    string col;
    goal_t goals[100];

    if(argc==1) DERR("no arguments");
    ifstream infile(argv[1], ifstream::in);
    if(infile.fail()) DERR("cannot open file");
    infile >> T;
    if(debug) cout << "T=" << T << endl;
    for(int k=0; k<T; k++)
    {
	// read one line
	infile >> N;
	if(debug) cout << "N=" << N << endl;
	for(int j=0; j<N; j++)
	{
	    infile >> col;
	    if(col.compare("O") == 0) 
	        goals[j].color = ORANGE;
	    else if(col.compare("B") == 0) 
	        goals[j].color = BLUE;
	    else 
	        DERR("unknown color");
	    infile >> loc;
	    goals[j].loc = loc;
	    goals[j].finish = false;
	    goals[j].pre = NULL;
	}

        // add tasks to queue
        queue<goal_t*> qorange;
        queue<goal_t*> qblue;

        goal_t* pre = NULL;
        for(int i=0; i<N; i++)
        {
            goal_t* g = &goals[i];
            g->pre = pre;
            if(g->color == ORANGE)
                qorange.push(g);
            else
                qblue.push(g);
            pre = g;
        }

        // digest queue
	int oloc = 1;
	int bloc = 1;
	int seconds = 0;
	while(qorange.size() > 0 || qblue.size() > 0)
	{
	    goal_t* g;
	    goal_t* pushed = NULL;

	    // Orange
	    if(qorange.size() == 0) 
	    {
		if(debug) cout << "Orange: Stay at button " << oloc << endl;
	    }
	    else {
	        g = qorange.front();
	        if(g->loc > oloc) 
		{
		    oloc++;
	            if(debug) cout << "Orange: Move to button " << oloc << endl;
		}
	        else if(g->loc < oloc) 
		{
		    oloc--;
	            if(debug) cout << "Orange: Move to button " << oloc << endl;
		}
	        else if(g->loc == oloc)
	        {
	            if(g->pre == NULL || g->pre->finish)
	            {
	                if(debug) cout << "Orange: Push button " << oloc << endl;
	                qorange.pop();
			pushed = g;
	            }
	            else 
		    {
	                if(debug) cout << "Orange: Stay at button " << oloc << endl;
		    }
	        }
	    }

	    // Blue
	    if(qblue.size() == 0)
	    {
		if(debug) cout << "Blue: Stay at button " << bloc << endl;
	    }
	    else
	    {
	        g = qblue.front();
	        if(g->loc > bloc)
		{
		    bloc++;
	            if(debug) cout << "Blue: Move to button " << bloc << endl;
		}
	        else if(g->loc < bloc)
		{
		    bloc--;
	            if(debug) cout << "Blue: Move to button " << bloc << endl;
		}
	        else if(g->loc == bloc)
	        {
	            if(g->pre == NULL || g->pre->finish)
	            {
	                if(debug) cout << "Blue: Push button " << bloc << endl;
	                qblue.pop();
			pushed = g;
	            }
	            else
		    {
	                if(debug) cout << "Blue: Stay at button " << bloc << endl;
		    }
	        }
	    }

	    if(pushed != NULL)
		pushed->finish = true;
	    seconds++;
	}

	cout << "Case #" << (k+1) << ": " << seconds << endl;
    }
}



