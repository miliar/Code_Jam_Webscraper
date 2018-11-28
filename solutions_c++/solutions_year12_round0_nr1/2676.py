#include <QtCore/QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QStringList>
#include <QDebug>

#include <QHash>

QMap<QChar, QChar> mapping;

QString solveCase(QTextStream *input) {
    QObject autodelete;
    mapping.insert(' ', ' ');
    mapping.insert('y', 'a');
    mapping.insert('n', 'b');
    mapping.insert('f', 'c');
    mapping.insert('i', 'd');
    mapping.insert('c', 'e');
    mapping.insert('w', 'f');
    mapping.insert('l', 'g');
    mapping.insert('b', 'h');
    mapping.insert('k', 'i');
    mapping.insert('u', 'j');
    mapping.insert('o', 'k');
    mapping.insert('m', 'l');
    mapping.insert('x', 'm');
    mapping.insert('s', 'n');
    mapping.insert('e', 'o');
    mapping.insert('v', 'p');
    mapping.insert('q', 'z');
    mapping.insert('p', 'r');
    mapping.insert('d', 's');
    mapping.insert('r', 't');
    mapping.insert('j', 'u');
    mapping.insert('g', 'v');
    mapping.insert('t', 'w');
    mapping.insert('h', 'x');
    mapping.insert('a', 'y');
    mapping.insert('z', 'q');
    QString g = input->readLine();
    QString out;
    for(int i=0; i<g.length(); i++) {
        out.append(mapping.value(g.at(i)));
    }
    return out;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    QStringList params = a.arguments();
    QString filename = params.at(1);
    QFile input(filename);
    input.open(QFile::ReadOnly);
    QTextStream iStream(&input);
    QTextStream output(stdout);
    int cases = iStream.readLine().toInt();
    for(int i=0; i<cases; i++) {
        output << QString("Case #%1: %2\n").arg(i+1).arg(solveCase(&iStream));
    }

    input.close();
    return 0;

}
