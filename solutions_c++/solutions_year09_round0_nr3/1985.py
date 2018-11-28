#include <iostream>
#include <string>
#include <algorithm>
#include <stdint.h>

/* STRATEGY

Use recursion. Find the first letter we are looking for, then recurse on the substrings.

g++ wtcj.cpp

*/

typedef uint64_t count_t;

void output(const count_t& count, size_t line)
{
    char count_cstr[5];
    sprintf(count_cstr, "%04u", (size_t)(count % 10000));

    std::cout << "Case #" << line + 1 << ": " << count_cstr << std::endl;
}

static count_t max_ever = 0;

count_t sub_count(const char * target, size_t target_len, const char * key, size_t key_len)
{
    // printf("sub_count %s %d %s %d\n", target, target_len, key, key_len);
    if (key_len == 0)
        return 1;
    
    if (target_len == 0)
        return 0;

    const char * target_end = target + target_len;
    const char * target_loc = std::find(target, target_end, key[0]);
    if (target_loc == target_end)
        return 0;

    const char * next_target = target_loc + 1;
    int offset = next_target - target;
    
    count_t result =  
        // find next letter
        sub_count(next_target, target_len - offset, key + 1, key_len - 1) +
        // find next location of this letter
        sub_count(next_target, target_len - offset, key, key_len);

#ifdef FIND_MAX_EVER
    if (result > max_ever)
    {
        max_ever = result;
        printf("%lld\n", max_ever);
    }
#endif

    return result;
}

std::string prune(const std::string& target, const std::string& key)
{
    // remove anything from the target that's not in the key
    std::string result;

    for (std::string::const_iterator target_iter = target.begin();
         target_iter != target.end();
         ++target_iter)
    {
        if (std::find(key.begin(), key.end(), *target_iter) != key.end())
        {
            // it's in the key, we need it
            result.push_back(*target_iter);
        }
    }

    return result;
}

count_t sub_count(const std::string& target, const std::string& key)
{
    max_ever = 0;
   
    std::string pruned = prune(target, key);
    return sub_count(pruned.c_str(), pruned.size(), key.c_str(), key.size());
}

int main()
{
#ifdef UNIT_TEST
    assert(sub_count("a", "a") == 1);
    assert(sub_count("aa", "a") == 2);
    assert(sub_count("aaa", "a") == 3);
    assert(sub_count("aaba", "a") == 3);
    assert(sub_count("aa", "aa") == 1);
    assert(sub_count("a", "aa") == 0);
    assert(sub_count("aaa", "aa") == 3);
    assert(sub_count("aabb", "ab") == 4);
    assert(sub_count("aabbb", "ab") == 6);
    assert(sub_count("aababb", "ab") == 8);
#endif
    size_t num_cases;
    std::cin >> num_cases;
    std::string newline;
    std::getline(std::cin, newline);
    assert(newline.size() == 0);

    std::string key("welcome to code jam");
    for (size_t i_case = 0; i_case < num_cases; ++i_case)
    {
        std::string target;
        std::getline(std::cin, target);
        output(sub_count(target, key), i_case);
    }

    return 0;
}
