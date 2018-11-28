#include <string>
#include <iostream>
#include <fstream>

using namespace std;



struct engine {
    string name;
    engine *next;
};

void getInput (ifstream&, string[], string[], int&, int&);
void makeList (string[], int, engine*&);
   

int main() {
    
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("A-large.out");
    int cases;
    int thisCase = 1;
    int S, Q;
    int switches = 0;
    string engines[100];
    string queries[1000];
    engine *search = NULL;
    engine *prevEn, *currEn;
    int x = 0;
    
    in >> cases;
    
    while (thisCase <= cases) {
        getInput(in, engines, queries, S, Q);
        
        makeList(engines, S, search);
        while (x < Q) {
            currEn = search;
            prevEn = search;
            if (search -> next == NULL && search -> name == queries[x]) {
                switches++;
                delete search;
                makeList(engines, S, search);
                currEn = search;
                prevEn = search;
            }
            //else {
            while (currEn != NULL) {
                if (currEn->name == queries[x]) {
                    if (currEn == search) {
                        currEn = currEn->next;
                        delete search;
                        search = currEn;
                    }
                    else {
                        prevEn->next = currEn->next;
                        delete currEn;
                    }
                    break;
                }
                prevEn = currEn;
                currEn = currEn->next;
            }
            //}
            x++;
        }
        
        x = 0;
        
        
        out << "Case #" << thisCase << ": " << switches;
        if (thisCase != cases)
            out << endl;
        switches = 0;
                   
        
        
        thisCase++;
    }


    return 0;
}

void getInput (ifstream& in, string engines[], string queries[], int& S, int& Q) {
    int x = 0;
    in >> S;
    if (in.peek() == '\n')
        in.ignore(1);
    
    
    while (x < S) {
        getline(in, engines[x]);
        x++;
    }
    
    in >> Q;
    x = 0;
    if (in.peek() == '\n')
        in.ignore(1);
    while (x < Q) {
        getline(in, queries[x]);
        x++;
    }
}

void makeList (string engines[], int S, engine*& search) {
    int x = 1;
    engine *currEn, *nextEn;
    search = new engine;
    search->name = engines[0];
    search->next = NULL;
    currEn = search;

    
    while (x < S) {
        nextEn = new engine;
        nextEn->name = engines[x];
        nextEn->next = NULL;
        currEn->next = nextEn;
        currEn = nextEn;
        x++;
    }
}

