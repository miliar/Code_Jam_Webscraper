#include <fstream>
#include <set>
#include <iostream>

using namespace std;

ifstream f("input.in");
ofstream g("output.out");

int a, b, t, rez;
int Nr;
set<pair<int,int> > s;

void citeste(){

    f >> t;

}

int cate(int x){

    int nr = 1;
    while(x){
        nr*=10;
        x/=10;
    }

    return nr;

}

int convert(int val, int y){

    Nr = y%val;
    int j = y / val;
    Nr *= cate(j);
    Nr += j;

    if (Nr < y && Nr >= a){
         return 1;

    }
    return 0;


}

void rezolva(){

    for(int i=1; i<=t; i++){
        f >> a >> b;
        //g << "Case #" << i <<": ";
        s.clear();
        for(int j=a; j<=b; j++){
            int x = j;
            int cnt = 10;
            while(cnt <= x){
                if (convert(cnt,x)){
                    s.insert(make_pair(min(Nr,x), max(Nr,x)));
                }
                cnt *= 10;
            }
        }
        g<<"Case #"<<i<<": "<<s.size()<<'\n';
    }


}

int main(){

    citeste();
    rezolva();

    f.close();
    g.close();

    return 0;

}
