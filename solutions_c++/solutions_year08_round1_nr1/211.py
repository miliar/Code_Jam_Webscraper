#define _NOMINMAX

#include <stdio.h>
#include <tchar.h>
#include <math.h>

#include <assert.h>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

namespace{
    int get_result(const vector<int>& v1,const vector<int>& v2)
    {
        assert(v1.size() == v2.size());
        const int n = v1.size();

        vector<int> v3(v1);
        std::sort(v3.begin(),v3.end());
        vector<int> v4(v2);
        std::sort(v4.rbegin(),v4.rend());

        int ret(0);

        for(int i=0;i!=n;++i){
            ret += v3[i]*v4[i];
        }

        return ret;
    }
}

int main(int argc, char* argv[])
{
    int n_cases(0);
    cin >> n_cases;

    for(int c=0;c!=n_cases && !std::cin.eof();++c){
        int n_elements(0);
        cin >> n_elements;

        std::vector<int> v1(n_elements),v2(n_elements);
        for(int i=0;i!=n_elements;++i){
            cin >> v1[i];
        }
        for(int i=0;i!=n_elements;++i){
            cin >> v2[i];
        }

        std::cout << "Case #"<<(c+1)<<": "<< get_result(v1,v2) <<"\n";
    }
	return 0;
}
