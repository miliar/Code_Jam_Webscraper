#include <iostream>
#include <string>
#include <fstream>
#include <map>
using namespace std;

int main()
{

int T; //no of test cases
cin>>T;

ifstream ifile("magicka_input.txt");
for(int main = 0;main<T;main++)
{
char *result;
char *calls;
map<string, char> coms;
map<string, char>::const_iterator it;
map<string, char> dest;
int C; //no of combinations
int D; //no of destroyers, combinations that destroy each other
int N; //no of invokings
ifile >> C;
char chTemp;
ifile.get(chTemp); //read space
//cout<<"\n--------------------C " <<C;
	if(C > 0)
	{
		for(int i =0 ;i<C;i++)
		{	
			char  result, temp1, temp2;
			string elements;
			ifile.get(temp1);
			elements.push_back(temp1);
//			cout<<"\n------------------Element[0]"<<elements[0];
			ifile.get(temp2);
			elements.push_back(temp2);
//			cout<<"\n------------------Element[1]"<<elements[1];
			ifile.get(result);

			coms[elements] = result;	

			if(temp1 != temp2)
			{	
				char temp;		
				//swapping to include other combination too
				temp = temp2;
				temp2 = temp1;
				temp1 = temp;
				elements.erase();
				elements.push_back(temp1);
				elements.push_back(temp2);
				coms[elements] = result;		
//				if(main == 1)
	//				cout<<"\n"<<elements;
			}
	
			ifile.get(chTemp); // read space
			it = coms.find(elements);
	//		cout<<"\n Combinations "<<elements<<" result "<<(*it).second <<" count "<<coms.count(elements);	
		}
	}

ifile>>D;
ifile.get(chTemp); //read space
//cout<<"\n---------------------D "<<D;
	if(D>0)
	{
		for(int i=0;i<D;i++)
		{
			char temp1, temp2;
			string elements;
			ifile.get(temp1);
			elements.push_back(temp1);
//			cout<<"\n----------------------Element[0]"<<elements[0];
			ifile.get(temp2);
			elements.push_back(temp2);
//			cout<<"\n----------------------Element[1]"<<elements[1];
			dest[elements] = ' ';

			if(temp1 != temp2)
			{
				char temp;
				//swapping for other combination
				temp = temp1;
				temp1 = temp2;
				temp2  = temp;
				elements.erase();
				elements.push_back(temp1);
				elements.push_back(temp2);
				dest[elements] = ' ';
			}

			ifile.get(chTemp); //read space
//			cout<<"\n Destroyers  : "<<elements<<" result ";
		}
	}


ifile>>N;
ifile.get(chTemp); //read space
calls = new char[N];
result = new char[N*2];
//cout<<"\n-----------------------N "<<N;
	for(int i=0 ;i < N; i++)
	{
		char ch;
		ifile.get(ch);
		calls[i] = ch;
//		cout<<"\n--------------------------Calls : "<<calls;
	}

int iRes =0;
result[iRes] = calls[0];
for(int iCall =1; iCall<N ;iCall++)
{	
	string cb, ds;
	cb.push_back(result[iRes]);
	cb.push_back(calls[iCall]);

//	cout<<"\n string "<<cb;
	//cout <<"\nResult comb : "<<cb;
	if(C>0)
	{
		it = coms.find(cb);
		if((char)(*it).second >= 65 && (char)(*it).second <= 90)
		{
			result[iRes] = (char)((*it).second);
//			cout<<"\n Replacing "<<cb<<" with "<<(*it).second;
			continue;
		}	
	}

	if(D>0)
	{
		for(int j=iRes;j>=0;j--)
		{
			ds.erase();
			ds.push_back(calls[iCall]);
			ds.push_back(result[j]);
//			cout<<"\n destroyer :"<<ds;
			it = dest.find(ds);
			if((char)(*it).second == ' ')
			{
//				cout<<"\n Removing upto "<<j;
				iRes = -1;
				iCall++;
				
				break;	
			}	
		}
	}
if(iCall<N)
result[++iRes] = calls[iCall];
}	

string strTemp;
for(int k =0 ;k<=iRes ;k ++)
{
if(result[k] >= 65 && result[k]<=90)
{
strTemp.push_back(result[k]);
if(k!=iRes)
{
strTemp.push_back(',');
strTemp.push_back(' ');
}
}
}
cout<<"\n Case #"<<main+1<<": ["<<strTemp<<"]";
delete result;
delete calls;

}

ifile.close();
}

