#include <iostream>
#include <QtCore/QFile>
#include <QtCore/QTextStream>
#include <QtCore/QHash>
#include <QtCore/QDebug>

int main(int argc, char **argv) {
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
        int N, S, p;
        stream >> N >> S >> p;
        int t[N];
        
        for(int j = 0; j < N; ++j)
        {
            stream >> t[j];
        }
        
        int sure = 0;
        int noway = 0;
        int maybe = 0;
        for (int j = 0; j < N; ++j)
        {
            if (t[j] > 3*p-3)
            {
                ++sure;
            }
            else if ( (p > 1 && t[j] > 3*p-5) || (p == 1 && t[j] > 0) )
            {
                ++maybe;
            }
        }
        out << "Case #" << i+1 << ": " << sure + qMin(maybe, S) << endl;
    }
    
    file.close();
    outfile.close();
    return 0;
}
