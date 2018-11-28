// Copyright 2012, Vanya Davidenko.
// Используемая кодировка: UTF-8.

#include <algorithm>
#include <cassert>
#include <deque>
#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <set>



namespace {

typedef size_t Int;
typedef char Digit;
typedef ::std::pair<Int,Int> AB;


template<class T, class TStream>
T Input(TStream& s) {
    T result;
    s >> result;
    return result;
}

///////////////////////////////////////

template<class TStream>
::std::vector<AB> InputData(TStream& s) {
    ::std::vector<AB> result;

    size_t n = Input<size_t>(s);
    result.reserve(n);

    for ( size_t i = 0 ; i != n ; ++i ) {
        const Int first = Input<Int>(s);
        const Int second = Input<Int>(s);
        result.push_back(::std::make_pair(first,second));
    }

    return result;
}

////////////////////////////////////////////////////////////////////////////////

void GetDigits(Int n, ::std::deque<Digit>* result) {
    result->clear();

    do {
        result->push_front(n % 10);
        n /= 10;
    } while ( n > 0 );
}


Int Build(const ::std::deque<Digit>& digits) {
    Int result = 0;
    for ( size_t i = 0 ; i != digits.size() ; ++i ) {
        result *= 10;
        result += digits[i];
    }
    return result;
}

size_t Solve(const AB& ab) {
    size_t result = 0;
    typedef AB::first_type Int;

    ::std::deque<Digit> b, n, m;
    GetDigits(ab.second, &b);

    for ( Int i = ab.first ; i <= ab.second ; ++i ) {
        GetDigits(i, &n);
        m = n;
        ::std::set<Int> found;

        size_t total_rotated = 0;
        for ( size_t j = 1 ; j != n.size() ; ++j ) {
            const size_t r = ( j - total_rotated ) % m.size();
            total_rotated += r;

            ::std::rotate(m.begin(), m.end() - r, m.end());
            Int built_m;

            using ::std::lexicographical_compare;
            if ( m.front() != 0 &&
                lexicographical_compare(n.begin(),n.end(), m.begin(),m.end()) &&
                !lexicographical_compare(b.begin(),b.end(), m.begin(),m.end())&&
                ( built_m = Build(m) ) &&
                found.find(built_m) == found.end() ) {
                found.insert(built_m);
                result++;
            }
        }
    }

    return result;
}

}  // anonymous namespace




int main(int argc, char** argv) {
    auto v = InputData(::std::ifstream(argv[1]));

    for ( size_t i = 0 ; i != v.size() ; ++i ) {
        ::std::cout << "Case #" << (i+1) << ": " << Solve(v[i]) << ::std::endl;
    }

    //system("pause");
    return 0;
}
