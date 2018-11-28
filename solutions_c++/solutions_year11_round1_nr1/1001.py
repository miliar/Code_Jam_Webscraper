#include <QtCore/QCoreApplication>
#include <QDebug>
#include <QFile>
#include <QString>
#include <QList>
#include <cstdio>

long long int lnko(long long int a, long long int b) {
   while (b != 0) {
       long long int t = b;
       b = a % b;
       a = t;
   }
   return a;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QTextStream in(stdin);
    QTextStream out(stdout);

    long long int T;
    in >> T;
    in.readLine();

    for (long long int i = 0; i<T; ++i) {
        long long int N;
        in >> N;

        long long int Pd;
        in >> Pd;

        long long int Pg;
        in >> Pg;

        if (Pg == 100 && Pd != 100 || Pg == 0 && Pd != 0) {
            out << "Case #" << i+1 << ": Broken" << endl;
        } else {
            long long int d = 100 / lnko(100, Pd);
            if (d <= N) out << "Case #" << i+1 << ": Possible" << endl;
            else out << "Case #" << i+1 << ": Broken" << endl;
        }

    }

    a.exit();
}
