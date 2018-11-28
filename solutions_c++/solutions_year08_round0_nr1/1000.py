#pragma warning (disable:4786)

#include <string>
#include <map>
#include <stdio.h>

using namespace std;

typedef std::map  <std::string, int> EngineMap;
typedef std::pair <std::string, int> EnginePair;

void trunc(char *s)
{
    char *p = strchr(s, '\n');
    if (p != NULL)
        *p = '\0';
}

int main ()
{
    int i, j;
    FILE *fp = NULL;

    fp = fopen("A-large.in", "r");
    if (!fp)
    {
        printf("Failed to open input file\n");
        exit(0);
    }

    // Read the number of cases
    int nCases;
    fscanf(fp, "%d", &nCases);

    i = 0;
    while (i < nCases)
    {
        // Read the number of search engines
        int nEngines;
        fscanf(fp, "%d", &nEngines);

        // Read the names of search engines, store the corresponding engine number in map
        j = 0;
        EngineMap engineMap;
        while (j < nEngines)
        {
            char engineName[128];
            fgets(engineName, sizeof(engineName), fp);
            trunc(engineName);
            if (engineName[0] == '\0')
            {
                fgets(engineName, sizeof(engineName), fp);
                trunc(engineName);
            }
            EnginePair enginePair(engineName, j);
            engineMap.insert(enginePair);
            j++;
        }

        // Read the number of queries
        int nQueries;
        fscanf(fp, "%d", &nQueries);

        // Allocate an array of ints to keep the cumulative frequencies
        int *freq = (int*) new int[nEngines];
        if (!freq)
        {
            printf ("malloc failed\n");
            exit(0);
        }

        j = 0;
        int nSwitches = 0;
        memset(freq, 0, nEngines * sizeof(int));
        while (j < nQueries)
        {
            int k;
            char query[128];
            fgets(query, sizeof(query), fp);
            trunc(query);
            if (query[0] == '\0')
            {
                fgets(query, sizeof(query), fp);
                trunc(query);
            }
            EngineMap::iterator iter = engineMap.find(query);

            freq[(*iter).second]++;
            for (k = 0; k < nEngines; k++)
                if (freq[k] == 0)
                    break;

            j++;
            if (k < nEngines) // found a 0 frequency
                continue;

            // time to switch, and reset frequencies
            nSwitches++;
            for (k = 0; k < nEngines; k++)
                if (k != (*iter).second)
                    freq[k] = 0;
        }

        // Print the output
        printf("Case #%d: %d\n", i + 1, nSwitches);

        delete freq;
        i++;
    }

    fclose(fp);
    return 0;
}
