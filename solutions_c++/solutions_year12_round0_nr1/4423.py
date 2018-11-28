#include <QTextStream>
#include <QString>
#include <QMap>
#include <QSet>

#include <iostream>

using namespace std;

QMap<QChar, QChar> m;

QString input_sample = 
    "ejp mysljylc kd kxveddknmc re jsicpdrysi"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" 
"de kr kd eoya kw aej tysr re ujdr lkgc jv";

QString output_sample = 
    "our language is impossible to understand"
"there are twenty six factorial possibilities"
"so it is okay if you want to just give up";

void fatal_error(const QString & msg) 
{
    cerr << "Fatal error: " << msg.toUtf8().data() << "\n";
    exit(-1);
}

void find_mapping() 
{
    if (input_sample.size() != output_sample.size())  
        fatal_error("Input and output samples are not of same size");
    
    m['y'] = 'a';
    m['e'] = 'o';
    m['q'] = 'z';
    
    for (int i = 0; i < input_sample.size(); ++i) {
        if (! m.contains(input_sample.at(i)))
            m[input_sample.at(i)] = output_sample.at(i);
        else if (m[input_sample.at(i)] != output_sample.at(i))
            fatal_error(QString("Already found different mapping for char %1 at pos %2").arg(input_sample[i]).arg(i));
    }
    
    int n_missing_g_chars = 0;
    QChar missing_g_char;
    for (int i = 'a'; i <= 'z'; ++i) {
        if (m.contains(QChar(i))) 
            cerr << (char) i << " -> " << m[QChar(i)].toLatin1() << "\n";
        else {
            cerr << (char) i << " -> missing\n";
            missing_g_char = QChar(i);
            n_missing_g_chars++;
        }
    }
    
    // Find the missing g mapping
    if (n_missing_g_chars == 1) {
        QSet<QChar> s = m.values().toSet();
        for (int i = 'a'; i <= 'z'; ++i) {
            if (! s.contains(i)) {
                cerr << "Found missing mapping: " << missing_g_char.toLatin1() << " -> " << (char) i << "\n";
                m[missing_g_char] = QChar(i);
            }
        }
    }
}

QString map_line(QString & s)
{
    QString r;
    
    for (int i = 0; i < s.size(); ++i) {
        if (m.contains(s.at(i))) {
            r += m[s.at(i)];
        }
        else {
            cerr << "No mapping found for '" << s.at(i).toLatin1() << "'\n";
            exit(-1);
        }
    }
    
    return r;
}

int main()
{
    int n_cases;
    QTextStream qtin(stdin);
    
    find_mapping();
    
    qtin >> n_cases;
    // eat line ending of 1st line
    qtin.readLine();
    
    for (int i = 1; i <= n_cases; i++) {
        QString line = qtin.readLine();

        cout << "Case #" << i << ": " << map_line(line).toUtf8().data() << "\n";
    }
}
