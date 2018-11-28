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
    static QList<unsigned long long> readIntegers();
    static double readDouble();
    static QList<double> readDoubles();

};

#endif // INPUT_H
