#include <QtCore>
#include <QFile>
#include <iostream>

typedef struct{
    qint64 K;
    qint64 R;
    qint64 N;
    QList<qint64> qlGroups;
}stTc;
QList<QString> load( const QString& filename )
{
    QList<QString> returnList;
    QFile file( filename );
    if ( !file.open( QIODevice::ReadOnly ) ) {
        qDebug()<< qPrintable(QString( "Failed to load \'%1\'" ).arg( filename ));
        return returnList;
    }
    QTextStream ts( &file );
    QString qsLine;


    while ( !ts.atEnd() ) {
        returnList.append(ts.readLine());
    }
    return returnList;
}
void fileSave(const QString& filename,QList<QString> qlContent)
{
    QFile file( filename );
    if ( !file.open( QIODevice::WriteOnly ) ) {
        qDebug()<< qPrintable(QString( "Failed to write file \'%1\'" ).arg( filename ));
        return ;
    }
    QTextStream ts( &file );
    QListIterator<QString> qliList(qlContent);
    while(qliList.hasNext()){

        ts << qliList.next() << endl;

    }
    file.close();

}

qint64 sum(stTc st){
    qint64 totalSum=0;
    for(qint64 i=0;i<st.R;i++){
        QList<qint64> costerList;
        qint64 roundSum=0;
        while(!st.qlGroups.isEmpty() && (roundSum+st.qlGroups.at(0)) <=st.K){
            roundSum += st.qlGroups.at(0);
            costerList.append(st.qlGroups.at(0));
            st.qlGroups.removeFirst();
        }
        totalSum += roundSum;
        while(!costerList.isEmpty()){
            st.qlGroups.append(costerList.at(0));
            costerList.removeFirst();
        }
    }
    return totalSum;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    QList<QString> qlInContent = load("C-small-attempt0.in");


    QList<QString> qlOutContent;
    bool ok;
    qint64 count = 1;
    qlInContent.removeAt(0);
    QListIterator<QString> qliList(qlInContent);
    while(qliList.hasNext()){

        stTc st;
        QStringList qslCaseMeta = qliList.next().split( " ",QString::SkipEmptyParts);
        st.R = QString(qslCaseMeta.at(0)).toInt(&ok);
        st.K = QString(qslCaseMeta.at(1)).toInt(&ok);
        st.N = QString(qslCaseMeta.at(2)).toInt(&ok);
        qslCaseMeta = qliList.next().split( " ",QString::SkipEmptyParts);
        for(int i=0;i< st.N;i++){
            st.qlGroups.append((qint64)QString(qslCaseMeta.at(i)).toInt(&ok));
        }


        qlOutContent.append(QString("Case #")+QString::number(count)+": "+QString::number(sum(st)));

        count++;
    }
    fileSave("output_file.out",qlOutContent);
    return 0;

}
