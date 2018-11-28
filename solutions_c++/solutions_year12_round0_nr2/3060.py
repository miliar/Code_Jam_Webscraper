/*
    Google Code Jam 2012
    Problem B
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
#define MAX_TEST_CASE 100

#define MIN_GOOGLERS 1
#define MAX_GOOGLERS 100

#define MAX_BEST_RES 10
#define MAX_SCORES_VAL 30

static bool its_maximum(int iscore, int bestres, int &uberraschung)
{
    bool result = false;
    int mid = iscore / 3;
    int frac = iscore % 3;

    if(mid >= bestres)
    {
        result = true;
    }
    else if((mid + 1) == bestres)
    {
        if(frac == 0)
        {
            if((mid > 0) && uberraschung)
            {
                uberraschung--;
                result = true;
            }
        }
        else
            result = true;
    }
    else if((mid + 2) == bestres)
    {
        if(frac == 2)
        {
            if(uberraschung)
            {
                uberraschung--;
                result = true;
            }
        }
    }

    return result;
}

static int get_googlers(QString &testCase)
{
    int result = 0;
    QStringList scores = testCase.split(" ", QString::SkipEmptyParts);
    bool converted = false;
    int googlers;
    int uberraschung;
    int bestres;

    if(scores.count() >= 3)
    {
        googlers = scores.at(0).toInt(&converted);
        if(converted && (googlers >= MIN_GOOGLERS) && (googlers <= MAX_GOOGLERS))
        {
            uberraschung = scores.at(1).toInt(&converted);
            if(converted && (uberraschung >= 0) && (uberraschung <= googlers))
            {
                bestres = scores.at(2).toInt(&converted);
                if(converted && (bestres >= 0) && (bestres <= MAX_BEST_RES))
                {
                    qWarning("Googlers %d Surp %d bestres %d", googlers, uberraschung, bestres);
                    for(int i = 0; i < googlers; i++)
                    {
                        int iscores = scores.at(3 + i).toInt(&converted);
                        if(converted && (iscores >= 0) && (iscores <= MAX_SCORES_VAL))
                        {
                            if(its_maximum(iscores, bestres, uberraschung))
                                result++;
                        }
                        else
                        {
                            qWarning("Invalid score %d", iscores);
                        }
                    }
                }
                else
                {
                    qWarning("Invalid best result: %d\n", bestres);
                }
            }
            else
            {
                qWarning("Invalid count of surprise: %d\n", uberraschung);
            }
        }
        else
        {
            qWarning("Invalid count of googlers: %d\n", googlers);
        }
    }
    else
    {
        qWarning("Invalid args count: %d\n", scores.count());
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
            outStream << "Case #" << ++caseNo << ": " << get_googlers(line) << endl;
        } while (caseNo < countTests);

        if(caseNo == countTests)
            result = 0;
    }

    return result;
}
