
#include <iostream>
#include <vector>

// 3
// 4 O 2 B 1 B 2 O 4
// 3 O 5 O 8 B 100
// 2 B 2 B 1

using namespace std;
typedef std::vector<int> VI;
typedef std::vector<char> VC;

class Combiner {
public:
    Combiner(char c1, char c2, char r) :
        _c1(c1), _c2(c2), _r(r)
    {}
    bool combines(char t1, char t2) const {
        if ((t1 == _c1 && t2 == _c2) || (t1 == _c2 && t2 == _c1)) {
            return true;
        }
        return false;
    }
    char result() const {
        return _r;
    }
        
private:
    char _c1;
    char _c2;
    char _r;
};

class Opposer {
public:
    Opposer(char c1, char c2) :
        _c1(c1), _c2(c2)
    {}
    bool opposes(char t1, char t2) const {
        if ((t1 == _c1 && t2 == _c2) || (t1 == _c2 && t2 == _c1)) {
            return true;
        }
        return false;
    }
private:
    char _c1;
    char _c2;
};

class ElementList {
public:
    ElementList(vector<Combiner> &combiners, vector<Opposer> &opposers) :
        _combiners(combiners), _opposers(opposers)
    {}

    void invoke(char c) {
        if (_elem.size() == 0) {
            _elem.push_back(c);
        } else {
            unsigned int l = _elem.size() - 1;
            bool do_append = true;
            for (vector<Combiner>::const_iterator i = _combiners.begin(); i != _combiners.end(); ++i) {
                if (i->combines(c, _elem[l])) {
                    _elem[l] = i->result();
                    do_append = false;
                    break;
                }
            }
            if (do_append) {
                _elem.push_back(c);
                l++;
            }
            for (vector<char>::const_iterator i = _elem.begin(); i != _elem.end(); ++i) {
                bool stop = false;
                for (vector<Opposer>::const_iterator j = _opposers.begin(); j != _opposers.end(); ++j) {
                    if (j->opposes(_elem[l], *i)) {
                        _elem.clear();
                        stop = true;
                        break;
                    }
                }
                if (stop) break;
            }
        }           

    }

    void out(ostream &o) {
        o << "[";
        for (unsigned int i = 0; i < _elem.size(); i++) {
            o << _elem[i];
            if (i+1 != _elem.size()) {
                o << ", ";
            }
        }
        o << "]";
    }
    
private:
    vector<Combiner> &_combiners;
    vector<Opposer> &_opposers;
    vector<char> _elem;
};
    


void
do_test(int test_num, vector<Combiner> &combiners, vector<Opposer> &opposers, vector<char> &elements)

{
    ElementList e(combiners, opposers);
    for (vector<char>::const_iterator i = elements.begin(); i != elements.end(); ++i) {
        e.invoke(*i);
    }
    
    cout << "Case #" << test_num << ": ";
    e.out(cout);
    cout << endl;
}

int
main(int argc, char **argv)
{
    int num_tests = 0;

    cin >> num_tests;

    for (int i = 1; i <= num_tests; ++i) {
        int num_combiners = 0;
        int num_opposers = 0;
        int num_elements = 0;

        vector<Combiner> combiners;
        vector<Opposer> opposers;
        vector<char> elements;
        cin >> num_combiners;
        for (int j = 0; j < num_combiners; j++) {
            char c1, c2, r;
            cin >> c1;
            cin >> c2;
            cin >> r;
            combiners.push_back(Combiner(c1, c2, r));
        }
        cin >> num_opposers;
        for (int j = 0; j < num_opposers; j++) {
            char c1, c2;
            cin >> c1;
            cin >> c2;
            opposers.push_back(Opposer(c1, c2));
        }
        cin >> num_elements;
        for (int j = 0; j < num_elements; j++) {
            char c;
            cin >> c;
            elements.push_back(c);
        }
            

        do_test(i, combiners, opposers, elements);

    }
}
    
