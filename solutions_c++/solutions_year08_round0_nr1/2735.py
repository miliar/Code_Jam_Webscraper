#include <iostream>
#include <map>
#include <string>
#include <vector>

// #define DEB_PRINT

int main(int argc, char *argv[])
{
    std::map<std::string, int> searchMap;
    std::vector<std::string> queryList;
    std::string nl;
    int N = 0;

    std::cin >> N;

#ifdef DEB_PRINT
    std::cout << "DEB: Trials" << N << std::endl;
#endif
    for (int i = 0; i < N; ++i)
    {
        int O = 0, Q = 0, S = 0;
        searchMap.clear();
        queryList.clear();
        std::cin >> S;
        getline(std::cin, nl); // flush newline
#ifdef DEB_PRINT
        std::cout << "DEB: Engines " << S << std::endl;
#endif
        for (int j = 0; j < S; ++j)
        {
            std::string engine;
            getline(std::cin, engine);
            searchMap.insert(std::make_pair(engine, 0));
#ifdef DEB_PRINT
            std::cout << "DEB: Engine#" << j << " " << engine << std::endl;
#endif
        } // Search engine loop
        std::cin >> Q;
        getline(std::cin, nl); // flush newline
#ifdef DEB_PRINT
        std::cout << "DEB: Queries " << Q << std::endl;
#endif
        for (int k = 0; k < Q; ++k)
        {
            std::string query;
            getline(std::cin, query);
            std::map<std::string, int>::iterator srch = searchMap.find(query);
            int count = srch->second + 1;
            searchMap.erase(srch);
            searchMap.insert(std::make_pair(query, count));
            queryList.push_back(query);
#ifdef DEB_PRINT
            std::cout << "DEB: Query#" << k << " " << query << std::endl;
#endif
        } // Query loop

        for (std::map<std::string, int>::iterator mIt = searchMap.begin();
             mIt != searchMap.end(); ++mIt)
        {
#ifdef DEB_PRINT
            std::cout << "DEB: Key " << mIt->first << " " << mIt->second << std::endl;
#endif
        }
        std::string lowname;
        lowname.clear();
        for (std::vector<std::string>::iterator qIt = queryList.begin();
             qIt != queryList.end(); ++qIt)
        {
            std::string query = *qIt;
#ifdef DEB_PRINT
            std::cout << "DEB: query " << query << " vs " << lowname << std::endl;
#endif
            if (qIt == queryList.begin() || lowname == query)
            {
#ifdef DEB_PRINT
                std::cout << "DEB: checking" << std::endl;
#endif
                int l, longest = -1;
                // Go through all search engines, looking for the longest run
                for (std::map<std::string, int>::iterator mIt = searchMap.begin();
                     mIt != searchMap.end(); ++mIt)
                {
                    // Name can't match
                    if (! lowname.empty() && query == mIt->first)
                        continue;
                    if (! mIt->second) // Zero count
                    {
#ifdef DEB_PRINT
                        std::cout << "DEB: trivial result: " << mIt->first << std::endl;
#endif
                        lowname = mIt->first;
                        break;
                    }
                    std::vector<std::string>::iterator q2It = qIt;
                    // Skip the present guy, not for first
                    if (qIt != queryList.begin())
                        q2It ++;
                    for (l = 0; q2It != queryList.end(); ++q2It, ++l)
                    {
                        if (*q2It == mIt->first)
                            break;
                    }
#ifdef DEB_PRINT
                    std::cout << "DEB: run length for " << mIt->first << ": " << l << std::endl;
#endif
                    if (longest == -1 || l > longest)
                    {
                        longest = l;
                        lowname = mIt->first;
                    }
                }
                if (qIt != queryList.begin())
                    ++O;
#ifdef DEB_PRINT
                std::cout << "DEB: selected " << lowname << std::endl;
#endif
            }
            // Reduce counts accordingly
            std::map<std::string, int>::iterator srch = searchMap.find(query);
            int count = srch->second - 1;
            if (count < 0)
                count = 0;
            searchMap.erase(srch);
            searchMap.insert(std::make_pair(query, count));
        }
        std::cout << "Case #" << i + 1 << ": " << O << std::endl;
    } // Case loop
}
/* Keep these lines at the end of the file for VI/VIM: Set shift width to 4 */
/* vi: set sw=4: */
