#include <iostream>
#include <string>
#include <map>
#include <boost/regex.hpp>

/* STRATEGY

Create a regular expression for each input expression and try to 
match the words in the language to that expression. Count the matches.

Using Boost.Regex from boost-1.33.1-4 (latest cygwin build)

to compile:

g++ -I /usr/include/boost-1_33_1/ al.cpp -lboost_regex-gcc-mt

(Note that the -l comes after the .cpp. It doesn't work the other way around.)

*/

void output(size_t result, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << result << std::endl;
}

class Lang
{
    private:
    typedef std::vector<std::string> string_list_t;
    typedef std::vector<std::string>::iterator string_iter_t;
    size_t m_num_letters;
    string_list_t m_words;

    public:
    Lang(size_t num_letters, string_list_t& words)
        : m_num_letters(num_letters),
          m_words(words)
    {
    }

    size_t get_match_count(const std::string& expression)
    {
        const boost::regex e(convert_expression(expression).c_str());
        size_t result = 0;

        for (string_iter_t iter = m_words.begin(); 
            iter != m_words.end(); 
            ++iter)
        {
            if (boost::regex_match(*iter, e))
                ++result;
        }

        return result;
    }

    private:
    std::string convert_expression(const std::string& alien_expr)
    {
        std::string result;
        result.reserve(alien_expr.size());

        for (std::string::const_iterator iter = alien_expr.begin(); 
             iter != alien_expr.end();
             ++iter)
        {
            switch (*iter)
            {
                case '(': 
                    result.push_back('[');
                    break;
                case ')': 
                    result.push_back(']');
                    break;
                default:    
                    result.push_back(*iter);
            }
        }

        return result;
    }
};

int main()
{
    size_t num_letters, num_words, num_cases;
    std::cin >> num_letters >> num_words >> num_cases;

    std::vector<std::string> alien_words;
    alien_words.reserve(num_words); 

    for (size_t word = 0; word < num_words; ++word)
    {
        std::string alien_word;
        std::cin >> alien_word;
        alien_words.push_back(alien_word);
    }

    Lang lang(num_letters, alien_words);

    for (size_t tcase = 0; tcase < num_cases; ++tcase)
    {
        std::string case_string;
        std::cin >> case_string;
        output(lang.get_match_count(case_string), tcase);
    }

    return 0;
}
