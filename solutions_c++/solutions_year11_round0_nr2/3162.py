#include <iostream>

#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> TIV;
typedef vector<short> TSV;

static const char FOUND_A = 1;
static const char FOUND_B = 2;
static const char FOUND_BOTH = FOUND_A | FOUND_B;

class OPElement {
public:
    char a;
    char b;
    char state;

    OPElement() : a(0), b(0), state(0) {}

    bool Test(char inInvoke)
    {
        if(!(state & FOUND_A) && a == inInvoke) {
            state |= FOUND_A;
        }
        else if(!(state & FOUND_B) && b == inInvoke) {
            state |= FOUND_B;
        }

        if((state & FOUND_BOTH) == FOUND_BOTH){
            state = 0;
            return true;
        }
        else {
            return false;
        }
    }
};

class NBElement {
public:
    char a;
    char b;
    char c;
    char state;

    NBElement() : a(0), b(0), c(0), state(0) {}

    bool Test(char inInvoke)
    {
        if( ((state & FOUND_A) && inInvoke != b)
            || ((state & FOUND_B) && inInvoke != a) ){
            state = 0;
        }

        if(!(state & FOUND_A) && a == inInvoke) {
            state |= FOUND_A;
        }
        else if(!(state & FOUND_B) && b == inInvoke) {
            state |= FOUND_B;
        }

        if((state & FOUND_BOTH) == FOUND_BOTH){
            state = 0;
            return true;
        }
        else {
            return false;
        }
    }
};

typedef vector<NBElement> TNV;
typedef vector<OPElement> TOV;

typedef vector<char> TCV;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int numCases = 0;
    in >> numCases;

    for(int c = 0; c < numCases; c++) {
        short numNonBase = 0;
        TNV nonbase;

        in >> numNonBase;

        for(int i = 0; i < numNonBase; i++){
            NBElement nbe;
            in >> nbe.a;
            in >> nbe.b;
            in >> nbe.c;

            nonbase.push_back(nbe);
        }

        short numOposites = 0;
        in >> numOposites;

        TOV oposites;

        for(int i = 0; i < numOposites; i++) {
            OPElement op;

            in >> op.a;
            in >> op.b;

            oposites.push_back(op);
        }

        TCV invokes;
        short numInvokes = 0;
        in >> numInvokes;

        for(int i = 0; i < numInvokes; i++) {
            char invoke = 0;
            in >> invoke;
            invokes.push_back(invoke);
        }

        TCV result;
        TCV::iterator cit(invokes.begin());
        for(;cit!=invokes.end();++cit){
            char c = *cit;
            bool add = true;
            TNV::iterator nbit(nonbase.begin());
            for(;nbit!=nonbase.end();++nbit){
                if(nbit->Test(c)){
                    result[result.size()-1] = nbit->c;
                    c = nbit->c;
                    add = false;

                    TOV::iterator clearit(oposites.begin());

                    for(; clearit != oposites.end(); ++clearit){
                        clearit->state = 0;
                        for(short n = 0; n < result.size(); n++) {
                            clearit->Test(result[n]);
                        }
                        //if(clearit->a == nbit->a || clearit->a == nbit->b){
                        //    clearit->state &= (~FOUND_A & FOUND_BOTH);
                        //}
                        //if(clearit->b == nbit->a || clearit->b == nbit->b){
                        //    clearit->state &= (~FOUND_B & FOUND_BOTH);
                        //}
                    }

                    break;
                }
            }

            if(add) {
                TOV::iterator opit(oposites.begin());
                for(;opit!=oposites.end();++opit){
                    if(opit->Test(c)){
                        result.clear();
                        add = false;

                        for(nbit = nonbase.begin(); nbit!=nonbase.end(); ++nbit){
                            nbit->state = 0;
                        }

                        break;
                    }
                }
            }

            if(add){
                result.push_back(c);
            }
        }

        out << "Case #" << c + 1 << ": [";

        for(int i = 0; i < result.size(); i++){
            out << result[i];

            if(i != (result.size() - 1)) {
                out << ", ";
            }
        }

        out << "]" << endl;

#if DEBUGA
        TNV::iterator a(nonbase.begin());
        for(; a!=nonbase.end(); ++a){
            out << a->a << a->b << a->c << ", ";
        }
        TOV::iterator b(oposites.begin());
        for(; b!=oposites.end(); ++b){
            out << b->a << b->b << ", ";
        }

        TCV::iterator c(invokes.begin());
        for(; c!=invokes.end(); ++c){
            out << *c;
        }
        out << endl;
#endif
    }

    in.close();
    out.close();
    return 0;
}
