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
    const int IMPOSSIBLE = 1<<16;

    struct node{
        bool changeable;
        bool is_and;
        int i_child[2];
        bool b;
    };

    bool get_value(const std::vector<node> &nodes,int i_target)
    {
        const node& n = nodes[i_target];

        if(n.i_child[0] < 0){
            return n.b;
        }

        const bool b1 = get_value(nodes,n.i_child[0]);
        const bool b2 = get_value(nodes,n.i_child[1]);

        bool b;
        if(n.is_and){
            b = b1&&b2;
        }
        else{
            b = b1||b2;
        }
        return b;
    }


    int get_steps(const std::vector<node> &nodes,int i_target,bool desired_value)
    {
        const node& n = nodes[i_target];

        if(n.i_child[0] < 0){
            if(n.b != desired_value){
                return IMPOSSIBLE;//IMPOSSIBLE
            }
            else{
                return 0;
            }
        }

        const bool b1 = get_value(nodes,n.i_child[0]);
        const bool b2 = get_value(nodes,n.i_child[1]);

        bool b;
        if(n.is_and){
            b = b1&&b2;
        }
        else{
            b = b1||b2;
        }

        if(b == desired_value){
            return 0;
        }

        if(n.changeable){
            if(n.is_and){
                if(desired_value){
                    if(b1 || b2){
                        return 1;
                    }
                    else{
                        return 1+min(get_steps(nodes,n.i_child[0],true),get_steps(nodes,n.i_child[1],true));
                    }
                }
                else{
                    return min(get_steps(nodes,n.i_child[0],false),get_steps(nodes,n.i_child[1],false));
                }
            }
            else{
                if(desired_value){
                    return min(get_steps(nodes,n.i_child[0],true),get_steps(nodes,n.i_child[1],true));
                }
                else{
                    if(!b1 || !b2){
                        return 1;
                    }
                    else{
                        return 1+min(get_steps(nodes,n.i_child[0],false),get_steps(nodes,n.i_child[1],false));
                    }
                }
            }
        }
        else{
            if(n.is_and){
                if(desired_value){
                    if(b1){
                        return get_steps(nodes,n.i_child[1],true);
                    }
                    else if(b2){
                        return get_steps(nodes,n.i_child[0],true);
                    }
                    else{
                        return get_steps(nodes,n.i_child[0],true) + get_steps(nodes,n.i_child[1],true);
                    }
                }
                else{
                    return min(get_steps(nodes,n.i_child[0],false),get_steps(nodes,n.i_child[1],false));
                }
            }
            else{
                if(desired_value){
                    return min(get_steps(nodes,n.i_child[0],true),get_steps(nodes,n.i_child[1],true));
                }
                else{
                    if(!b1){
                        return get_steps(nodes,n.i_child[1],false);
                    }
                    else if(!b2){
                        return get_steps(nodes,n.i_child[0],false);
                    }
                    else{
                        return get_steps(nodes,n.i_child[0],false) + get_steps(nodes,n.i_child[1],false);
                    }
                }
            }
        }
    }

    std::string get_result(const std::vector<node> &nodes,bool desired_value)
    {
        const int r = get_steps(nodes,0,desired_value);

        if(r>=IMPOSSIBLE){
            return "IMPOSSIBLE";
        }

        char str[1024];
        sprintf(str,"%d",r);
        return str;
    }
}

int main(int argc, char* argv[])
{
    int n_cases(0);
    cin >> n_cases;

    for(int c=0;c!=n_cases && !std::cin.eof();++c){
        int n_nodes(0);
        cin >> n_nodes;

        int desired_value(0);
        cin >> desired_value;

        std::vector<node> nodes;

        for(int i=0;i!=(n_nodes-1)/2;++i){
            int g,c;
            cin >> g;
            cin >> c;
            node n;
            n.is_and = g!=0;
            n.changeable = c!=0;
            n.i_child[0] = 2*(i+1)-1;
            n.i_child[1] = 2*(i+1);
            nodes.push_back(n);
        }
        for(int i=(n_nodes-1)/2;i!=n_nodes;++i){
            int b;
            cin >> b;
            node n;
            n.is_and = n.changeable = false;
            n.i_child[0] = n.i_child[1] = -1;
            n.b = b!=0;
            nodes.push_back(n);
        }
        std::cout << "Case #"<<(c+1)<<": "<< get_result(nodes,desired_value!=0) <<"\n";
    }
	return 0;
}
