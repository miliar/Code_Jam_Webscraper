#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int stanje[1<<30];
vector< pair<bool, bool> > bulbs; // first = power, second = on/off

int provjeri(){
    int sol = 0;
    string s = "";
    for(int x = 0;x<(int)bulbs.size();++x)
        if( bulbs[x].first == true && bulbs[x].second == true )sol = sol | (1<<x);
    return sol;
}

int main(){
    int test,n,k;
    scanf("%d",&test);
    bulbs.push_back( make_pair(0,0) );
    for(int x = 0;x<29;++x){
        bulbs.push_back( make_pair(0,0) );
    }

    for(int x = 0;x<100000100;++x){
        bulbs[0].second = !bulbs[0].second;
        for(int y = 1;y<(int)bulbs.size();++y){
            if( bulbs[y-1].first == true) bulbs[y].second = !bulbs[y].second;
        }
        if( bulbs[0].second == true ) bulbs[0].first = true; else bulbs[0].first = false;
        for(int y = 1;y<(int)bulbs.size();++y){
            if( bulbs[y-1].first == true && bulbs[y].second == true) bulbs[y].first = true; else bulbs[y].first = false;
        }
        stanje[x] = provjeri();
    }
    
    for(int x = 0;x<test;++x){
        scanf("%d %d",&n,&k);
        --k;
        --n;
        /*   for(int y = 0;y<10;++y)
            if( (stanje[k]&(1<<y)) > 0 ) printf("1"); else printf("0");
            printf("\n");*/
        if( (stanje[k]&(1<<n)) > 0 ) printf("Case #%d: ON\n",x+1); else printf("Case #%d: OFF\n",x+1);
    }
    return 0;
}
