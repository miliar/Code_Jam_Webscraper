#include <QtCore>
#include <iostream>
#include <string>

using namespace std;

QMap<QString, QString> check()
{
	QVector<QString> encoded;
	encoded.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	encoded.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	encoded.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");

	QVector<QString> decoded;

	decoded.push_back("our language is impossible to understand");
	decoded.push_back("there are twenty six factorial possibilities");
	decoded.push_back("so it is okay if you want to just give up");

	QMap<QString, QString> map;
	char c, d;

	for(int i = 0 ; i < encoded.size() ; ++i)
	{
		for(int j = 0 ; j < encoded[i].size() ; ++j)
		{
			d = encoded[i].toStdString()[j];
			c = decoded[i].toStdString()[j];

			map[QString(d)] = QString(c);
		}
	}
	map[QString("q")] = QString("z");
	map[QString("z")] = QString("q");

	return map;

/*
	QList<QString> keys = map.keys();
	QList<QString> values = map.values();
	QVector<bool> test(26, false);

	for(int i = 0 ; i < values.size() ; ++i)
	{
		c = values[i].toStdString()[0];
		if(c != ' ')
			test[c - 'a'] = true;
	}

	for(int i = 0 ; i < test.size() ; ++i)
	{
		if(!test[i])
			qDebug() << "missing : " << (char)(i + 'a');
	}

	for(int i = 0 ; i < keys.size() ; ++i)
	{
		qDebug() << keys[i] << "->" << map[keys[i]];
	}

	for(int i = 0 ; i < encoded.size() ; ++i)
	{
		for(int j = 0 ; j < encoded[i].size() ; ++j)
		{
			d = decoded[i].toStdString()[j];
			c = map[QString(d)].toStdString()[0];
			if(c != encoded[i].toStdString()[j])
				qDebug() << "ERROR ; " << d << " -> " << c;
		}
	}
	*/
}

int main(int argc, char *argv[])
{
	QMap<QString, QString> matrice = check();

	int n;
	QString encode;
	QString decode;
	char line[10000];

	cin >> n;
	fgets(line, sizeof(line), stdin);
	for(int i = 0 ; i < n ; ++i)
	{
		fgets(line, sizeof(line), stdin);
		encode = QString::fromStdString(string(line));
		decode = "";
		for(int j = 0 ; j < encode.size() ; ++j)
		{
			decode += matrice[QString(encode.toStdString()[j])];
		}
		cout << "Case #" << (i+1) << ": " << decode.toStdString() << endl;
	}
	return 0;
}
