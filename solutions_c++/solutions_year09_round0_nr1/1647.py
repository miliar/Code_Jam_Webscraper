#include <cassert>
#include <iostream>
#include <string>
#include <vector>

struct token_t
{
    std::vector<char> letters;
};

struct pattern_t
{
    ~pattern_t()
    {
        for (unsigned int i = 0; i < tokens.size(); i++)
        {
            delete tokens[i];
        }
        tokens.clear();
    }
    std::vector<token_t*> tokens;
};

typedef std::string word_t;

void parse_pattern(const std::string& pattern_str, pattern_t& pattern)
{
    for (unsigned int i = 0; i < pattern_str.size(); i++)
    {
        char character = pattern_str[i];
        token_t *token = new token_t;
        if (character == '(')
        {
            i++;
            while (pattern_str[i] != ')')
            {
                character = pattern_str[i];
                assert(isalpha(character));
                assert(tolower(character) == character);
                token->letters.push_back(character);
                i++;
            }
        }
        else
        {
            assert(isalpha(character));
            assert(tolower(character) == character);
            token->letters.push_back(character);
        }
        pattern.tokens.push_back(token);
    }
}

bool does_pattern_match_word(const pattern_t& pattern, const word_t& word)
{
    assert(pattern.tokens.size() == word.size());
    for (unsigned int i = 0; i < word.size(); i++)
    {
        const char word_letter = word[i];
        const token_t &token = *pattern.tokens[i];
        bool match = false;
        for (unsigned int j = 0; j < token.letters.size(); j++)
        {
            const char token_letter = token.letters[j];
            if (word_letter == token_letter)
            {
                match = true;
                break;
            }
        }
        if (!match)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    unsigned int L, D, N;

    std::cin >> L; // number of tokens per word/pattern
    std::cin >> D; // number of words
    std::cin >> N; // number of patterns

    // read words
    word_t *words = new word_t[D];
    for (unsigned int i = 0; i < D; i++)
    {
        std::cin >> words[i];
        assert(words[i].size() == L);
    }

    // read patterns
    pattern_t *patterns = new pattern_t[N];
    for (unsigned int i = 0; i < N; i++)
    {
        std::string pattern_str;
        std::cin >> pattern_str;
        parse_pattern(pattern_str, patterns[i]);
        assert(patterns[i].tokens.size() == L);
    }

    // find the number of matching words for every pattern
    for (unsigned int i = 0; i < N; i++)
    {
        int num_matching_words = 0;
        const pattern_t &pattern = patterns[i];
        for (unsigned int j = 0; j < D; j++)
        {
            const word_t &word = words[j];
            if (does_pattern_match_word(pattern, word))
            {
                num_matching_words++;
            }
        }

        std::cout << "Case #" << (i+1) << ": " << num_matching_words << std::endl;
    }

    delete[] words;
    delete[] patterns;

    return 0;
}

