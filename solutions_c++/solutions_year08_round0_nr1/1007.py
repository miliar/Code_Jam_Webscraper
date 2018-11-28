/*
 * Google Code Jam, 2008
 *
 * UserID: jayeshvyas
 * Date: July 16, 2008
 */

#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <vector>

//#define DEBUG

#ifdef DEBUG
#define DPRINT printf
#else
#define DPRINT ignore
#endif

#define INF 100000
#define NAME_SIZE 101

using namespace std;

void ignore(const char * c, ...)
{

}

typedef vector<string> Vstring;
typedef map<string, int> DistMap;

Vstring engines;
Vstring queries;

void printOut(int caseNo, int answer)
{
    cout << "Case #" << caseNo << ": " << answer << endl << flush;
}

bool isWhiteSpace(char ch)
{
    switch (ch) {
        case ' ':
        case '\t':
        case '\n':
        case '\r':
            return true;
            break;
        default:
            return false;
    }
}

void proceed(ifstream &f)
{
    while (isWhiteSpace(f.peek()))
        f.get();

}

int getDistanceFromIndex(unsigned index, const string &engine)
{
    int distance = 0;
    for (unsigned ii = index; ii < queries.size(); ii++) {
        if (engine == queries[ii]) {
            return distance;
        }
        distance++;
    }
    return INF;
}

// Returns the max entry in the map
int getMax(DistMap distMap)
{
    int max = 0;
    DistMap::iterator iter = distMap.begin();
    max = (*iter).second;
    for (; iter != distMap.end(); iter++) {
        if ((*iter).second > max) {
            string eng = (*iter).first;
            DPRINT("gotMax: engine: %s, dist: %d\n", eng.c_str(), (*iter).second);
            max = (*iter).second;
        }
    }
    DPRINT("returning max: %d\n", max);
    return max;
}

// Uses the global engines and queries variables
int getMinNumberOfShifts()
{
    int numberOfShifts = 0;
    // Current serving index in queries
    DistMap distMap;
    Vstring::iterator vsIter;
    for (vsIter = engines.begin(); vsIter != engines.end(); vsIter++) {
        distMap[*vsIter] = 0;
    }
    unsigned currIndex = 0;
    while (currIndex < queries.size()) {
        
        // First calculating the distance from the current index
        for (vsIter = engines.begin(); vsIter != engines.end(); vsIter++) {
            distMap[*vsIter] = getDistanceFromIndex(currIndex, *vsIter);
            DPRINT("engine: %s, distance: %d\n", (*vsIter).c_str(), distMap[*vsIter]);
        }

        // Now getting the maximum element from index;
        int forwardBy = getMax(distMap);
        if (forwardBy != INF)
            numberOfShifts++;

        currIndex += forwardBy;
    }
    return numberOfShifts;
}

int main(int argc, char * argv[])
{
    if (argc != 2) {
        cerr << "Usage: SavingUniverse <input_file.in>\n";
        exit(-1);
    }

    string inp = argv[1];
    DPRINT("file name: %s\n", argv[1]);
    ifstream fin(argv[1]);
    if (!fin) {
        cerr << "Failed to open input file: " << argv[1] << endl;
        exit(-1);
    }
    int N;
    fin >> N;
    DPRINT("Number of inputs: %d\n", N);
    int caseNo = 1;
    char name[NAME_SIZE];
    while (N > 0) {
        engines.clear();
        queries.clear();
        int eng_count;
        fin >> eng_count;
        DPRINT("********* Case no: %d ******** , eng_count: %d\n", caseNo, eng_count);
        while (eng_count > 0) {
            proceed(fin);
            fin.getline(name, NAME_SIZE);
            engines.push_back(string(name));
            eng_count--;
        }
        int query_count;
        fin >> query_count;
        DPRINT("Query count: %d\n", query_count);
        while (query_count > 0) {
            proceed(fin);
            fin.getline(name, NAME_SIZE);
            queries.push_back(string(name));
            query_count--;
        }

        printOut(caseNo, getMinNumberOfShifts());

        caseNo++;
        N--;
    }

    fin.close();

    return 0;
}
