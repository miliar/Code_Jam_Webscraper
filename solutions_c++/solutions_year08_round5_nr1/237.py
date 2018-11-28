#define _NOMINMAX

#include <stdio.h>
#include <math.h>
#include <float.h>
#include <assert.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <boost/foreach.hpp>

#define foreach BOOST_FOREACH

using namespace std;

namespace{
    struct action{
        string s;
        int t;
    };
    struct edge{
        int x,y;//left-top
        int l;
    };
    int get_result(const vector<action>& actions){
        int dx(0),dy(-1);
        int x(0),y(0);
        int l(0);
        vector<edge> v_edges,h_edges;
        foreach(const action& a,actions){
            const int t = a.t;
            const string& s = a.s;
            for(int i=0;i!=t;++i){
                for(int j=0;j!=s.length();++j){
                    switch(s[j]){
                        case 'F':
                            x += dx;
                            y += dy;
                            l++;
                            break;
                        case 'R':
                            if(l>0){
                                edge e;
                                e.x = x + ((dx>0)?-l:0);
                                e.y = y + ((dy>0)?-l:0);
                                e.l = l;

                                if(dx){
                                    h_edges.push_back(e);
                                }
                                else{
                                    v_edges.push_back(e);
                                }
                            }
                            swap(dx,dy);
                            dx = -dx;
                            l = 0;
                            break;
                        case 'L':
                            if(l>0){
                                edge e;
                                e.x = x + ((dx>0)?-l:0);
                                e.y = y + ((dy>0)?-l:0);
                                e.l = l;

                                if(dx){
                                    h_edges.push_back(e);
                                }
                                else{
                                    v_edges.push_back(e);
                                }
                            }
                            swap(dx,dy);
                            dy = -dy;
                            l = 0;
                            break;
                        default:
                            assert(0);
                    }
                }
            }
        }

        if(l>0){
            edge e;
            e.x = x + ((dx>0)?-l:0);
            e.y = y + ((dy>0)?-l:0);
            e.l = l;

            if(dx){
                h_edges.push_back(e);
            }
            else{
                v_edges.push_back(e);
            }
        }

        int ret(0);
        for(int y=-100;y<=100;++y){
            for(int x=-100;x<=100;++x){
                int nl(0),nr(0),nu(0),nd(0);
                foreach(const edge& e,h_edges){
                    if(e.x <= x+0.5 && x+0.5 <= e.x + e.l){
                        if(y+0.5 < e.y){
                            nu++;
                        }
                        else{
                            nd++;
                        }
                    }
                }
                foreach(const edge& e,v_edges){
                    if(e.y <= y+0.5 && y+0.5 <= e.y + e.l){
                        if(x+0.5 < e.x){
                            nl++;
                        }
                        else{
                            nr++;
                        }
                    }
                }
                if((nu%2==0 && nd%2==0 && nu>0 && nd>0) || (nl%2==0 && nr%2==0 && nl>0 && nr > 0)){
                    ret++;
                }
            }
        }
        return ret;
    }
}

int main(int argc, char* argv[])
{
    istream& is = ifstream("A-small-attempt0.in");

    int n_cases(0);
    is >> n_cases;

    for(int c=0;c!=n_cases && !std::cin.eof();++c){
        int l;
        is >> l;
        std::vector<action> actions(l);
        for(int i=0;i!=l;++i){
            action &a = actions[i];
            is >> a.s >> a.t;
        }
        std::cout.precision(20);
        std::cout << "Case #"<<(c+1)<<": "<< get_result(actions) <<"\n";
    }
	return 0;
}
