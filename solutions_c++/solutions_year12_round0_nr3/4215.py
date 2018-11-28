#include <assert.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

/*
int ElapsedTime(const vector<int>& vecButtons, int index) {
	return abs(vecButtons[index] - vecButtons[index - 1]);
}
*/

#define M 9
int C[M][M] = {0};
void getC() {
    for (int i=0; i<M; i++) {
        C[i][0] = 0; 
        C[i][1] = i;
        C[i][i] = 1;
    }

    for (int i=3; i<M; i++) {
        for (int j=2; j<i; j++) {
            C[i][j] = C[i-1][j-1] + C[i-1][j];
        }
    }
}

void getNumbers(vector<int> &vec, int a, int b, int n)
{
    vec.push_back(n);
    int i = 1; 
    int nn = n; 
    while (nn > 9) {
        nn = nn / 10; 
        i++;
    }
    int p = 1; 
    for (int ii = 1; ii < i; ii++)
    {
        p = p * 10;
    }
 
    nn = n;
    while (i > 1) {
        i--;
         
        int lastNum = nn - nn / 10 * 10;
        
        int newNum = lastNum * p + nn / 10;
        if ((newNum >= a) && (newNum <= b))
        {
            if (find(vec.begin(), vec.end(), newNum) == vec.end()) {
                vec.push_back(newNum);
            }
        }
        nn = newNum;
    }
}

int main(int argc, char* argv[]) {
    
	if (argc != 2) {
		cerr << "wrong number of parameter" << endl;
		return -1;
	}

	ifstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}
    
    getC();

	string ln;  
    char buf[200] = {0};
    inf.getline(buf, 200);

    int n = atoi(buf);
    
	for (int i=0; i<n; i++) 
    {
        int a = 0, b = 0;
        int allNum = 0; 

        string str; 
        inf >> str; a = atoi(str.c_str());
        inf >> str; b = atoi(str.c_str());

        list<int> vec;
        for (int ii=a; ii<=b; ii++)
            vec.push_back(ii);

        list<int>::iterator iter = vec.begin();
        while (iter != vec.end()) {
            int num = *iter; 
            vector<int> newVec; 
            getNumbers(newVec, a, b, num);
            if (newVec.size() > 1) {
                allNum += C[newVec.size()][2];
            }
            vec.erase(vec.begin());
            for (int nn=1; nn<newVec.size(); nn++) {
                list<int>::iterator newIter = find(vec.begin(), vec.end(), newVec[nn]);
                if (newIter != vec.end())
                    vec.erase(newIter);
            }
            iter = vec.begin();
        }

		// find solution
		cout << "Case #" << i+1 << ": " << allNum << endl;
	}

	return 0;
}

