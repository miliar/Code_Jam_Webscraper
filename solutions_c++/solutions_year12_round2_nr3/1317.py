#include <iostream>
#include <vector>
#include <fstream>
#include <map>
#include <sstream>
using namespace std;

int main (int argc, char** argv) {

    // read file
    ifstream f(argv[1]);
    int bufsize = 1000000;
    char buf[bufsize];
    f.getline(buf, bufsize, '\n');
    int num_cases = atoi(buf);
    cout << "num_cases:" << num_cases << endl;
    ofstream outf("C-small-1.out");

    for (int c=0; c < num_cases; c++) {
        cout << "------------------------------------------" << endl;
        cout << "Case: " << c+1 << endl;
        f.getline(buf, bufsize, ' ');
        int num_ints = atoi(buf);
        cout << "num_ints:" << num_ints << endl;
        vector<long long> vals;
        for (int i=0; i < num_ints; i++) {
            string next;
            f >> next;
            long long val;
            stringstream ss_next(next);
            ss_next >> val;
            vals.push_back(val);
            cout << val << " ";
        }
        cout << endl;

        long long modsize = 1000000;
        map<long long, vector<vector<long long> > > m;

        vector<long long> empty;
        vector<vector<long long> > empty2;
        empty2.push_back(empty);
        m[0 % modsize] = empty2;


        bool case_done = false;
        cout << "------------------------------------------" << endl;
        
        for (long long i=0; i < num_ints; i++) {
            long long val = vals[i];
            cout << "adding val: " << i << "..." << endl;
            cout << "m.size(): " << m.size() << endl;

            vector<vector<long long> > sets;
            vector<long long> set;

            map<long long, vector<vector<long long> > > new_m = m;
            long long matches_found = 0;

            for (map<long long, vector<vector<long long> > >::iterator it = m.begin(); it != m.end() ; it++) {
                long long sets_sum = it->first;
                sets = it->second;
                for (long long l=0; l < sets.size(); l++) {
                    vector<long long> set = sets[l];

                    set.push_back(val);
                    long long sum = (sets_sum + val) % modsize;

                    map<long long, vector<vector<long long> > >::iterator pos;
                    pos = m.find(sum);

                    if (pos == m.end()) {
                        vector<vector<long long> > new_sets;
                        new_sets.push_back(set);
                        new_m[sum] = new_sets;
                    } else {
                        matches_found += 1;
                        long long my_true_sum = 0;
                        for (long long j=0; j < set.size(); j++) {
                            my_true_sum += set[j];
                        }

                        vector<vector<long long> >& other_sets = pos->second;
                        for (long long j=0; j < other_sets.size(); j++) {
                            long long other_true_sum = 0;
                            for (long long k=0; k < other_sets[j].size(); k++) {
                                other_true_sum += other_sets[j][k];
                            }

                            if (my_true_sum == other_true_sum) {
                                outf << "Case #" << c+1 << ":" << endl;
                                for (long long k=0; k < other_sets[j].size(); k++) {
                                    outf << other_sets[j][k] << " ";
                                }
                                outf << endl;
                                for (long long k=0; k < set.size(); k++) {
                                    outf << set[k] << " ";
                                }
                                outf << endl;
                                case_done = true;
                                break;
                            }
                        }

                    }
                    if (case_done) break;
                }
                if (case_done) break;
            }
            if (case_done) break;
            //cout << "found_matches: " << matches_found << endl;
            m = new_m;
            //cout << "done adding val: " << val << endl;


        
        }







        cout << " done with case." << endl;
    }
    outf.close();
    


    return 0;

}


