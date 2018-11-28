#include <cstdio>
#include <cstring>

#include <map>
#include <string>

typedef std::map<std::string, void*> DIRECTORY;

int insertdir(DIRECTORY* dir, char* path)
{
    int numins = 0; std::string f;
    for (char* t = strtok(path, "/"); t; t = strtok(NULL, "/")) 
    {
        f = std::string(t);       
        if (dir->find(f) == dir->end()) { ++numins; dir->operator[](f) = new DIRECTORY(); }
        dir = (DIRECTORY*)(dir->operator[](f));
    };
        
    return numins;
};

int main()
{
    char line[255];

    int cases; fscanf(stdin, "%d", &cases);
    for (int c = 1; c <= cases; ++c)
    {
        DIRECTORY root;
        int d, w; fscanf(stdin, "%d %d", &d, &w);
        for (int i = 0; i < d; ++i)
        {
            fscanf(stdin, "%s", line);
            insertdir(&root, line + 1);
        };
        
        int numins = 0;
        for (int i = 0; i < w; ++i)
        {
            fscanf(stdin, "%s", line);
            numins += insertdir(&root, line + 1);
        };
        
        fprintf(stdout, "Case #%d: %d\n", c, numins);
    };
};

