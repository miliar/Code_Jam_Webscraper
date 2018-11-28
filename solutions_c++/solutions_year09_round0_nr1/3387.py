#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <list>
#include <set>

namespace codejam
{

struct Language
{
    unsigned letters;
    unsigned words;

    std::set<std::string> dict;

    template<class char_t, class char_traits>
    friend std::basic_istream<char_t, char_traits>& operator>>(std::basic_istream<char_t, char_traits>& is, Language& language);
};

template<class char_t, class char_traits>
std::basic_istream<char_t, char_traits>& operator>>(std::basic_istream<char_t, char_traits>& is, Language& language)
{
    if (!is.good())
        return is;

    const typename std::basic_istream<char_t, char_traits>::sentry ok(is);
    if (ok)
    {
        std::string buffer;

        for (unsigned i = 0; i < language.words; ++i)
        {
            std::getline(is, buffer);
            language.dict.insert(buffer);
        }
    }

    return is;
}

struct Problem
{
    struct Case
    {
        const std::string pattern;
        const Language& language;

        unsigned result;
        void resolve();

        Case(std::string pattern, const Language& language) : pattern(pattern), language(language), result(0)
        {
            resolve();
        }

    };

    unsigned cardinality;

    Language language;

    std::list<Case> cases;

    template<class char_t, class char_traits>
    friend std::basic_ostream<char_t, char_traits>& operator<<(std::basic_ostream<char_t, char_traits>& os, const Problem& problem);

    template<class char_t, class char_traits>
    friend std::basic_istream<char_t, char_traits>& operator>>(std::basic_istream<char_t, char_traits>& is, Problem& problem);
};

template<class char_t, class char_traits>
std::basic_ostream<char_t, char_traits>& operator<<(std::basic_ostream<char_t, char_traits>& os, const Problem& problem)
{
    if (!os.good())
        return os;

    const typename std::basic_ostream<char_t, char_traits>::sentry ok(os);
    if (ok)
    {
        unsigned i = 0;
        std::list<Problem::Case>::const_iterator it = problem.cases.begin();
        for (; it != problem.cases.end(); ++it)
        {
            os << "Case #" << ++i << ": " <<
                it->result << '\n';
        }

        os << std::flush;
    }

    return os;
}

template<class char_t, class char_traits>
std::basic_istream<char_t, char_traits>& operator>>(std::basic_istream<char_t, char_traits>& is, Problem& problem)
{
    if (!is.good())
        return is;

    const typename std::basic_istream<char_t, char_traits>::sentry ok(is);
    if (ok)
    {
        std::string buffer;
        std::stringstream stream;

        std::getline(is, buffer, ' ');
        stream.str(buffer);
        stream >> problem.language.letters;
        stream.clear();

        std::getline(is, buffer, ' ');
        stream.str(buffer);
        stream >> problem.language.words;
        stream.clear();

        std::getline(is, buffer);
        stream.str(buffer);
        stream >> problem.cardinality;
        stream.clear();

        is >> problem.language;

        for (unsigned i = 0; i < problem.cardinality; ++i)
        {
            std::getline(is, buffer);
            problem.cases.push_back(Problem::Case(buffer, problem.language));
        }
    }

    return is;
}

void Problem::Case::resolve()
{
    typedef std::string token;
    std::list<token> tokens;

    // tokenize
    token curr_token;
    bool in = false;
    for (unsigned i = 0; i < pattern.length(); ++i)
    {
        if (pattern[i] == '(')
            in = true;
        else if (pattern[i] == ')')
            in = false;
        else
            curr_token += pattern[i];

        if (!in)
        {
            tokens.push_back(curr_token);
            curr_token.clear();
        }
    }

    std::set<std::string> tmp = language.dict;

    std::list<token>::const_iterator it = tokens.begin();
    for (unsigned i = 0; it != tokens.end(); ++it, ++i)
    {
        std::set<std::string>::const_iterator jt = tmp.begin();
        for (; jt != tmp.end(); ++jt)
            if (it->find((*jt)[i]) == std::string::npos)
                tmp.erase(jt);
    }

    result = tmp.size();
}

}

int main()
{
    codejam::Problem problem;
    std::ifstream input("A-small-attempt0.in");

    input >> problem;
    std::cout << problem;
}
