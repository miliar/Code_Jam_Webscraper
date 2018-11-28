#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <limits>
#include <algorithm>

using namespace std;

//struct _2int {int index; int t;};

int main(int argc, char** argv)
{
        ofstream ofs("output");
        ofs.close();
        ifstream ifs(*(++argv));
        if (!ifs)
        {
                cout << "no file" << endl;
                return 1;
        }

        int caseNum;
        ifs >> caseNum;
        
        for (int caseX = 0; caseX < caseNum; ++caseX)
        {
                // parse
                int P, K, L, t;
                vector<int> vec;
//                _2int tmp;
                
                ifs >> P;
                ifs >> K;
                ifs >> L;
                
                for (int i = 0; i < L; ++i)
                {
//                        tmp.index = 0;
                        ifs >> t;
                        vec.push_back(t);
                }
                sort(vec.begin(), vec.end());
/*                
                for (int i = L-1; i >= 0; --i)
                        cout << vec[i] << " ";
                cout << endl;
                cout << "K = " << K << endl;
*/                
                int sum = 0;
                int foo = 0;
                for (int i = L-1; i >= 0; i-=K)
                {
                        foo = 0;
                        for (int j = 0; j < K; ++j)
                        {
                                if (i-j < 0) break;
//                                cout << vec[i-j] << " ";
                                foo += vec[i-j];
                        }
                        sum += foo * ((L-i)/K+1);
//                        cout << foo << " ";
//                        cout << sum << endl;
                }
                

                ofs.open("output", ios::app);
                ofs << "Case #" << caseX+1 << ": " << sum << endl;
                ofs.close();
        }

        return 0;
}
