#include <vector>
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
#include <string>
#include <cstring>

using namespace std;
#define CX(r,c) (vs[r][c]=='X' || vs[r][c]=='T')
#define CY(r,c) (vs[r][c]=='O' || vs[r][c]=='T')


void doit(){
    vector <string> vs (4);
    cin>>vs[0]>>vs[1]>>vs[2]>>vs[3];
    if (CX(0,0) && CX(0,1) && CX(0,2) && CX(0,3)){cout<<"X won"<<endl;return;}
    if (CX(1,0) && CX(1,1) && CX(1,2) && CX(1,3)){cout<<"X won"<<endl;return;}
    if (CX(2,0) && CX(2,1) && CX(2,2) && CX(2,3)){cout<<"X won"<<endl;return;}
    if (CX(3,0) && CX(3,1) && CX(3,2) && CX(3,3)){cout<<"X won"<<endl;return;}
    if (CX(0,0) && CX(1,0) && CX(2,0) && CX(3,0)){cout<<"X won"<<endl;return;}
    if (CX(0,1) && CX(1,1) && CX(2,1) && CX(3,1)){cout<<"X won"<<endl;return;}
    if (CX(0,2) && CX(1,2) && CX(2,2) && CX(3,2)){cout<<"X won"<<endl;return;}
    if (CX(0,3) && CX(1,3) && CX(2,3) && CX(3,3)){cout<<"X won"<<endl;return;}
    if (CX(0,0) && CX(1,1) && CX(2,2) && CX(3,3)){cout<<"X won"<<endl;return;}
    if (CX(3,0) && CX(2,1) && CX(1,2) && CX(0,3)){cout<<"X won"<<endl;return;}

    if (CY(0,0) && CY(0,1) && CY(0,2) && CY(0,3)){cout<<"O won"<<endl;return;}
    if (CY(1,0) && CY(1,1) && CY(1,2) && CY(1,3)){cout<<"O won"<<endl;return;}
    if (CY(2,0) && CY(2,1) && CY(2,2) && CY(2,3)){cout<<"O won"<<endl;return;}
    if (CY(3,0) && CY(3,1) && CY(3,2) && CY(3,3)){cout<<"O won"<<endl;return;}
    if (CY(0,0) && CY(1,0) && CY(2,0) && CY(3,0)){cout<<"O won"<<endl;return;}
    if (CY(0,1) && CY(1,1) && CY(2,1) && CY(3,1)){cout<<"O won"<<endl;return;}
    if (CY(0,2) && CY(1,2) && CY(2,2) && CY(3,2)){cout<<"O won"<<endl;return;}
    if (CY(0,3) && CY(1,3) && CY(2,3) && CY(3,3)){cout<<"O won"<<endl;return;}
    if (CY(0,0) && CY(1,1) && CY(2,2) && CY(3,3)){cout<<"O won"<<endl;return;}
    if (CY(3,0) && CY(2,1) && CY(1,2) && CY(0,3)){cout<<"O won"<<endl;return;}

    for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(vs[i][j]=='.'){cout<<"Game has not completed"<<endl;return;}

    cout<<"Draw"<<endl;


    return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
      cout<<"Case #"<<i<<": ";
      doit();
    }
    return 0;
}

