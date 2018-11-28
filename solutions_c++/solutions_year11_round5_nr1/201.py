#include <iostream>
#include <vector>
using namespace std;


struct Point {
    long double x, y;
};


vector<Point> A, B;
int W, L, U, G;


long double sum(long double xx, const vector<Point>& v) {
    int i=0;
    long double s = 0;
    while (v[i+1].x < xx) {
        assert(i+1<v.size());
        s+=(v[i+1].x-v[i].x)*(v[i].y+v[i+1].y)/2;
        i++;
    }
    
     long double a=xx-v[i].x;
     long double b=v[i+1].x-xx;
//      s+= (v[i].y*b+v[i+1].y*a)/(a+b)/2 * a;
    s+= a * (v[i].y + (v[i].y*b+v[i+1].y*a)/(a+b)) / 2;
    
    return s;
}


int main() {
    int Z; cin>>Z;
    for (int z=1; z<=Z; z++) {
        A.clear(), B.clear();
        
        cin>>W>>L>>U>>G;
        for (int i=0; i<L; i++) {
            Point p; cin>>p.x>>p.y; //p.y+=1000;
            A.push_back(p);
        }
        for (int i=0; i<U; i++) {
            Point p; cin>>p.x>>p.y; //p.y+=1000;
            B.push_back(p);
        }
        
        
        long double totalSum = sum(B.back().x, B) - sum(A.back().x, A);
//         cout<<"total"<<sum(B.back().x, B)<<" "<<sum(A.back().x, A)<<endl;
        
        cout<<"Case #"<<z<<":"<<endl;
        
        for (int g=1; g<G; g++) {
            long double expected = totalSum/G*g;
            
            long double x0=A.front().x, x1=A.back().x;
            while (x1-x0 > 0.0000000001) {
                long double xx = (x0+x1)/2;
                long double s = sum(xx, B) - sum(xx, A);
                if (s<expected) x0=xx;
                else x1=xx;
            }
            cout.precision(13);
            cout<<(x0+x1)/2<<endl;
        }
        
    }
    
    return 0;
}
