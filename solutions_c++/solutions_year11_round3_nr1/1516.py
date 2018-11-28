#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

#define fi(n) for(int i=0;i< n;i++)
#define fj(n) for(int j=0;j< n;j++)
#define fk(n) for(int k=0;k< n;k++)

using namespace std;
		   
int main()
{
    bool imp;
 	int cases;
	int xs;
	int ys;
    char tmp;
	char tiles[51][51];
    cin >> cases;
	fi(cases){
        imp=false;
		cin >> xs;
		cin >> ys;
        fj(51){
            fk(51){
                tiles[j][k] = 0;
            }
        }
        fj(xs){
            fk(ys){
                tmp='\n';
                while(tmp=='\n'){
                    cin.get(tmp);
                    if(tmp!='\n')
                        tiles[j][k] = tmp;
                }
            }
        }
        fj(xs){
            fk(ys){
                if(tiles[j][k]=='#'){
                    if(tiles[j+1][k]=='#' && tiles[j][k+1]=='#' && tiles[j+1][k+1]=='#'){
                        tiles[j][k] = '/';
                        tiles[j+1][k] = '\\';
                        tiles[j][k+1] = '\\';
                        tiles[j+1][k+1] = '/';
                    }
                    else{
                        imp=true;       
                    }
                }
                if (imp==true)
                    break;
            }
            if (imp==true)
                break;
        }
        
        cout << "Case #" << i+1<< ":" << endl;
        if(imp==true)
            cout << "Impossible" << endl;
        else{
            fj(xs){
                fk(ys){
                    cout << tiles[j][k];
                }
                cout << endl;
            }
        }
	}      
	return 0;
		     
}

