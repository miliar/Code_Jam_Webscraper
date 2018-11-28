#include <QtCore/QCoreApplication>
#include <QtCore>
#include <QVector>

//#include <QTimer>
#include <iostream>
#include <QDebug>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    float foot = 0;

        std::cout <<  "Plz enter ";
//        std::cin  >> foot;

//        std::cout << "foots = " << foot/ 7.481;


        QFile file1("Input.in");
        QFile file2("Output.txt");
        file2.remove();

        file1.open(QIODevice::ReadOnly);
        file2.open(QIODevice::WriteOnly);

        QTextStream in(&file1);
        QTextStream out(&file2);


        QString str;
        int T;
        QString f[4];

        QString Res;


        in >> T;
//T=1;
        for(int i=1;i<=T;i++)
        {
            f->clear();
            for(int k=0;k<=3;k++)
            {

                in >> f[k];

            }

//qDebug() << f[1].at(0)<< " "<< f[1].at(1)<< " "<< f[1].at(2)<< " "<< f[1].at(3)<< " ";


            int xC,oC,pointC;
            bool xWon,oWon,Draw,notEnded;
            xWon=false;oWon=false;Draw=false;notEnded=false;
            xC=0;oC=0;pointC=0;
            for(int k=0;k<=3;k++)
            {
                for(int j=0;j<=3;j++)
                {
                    if (f[j][k] =='X')
                    {
                        xC++;

                    }

                    if (f[j][k] =='O')
                    {
                        oC++;
                    }

                    if (f[j][k] =='T')
                    {
                        xC++;
                        oC++;
                    }

                    if (f[j][k] =='.')
                    {
                        pointC++;
                    }



                }
                if (xC >=4)xWon=true;
                if (oC >=4)oWon=true;
                xC=0;oC=0;

            }


            for(int k=0;k<=3;k++)
            {
                for(int j=0;j<=3;j++)
                {
                    if (f[k][j] =='X')
                    {
                        xC++;
                    }

                    if (f[k][j] =='O')
                    {
                        oC++;
                    }

                    if (f[k][j] =='T')
                    {
                        xC++;
                        oC++;
                    }

                    if (f[k][j] =='.')
                    {
                        pointC++;
                    }


                }
                if (xC >=4)xWon=true;
                if (oC >=4)oWon=true;
                xC=0;oC=0;
                //qDebug() << pointC;
            }



            for(int k=0, j=0;((k<=3)&&(j<=3));k++,j++)
            {

                if (f[k][j] =='X')
                {
                    xC++;
                }

                if (f[k][j] =='O')
                {
                    oC++;
                }

                if (f[k][j] =='T')
                {
                    xC++;
                    oC++;
                }

                if (f[k][j] =='.')
                {
                    pointC++;
                }


            }
            if (xC >=4)xWon=true;
            if (oC >=4)oWon=true;
            xC=0;oC=0;

            for(int k=0, j=3;((k<=3)&&(j>=0));k++,j--)
            {

                if (f[k][j] =='X')
                {
                    xC++;
                }

                if (f[k][j] =='O')
                {
                    oC++;
                }

                if (f[k][j] == 'T')
                {
                    xC++;
                    oC++;
                }

                if (f[k][j] =='.')
                {
                    pointC++;
                }


            }
            if (xC >=4)xWon=true;
            if (oC >=4)oWon=true;
            xC=0;oC=0;



            if (xWon)Res = "X won";
            if (oWon)Res = "O won";

            if ((!xWon) && (!oWon))
            {
                if (pointC >0)
                {

                    Res ="Game has not completed";
                }
                else Res = "Draw";
            }



            out << "Case #" << i << ": " << Res << "\r\n";
//            QString linee;
//            in>>linee;

            xWon=false;oWon=false;Draw=false;notEnded=false;
            xC=0;oC=0;pointC=0;
        }




//        while (!stream1.atEnd())
//        {
//            in >> foot;
//            std::cout << foot << "\r\n";
//            out << foot << "\r\n";
//        }

        file1.close();
        file2.close();



    return a.exec();
}
