//
//  main.cpp
//  GJRecycledNumbers
//
//  Created by Fedor Kazak on 14.04.12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
#include <vector>
#include <set>
#include <deque>

using namespace std;

int T;
int A, B;

inline int check(int a, int b);
inline vector<char> decompose(int n);
inline set<int> cycles(vector<char> digits);

int main(int argc, const char * argv[])
{

    // insert code here...
    freopen( "/Users/fek/testprograms/GJRecycledNumbers/GJRecycledNumbers/C-large.in", "r", stdin );
    freopen( "/Users/fek/testprograms/GJRecycledNumbers/GJRecycledNumbers/out.txt", "w", stdout );

    cin >> T;
    
    for(int i = 0; i != T; ++i)
    {
        cin >> A >> B;
        int count = check(A, B);
        
        cout << "Case #" << i+1 << ": " << count << "\n";
        
    }
    
    return 0;
}

inline int check(int a, int b)
{
    int result = 0;
    for(int i = a; i <= b; ++i)
    {
        vector<char> digits = decompose(i);
        set<int> cycled = cycles(digits);
        result += cycled.size();
    }
    
    return result;
}


inline vector<char> decompose(int n)
{
    deque<char> result;
    while(n>0)
    {
        result.push_front(n%10);
        n /= 10;
    }
    return vector<char>(result.begin(), result.end());
}

inline int num_from_vector(vector<char> digits, int startPos)
{
    if(startPos < 0 || startPos >= digits.size())
    {
        return -1;
    }
    
    int result = 0;
    int mult = 10;
    size_t size = digits.size();
    for(int i = startPos; i != startPos + size; ++i)
    {
        result *= mult;
        result += digits[i % size];
    }
    
    return result;
}

inline set<int> cycles(vector<char> digits)
{
    int rootNum = num_from_vector(digits, 0);
    size_t size = digits.size();
    
    set<int> result;
    
    for(int i = 1; i != size; ++i)
    {
        int nextNum = num_from_vector(digits, i);
        if(nextNum > rootNum && nextNum <= B)
        {
            result.insert(nextNum);
        }
    }
    
    return result;
}



