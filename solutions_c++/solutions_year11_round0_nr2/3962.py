#include <QtCore/QCoreApplication>

#include <QFile>
#include <QTextStream>
#include <QHash>
#include <QPair>
#include <QSet>
#include <QDebug>

#include <QMultiHash>
class
        GoogleJam
{
public:
    int nTests ;
    QHash< QPair<QChar, QChar>, QChar> combine;
    QMultiHash<QChar, QChar> opposed;
    QSet<QChar> waitingOpposed;
    QTextStream *in;
    QTextStream *out;

    GoogleJam(QString inputStr, QString outputStr)
    {
        QFile input(inputStr);
        nTests = 0;

        if (input.open(QFile::ReadOnly | QFile::Text)) {
            in = new QTextStream(&input);

        QFile output(outputStr);
        output.open(QFile::WriteOnly | QFile::Text );
        out = new QTextStream(&output);

        solve();

        } else
        {
            qDebug() << " couldnt open file " << inputStr;
        }
    }


void
solve()
{
    *in >> nTests;

    for(int i=0; i<nTests; ++i)
    {
        *out << "Case #" << i + 1 << ": " ;
        qDebug() << " case " << i;

        //read combines
        int nCombines = 0;
        combine.clear();
        *in >> nCombines;
        for (int j = 0; j < nCombines; ++j)
        {//3 chars each
            QString comb;
            *in >> comb;

            if (comb.size() != 3)
            {
                qDebug() << "not 3 chars!";
                continue;
            }

            QChar A, B, C;
            A = comb[0]; B = comb[1];
            C = comb[2];
     //       qDebug() << "[" << A << ", " << B << "]=>" << C;
            combine.insert(qMakePair(A, B), C);
            combine.insert(qMakePair(B, A), C);


        }

        //opposed
        int nOpposed = 0;
        opposed.clear();
        *in >> nOpposed;
        for (int j = 0; j < nOpposed; ++j)
        {//list of opposed 2 chars each
            QString opp;
            *in >> opp;
            if (opp.size()!=2)
            {
                qDebug() << "not 2 chars!";
                continue;
            }

            QChar A = opp[0], B = opp[1];
       //     qDebug() << A << " x " << B;
            opposed.insert(A, B);
            opposed.insert(B, A);
        }

        //input
        int nInput = 0;
        initTest();
        *in >> nInput;
        QString input;
        *in >> input;
        if (input.size() != nInput)
        {
            qDebug() << " incorrect input size ";
            continue;
        }

       QString output = solveString(input);
  //      qDebug() << " out: " << output;
       *out << formatOutput(output) << "\n";
    }

}

QString
formatOutput(QString in)
{
    QString res = "[";
    bool first = true;
    foreach(QChar c, in)
    {
        if (first)
            first = false;
        else
            res += ", ";
        res += QString("%1").arg(c);
    }
    res += "]";
    return res;
}

QString
solveString(QString input)
{
    QString res;
    for (int i = 0; i < input.size(); ++i)
    {
        res.append(input[i]);

        //try to combine
        if (res.size() >= 2)
        {
            QPair<QChar, QChar> pair (res[res.size()-1], res[res.size()-2]);
            if (combine.contains(pair))
            {
                res.truncate(res.size() - 1);
                res[res.size() - 1] = combine.value(pair);
                continue;
            }
        }

        //try to oppose
//        if (waitingOpposed.contains(input[i]))
//        {
//            waitingOpposed.clear();
//            res.clear();
//            continue;
//        }
        for (int j = 0; j < res.size() - 1; ++j)
        {
            if (opposed.contains(res[j], res[res.size() - 1]))
            {
                res.clear();
                break;
            }

        }

        //if we are here, it didnt combine nor collapse
//        foreach(QChar op, opposed.values(input[i]))
//        {
//            waitingOpposed.insert(op);
//        }


    }
    return res;
}

void
initTest()
{
    waitingOpposed.clear();
}


};

int main(int argc, char *argv[])
{
    qDebug() << " hello ";
    QCoreApplication a(argc, argv);

    GoogleJam("small.txt", "smallOut.txt");
//    GoogleJam("large.txt", "largeOut.txt");
    return 1;

    return a.exec();
}
