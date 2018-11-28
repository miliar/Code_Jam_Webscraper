#ifndef INPUT_H
#define INPUT_H

#include <QString>
#include <QList>
#include <QStringList>
#include <QPair>
#include <cstdio>

#include <iostream>

class Input
{

  public:
    static const QString& readLine();
    static int readInteger();
    static QList<int> readIntegers();

};

#endif // INPUT_H
