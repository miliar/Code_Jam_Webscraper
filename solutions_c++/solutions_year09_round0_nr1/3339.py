#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;

void Generate_alpb(vector<string*> &words, string &alpb)
{
	for(int i=0; i < words.size(); i++)
	{
		string* tmp = words[i];
		size_t found;
		for(int j=0; j < tmp->size(); j++)
		{
//			cout << "string: " << *tmp << " size: " << tmp->size() << endl;
			found = alpb.find(tmp->at(j));
			if(found==string::npos)
			{
				char tp = tmp->at(j);
				alpb.append(1,tp);
			}
		}
	}
}

int validateCase(const string* tct,const string &alpb, vector<string*> &words)
{
	vector<string*> csv;
	bool flag=false;
	int var = 0, var1 = 0;
	int cnt = 0;
	for(int i=0;i<tct->length();i++)
	{
		string *tmp;
		
		switch(tct->at(i))
		{
		case '(':
			flag = true;
			var++;
			tmp = new string("");
			break;
		case ')':
			flag = false;
			var1++;
			csv.push_back(tmp);
			break;
		default:
			size_t found = alpb.find(tct->at(i));
			if(found == string::npos)
				return 0;
			if(flag == false)
			{
				char tp[2];
				tp[0] = tct->at(i);
				tp[1] = '\0';
				tmp = new string(tp);
				csv.push_back(tmp);
			}
			else
			{
				tmp->append(1,tct->at(i));
			}
			break;	
		}
	}
/*	for(int i=0;i<csv.size();i++)
	{
		cout << "index: " << i << "letters: " << (csv[i])->c_str() << endl;
	}
*/	if(var != var1)
		return -1;
	for(int i=0;i<words.size();i++)
	{
		bool match = true;
		string *twd = words[i];
		for (int j = 0; j< twd->length(); j++)
		{
			size_t found = csv[j]->find(twd->at(j));
			if (found == string::npos)
			{
				match = false;
				break;
			}
		}
		if (match ==true)
			cnt++;
	}
	return cnt;
}

int main(int argc, char *argv[])
{
	if( argc < 2)
	{
		cout << "Error: No input file provided" << endl;
		return -1;
	}
	
	ifstream ifs(argv[1], ifstream::in);
	int L = 0, D = 0, N = 0, cnt = 0;
/*	int ch = ifs.get();
	int cnt = 0;
	while(ch == '\n')
	{
		if(ch == 32)
			cnt++;
		switch(cnt)
		{
		case 0:
			L = ((L*10) + (ch - 48));
		case 1:
			D = ((D*10) + (ch - 48));
		case 2:
			N = ((N*10) + (ch - 48));
		}
	}
*/
	char *line = (char*)malloc(sizeof(char)*256);
	ifs.getline(line, 256);
	string ins(line);
	size_t found = ins.find_first_of(' ', 0);
	size_t found1 = ins.find_last_of(' ', 0);
	string ls = ins.substr(0,found-1);
	L =atoi(ls.c_str());
	string ds = ins.substr(found+1, found1 - 1);
	string ns = ins.substr(found1+1, ins.size());
	D=atoi(ds.c_str());
	N=atoi(ns.c_str());
/*	cout << line << endl;
	for(int i = 0; i < 256; i++)
	{
		if(line[i] == '\n' || line[i] == '\0')
			break;
		if(line[i] == ' ')
		{
                        cnt++;
			continue;
		}
                switch(cnt)
                {
                case 0:
                        L = ((L*10) + atoi(&line[i]));
			break;
                case 1:
                        D = ((D*10) + atoi(&line[i]));
			break;
                case 2:
                        N = ((N*10) + atoi(&line[i]));
			break;
                }
	}*/
	free(line);
	line = 0;
	vector<string*> words;
	vector<string*> tc;
//	cout << "L: " << L << " D: " << D << " N: " << N;
	for (int i=0; i<D; i++)
	{
		line = (char*)malloc(sizeof(char)*256);
		ifs.getline(line, 256);
		string *a = new string(line);
		words.push_back(a);
		free(line);
	}
	for (int i=0; i<N; i++)
        {
                line = (char*)malloc(sizeof(char)*256);
                ifs.getline(line, 256);
                string *a = new string(line);
                tc.push_back(a);
		free(line);
        }
/*	vector<string*> words;
	words.push_back(new string("abc"));
	words.push_back(new string("bca"));
	words.push_back(new string("dbc"));
	words.push_back(new string("dac"));
	words.push_back(new string("cba"));

	vector<string*> tc;
	tc.push_back(new string("(ab)(bc)(ca)"));
	tc.push_back(new string("abc"));
	tc.push_back(new string("(abc)(abc)(abc)"));
	tc.push_back(new string("(zyx)bc"));
*/
//	cout << "Input loaded" <<endl;
	string alpb;
	Generate_alpb(words, alpb);
//	cout << "ALPB: " << alpb <<endl;
	for (int i = 0; i < tc.size(); i++)
	{
		int result = validateCase(tc[i], alpb, words);
		if(result == -1)
			cout << "Case #" << i + 1<< ": Invalid Input: " << tc[i] << endl;
		else
			cout << "Case #" << i + 1<< ":  " << result << endl;
	}
}
