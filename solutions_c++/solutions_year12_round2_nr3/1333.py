/* 
 * File:   sum.cc
 * Author: vivek
 *
 * Created on May 5, 2012, 9:35 PM
 */

#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
typedef vector<int> VectorInt;
map<long int, vector<int> > allsum;
int found = 0;
int caset;

/*
 * 
 */
void print_vector(vector<int> number) {
    int i=0;
    for (int i = 0; i < number.size()-1; i++)
        printf("%d ", number.at(i));
    printf("%d", number.at(i));
}

void sum_up_recursive(vector<int> numbers, long int target, vector<int> partial) {
    if (found == 1) {
        return;
    }
    long int s = 0;
    if (partial.empty() == false) {
        for (int i = 0; i < partial.size(); i++) s += partial.at(i);
        if (allsum.find(s) == allsum.end()) {
            // not found
        } else {
            vector<int> temp = allsum[s];
            if (temp.size() != partial.size()) {
                found = 1;
                printf("\n");
                print_vector(temp);
                print_vector(partial);
                return;
            }
            for (int i = 0; (i < temp.size()) && (i < partial.size()); i++) {
                if (temp.at(i) != partial.at(i)) {
                    found = 1;
                    printf("\n");
                    print_vector(temp);
                    print_vector(partial);                    
                    return;
                }
            }
        }
        sort(partial.begin(), partial.end());
        //printf("<<-pushing");
        allsum[s] = partial;
        //print_vector(partial);
        //printf(">>");
    }

    if (s >= target)
        return;
    for (int i = 0; i < numbers.size(); i++) {
        vector<int> remaining;
        int n = numbers.at(i);
        for (int j = i + 1; j < numbers.size(); j++) remaining.push_back(numbers.at(j));
        vector<int> partial_rec(partial);
        partial_rec.push_back(n);
//        printf("<<--");
//        print_vector(remaining);
//        print_vector(partial_rec);
//        printf("-->\n");
        sum_up_recursive(remaining, target, partial_rec);
    }
}

static void sum_up(vector<int> numbers, long int target) {
    vector<int> partial;
    sum_up_recursive(numbers, target, partial);
}

int main(int argc, char** argv) {
    int t;
    int n;
    int i;
    int temp;
    long int sum;
    vector<int> array;
    scanf("%d", &t);
    while (t--) {
        caset++;
        printf("Case #%d: ", caset);
        sum = 0;
        allsum.clear();
        array.clear();
        found = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &temp);
            sum += temp;
            array.push_back(temp);
        }
        sum_up(array, sum);
        if (found == 0) {
            printf("Impossible\n");
        }

    }
    return 0;
}

