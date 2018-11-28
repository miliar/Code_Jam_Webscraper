#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

void A_small();

int main(int argc, int** argv) {
    A_small();
    return 0;
}

void A_small() {
    int n;
    cin>>n;

    for (int i=0; i<n; i++) {
        int n_engines;
        cin>>n_engines;
        
        // Throw away terminating newline
        string unused;
        getline(cin,unused);
        
        // Read engines
        vector<string> engines;
        for (int j=0; j<n_engines; j++) {
            string engine;
            getline(cin,engine);
            engines.push_back(engine);
        }
        
        // Process queries
        int result = 0;
        vector<bool> seen;
        for (int j=0; j<n_engines; j++) {
            seen.push_back(false);
        }
        int count = 0;
        int n_queries;
        cin>>n_queries;
        
        // Throw away terminating newline
        getline(cin,unused);
        
        for (int q=0; q<n_queries; q++) {
            string query;
            getline(cin,query);
            for (int j=0; j<n_engines; j++) {
                if (seen[j]==false && query == engines[j]) {
                    count++;
                    if (count == n_engines) {
                        count = 1;
                        for (int k=0; k<n_engines; k++) {
                            seen[k] = false;
                        }
                        result++;
                    }
                    seen[j] = true;
                }
                        
            }
        }
        
        cout<<"Case #"<<i+1<<": ";
        cout<<result<<'\n';
    }
}

