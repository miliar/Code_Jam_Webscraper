#include <iostream>
#include <QtCore/QFile>
#include <QtCore/QTextStream>
#include <QtCore/QHash>
#include <QtCore/QDebug>

int main(int argc, char **argv) {
    
    QString G = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv q z";
    QString E = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up z q";
    
    QFile file("input.dat");
    file.open(QIODevice::ReadOnly);
    QTextStream stream(&file);
    
    QFile outfile("output.dat");
    outfile.open(QIODevice::WriteOnly);
    QTextStream out(&outfile);
    
    int n;
    stream >> n;
    
    qDebug() << n;
    stream.readLine();
    
    for (int i = 0; i < n; ++i)
    {
        QString line = stream.readLine();
        QString output;
        for (int j = 0; j < line.size(); ++j)
        {
            if (!G.contains(line[j]))
            {
                qDebug() << line[j];
            }
            output += E[G.indexOf(line[j])];
        }
        out << "Case #" << i+1 << ": " << output << endl;
    }
    
    file.close();
    outfile.close();
    return 0;
}
