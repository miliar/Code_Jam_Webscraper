#include <gmp.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

#include <algorithm>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;



int main(){


	ifstream input("A-large.in");
	ofstream output("A-large.out");
	string num;
	input >> num;
	int num_ = atoi(num.c_str());
	cout << num << endl;

	int count=1;
	string tmp;
	while(!input.eof() && count <= num_){
		int N=0;
		input>>N;
		int **m=new int*[N];
		for(int i=0;i<N;i++)
			m[i]=new int[2];

		for(int i=0;i<N;i++)
			input>>m[i][0]>>m[i][1];

		int num=0;
		for(int i=0;i<N;i++){
			for(int j=i;j<N;j++){
				if((m[i][0]-m[j][0])*(m[i][1]-m[j][1])<0)
					num++;
			}
		}
		output << "Case #" << count << ": " << num << endl;
		count++;
	}


	input.close();

}
