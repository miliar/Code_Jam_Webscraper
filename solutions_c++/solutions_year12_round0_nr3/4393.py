#include "traite.h"
#include <QDebug>


Traite::Traite()
{
    m_fichierSortie = new QFile("./pb/sortie.txt");
    if ( m_fichierSortie->exists() )
        m_fichierSortie->remove();

    m_fichierEntree = NULL;
    m_isBeginning = false;
    m_numCase = 1;

    load();
}

void Traite::traite(QStringList allSl)
{
    QString strNumcase;
    QString str_rslt("");

    int rslt = 0;

    QStringList sl = allSl.at(0).split(" ");
    int A = sl.at(0).toInt();
    int B = sl.at(1).toInt();

    QString strA; strA.setNum(A);
    QString strB; strB.setNum(B);

    str_rslt = strA +","+ strB;
    QString strT;

    qDebug() << "A = " << A << ", B = " << B;
    for(int t=A ; t<=B ; t++)
    {
        strT.setNum(t);
        for( int n=1; n<strA.length(); n++)
        {
            QString tmp = strT.right(n) + strT.left(strT.length() - n );
            int p = tmp.toInt();
            if( p>=A && p<=B && p!=t )
                rslt++;
        }
    }
    qDebug() << "endCase";
    str_rslt.setNum(rslt/2);
    write("Case #"+ strNumcase.setNum(m_numCase++) +": "+ str_rslt) ;
}

void Traite::load()
{
    if( m_fichierEntree==NULL )
        m_fichierEntree = new QFile ("./pb/entree.txt");

    if(m_fichierEntree->open(QFile::ReadOnly))
    {
        QTextStream * stream = new QTextStream(m_fichierEntree);

        QString strNbCas = stream->readLine();
        int nbCas = strNbCas.toInt();
        qDebug() << "----------- nbCas = "<< nbCas;
        for( int k=0 ; k<nbCas ; k++ )
        {
            qDebug() << "-- cas "<< k+1;
            //            int strNblignePour1Cas = stream->readLine().toInt();
            QStringList sl;

            //            for(int t=0 ; t<strNblignePour1Cas ; t++ )
            //                sl << stream->readLine();

            sl << stream->readLine();

            traite(sl);
        }

        while ( !stream->atEnd() )
        {
            QString ligne = stream->readLine();
            qDebug() << ligne;
        }
        delete stream ;
        stream = NULL ;
        m_fichierEntree->close();
    }
    else
        qDebug() << "file not found.";
}

void Traite::write(QString ligne)
{
    bool isOkInMainFile = !m_fichierSortie->isOpen() && m_fichierSortie->open(QFile::Append) ;
    if ( isOkInMainFile )
    {
        QTextStream out( m_fichierSortie );
        out.setCodec("UTF-8");

        if( !m_isBeginning )
            m_isBeginning = true;
        else
            out << "\r\n";

        out << ligne ;
        out.flush();

        qDebug() << ligne;

        if( m_fichierSortie->isOpen() )
            m_fichierSortie->close();
    }
}
