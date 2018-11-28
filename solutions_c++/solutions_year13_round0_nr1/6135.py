#include <iostream>
#include<cassert>
using namespace std;

#define MAX_DEPTH   (4)
 
int a[4][4];

class base_iterator {
public:
    base_iterator(/*int *a[4], */int max_depth, int frow, int fcol): _fcol(fcol), _frow(frow), /*_m(a), */_max_depth(max_depth) {}
    virtual bool end(void) const = 0;
    virtual char getCurrentValue(void) const = 0;
    virtual void next(void) = 0;
    virtual ~base_iterator() {}

protected:
    int _fcol;
    int _frow;
    //int *_m[4];
    const int _max_depth;
};

class horizontal_iterator:public base_iterator {
public:
    horizontal_iterator(/*int *a[4], */int max_depth, int frow, int fcol): base_iterator(/*a, */max_depth, frow, fcol) {}
    virtual bool end(void) const { return _fcol >= _max_depth; }
    virtual char getCurrentValue(void) const { return a[_frow][_fcol]; }
    virtual void next(void) { _fcol++; }
    virtual ~horizontal_iterator() {}
};

class fd_iterator:public base_iterator {
public:
    fd_iterator(/*int *a[4], */int max_depth, int frow, int fcol): base_iterator(/*a, */max_depth, frow, fcol) {}
    virtual bool end(void) const { return _frow >= _max_depth || _fcol >= _max_depth; }
    virtual char getCurrentValue(void) const { return a[_frow][_fcol]; }
    virtual void next(void) { _fcol++;  _frow++; }
    virtual ~fd_iterator() {}
};

class rd_iterator:public base_iterator {
public:
    rd_iterator(/*int *a[4], */int max_depth, int frow, int fcol): base_iterator(/*a, */max_depth, frow, fcol) {}
    virtual bool end(void) const { return _frow >= _max_depth || _fcol <= 0; }
    virtual char getCurrentValue(void) const { return a[_frow][_fcol]; }
    virtual void next(void) { _frow++ ;   _fcol--; }
    virtual ~rd_iterator() {}
};

class vert_iterator:public base_iterator {
public:
    vert_iterator(/*int *a[4], */int max_depth, int frow, int fcol): base_iterator(/*a, */max_depth, frow, fcol) {}
    virtual bool end(void) const { return _frow >= _max_depth; }
    virtual char getCurrentValue(void) const { return a[_frow][_fcol]; }
    virtual void next(void)  { _frow++; }
    virtual ~vert_iterator() {}
};


bool checkline(base_iterator &iter, char &out)
{
    int tchar_count = 0;
    char fchar = iter.getCurrentValue();

    // check if row is valid
    if (fchar == '.')
        return false;

    if (fchar == 'T') {
        tchar_count++;
        iter.next();
        fchar = iter.getCurrentValue();
        if (fchar == '.')
            return false;
    }



    for (iter.next(); !iter.end(); iter.next()) {
        char curr = iter.getCurrentValue();
        if (curr == 'T') {
            if (tchar_count == 1)
                return false;
            else {
                tchar_count++;
                continue;
            }
        }
        if (fchar != curr)
            return false;
    }

    out = fchar;
    return true;
}


// check first row or first column
char checkWinCase(/*int *a[4]*/) 
{
    char out = ' ';
    bool not_completed = false;

    // first column cases 
    for (int r = 0; r < MAX_DEPTH; r++) {
        if (r == 0) {
            fd_iterator fd(/*a,*/ MAX_DEPTH, 0, 0);
            if (checkline(fd, out)) {
                return out;
            }
        }

        if (r == MAX_DEPTH - 1) {
            rd_iterator rd(/*a,*/ MAX_DEPTH, 0, r);
            if (checkline(rd, out))
                return out;
        }

        vert_iterator v(/*a,*/ MAX_DEPTH, 0, r);
        if (checkline(v, out))
            return out;
    }

    // first row cases 
    for (int r = 0; r < MAX_DEPTH; r++) {
        horizontal_iterator h(/*a,*/ MAX_DEPTH, r, 0);
        if (checkline(h, out))
            return out;
    }

    return out;
}

void runCase(int tcase/*, int *a[4]*/) 
{
    char out = ' ';
    bool not_completed = false;

    // check if game not ocmpleted
    for (int i=0; i < MAX_DEPTH; i++) {
        for(int j=0; j < MAX_DEPTH; j++) {
            if (a[i][j] == '.') {
                not_completed = true;
                break;
            }
        }
    }

    out = checkWinCase(); 
    assert(out != 'T');

    cout<<"Case #"<<tcase<<": ";
    if ('X' == out || 'O' == out) {
        cout<<out<<" won";
    } else {
        if (not_completed) {
            cout<<"Game has not completed";
        } else {
            cout<<"Draw";
        }
    }
    cout<<endl;
}

int main(int argc, char** argv)
{
    int ntcases = 1;
    int b[4][4] = {
        /*{'X','X','X','T'},
        {'.','.','.','.'},
        {'O','O','.','.'},
        {'.','.','.','.'}*/
        {'X','O','X','T'},
        {'X','X','O','O'},
        {'O','X','O','X'},
        {'X','X','O','O'}
    };

    cin>>ntcases;
    for (int tcase = 0; tcase < ntcases; tcase++) {
        // fill array first for case,
        for (int i=0; i <4; i++) {
            for(int j=0; j<4; j++) {
                char temp;
                cin>>temp;
                a[i][j] = temp;
                //a[i][j] = b[i][j];
            }
        }
        runCase(1 + tcase/*, a*/);
    }


    return 0;
}