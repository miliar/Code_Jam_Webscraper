#include <iostream>
#include <fstream>
#include <string>
#include <cassert>
#include <cstdlib>
#include <set>
#include <deque>

using namespace std;

ifstream inSmallFile ("A-small.in");
//ifstream inLargeFile ("A-large-practice.in");
ofstream outSmallFile ("A-small.out", fstream::in|fstream::ate|fstream::trunc);
//ofstream outLargeFile ("A-large-practice.out", fstream::in|fstream::ate|fstream::trunc);

void processAlienLanguage (ifstream* in, ofstream* out);
int dispatch (int n, string *eng, int m, int nMsg, string *msg);
void process (ifstream* in, ofstream* out);

int main ()
{
    assert (inSmallFile != NULL);
    //assert (inLargeFile != NULL);
    assert (outSmallFile != NULL);
    //assert (outLargeFile != NULL);
    processAlienLanguage (&inSmallFile, &outSmallFile);
    //process (&inLargeFile, &outLargeFile);

    return 0;
}

void processAlienLanguage (ifstream* in, ofstream* out)
{
    int nTestCase;
	char newLineChar;
	int nResult;
	int nL;
	int nD;
	int nN;

    //处理

		(*in) >> nL;
		(*in) >> nD;
		(*in) >> nN;
		in->get (newLineChar);		//get the '/n' char
		/* 1 获取字典 */
		deque <string> dDic;
		dDic.clear ();

		for (int i=0; i < nD; i++)
        {
			string sDic;
            getline (*in, sDic);
			dDic.push_back (sDic);
			//(*in) >> pSearchEngine[i];
        }
		/* 1 获取字典结束 */

		/*
		for (int j=0; j < nD; j++)
        {
			cout << vDic [j] << endl;
			//(*in) >> pSearchEngine[i];
        }
		*/

		//2 解析testCase, 查字典
		for (nTestCase = 0; nTestCase < nN; nTestCase++)
		{
			deque <string> dResult;
			char cToken;
			dResult.clear();

			//1 按词的个数循环
			for (int k=0; k < nL; k++)
			{
				int nSize = dResult.size ();

				string currChars;
				in->get (cToken);
				if (cToken == '('){
					getline (*in, currChars, ')');
					//in->get (cToken);
				}
				else {
					currChars.append (1, cToken);
				}
				//用所有有效的subStr加上最新的char到dic中去查询
				do {
					string tmpString;
					cout << "dresult length: " << dResult.size () << endl;

					for (int i=0; i < dResult.size (); i++)
					{
						cout << "dump dResult [" << i << "]: " << dResult[i] << endl;
					}

					if (nSize == 0)
						tmpString = "";
					else 
					{
						tmpString.append (dResult[0]);
						dResult.pop_front ();
					}

					for (int m=0; m < currChars.size (); m++)
					{
						string comString = tmpString;

						comString.append (1, currChars.at(m));

						for (int n=0; n < dDic.size (); n++)
						{
							cout <<comString <<"\tvs\t" << dDic[n] << "\tn:\t"<< k+1 <<endl;
							if (dDic[n].compare (0, k+1, comString) == 0)
							{
								dResult.push_back (comString);
								break;
							}
						}
					}
					nSize --;
				} while (nSize > 0);

				//return 0;
				if (dResult.size () ==0)
				{
					break;
				}
			}

			(*out) << "Case #" << nTestCase+1 << ": " << dResult.size() << endl; 
			dResult.clear ();
			string a;
			getline (*in, a); //clear the new line char
		}

    return;
}