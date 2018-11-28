// c.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
#include <vector>
#include <math.h>
#include <map>
#include <string.h>

class Combine{
	char a,b, to;
public:
	Combine(char c1, char c2, char res){
		a = c1;
		b = c2;
		to = res;
	}
	bool isCombine(char c1, char c2){
		return ((c1 == a) && (c2 == b)) || ((c2 == a) && (c1 == b));
	}
	char getResult(){
		return to;
	}
};
class Opposed{
	char a,b;
public:
	Opposed(char c1, char c2){
		a = c1;
		b = c2;
	}
	bool haveOpposed(char c1){
		return ((c1 == a)  ||  (c1 == b));
	}
	char getOpposed(char c){
		if(c==a) return b;
		if(c==b) return a;
		return 0;
	}
};
class Cont{
	map<char, int> amount;
	vector<Combine> comb;
	vector<Opposed> opp;
	vector<char> *str;
	int count;
public:
	void Init(int length){
		str = new vector<char>(length);
		count = 0;
	}
	~Cont(){
		delete str;
	}
	void addCombine(Combine c){
		comb.push_back(c);
	}
	void addOpposed(Opposed o){
		opp.push_back(o);
	}
	void addElement(char c){
		if(count == 0){
			(*str)[count]=c;
			count++;
			amount[c]++;
			return;
		}
		for(int i=0; i<comb.size(); i++)
			if(comb[i].isCombine(c, (*str)[count-1])){
				if(amount[(*str)[count-1]]>0) amount[(*str)[count-1]]--;
				(*str)[count-1] = comb[i].getResult();
				return;
			}
		for(int i=0; i<opp.size(); i++)
			if(opp[i].haveOpposed(c) && amount[opp[i].getOpposed(c)]>0){
				count = 0;
				for(map<char, int>::iterator i = amount.begin(); i!=amount.end(); i++)
					i->second = 0;
				return;
			}
		(*str)[count] = c;
		count++;
		amount[c]++;
	}
	char* getString(){
		char* res = new char[count+1];
		for(int i=0; i<count; i++)
			res[i] = (*str)[i];
		res[count]='\0';
		return res;
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
	/*FILE* f = freopen("myLarge.txt", "w", stdout);
	int T = 100, C=36, D=28, N = 100;
	cout<<T<<endl;
	for(int t=0; t<T; t++){
		cout<<C<<' ';
		for(int c=0; c<C; c++)
			cout<<(char)('a'+rand()%8)<<(char)('a'+rand()%8)<<(char)('a'+rand()%8+10)<<' ';
		cout<<D;
		for(int d=0; d<D; d++)
			cout<<(char)('a'+rand()%8)<<(char)('a'+rand()%8)<<' ';
		cout<<N;
		for(int n=0; n<N; n++)
			cout<<(char)('a'+rand()%8);
		cout<<endl;
	}
	fclose(f);*/
	FILE* fin = freopen("b.in", "r", stdin);
	FILE* fout = freopen("output.txt", "w", stdout);
	
	int T;
	cin>>T;
	for(int t=0; t<T; t++){
		Cont cont;

		int c;
		cin>>c;
		for(int i=0; i<c; i++){
			char str[4];
			cin>>str;
			cont.addCombine(Combine(str[0],str[1],str[2]));
		}

		int d;
		cin>>d;
		for(int i=0; i<d; i++){
			char str[3];
			cin>>str;
			cont.addOpposed(Opposed(str[0], str[1]));
		}

		int n;
		cin>>n;
		cont.Init(n);

		char* str = new char[n+1];
		cin>>str;
		for(int i=0; i<n; i++)
			cont.addElement(str[i]);
		delete[] str;		

		cout<<"Case #"<<t+1<<": [";

		str = cont.getString();
		for(int i=0; i<strlen(str); i++){
			if(i>0) cout<<", ";
			cout<<str[i];
		}
		delete[] str;
		cout<<']'<<endl;
	}

	fclose(fin);
	fclose(fout);
	return 0;
}

