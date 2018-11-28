/*
    Google Code Jam 2012
    Problem A
    int31

    This source code uses free and open source software - Qt library(http://qt.nokia.com)
    For compilation of this program you should:
        1. Create an empty directory and copy there this file.
        2. Execute the following commands in this directory:
            qmake -project
            make
 */

#include <QTextStream>
#include <QHash>

#define MIN_TEST_CASE 1
#define MAX_TEST_CASE 100

class GooglereseMap : public QHash<QChar, QChar>
{
public:
    GooglereseMap();
};

GooglereseMap::GooglereseMap()
{
    insert(' ', ' ');
    insert('y', 'a');
    insert('n', 'b');
    insert('f', 'c');
    insert('i', 'd');
    insert('c', 'e');
    insert('w', 'f');
    insert('l', 'g');
    insert('b', 'h');
    insert('k', 'i');
    insert('u', 'j');
    insert('o', 'k');
    insert('m', 'l');
    insert('x', 'm');
    insert('s', 'n');
    insert('e', 'o');
    insert('v', 'p');
    insert('z', 'q'); // !!! last char
    insert('p', 'r');
    insert('d', 's');
    insert('r', 't');
    insert('j', 'u');
    insert('g', 'v');
    insert('t', 'w');
    insert('h', 'x');
    insert('a', 'y');
    insert('q', 'z');
}

static GooglereseMap gmap;

static QString get_english_test(QString &testCase)
{
    QString result;

    for(QString::iterator i = testCase.begin(); i != testCase.end(); i++)
    {
        if(*i == QChar('\n'))
        {
            break;
        }
        else
        {
            QChar engChar = gmap.value(*i);
            if(engChar != 0)
            {
                result.push_back(engChar);
            }
            else
            {
                qWarning("Unknown value for %c\n", i->toAscii());
            }
        }
    }

    return result;
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
            outStream << "Case #" << ++caseNo << ": " << get_english_test(line) << endl;
        } while (caseNo < countTests);

        if(caseNo + 1 == countTests)
            result = 0;
    }

    return result;
}
