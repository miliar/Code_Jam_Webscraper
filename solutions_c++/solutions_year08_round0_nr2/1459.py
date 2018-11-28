#include <iostream>
#include <string>
#include <sstream>
#include <list>
#include <vector> 
#include <algorithm> 

using namespace std;

#define CASE(x) "Case #" << x << ": " 
#define TIME_PARSE(str) (((int)(str[0]-'0')*10+(int)(str[1]-'0'))*60+(int)(str[3]-'0')*10+(int)(str[4]-'0'))

string linebuf; 
#define cinline getline(cin, linebuf);\
		stringstream(linebuf)

void process_case()
{
    vector<int> SideA, SideB;
    vector<int>::iterator it; 
    string Time1, Time2; 
    int T, NA, NB, StartA, StartB, AtA, AtB; 
    StartA = StartB = AtA = AtB = 0; 
    cinline >> T; 
    cinline >> NA >> NB; 
    for (int j = 0; j < NA; j++) {
	cin >> Time1 >> Time2; 
	SideA.push_back(TIME_PARSE(Time1) * 2 + 1); 
	SideB.push_back((TIME_PARSE(Time2) + T) * 2); 
    }
    for (int k = 0; k < NB; k++) {
	cin >> Time1 >> Time2; 
	SideB.push_back(TIME_PARSE(Time1) * 2 + 1); 
	SideA.push_back((TIME_PARSE(Time2) + T) * 2); 
    }
    cin.ignore();
    sort(SideA.begin(), SideA.end()); 
    sort(SideB.begin(), SideB.end()); 
    for (it = SideA.begin(); it != SideA.end(); it++) {
	if (*it%2) 
	    if (AtA == 0) 
		StartA++; 
	    else 
		AtA--; 
	else 
	    AtA++; 
    }
    for (it = SideB.begin(); it != SideB.end(); it++) {
	if (*it%2) 
	    if (AtB == 0) 
		StartB++; 
	    else 
		AtB--; 
	else 
	    AtB++; 
    } 
    cout << StartA << " " << StartB; 
}

int main(int argc, char* argv[])
{
    int cases; 
    cinline >> cases;  
    for (int i = 1; i <= cases; i++) {
	cout << CASE(i); 
	process_case();
	cout << endl; 
    }
}
