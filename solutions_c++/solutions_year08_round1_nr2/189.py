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
    struct customer{
        vector<pair<int,bool> > types;//<flavor,malted>
    };

    std::string get_result(int n_flavors,const vector<customer>& customers)
    {
        const int n_customers = customers.size();
        vector<bool> malted(n_flavors,false);

        while(1){
            bool updated(false);
            bool all_customers_satisfied(true);

            for(int i=0;i!=n_customers;++i){
                bool satisfied(false);
                const customer& c = customers[i];
                const int n_types = c.types.size();
                for(int j=0;j!=n_flavors && !satisfied;++j){
                    for(int k=0;k!=n_types;++k){
                        if(c.types[k].first == j && c.types[k].second == malted[j]){
                            satisfied = true;
                            break;
                        }
                    }
                }
                if(!satisfied){
                    all_customers_satisfied = false;
                    for(int k=0;k!=n_types;++k){
                        if(c.types[k].second){
                            if(!malted[c.types[k].first]){
                                malted[c.types[k].first] = true;
                                updated = true;
                            }
                            break;
                        }
                    }
                }
            }

            if(all_customers_satisfied){
                break;
            }
            if(!updated){
                return "IMPOSSIBLE";
            }
        }

        std::string ret;
        for(int i=0;i!=n_flavors;++i){
            ret += (malted[i]?"1":"0");
            if(i < n_flavors-1)ret+=" ";
        }
        return ret;
    }
}

int main(int argc, char* argv[])
{
    int n_cases(0);
    cin >> n_cases;

    for(int c=0;c!=n_cases && !std::cin.eof();++c){
        int n_flavors(0);
        cin >> n_flavors;

        int n_customers(0);
        cin >> n_customers;

        vector<customer> customers;

        for(int i=0;i!=n_customers;++i){
            int n_types(0);
            cin >> n_types;
            customer c;
            for(int j=0;j!=n_types;++j){
                int flavor(0),malted(0);
                cin >> flavor;
                cin >> malted;
                c.types.push_back(make_pair(flavor-1,malted!=0));
            }
            customers.push_back(c);
        }
        std::cout << "Case #"<<(c+1)<<": "<< get_result(n_flavors,customers) <<"\n";
    }
	return 0;
}
