#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define IN(lo, hi, x) ((x) >= (lo) && (x) <= (hi))
typedef vector<int> triplet;
typedef vector<triplet> triplets_t;

void get_triplets(int n, triplets_t& result){
    if(!n){
        result.push_back(triplet());
        for(int i = 0; i < 4; i++)
            result.back().push_back(0);
        return;
    }
    int count = 0;
    int q0 = n / 3,
        q1 = (n-1) / 3, 
        q2 = (n-2) / 3,
        q3 = (n-3) / 3,
        q4 = (n-4) / 3;

    
    if((q0 * 3) == n && IN(0, 10, q0)){
        result.push_back(triplet());
        result.back().push_back(0);
        result.back().push_back(q0);
        result.back().push_back(q0);
        result.back().push_back(q0);
    }
    if((q1 * 3) == (n - 1) && IN(0, 10, q1)){
        result.push_back(triplet());
        result.back().push_back(0);
        result.back().push_back(q1);
        result.back().push_back(q1);
        result.back().push_back(q1+1);
    }
    if((q2 * 3) == (n - 2) && IN(0, 10, q2)){
        result.push_back(triplet());
        result.back().push_back(0);
        result.back().push_back(q2);
        result.back().push_back(q2+1);
        result.back().push_back(q2+1);

        result.push_back(triplet());
        result.back().push_back(1);
        result.back().push_back(q2);
        result.back().push_back(q2);
        result.back().push_back(q2+2);
    }
    if((q3 * 3) == (n - 3) && IN(0, 10, q3)){
        result.push_back(triplet());
        result.back().push_back(1);
        result.back().push_back(q3);
        result.back().push_back(q3+1);
        result.back().push_back(q3+2);
    }
    if((q4 * 3) == (n - 4) && IN(0, 10, q4)){
        result.push_back(triplet());
        result.back().push_back(1);
        result.back().push_back(q4);
        result.back().push_back(q4+2);
        result.back().push_back(q4+2);
    }
}

int get_the_count(const vector<int>& numbers, int s, int p){
    int count = 0;
    for(auto it = numbers.begin(); it != numbers.end(); it++){
        triplets_t t;
        get_triplets(*it, t);
        if(t.size() == 1){
            if(*max_element(t[0].begin()+1, t[0].end()) >= p){
                if(t[0][0]){
                    if(s){
                        --s;
                        ++count;
                    }
                }else{
                    ++count;
                }
            }
        }else{    
            int max0 = *max_element(t[0].begin(), t[0].end()),
                max1 = *max_element(t[1].begin(), t[1].end());
            
            if(!t[0][0] && max0 >= p){
                ++count;
            }else if(t[0][0] && !t[1][0] && max1 >= p){
                ++count;
            }else if(t[0][0] && max0 >= p){
                if(s){
                    ++count;
                    --s;
                }
            }else if(t[1][0] && max1 >= p){
                if(s){
                    ++count;
                    --s;
                }
            }
        }
    }
    return count;
}


int main(){
    int t;
    cin >> t;
    
    for(int i = 0; i < t; i++){
        int n, s, p;
        cin >> n >> s >> p;
        vector<int> nums;
        while(n--){
            int x;
            cin >> x;
            nums.push_back(x);
        }
        int count = get_the_count(nums, s, p);
        cout << "Case #" << i+1 << ": " << count << endl;
    }

    return 0;
}

