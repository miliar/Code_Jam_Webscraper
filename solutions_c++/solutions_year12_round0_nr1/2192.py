#ifndef TONGUES_H
#define TONGUES_H

#include "TestObj.h"

#define MAP_SIZE 128
class Tongues : public TestObj
{
    public:
        Tongues();
        virtual ~Tongues();
    protected:
        virtual const char* InputFileName() { return "tongues.txt"; }
        virtual void Process(std::ifstream& in, std::ofstream& out);
    private:
        char map_[MAP_SIZE];
};

#endif // TONGUES_H
