#include <iostream>
#include <QtCore/QFile>
#include <QtCore/QTextStream>
#include <QtCore/QHash>
#include <QtCore/QDebug>

inline int recycled(int a, int k, int v)
{
    return (a % k) * v + (a / k);
}

inline bool are_recycled(int a, int b)
{
    QString as = QString::number(a);
    QString bs = QString::number(b);
    int n = as.size();
    
    for (int i = 0; i < n; ++i)
    {
        if (as == bs.mid(i) + bs.left(i))
        {
            return true;
        }
    }
    return false;
}

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
        int A, B;
        stream >> A >> B;
        
        QList<int> K;
        int k = 10;
        while (k <= A)
        {
            K << k;
            k *= 10;
        }
                
        int R = 0;
        for (int a = A; a <= B; ++a)
        {
            QSet<int> rs;
            foreach (int t, K)
            {
                int r = recycled(a, t, k/t);
                if (r >= A && r < a)
                {
                    rs << r;
                }
            }
            R += rs.size();
        }
        out << "Case #" << i+1 << ": " << R << endl;
    }
    
    file.close();
    outfile.close();
    return 0;
}
