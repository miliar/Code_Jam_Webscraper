// Copyright 2012, Vanya Davidenko.
// Используемая кодировка: UTF-8.

#include <cassert>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>



namespace {

char g_converter[128];

void InitConverter() {
    g_converter['a'] = 'y';
    g_converter['b'] = 'h';
    g_converter['c'] = 'e';
    g_converter['d'] = 's';
    g_converter['e'] = 'o';
    g_converter['f'] = 'c';
    g_converter['g'] = 'v';
    g_converter['h'] = 'x';
    g_converter['i'] = 'd';
    g_converter['j'] = 'u';
    g_converter['k'] = 'i';
    g_converter['l'] = 'g';
    g_converter['m'] = 'l';
    g_converter['n'] = 'b';
    g_converter['o'] = 'k';
    g_converter['p'] = 'r';
    g_converter['q'] = 'z';
    g_converter['r'] = 't';
    g_converter['s'] = 'n';
    g_converter['t'] = 'w';
    g_converter['u'] = 'j';
    g_converter['v'] = 'p';
    g_converter['w'] = 'f';
    g_converter['x'] = 'm';
    g_converter['y'] = 'a';
    g_converter['z'] = 'q';
    g_converter[' '] = ' ';

    for ( char i = 'a' ; i <= 'z' ; ++i ) {
        g_converter[i+('A'-'a')] = g_converter[i] + ('A' - 'a');
    }
}

::std::vector< ::std::string > LoadLines(const ::std::string& filename) {
    ::std::ifstream f;
    f.exceptions(::std::ios::failbit | ::std::ios::badbit);

    f.open(filename);
    f.exceptions(::std::ios::badbit);

    size_t n;
    f >> n;

    ::std::vector< ::std::string > result;

    ::std::string s;
    ::std::getline(f, s);  // пропуск до конца строки

    while ( ::std::getline(f, s) ) {
        result.push_back(s);
    }

    assert(result.size() == n);

    f.close();
    return result;
}

::std::string Decode(const ::std::string& s) {
    ::std::vector<char> r(s.size());
    ::std::transform(s.begin(), s.end(), r.begin(), 
                     [](char s) { return g_converter[s]; });
    return ::std::string(r.begin(), r.end());
}

void Do(const ::std::vector< ::std::string >& s) {
    for ( size_t i = 0 ; i != s.size() ; ++i ) {
        ::std::cout << "Case #" << (i+1) << ": " << Decode(s[i]) << ::std::endl;
    }
}

}  // anonymous namespace



int main() {
    InitConverter();
    Do(LoadLines("f.txt"));

    //system("pause");
    return 0;
}