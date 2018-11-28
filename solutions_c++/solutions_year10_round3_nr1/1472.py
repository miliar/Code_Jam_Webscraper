#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

class Point {
    int den;
    int num1;
    int num2;
public:
    Point(int den, int num1, int num2) {
        this->den = den;
        this->num1 = num1;
        this->num2 = num2;
    }
    bool equals(const Point* p) {
        if (den * p->num1 != p->den * num1) return false;
        if (den * p->num2 != p->den * num2) return false;
        return true;
    }
    static Point* get_crossing(int li, int ri, int lj, int rj) {
        if ((li < lj) == (ri < rj)) return NULL;
        int dr = ri - rj;
        int dl = li - lj;
        int ca = lj - li;
        int bcad = ri * lj - rj * li;
        return new Point(dr - dl, ca, bcad);
    }
    string to_string() const {
        ostringstream ost;
        ost << "(" << (float)num1 / den << ", " << (float)num2 / den << ")";
        return ost.str();
    }
};

int main(int argc, char** argv) {
    int T;
    int N;
    cin >> T;
    for ( int cn = 1; cn <= T; cn++) {
        cin >> N;
        int num_intersections = 0;
        vector<pair<int,int> > lines;
        vector<Point*> points;
        //vector<pair<int, int> > points;
        for (int i = 0; i < N; i++) {
            int li, ri;
            cin >> li >> ri;
            for (int j = 0; j < (int)lines.size(); j++) {
                int lj = lines[j].first;
                int rj = lines[j].second;
                //if ((li < lj) != (ri < rj)) {
                Point* p = Point::get_crossing(li, ri, lj, rj);
                if (p != NULL) {
                    //cout << p->to_string() << endl;
                    bool not_unique = false;
                    for (int k = 0; k < (int)points.size(); k++) {
                        if (p->equals(points[k])) {
                            //cout << p->to_string() << " == " << points[k]->to_string() << endl;
                            not_unique = true;
                            break;
                        }
                    }
                    if (!not_unique) {
                        num_intersections ++;
                        points.push_back(p);
                    } else {
                        delete p;
                    }
                }
            }
            lines.push_back(make_pair(li, ri));
        }
        for (int i = 0; i < (int)points.size(); i++) delete points[i];
        cout << "Case #" << cn << ": " << num_intersections << endl;
    }
}
