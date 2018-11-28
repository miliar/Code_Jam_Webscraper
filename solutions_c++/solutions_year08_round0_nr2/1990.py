#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>


using namespace std;

long int str2num(string );
int hour2int(string);
typedef vector<int> vecint_t;
typedef vector<int>::iterator vecint_it;

int count_train(vecint_t, vecint_t, int);

int main(int argc, char* argv[])
{
	ifstream input;
	string line;
	if(argc!=2)
	{
		cout<<"Usage: "<<argv[0]<<" FILENAME"<<endl;
		exit(EXIT_FAILURE);
	}
	input.open(argv[1], ifstream::in);
	if(!input.is_open())
	{
		cerr<<"Error opening file "<<argv[1]<<" !"<<endl;
		exit(EXIT_FAILURE);
	}
	int N;
	getline(input, line);
	N = str2num(line);
	int i,j;
	for(i=0;i<N;i++)
	{
		int turn_time;
		getline(input,line);
		turn_time = str2num(line);
		int NA, NB;
		getline(input, line);
		char* nanb = new char[strlen(line.c_str())+1];
		strcpy(nanb, line.c_str());
		char* tok = strtok(nanb," ");
		NA = str2num(string(tok));
		tok = strtok(NULL, " ");
		NB = str2num(string(tok));
		vecint_t depA, depB, arrA, arrB;
		for(j=0;j<NA;j++)
		{
			getline(input, line);
			string currdep = line.substr(0,5);
			string currarr = line.substr(6);
			int cdep = hour2int(currdep);
			int carr = hour2int(currarr);
			depA.push_back(cdep);
			arrA.push_back(carr);
		}
		for(j=0;j<NB;j++)
		{
			getline(input, line);
			string currdep = line.substr(0,5);
			string currarr = line.substr(6);
			int cdep = hour2int(currdep);
			int carr = hour2int(currarr);
			depB.push_back(cdep);
			arrB.push_back(carr);
		}
		//cout<<"counting train A"<<endl;
		int trainA = count_train(arrB, depA, turn_time);
		//cout<<"counting train B"<<endl;
		int trainB = count_train(arrA, depB, turn_time);
		cout<<"Case #"<<i+1<<": "<<trainA<<" "<<trainB<<endl;
		/*
		cout<<"turn = "<<turn_time<<endl;
		cout<<"NA = "<<NA<<", NB = "<<NB<<endl;
		for(j=0;j<NA;j++)
		{
			cout<<depA.at(j)<<" "<<arrA.at(j)<<endl;
		}
		for(j=0;j<NB;j++)
		{
			cout<<depB.at(j)<<" "<<arrB.at(j)<<endl;
		}
		*/
		
	}
	input.close();
	return EXIT_SUCCESS;
}

long int str2num(string str)
{
	long int num;
	istringstream Nstr;
	Nstr.str(str);
	Nstr>>num;
	return num;
}

int hour2int(string h)
{
	int res;
	string hpart = h.substr(0,2);
	string mpart = h.substr(3);
	int hour = 100*str2num(hpart);
	int minute = str2num(mpart);
	return hour+minute;
}

int count_train(vecint_t arr, vecint_t dep, int turn)
{
	int train = 0;
	vecint_it it, rit;
	sort(arr.begin(), arr.end());
	reverse(arr.begin(), arr.end());
	for(it = arr.begin(); it!=arr.end();++it)
	{
		*it += turn;
	}
	for(it = dep.begin(); it!=dep.end(); ++it)
	{
		int i_erase = 0;
		bool found = false;
		//cout<<"looking for train at "<<*it<<endl;
		for(rit = arr.begin(); rit!=arr.end(); ++rit)
		{
			if(*rit <= *it)
			{
				//cout<<"found train at "<<*rit<<endl;
				arr.erase(arr.begin()+i_erase);
				found = true;
				break;
			}
			i_erase++;
		}
		if(!found)
		{
			//cout<<"not found"<<endl;
			train++;
		}
	}
	return train;
}


//END OF FILE
