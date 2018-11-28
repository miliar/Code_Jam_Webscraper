#define _NOMINMAX

#include <stdio.h>
#include <math.h>

#include <assert.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

namespace{
    int rle(const string& str)
    {
        if(str.empty()){
            return 0;
        }
        int ret=1;
        int i=1;
        char prev = str[0];
        while(i!=str.size()){
            if(str[i] != prev){
                ret++;
                prev = str[i];
            }
            ++i;
        }

        return ret;
    }
    string perm(const std::vector<int> p,const string& str)
    {
        const int n = p.size();
        string ret;
        for(int i=0;i!=str.size();++i){
            ret += str[i/n*n + p[i%n]];
        }
        return ret;
    }

    std::vector<std::vector<int> >perms(int k){
        std::vector<std::vector<int> > ret;
        if(k==1){
            std::vector<int> p(1);
            p[0] = 0;
            ret.push_back(p);
        }
        else{
            std::vector<std::vector<int> > ps = perms(k-1);
            for(int i=0;i!=ps.size();++i){
                for(int j=0;j!=k;++j){
                    std::vector<int> p = ps[i];
                    p.insert(p.begin()+j,k-1);
                    ret.push_back(p);
                }
            }
        }
        return ret;
    }

    int get_result(int k,const string& str)
    {
        int ret(str.size());

        std::vector<std::vector<int> > ps = perms(k);

        for(int i=0;i!=ps.size();++i){
            const int l = rle(perm(ps[i],str));
            if(l < ret){
                ret = l;
            }
        }


        return ret;
    }
}

int main(int argc, char* argv[])
{
    int n_cases(0);
    cin >> n_cases;

    for(int c=0;c!=n_cases && !std::cin.eof();++c){
        int k;
        cin >> k;
        string str;
        cin >> str;

        std::cout << "Case #"<<(c+1)<<": "<< get_result(k,str) <<"\n";
    }
	return 0;
}
