#include <stddef.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>

#include <utility>
#include <bitset>
#include <tuple>
#include <functional>
#include <memory>

#include <string>

#include <array>
#include <deque>
#include <forward_list>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

#include <iterator>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <initializer_list>
#include <exception>
#include <stdexcept>

using namespace std;

// non-short-circuiting logic.
bool either(bool left, bool right) {
    return left || right;
}

bool both(bool left, bool right) {
    return left && right;
}

void no_op() {}

template <typename Association, typename Key,
          typename Than>
bool if_key_found(Association& assoc, Key key,
                  Than than_func) {
    return if_key_found(assoc, key, than_func, no_op);
}

template <typename Association, typename Key,
          typename Than, typename Else>
bool if_key_found(Association& assoc, Key key,
                  Than than_func, Else else_func) {
    auto iter = assoc.find(key);
    if (iter != assoc.end()) {
        than_func(iter->second);
        return true;
    }
    else_func();
    return false;
}

template <typename Function>
void do_n(int n, Function func) {
    if (n < 0) throw runtime_error("do_n requires non-negative number.");
    for (; n; --n) {
        func();
    }
}

template <typename T = int>
T read(std::istream& stream = std::cin) {
    T val;
    if (!(stream >> val)) {
        throw std::runtime_error("Could not read value.");
    }
    return val;
}

// diagnostic utilities.
template <typename T>
string to_str(const T& val) {
    ostringstream stream;
    stream << val;
    return stream.str();
}

template <typename T, typename U>
string to_str(const pair<T,U>& a_pair) {
    ostringstream stream;
    stream << "(" << a_pair.first << ", " << a_pair.second << ")";
    return stream.str();
}

template <typename T>
string to_str(const vector<T>& vec) {
    ostringstream stream;
    stream << "[";
    for (auto iter = vec.begin(); iter != vec.end(); ++iter) {
        stream << to_str(*iter);
        auto next_iter = iter;
        ++next_iter;
        if (next_iter != vec.end()) {
            stream << ", ";            
        }
    }
    stream << "]";
    return stream.str();
}

template <typename T>
string to_str(const list<T>& vec) {
    ostringstream stream;
    stream << "[";
    for (auto iter = vec.begin(); iter != vec.end(); ++iter) {
        stream << to_str(*iter);
        auto next_iter = iter;
        ++next_iter;
        if (next_iter != vec.end()) {
            stream << ", ";            
        }
    }
    stream << "]";
    return stream.str();
}

template <typename Key, typename Value>
string to_str(const map<Key, Value>& vec) {
    ostringstream stream;
    cout << "{";
    for (auto iter = vec.begin(); iter != vec.end(); ++iter) {
        stream << to_str(*iter);
        auto next_iter = iter;
        ++next_iter;
        if (next_iter != vec.end()) {
            stream << ", ";            
        }
    }
    stream << "}";
    return stream.str();
}

// functional wrappers.
template <typename Collection>
Collection sorted(Collection coll) {
    std::sort(coll.begin(), coll.end());
    return coll;
}

template <typename Collection, typename Function>
vector<typename Collection::value_type> map_(const Collection& coll,
                                              Function func) {
    vector<typename Collection::value_type> vec;
    transform(coll.begin(), coll.end(),
              back_inserter(vec),
              func);
    return vec;
}

template <typename Collection, typename T>
T fold(const Collection& coll, T init) {
    return accumulate(coll.begin(), coll.end(), init);
}

template <typename Collection, typename T, typename BinaryFunc>
T fold(const Collection& coll, T init, BinaryFunc func) {
    return accumulate(coll.begin(), coll.end(), init, func);
}

template <typename Collection>
typename Collection::value_type min_(const Collection& coll) {
    return *min_element(coll.begin(), coll.end());
}

template <typename Collection>
string join(Collection coll, const string& seperator = "") {
    string result;
    for (auto iter = coll.begin(); iter != coll.end();) {
        result += *iter;
        ++iter;
        if (iter != coll.end()) {
            result += seperator;
        }
    }
    return result;
}

template <typename Collection, typename Function>
typename Collection::size_type count_if_(const Collection& coll,
                                         Function func) {
    return count_if(coll.begin(), coll.end(), func);
}

#define mp make_pair
#define pb push_back

typedef list<int> li;
typedef list<string> ls;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

void print_case(int num, string val) {
    cout << "Case #" << num << ": " << val << endl;
}

// pair(n,d);
double div(const pii& fract) {
    return double(fract.first) / double(fract.second);
}

int main(int argc, char *argv[])
{
    int case_num = 1;
    do_n(read(), [&]{
            vs schedules;
            do_n(read(), [&]{
                    schedules.pb(read<string>());
                });
            vector<pii> wp_vec;

            // accumulate wp
            for (const string& sched : schedules) {
                pii wp;
                wp.first = count_if_(sched, [&](char ch) { return ch == '1';});
                wp.second = count_if_(sched, [&](char ch) { return ch != '.';});
                wp_vec.pb(wp);
            }

            // accumulate owp.
            vector<double> owp_vec;
            for (size_t ii = 0; ii < schedules.size(); ++ii) {
                // ii you
                double num = 0;
                double denom = 0;
                for (size_t jj = 0; jj < schedules.size(); ++jj) {
                    // if opponent
                    if (schedules[ii][jj] != '.') {
                        num +=
                            (double(wp_vec[jj].first - (schedules[jj][ii] - '0'))
                             / double(wp_vec[jj].second - 1));
                        denom += 1;
                    }
                }
                if (denom) {
                    owp_vec.pb(num / denom);
                } else {
                    throw runtime_error("team " + to_str(ii) +
                                        " had no opponents.");;
                }
            }

            vector<double> oowp_vec;
            for (size_t ii = 0; ii < schedules.size(); ++ii) {
                double num = 0;
                double denom = 0;
                for (size_t jj = 0; jj < schedules.size(); ++jj) {
                    if (schedules[ii][jj] != '.') {
                        num += owp_vec[jj];
                        denom += 1;
                    }
                }

                if (denom) {
                    oowp_vec.pb(num / denom);
                } else {
                    throw runtime_error("team " + to_str(ii) +
                                        " had no opponents");
                }
            }

            cout << "Case #" << case_num << ":" << endl;
            cout.precision(12);
            for (size_t ii = 0; ii < schedules.size(); ++ii) {
                cout <<
                    (0.25 * div(wp_vec[ii]) + 0.5 * owp_vec[ii] + 0.25 * oowp_vec[ii])
                     << endl;
            }
            ++case_num;
        });
}
