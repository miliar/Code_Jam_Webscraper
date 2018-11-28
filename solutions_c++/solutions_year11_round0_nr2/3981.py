#include <QtCore/QCoreApplication>
# include <iostream>
# include <QStringList>
# include <QFile>
# include <QTextStream>
using namespace std;
int nTestCases,nAlloyCount,nOpposersCount,nDataCount;
QString strData;
QStringList strAlloys;
QStringList strOpposers, qsResultList;
QString strFinalData = "", strInput = "", strOutput = "";

QString getConversionCombo(QString qsCombo)
{
	QString qsMyCombo = "";
	QString qsResult = "";
	int nTotalCombos = strAlloys.count();
	for ( int nCount = 0;nCount< nTotalCombos ;nCount++)
	{
		qsMyCombo = strAlloys.at(nCount);
		if (qsMyCombo.mid(0,2) == qsCombo)
		{
			qsResult = qsMyCombo.mid(2,1);
			return qsResult ;
		}
	}
	return "";
}


QString checkOpposers(QString qsData)
{
	QString qsOpposer ,qsFirst , qsLast,qsFirstChar,qsToBeReplaced,qsLastChar;
	int nTotalOpposers = strOpposers.count();
	int qsDataLength = qsData.length();
	int pos1,pos2;
	//for (int nCharCount = 0; nCharCount < qsDataLength; nCharCount++ )
	{
		qsLastChar = qsData.at(qsDataLength-1);
		for ( int nCount = 0;nCount< nTotalOpposers ;nCount++)
		{
			pos1 = -1;pos2 =-1;
			qsOpposer = strOpposers.at(nCount);
			qsFirst = qsOpposer.left(1);
			qsLast = qsOpposer.at(1);
			//if (qsLastChar == qsFirst || qsLastChar == qsLast)
			//{
				if (qsData.contains(qsFirst)== true && qsData.contains(qsLast) == true )
				{
					if (qsLastChar == qsFirst)
						pos1 = qsData.indexOf(qsLast);
					else if (qsLastChar == qsLast)
						pos1 = qsData.indexOf(qsFirst);
					if (pos1 == -1 )
						continue;
					pos2 = qsDataLength-1;//qsData.indexOf(qsLast);
					//if (pos2 <  pos1 )
					//{
					//	int temp = pos2 ;
					//	pos2 = pos1;
					//	pos1 = temp;
					//}
					qsToBeReplaced = qsData.mid(pos1,qsDataLength - pos1);
					qsData =  "";//qsData.replace(qsToBeReplaced,"");
					//nCharCount = -1;
					//qsDataLength = qsData.length();
					break;
				}
			//}
		}
	}
	return qsData;
}


QString checkAlloys(QString qsData)
{
	QString qsAlloy ;
	int nDataLength  = 0;
	QString qsReverseCombo = "";
	while(1)
	{
		nDataLength = qsData.length();
		if (nDataLength > 1)
		{
			QString qsCombo = qsData.mid(nDataLength-2,2);
			qsReverseCombo = QString(qsCombo.at(1)) + qsCombo.at(0);
			qsAlloy = getConversionCombo(qsCombo);
			if (qsAlloy.trimmed().count() > 0 )
				qsData = qsData.replace(qsCombo,qsAlloy);
			else
			{
				qsAlloy = getConversionCombo(qsReverseCombo);
				if (qsAlloy.trimmed().count() > 0 )
					qsData = qsData.replace(qsCombo,qsAlloy);
				else
					break;
			}
		}
		else
			break;
	}
	return qsData;
}



QString processData(QString qsData)
{
	QString qsResult = checkAlloys(qsData);
	qsResult = checkOpposers(qsResult);
	return qsResult;
}



int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);
	char testcase[1000];
	QStringList testcases;
	QFile file("C:\\test.txt");
	if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
         return 0;
	
	while (!file.atEnd()) 
	{
         QByteArray line = file.readLine();
		 if (line.trimmed().length() < 5)
			 continue;
		 testcases.append(line);
     }
	file.close();

	//cout<<"Enter no of cases"<<endl;
	//cin>>nTestCases;

	//for ( int nCase = 0;nCase <nTestCases;nCase ++ )
	//{
	//	cin>>testcase;
	//	testcases.append(testcase);
	//}

	//testcases<<"0 0 2 EA"<<"1 QRI 0 4 RRQR"<<"1 QFT 1 QF 7 FAQFDFQ"<<"1 EEZ 1 QE 7 QEEEERA"<<"0 1 QW 2 QW";
	//testcases<<"1 EEZ 1 QE 7 QEEEERA"<<"0 1 QW 2 QW";



	int nCases =testcases.count();

	QStringList Query;
	QString ColData ;
	for ( int nCase = 0;nCase < nCases ; nCase++ )
	{
		int nColId = 0;
		strAlloys.clear();
		strOpposers.clear();
		strInput.clear();
		QString qsData = testcases.at(nCase);
		Query = qsData.split(" ");
		int nTotalColumnCount = Query.count();
		for (int nColumn = 0;nColumn < nTotalColumnCount;nColumn ++ )
		{
			bool ok = false;
			ColData = Query.at(nColumn);
			ColData = ColData.trimmed();
			if (ColData.length()  == 0)
				continue;
			ColData.toInt(&ok);
			if ( ok == true )
			{
				nColId++;
				continue;
			}
			if ( nColId == 1 )
				strAlloys.append(ColData);
			if ( nColId == 2 )
				strOpposers.append(ColData);
			if ( nColId == 3 )
				strInput  = ColData;
		}

		// Supply Data
		QString qsChar = "",strSampleData  ="";
		for ( int nLen = 0; nLen < strInput.length() ;nLen++)
		{
			qsChar = strInput.at(nLen);
			strSampleData = strSampleData.append(qsChar);
			strSampleData  = processData(strSampleData);
		}

		// Format it
		strSampleData = strSampleData.trimmed();
		QString strNewFormatData = "";
		if (strSampleData.isEmpty() == true )
			strNewFormatData = "[]";

		for ( int nLen = 0; nLen < strSampleData.length() ;nLen++)
		{
			qsChar = strSampleData.at(nLen);
			if (qsChar.isEmpty() == false)
			{
				strNewFormatData = strNewFormatData.append(qsChar);
				strNewFormatData += ", ";
			}
		}
		strNewFormatData.chop(2);
		QString qsCaseFormat = QString("Case #%1: [").arg(nCase+1);
		strNewFormatData.prepend(qsCaseFormat);
		strNewFormatData.append("]\n");

		qsResultList.append(strNewFormatData);

	}

	QFile file1("C:\\output.txt");
	if (!file1.open(QIODevice::WriteOnly | QIODevice::Text))
         return 0;
	
	 QTextStream out(&file1);
	for ( int nLen = 0; nLen < qsResultList.length() ;nLen++)
	{
		out<<qsResultList.at(nLen).toAscii().data();
	}
     
	file1.close();

	return 0;
}
