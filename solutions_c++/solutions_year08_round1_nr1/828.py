#include <map>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int tab [ 1024][1024];

int main(int argc, char *argv[])
{

    
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
        int dim;
        
        cin >> dim;
        vector < int> v1;
        vector < int> v2;
                
        for ( int engine = 0; engine < dim; engine ++) {
            
            int temp;
            cin >> temp;
            v1.push_back ( temp);
            
        } 
        for ( int engine = 0; engine < dim; engine ++) {
            
            int temp;
            cin >> temp;
            v2.push_back ( temp);
            
        }
        sort ( v1.begin(), v1.end());
        sort ( v2.begin(), v2.end());
        long long sum = 0;
        for ( int i = 0; i < dim; i++)
            sum += v1[i] * v2[v2.size() - 1 - i];
        
        cout << "Case #" << testCase << ": "<< sum << endl;
    }
    //cout << "done";

    
    
    return 0;
}
