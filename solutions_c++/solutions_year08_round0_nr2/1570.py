#include "testcase.h"
#include <fstream>
#include <iostream>

using namespace std;
int solve(Station ts, int t);
//void reset(bool b, bool a[], int n);
void save(std::ostream& output, int resultA[], int resultB[], int n);
void load(istream & file, int n, TestCase result[]);
int main() {
    string temp  = "";
    std::ifstream input("input.txt");
    std::ofstream output("output.txt");
    int n;
    input >> n;
    TestCase testCases[n];
    getline(input, temp,'\n');
    load(input, n, testCases);
    int resultA[n];
    int resultB[n];
    int i = 0;
    while(i<n) {
        resultA[i] = solve(testCases[i].a, testCases[i].turnaround);
        resultB[i] = solve(testCases[i].b, testCases[i].turnaround);
        i++;
    }
    save(output,resultA, resultB, n);
    return 0;
}

int solve(Station ts, int t) {
    int a = 0;
    int d = 0;
    int trains = 0;
    int result = 0;
    bool flag = !(a>=ts.nArrivals||d>=ts.nDepartures);
    if(!flag) {
        while(d<ts.nDepartures) {
            trains--;
            d++;
            if(trains<result) result = trains;
        }
    }
    Time temp;
    while(flag) {
        temp = Time(ts.arrivals[a].hours,ts.arrivals[a].minutes);
        if(temp.addTime(t)<=ts.departures[d]) {
            trains++;
            a++;
        }
        else {
            trains--;
            d++;
            if(trains<result) result = trains;
        }
        if (a>=ts.nArrivals||d>=ts.nDepartures) flag = false;
        while(!flag&&d<ts.nDepartures) {
            trains--;
            d++;
            if(trains<result) result = trains;
        }
    }
    if(result>0) result =0;
    result = abs(result);
    return result;
}

void save(std::ostream& output, int resultA[], int resultB[], int n) {
    int i = 0;
    while(i<n) {
        output << "Case #" << (i+1) << ": " << resultA[i] << " " << resultB[i] << endl;
        i++;
    }
    output.flush();
}

void load(istream & file, int n, TestCase result[]) {
    string temp = "";
    int turnaround;
    int i = 0;
    while(i<n) {
        file >> turnaround;
        getline(file, temp,'\n');
        int tempH;
        int tempM;
        int a2b;
        int b2a;
        file >> a2b;
        file >> b2a;
        int j = 0;
        Time departuresA[a2b];
        Time departuresB[b2a];
        Time arrivals2A[b2a];
        Time arrivals2B[a2b];
        while(j<a2b){
            file >> tempH;
            getline(file, temp,':');
            file >> tempM;
            insert(Time(tempH,tempM), departuresA, j);
            file>> tempH;
            getline(file, temp,':');
            file>>tempM;
            insert(Time(tempH,tempM), arrivals2B,j);
            getline(file, temp, '\n');
            j++;
        }
        j= 0;
        while(j<b2a){
            file >> tempH;
            getline(file, temp,':');
            file >> tempM;
            insert(Time(tempH,tempM),departuresB, j);
            file>> tempH;
            getline(file, temp,':');
            file>>tempM;
            insert(Time(tempH,tempM),arrivals2A,j);
            getline(file, temp, '\n');
            j++;
        }
        result[i] = TestCase(arrivals2A, departuresA, arrivals2B, departuresB, a2b, b2a, turnaround);
        i++;
    }
}
