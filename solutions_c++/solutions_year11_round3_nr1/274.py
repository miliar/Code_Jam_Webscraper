#include <QtCore/QCoreApplication>
#include <QDebug>
#include <QFile>
#include <QString>
#include <QVector>
#include <cstdio>

bool firsthm(const QVector<QVector<char> > &m, int &x, int &y) {
    for (int j=0; j<m.size(); ++j) {
         for (int k=0; k<m[j].size(); ++k) {
             if (m[j][k] == '#') {
                 x = j;
                 y = k;
                 return true;
             }
         }
    }
    return false;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QTextStream in(stdin);
    QTextStream out(stdout);

    int T;
    in >> T;
    in.readLine();

    for (int i = 0; i<T; ++i) {
        int R;
        in >> R;

        int C;
        in >> C;
        in.readLine();

        QVector<QVector<char> > matrix;

        for (int j=0; j<R; ++j) {
            matrix << QVector<char>();
            for (int k=0; k<C; ++k) {
                char next;
                in >> next;
                matrix.back() << next;
            }
            matrix.back() << '.';
            in.readLine();
        }
        matrix << QVector<char>();
        for (int l=0; l<C; ++l) {
            matrix.back() << '.';
        }

   //     qDebug() << matrix;

        bool possible = true;
        while (true) {
            int x, y;
            if (!firsthm(matrix, x, y))
                break;
            matrix[x][y] = '/';
            if (matrix[x][y+1] == '#') {
               matrix[x][y+1] = '\\';
            } else {
               possible = false;
               break;
           }

            if (matrix[x+1][y] == '#') {
               matrix[x+1][y] = '\\';
            } else {
               possible = false;
               break;
           }

            if (matrix[x+1][y+1] == '#') {
               matrix[x+1][y+1] = '/';
            } else {
               possible = false;
               break;
           }
        }

        if (possible) {
            out << "Case #" << i+1 << ":" << endl;
             for (int j=0; j<R; ++j) {
                  for (int k=0; k<C; ++k) {
                      out << matrix[j][k];
                  }
                  out << endl;
             }
        } else {
            out << "Case #" << i+1 << ":\nImpossible" << endl;
        }

     //   printf("Case #%d: %.10f\n", i+1, max);


    }

    a.exit();
}
