/*
    Google Code Jam 2012
    Problem C
    int31

    This source code uses free and open source software - Qt library(http://qt.nokia.com)
    For compilation of this program you should:
        1. Create an empty directory and copy there this file.
        2. Execute the following commands in this directory:
            qmake -project
            make
 */

#include <QTextStream>
#include <QStringList>

#define MIN_TEST_CASE 1
#define MAX_TEST_CASE 50
#define MIN_NUMBER_VALUE 1
#define MAX_NUMBER_VALUE 2000000

class Pairs
{
public:
    Pairs(int a, int b) { pairs[0] = a; pairs[1] = b; }
    bool have(int a, int b) { return (((a == pairs[0]) && (b == pairs[1])) || ((a == pairs[1]) && (b == pairs[0]))); }
    int pairs[2];
};

typedef QList<Pairs> PairsList;

static int get_number_of_pairs(QString &testCase)
{
    QStringList integers = testCase.split(" ", QString::SkipEmptyParts);
    PairsList list;

    if(integers.count() >= 2)
    {
        bool converted = false;
        int min_val = integers.at(0).toInt(&converted);
        int max_val;

        if(!converted || (min_val < MIN_NUMBER_VALUE) || (min_val >= MAX_NUMBER_VALUE))
        {
            qWarning("Test case %s: invalid min value %d\n", qPrintable(testCase), min_val);
        }
        else
        {
            max_val = integers.at(1).toInt(&converted);
            if(!converted || (max_val <= MIN_NUMBER_VALUE) || (max_val > MAX_NUMBER_VALUE))
            {
                qWarning("Test case %s: invalid max value %d\n", qPrintable(testCase), max_val);
            }
            else
            {
                for(int i = min_val; i <= max_val; i++)
                {
                    QString startInteger = QString("%1").arg(i);

                    //qWarning("Integer %s\n", qPrintable(startInteger));
                    for(int j = 1; (j < startInteger.count()) && (startInteger.count() > 1); j++)
                    {
                        QString newInteger = startInteger.right(startInteger.count() - j);
                        newInteger += startInteger.left(j);
                        int value = newInteger.toInt(&converted);
                        //qWarning("Test value %d\n", value);
                        if(converted && (value >= min_val) && (value <= max_val) && (value != i))
                        {
                            bool have = false;

                            for(PairsList::iterator k = list.begin(); k != list.end(); ++k)
                            {
                                if(k->have(i, value))
                                {
                                    have = true;
                                    break;
                                }
                            }

                            if(!have)
                                list.push_back(Pairs(i, value));
                        }
                    }

                }
            }
        }
    }
    else
    {
        qWarning("Test case %s: bad count %d\n", qPrintable(testCase), integers.count());
    }

    return list.count();
}

int main()
{
    int result = -1;
    QTextStream inStream(stdin);
    QTextStream outStream(stdout);
    QString line = inStream.readLine();
    bool converted = false;
    int countTests = line.toInt(&converted);

    if(!converted || (countTests < MIN_TEST_CASE) || (countTests > MAX_TEST_CASE))
    {
        qWarning("Invalid count of tests: %d\n", countTests);
    }
    else
    {
        int caseNo = 0;

        qWarning("Count of tests: %d\n", countTests);

        do {
            line = inStream.readLine();
            if(line.isNull())
            {
                qWarning("Readed null string on %d test case\n", caseNo + 1);
                break;
            }
            outStream << "Case #" << ++caseNo << ": " << get_number_of_pairs(line) << endl;
        } while (caseNo < countTests);

        if(caseNo == countTests)
            result = 0;
    }

    return result;
}
