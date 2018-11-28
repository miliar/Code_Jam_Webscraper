#include <cstdio>
#include <vector>
using namespace std;

vector<int>o,b;
vector<bool> turn;


main(){
    int t,n,aux,posO,posB,time,ato,atb;
    char c;
    scanf("%d",&t);
    for(int k=1;k<=t;k++){
        o.clear();
        b.clear();
        posO = posB =1;
        time = 0;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
           scanf(" %c %d",&c,&aux);
           if(c=='O'){ o.push_back(aux); turn.push_back(true);}
           else {b.push_back(aux); turn.push_back(false);}
        }
        while(o.size() !=0 || b.size() !=0){
            if(o.size()!=0) ato= o.front();
            if(b.size()!=0) atb= b.front();
            bool at = turn.front();

            if(posO < ato) posO++;
            else if(posO > ato)  posO--;
            else if( at ){ o.erase(o.begin()); turn.erase(turn.begin());}

            if(posB < atb) posB++;
            else if(posB > atb)  posB--;
            else if( !at ){ b.erase(b.begin()); turn.erase(turn.begin());}
            time++;
            //printf(at?"O %d\n":"B %d\n", at?posO:posB);
        }

        printf("Case #%d: %d\n",k,time);

    }
return 0;
}
