#ifndef RECYCLE_H
#define RECYCLE_H

#include "TestObj.h"


class Recycle : public TestObj
{
    public:
        Recycle();
        virtual ~Recycle();
    protected:
        virtual const char* InputFileName() { return "recycle.txt"; }
        virtual void Process(ifstream& in, ofstream& out, int count);
    private:
};

#endif // RECYCLE_H
