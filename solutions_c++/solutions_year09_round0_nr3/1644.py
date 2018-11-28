#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <functional>
#include <iterator>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <cassert>
#include <list>

using namespace std;

#define FOR(i, l, u) for(int (i)=(l); (i) < (u); ++(i))
#define FORD(i, u, l) for(int (i) = (u); (i) >= (l); --(i))
#define SHIFTL(i,n) ((i) << (n))
#define SHIFTR(i,n) ((i) >> (n))
#define POW2(n) SHIFTL(1, n)

typedef vector<int> v_int;
typedef vector<string> v_string;
typedef map<string, int> map_s;
typedef set<string> set_s;
typedef set<int> set_i;
typedef pair<int,int> pair_i;

long long total_count = 0;

string Match="welcome to code jam";

void process(string x,int index,int len_matched,int length){
                          if(len_matched==19){
                                                  total_count++;
                                                  return;
                              }
                              if(index==length)
                                               return;
    
                              else{
                                   if(x[index]==Match[len_matched])
                                                                   process(x,index+1,len_matched+1,length);
                              }
                              process(x,index+1,len_matched,length);
}

int main() {
	int n;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
    fin>>n;
    string s;
    getline(fin,s);
    for(int i=0;i<n;i++){
            getline(fin,s);
            total_count = 0;
            process(s,0,0,s.length());
            fout<<"Case #"<<i+1<<": "<<setw(4)<<setfill('0')<<right<<total_count%10000<<endl;       
    }
	return 0;
}
