//
//  main.cpp
//  GCJGooglersDance
//
//  Created by Fedor Kazak on 14.04.12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <vector>
#include <set>
#include <deque>
#include <algorithm>
#include <map>

using namespace std;

int T;
int N, S, p;

/*class char_less_than : public std::binary_function<char, char, bool> {
public:
	bool operator() (const char c1, const char c2) {
		return p1.age() < p2.age();
	}
};*/



template <typename T>
struct IsLessThanVal : public unary_function<T,bool> {
    T refVal;
    IsLessThanVal(T i):refVal(i)
    {
        refVal = i;
    };
    bool operator() (T number) {return (number < refVal);}
};


int main(int argc, const char * argv[])
{

    // insert code here...

    freopen( "/Users/fek/testprograms/GCJGooglersDance/GCJGooglersDance/B-large.in", "r", stdin );
    freopen( "/Users/fek/testprograms/GCJGooglersDance/GCJGooglersDance/out.txt", "w", stdout );
    cin >> T;
    
    for(int i = 0; i != T; ++i)
    {
        cin >> N >> S >> p;
        int count = 0;
        vector<int> scores;
        scores.reserve(N);
        for(int j = 0; j != N; ++j)
        {
            int curScore;
            cin >> curScore;
            scores.push_back(curScore);
        }
        stable_sort(scores.begin(), scores.end());
        int minNonSpecScore = p + 2*(p-1);
        int minSpecScore = p + 2*(p-2);
        if(p == 0)
        {
            minNonSpecScore = 0;
        }
        if(p == 1)
        {
            minSpecScore = 1;
        }
        if(p == 0)
        {
            minSpecScore = 0;
        }
            
        IsLessThanVal<int> filt1(minNonSpecScore);
        vector<int>::reverse_iterator pos = find_if(scores.rbegin(), scores.rend(), filt1);
        count += pos - scores.rbegin();
        
        
        
        IsLessThanVal<int> filt2(minSpecScore);
        vector<int>::reverse_iterator posSpec = find_if(pos, scores.rend(), filt2);
        int potential = posSpec - pos;
        count += min(potential, S);
        
        
        cout << "Case #" << i+1 << ": " << count << "\n";
        
    }
    
    
    return 0;
}

