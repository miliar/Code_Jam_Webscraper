// Copyright 2012, Vanya Davidenko.
// Используемая кодировка: UTF-8.

#include <fstream>
#include <iostream>



namespace {

template<class T, class TStream>
T Input(TStream& s) {
    T result;
    s >> result;
    return result;
}

template<class TStream>
size_t Solve(TStream& stream) {
    const size_t n = Input<size_t>(stream);
    size_t num_surprises = Input<size_t>(stream);
    const size_t max = Input<size_t>(stream);

    size_t result = 0;

    for ( size_t i = 0 ; i != n ; ++i ) {
        const size_t sum = Input<size_t>(stream);
        size_t min = sum / 3 + !!(sum % 3);

        if ( min >= max ) {
            result++;
        } else if ( num_surprises > 0 && sum >= 2 ) {
            if ( sum % 3 != 1 ) {
                min++;
            }
            if ( min >= max ) {
                num_surprises--;
                result++;
            }
        }
    }

    return result;
}

}  // anonymous namespace



int main(int argc, char** argv) {
    auto& stream = ::std::ifstream();
    stream.exceptions(::std::ios::failbit | ::std::ios::badbit);
    stream.open(argv[1]);
    stream.exceptions(::std::ios::badbit);

    const size_t num_cases = Input<size_t>(stream);
    for ( size_t i = 0 ; i != num_cases ; ++i ) {
        ::std::cout << "Case #" << (i+1) << ": " << Solve(stream) <<::std::endl;
    }

    //system("pause");
    return 0;
}
