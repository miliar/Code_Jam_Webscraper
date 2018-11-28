#include <QtCore>

char f(char ch) {
    switch(ch) {
        case 'a': return 'y';
        case 'b': return 'h';
        case 'c': return 'e';
        case 'd': return 's';
        case 'e': return 'o';
        case 'f': return 'c';
        case 'g': return 'v';
        case 'h': return 'x';
        case 'i': return 'd';
        case 'j': return 'u';
        case 'k': return 'i';
        case 'l': return 'g';
        case 'm': return 'l';
        case 'n': return 'b';
        case 'o': return 'k';
        case 'p': return 'r';
        case 'q': return 'z';
        case 'r': return 't';
        case 's': return 'n';
        case 't': return 'w';
        case 'u': return 'j';
        case 'v': return 'p';
        case 'w': return 'f';
        case 'x': return 'm';
        case 'y': return 'a';
        case 'z': return 'q';
    }
}

int main()
{
    QFile file_in("A-small-attempt0.in"), file_out("output.txt");
    if(!file_in.open(QFile::ReadOnly) || !file_out.open(QFile::WriteOnly))
        return EXIT_FAILURE;

    QTextStream fin(&file_in);
    //QTextStream fout(stdout);
    QTextStream fout(&file_out);

    int N;
    fin >> N;
    fin.skipWhiteSpace();
    for(int Ni=0; Ni<N; ++Ni) {
        QString line = fin.readLine();
        QTextStream lin(&line);
        QString str;
        fout << QString("Case #%1: ").arg(Ni+1);
        while(!lin.atEnd()) {
            lin >> str;
            QString str_true(str);
            for(int i=0; i<str.size(); ++i) {
                str_true[i] = QChar::fromAscii(f(str[i].toAscii()));
            }
            fout << str_true << " ";
        }
        endl(fout);
    }

    file_in.close();
    file_out.close();
    return EXIT_SUCCESS;
}
