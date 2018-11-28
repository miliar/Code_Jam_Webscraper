#include <vector>
#include <fstream>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;

typedef long long ll;

int main(){

	ifstream in("A-large.in");
	ofstream out("output.out");

	long long N;
	in>>N;
 
	for(int i=0;i<N;i++){
        long long  P,K,L;
        in>>P;
        in>>K;
        in>>L;
        vector <ll> letters;

        for(int j=0;j<L;j++){
            long long temp;
            in>>temp;
            letters.push_back(temp);
        }

        sort(letters.begin(),letters.end());
        reverse(letters.begin(),letters.end());

        long long count=0;
        ll pos=0;
        for(int j=0;j<letters.size();j++){
           if((j%K)==0)
               pos++;

           count+=letters[j]*pos;
        }
       
        
        
      
		out<<"Case #"<<(i+1)<<": "<<count<<endl;
 
	}
	
	//int a;
    //cin>>a;

	return 0;


}
