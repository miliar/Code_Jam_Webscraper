#include <iostream>
#include <string>
#include <set>
#include <vector>

//#define DEBUG

void output(size_t result, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << result << std::endl;
}

class EngineBlock
{
    public:
    EngineBlock()
    {
    }

    void add(const std::string& engine)
    {
#ifdef DEBUG
        std::cout << "adding engine: \"" << engine << "\"" << std::endl;
#endif
        m_engines.insert(engine);
    }

    // Algorithm:
    // 1) copy the map of engines
    // 2) remove engines iterating through queries
    // 3) if all engines removed, 
    //    increment result and add them all except the current one back

    // This assumes the greedy algorithm (find the farthest path for each
    // "leg") is the optimal one. That can be proven.

    size_t optimize(const std::vector<std::string>& queries)
    {
#ifdef DEBUG
        std::cout << "optimizing" << std::endl;
#endif
        size_t result = 0;

        std::vector<std::string>::const_iterator q_iter = queries.begin();

        while (q_iter != queries.end())
        {
            std::set<std::string> current_engines = m_engines; 
            while(q_iter != queries.end())
            {
                current_engines.erase(*q_iter);
                if (current_engines.empty())
                {
                   ++result;
                   break; 
                }
                ++q_iter;
            }
        }

        return result;
    }

    private:
    std::set<std::string> m_engines;
};

static const int MAX_ENGINE_BUFSIZE = 100 + 1;
static const int MAX_QUERY_BUFSIZE = 100 + 1;

int main()
{
    size_t numcases;
    std::cin >> numcases;
#ifdef DEBUG
    std::cout << numcases << " cases" << std::endl;
#endif
    for (size_t casex = 0; casex < numcases; ++casex)
    {
        size_t num_engines;
        std::cin >> num_engines;
        std::cin.ignore(4, '\n'); // apparently need to suck in EOL here
#ifdef DEBUG
        std::cout << num_engines << " engines" << std::endl;
#endif
        EngineBlock engines;
        for (size_t engine = 0; engine < num_engines; ++engine)
        {
            char engine_cstr[MAX_ENGINE_BUFSIZE];
            std::cin.getline(engine_cstr, MAX_ENGINE_BUFSIZE, '\n');
            engines.add(std::string(engine_cstr));
        }

        size_t num_queries;
        std::cin >> num_queries;
        std::cin.ignore(4, '\n'); // apparently need to suck in EOL here
#ifdef DEBUG
        std::cout << num_queries << " queries" << std::endl;
#endif
        std::vector<std::string> queries(num_queries);
        for (size_t query = 0; query < num_queries; ++query)
        {
            char query_cstr[MAX_QUERY_BUFSIZE];
            std::cin.getline(query_cstr, MAX_QUERY_BUFSIZE, '\n');
            queries[query] = query_cstr;
        }
        size_t result = engines.optimize(queries);
        output(result, casex);
    }

    return 0;
}
