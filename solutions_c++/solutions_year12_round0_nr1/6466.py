//Kamyar Kaviani
//Google Codejam Qualification, Problem A
//4/14/2012

#include <QtCore/QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QMap>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QFile *inFile = new QFile("C:\\Users\\Kamyar\\Desktop\\A-small-attempt6.in");
    QFile *outFile = new QFile("C:\\Users\\Kamyar\\Desktop\\output.txt");
    QTextStream in(inFile);
    QTextStream out(outFile);
    QString line, decrypted;
    QMap<QChar, QChar>* charMap = new QMap<QChar, QChar>();

    if (!inFile->open(QIODevice::ReadOnly | QIODevice::Text)){
        printf("Error opening input file.");
    }
    if (!outFile->open(QIODevice::ReadWrite | QIODevice::Text)) {
        printf("Error opening output file.");
    }

    QString sampleInput("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv");
    QString sampleOutput("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up");

    for (int c = 0; c < sampleInput.length(); c++) {
        charMap->insert(sampleInput.at(c).toLower(), sampleOutput.at(c).toLower());
    }
    charMap->insert('y', 'a');
    charMap->insert('e', 'o');
    charMap->insert('q', 'z');
    charMap->insert('z', 'q');

    line = in.readLine();
    int numberOfLines = line.toInt();

    for (int i = 0; i < numberOfLines; i ++) {
        line = in.readLine();
        decrypted = "";
        for (int c = 0; c < line.length(); c++) {
            decrypted += charMap->value(line[c]);
        }
        out << "Case #" << i+1 << ": "<< decrypted << endl;
    }

    return a.exec();
}
