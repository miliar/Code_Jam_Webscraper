#include<iostream>
#include<string>
#include<map>
#include<iomanip>
#include<fstream>
using namespace std;

string Dec[200];
map<string,int> fea;
int main()
{
	ofstream fout("out");
	int test;
	int Case = 1;
	char tmp[100000];
	cin >> test;
	cin.getline(tmp,100000);
	while( test > 0 )
	{
		test--;
		int L;
		cin >> L;
		cin.getline(tmp,100000);
		for(int i=0;i<L;i++)
		{
			cin.getline(tmp,100000);
			Dec[i] = tmp;
		}
		int animal;
		cin >> animal;
		fout << "Case #" << Case++ << ": " << endl;
		for(int i=0;i<animal;i++)
		{
			cin >> tmp;//name
			int A;
			cin >> A;
			string b;
			for(int i=0;i<A;i++)
			{
				cin >> b;
				fea[ b ] = 1;
			}
			double value = 1.0;
			int move = 0;
			double pp;
			int go = 1;
			int line,counter;
			string tmpf;
			bool down=false;
			line = 0;
			while( true )
			{
				counter = 1;
					for(;line<L;line++)
						if(move < Dec[line].size() && Dec[line][move]=='(')
							if( counter == go )
								break;
							else
								counter++;
				int t;
				for(t=move+1;;t++)
					if(Dec[line][t] >='0' && Dec[line][t] <='9')
						break;
				for(int i=0;i<1000;i++)
					tmp[i] =0;
				//cout << 'd';
				for(int i=t,k=0;Dec[line][i]!=' ' && Dec[line][i]!=')';i++)
				{
					//cout << Dec[line][i];
					tmp[k++] = Dec[line][i];
				}
				//cout << endl;
				pp = atof( tmp );
				
				//cout << pp<<endl;
			//	system("pause");
				for(int i=move+1;i<Dec[line].size();i++)
					if( Dec[line][i-1]==' ' &&Dec[line][i]!=' ')
					{
						for(int k=i;k<Dec[line].size();k++)
						{
							if(Dec[line][k]==')')
							{//cout << "shit";
								down = true;
								break;
							}
							if(Dec[line][k]!=' ')
								tmpf.push_back(Dec[line][k]);
						}
						break;
					}
					else if(Dec[line][i] ==')')
					{
						//cout << 'L' << line << endl;
						down = true;
						break;
					}
				value *= pp;
				if(down)
					break;
				if( fea[ tmpf ] > 0 )
					go = 1;
				else
					go = 2;//cout << 'g' << go << endl;
				move += 2;
				tmpf.clear();
			}
			fout << fixed << setprecision(7) << value << endl;
			fea.clear();
		}
	}
}