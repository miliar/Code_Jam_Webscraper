/*
 * (C) Copyright Martin Juhlin, 2013
 * martin.juhlin@gmal.com
 */

#ifndef __TEXTOUTPUT_H__
#define __TEXTOUTPUT_H__

#include <QByteArray>
#include <QList>

class TextOutput
{
public:
    TextOutput();
    virtual ~TextOutput();
    
    void out(char value);
    void out(const char * text);
    void out(const QByteArray & data);
    void out(int value);
    void out(const QList<int> & values);
    void endl();
    
    bool isEmpty();

private:
    void prepare();
    
private:
    struct Data {
        QByteArray buf;
        int caseNumber;
        bool empty;
    };
    Data d;
};

#endif // __TEXTOUTPUT_H__
