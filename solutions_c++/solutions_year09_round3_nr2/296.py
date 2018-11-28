#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <math.h>

#define LOG(x)  //x

using namespace std;

int64_t slen2(int64_t sv[3])
{
    int64_t len = 0;
    for (int i = 0; i < 3; ++i) {
        len += sv[i]*sv[i];
    }
    return len;   
}

void crossprod(int64_t r[3],int64_t a[3],int64_t b[3],int64_t n)
{
    r[0] = a[1]*b[2]-a[2]*b[1];
    r[1] = a[2]*b[0]-a[0]*b[2];
    r[2] = a[0]*b[1]-a[1]*b[0];
}


string solve(int64_t sm[3], int64_t sv[3],int64_t n)
{
    int64_t svlen2 = slen2(sv);
    
    ostringstream result;
    
    double zdist = sqrt(double(slen2(sm)))/double(n);
    if (svlen2 == 0) {
        result << zdist << " " << 0.0;
        return result.str();
    }
    
    int64_t cm[3] = {0};
    crossprod(cm,sm,sv,n);
    int64_t cmlen2 = slen2(cm);
    
    double dist2 = double(cmlen2)/double(svlen2);
    double dist = sqrt(double(cmlen2)/double(svlen2));
    int64_t smlen2 = slen2(sm);
    
    double tsvlen2 = smlen2-dist2;
    double t2 = tsvlen2/svlen2;
    double t = sqrt(t2);
    
    double p[3];
    double vdist2 = 0.0;
    for (int i =0 ; i <3; ++i) {
        p[i] = sm[i]+double(sv[i])*t;
        vdist2 += p[i]*p[i];
    }
    double eps = 0.00000001;
    if (sqrt(vdist2)/double(n) < zdist-eps) {
        result << dist/double(n) << " " << t;
    } else {
        result << zdist << " " << 0.0;
    }
    return result.str();
}

void test(istream& input, ostream& output)
{
    int numcases;
    input >> numcases;
    
     for (int i = 0; i < numcases; ++i) {
        int n;
        input >> n;
        
        int64_t sm[3] = {0};
        int64_t sv[3] = {0};
        for (int j = 0; j < n; ++j) {
            for (int c = 0; c < 3; ++c) {
                int mc;
                input >> mc;
                sm[c] += mc;
            }
            for (int c = 0; c < 3; ++c) {
                int vc;
                input >> vc;
                sv[c] += vc;
            }
        }
        
        output << "Case #" << i+1 << ": " << solve(sm,sv,n) << endl;
     } 

    std::string line;
}

void run_test_data(void)
{
    string testdatadir = "../../test_data/";
    string basename = "B-large.in";
    string input_path = testdatadir+basename+".txt";
    ifstream input;
    input.exceptions(input.failbit | input.badbit);
    input.open(input_path.c_str());
    string output_path = testdatadir+basename+".output.txt";
    ofstream output;
    output.exceptions(output.failbit | output.badbit);
    output.open(output_path.c_str(),std::ios::out|std::ios::trunc);
    
    test(input,output);
}

int main (int argc, char * const argv[]) {
    // insert code here...
    try {
        run_test_data();
        return 0;
    } catch (exception& err) {
        cerr << "Exception cathed:" << endl;
        cerr << err.what() << endl;
    } catch(...) {
        cerr << "Unkown exception catched" << endl;
        cerr << endl;
    }
    cerr << "Some error occured!\n";
    return 1;
}
