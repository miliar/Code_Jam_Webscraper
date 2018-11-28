//#include <iostream>

#include <QTextStream>
#include <QStringList>
#include <QMap>
#include <QSet>

typedef QMap<QChar, QChar> dictionary;

dictionary learn(QString sample, QString source)
{
    dictionary dict;
    Q_ASSERT(sample.size() == source.size());
    for (int i = 0; i < sample.size(); ++i)
    {
        QChar ch = sample[i];
        if (dict.contains(ch)) {
            Q_ASSERT(dict[ch] == source[i]);
        } else {
            dict[ch] = source[i];
        }
    }
    return dict;
}

void trycomplement(dictionary& dict)
{
    QString abcd = "abcedfghijklmnopqrstuvwxyz";
    QSet<QChar> source, dest;
    foreach(QChar ch, abcd)
    {
        source.insert(ch);
        dest.insert(ch);
    }
    foreach(QChar ch, dict.keys())
    {
        source.remove(ch);
        dest.remove(dict[ch]);
    }

    if (source.size() == 1 && dest.size() == 1)
    {
        dict[*source.begin()] = *dest.begin();
    }
}


char sample[] = "y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char source[] = "a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int main(int argc, char *argv[])
{
    dictionary dict = learn(sample, source);
    trycomplement(dict);

    dict[' '] = ' ';

    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        QString instr, outstr;
        instr = ins.readLine();
        foreach(QChar ch, instr)
        {
            outstr.append(dict[ch]);
        }
        out << QString("Case #%1: %2\n").arg(QString::number(i + 1), outstr);
    }

    return 0;
}
