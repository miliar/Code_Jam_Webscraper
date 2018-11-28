#include <iostream>
#include <string>
#include <map>
#include <sys/time.h>

using namespace std;
typedef unsigned long u32;
typedef unsigned long long u64;
typedef signed long s32;

#pragma pack(0)

u64 GetUs()
{
    timeval tv;
    gettimeofday(&tv, 0);
    return tv.tv_sec * 1000000 + tv.tv_usec;
}

inline u64 djbHash(const char* str)
{
    u64 hash = 5381, c;

    while((c = *str++) != 0)
        hash = ((hash << 5) + hash) + c;

    return hash;
}

class FS
{
    typedef map< u64, FS > DirMap;
    DirMap mSubdirs;

public:
    u64 insert(string folders)
    {
        u64 count = 0;

        FS* lookup = this;
        string::size_type pos;
        string currFolder;

        while(folders.length())
        {
            pos = folders.find('/');
            if(pos != string::npos)
            {
                currFolder = folders.substr(0, pos);
                folders = folders.substr(pos + 1);
            }
            else
            {
                currFolder = folders;
                folders = "";
            }

            u64 hash = djbHash(currFolder.c_str());
            DirMap::iterator it = lookup->mSubdirs.find(hash);
            if(it == lookup->mSubdirs.end())
            {
                lookup->mSubdirs[hash] = FS();
                lookup = &(lookup->mSubdirs[hash]);

                ++count;
            }
            else
                lookup = &(it->second);
        }

        return count;
    }
};

int main()
{
    u32 t;
    cin >> t;

    for(u32 cs = 1; cs <= t; ++cs)
    {
        u32 n, m;
        cin >> n >> m;

        FS rootFs;

        for(u32 i = 0; i < n; ++i)
        {
            char root;
            cin >> root;

            string line;
            cin >> line;

            rootFs.insert(line);
        }

        u64 count = 0;

        for(u32 i = 0; i < m; ++i)
        {
            char root;
            cin >> root;

            string line;
            cin >> line;

            count += rootFs.insert(line);
        }

        cout << "Case #" << cs << ": " << count << endl;
    }

    return 0;
}
