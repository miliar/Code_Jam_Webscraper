#include <QtCore>

QTextStream in(stdin);
QTextStream out(stdout);

int main()
{
    int L, D, N;
    in >> L;
    in >> D;
    in >> N;

    QStringList dic;
    for(int i=0; i<D;i++) {
        QString a; in >> a;
        dic.push_back(a);
    }

    for(int cas = 1; cas <= N; cas++) {
        QString str;
        in >> str;

        str.replace("(","[");
        str.replace(")","]");

        int count = 0;
        QRegExp rx("^" + str);
        foreach(const QString &s, dic)
            if(s.contains(rx))
                count++;

        out << QString("Case #%1: %2").arg(cas).arg(count) << endl << flush;
    }
    return 0;
}
